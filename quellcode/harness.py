# CodingTrainer – Python-Seite: Ausführen, Testen, Konstrukt-Prüfung.
# Läuft in Pyodide (Browser) und zum Testen in CPython.
import sys, io, ast, json, traceback, builtins, os, time, linecache, random, math, shutil

USER_FILE = "<dein Code>"
MAX_STEPS = 4_000_000
TIME_LIMIT = 6.0


class StepLimit(BaseException):
    pass


class UserCodeError(Exception):
    def __init__(self, text, kind):
        super().__init__(text)
        self.text = text
        self.kind = kind


class TestFailure(Exception):
    pass


_state = {"code": "", "lang": "de", "checks": [], "outs": [], "run_id": 0}


def _tr(de, en):
    return de if _state["lang"] == "de" else en


# ---------------------------------------------------------------- Ausführung

def _register_source(src):
    linecache.cache[USER_FILE] = (len(src), None, [l + "\n" for l in src.split("\n")], USER_FILE)


def _format_user_tb(exc):
    if isinstance(exc, StepLimit):
        return _tr(
            "Abbruch: Das Programm läuft zu lange (Endlosschleife?). Prüfen Sie die Abbruchbedingung Ihrer Schleife.",
            "Stopped: the program runs too long (infinite loop?). Check your loop's exit condition.")
    if isinstance(exc, SyntaxError):
        line = exc.lineno or 0
        txt = (exc.text or "").rstrip("\n")
        caret = ""
        if exc.offset and txt:
            caret = "\n    " + " " * max(0, exc.offset - 1) + "^"
        return f'  File "{USER_FILE}", line {line}\n    {txt.strip()}{caret}\n{type(exc).__name__}: {exc.msg}'
    frames = [f for f in traceback.extract_tb(exc.__traceback__) if f.filename == USER_FILE]
    lines = ["Traceback (most recent call last):"]
    for f in frames:
        loc = f'  File "{USER_FILE}", line {f.lineno}' + (f", in {f.name}" if f.name != "<module>" else "")
        lines.append(loc)
        if f.line:
            lines.append("    " + f.line.strip())
    lines.append("".join(traceback.format_exception_only(type(exc), exc)).strip())
    return "\n".join(lines)


def _compile(src, sub=None):
    tree = ast.parse(src, USER_FILE)
    if sub:
        for node in tree.body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                name = node.targets[0].id
                if name in sub:
                    node.value = ast.parse(repr(sub[name]), mode="eval").body
                    ast.copy_location(node.value, node)
                    ast.fix_missing_locations(node)
    return compile(tree, USER_FILE, "exec")


class _Sandbox:
    """Kontext: stdout umleiten, input() füttern, Schritte begrenzen."""

    def __init__(self, inputs=None, out=None):
        self.inputs = list(inputs or [])
        self.out = out if out is not None else io.StringIO()
        self.steps = 0
        self.t0 = 0

    def fake_input(self, prompt=""):
        self.out.write(str(prompt))
        if not self.inputs:
            raise EOFError(_tr("input(): Es sind keine (weiteren) Eingaben vorhanden.",
                               "input(): no (more) input available."))
        v = str(self.inputs.pop(0))
        self.out.write(v + "\n")
        return v

    def _tracer(self, frame, event, arg):
        if frame.f_code.co_filename != USER_FILE:
            return None
        self.steps += 1
        if self.steps > MAX_STEPS or (self.steps % 20000 == 0 and time.time() - self.t0 > TIME_LIMIT):
            raise StepLimit()
        return self._tracer

    def __enter__(self):
        self._old_out, self._old_input = sys.stdout, builtins.input
        sys.stdout = self.out
        builtins.input = self.fake_input
        self.t0 = time.time()
        sys.settrace(self._tracer)
        return self

    def __exit__(self, *a):
        sys.settrace(None)
        sys.stdout, builtins.input = self._old_out, self._old_input
        return False


def _fresh_dir(files=None):
    _state["run_id"] += 1
    base = os.path.join("/tmp", "ct_runs", f"run{_state['run_id']}")
    if os.path.isdir(base):
        shutil.rmtree(base)   # Reste eines früheren Laufs entfernen
    os.makedirs(base, exist_ok=True)
    os.chdir(base)
    os.makedirs("data", exist_ok=True)
    for name, content in (files or {}).items():
        d = os.path.dirname(name)
        if d:
            os.makedirs(d, exist_ok=True)
        with open(name, "w", encoding="utf-8") as f:
            f.write(content)
    return base


def run(inputs=None, sub=None, files=None, seed=None):
    """Führt den Code der Studierenden aus. Liefert (namespace, ausgabe)."""
    src = _state["code"]
    _register_source(src)
    _fresh_dir(files)
    if seed is not None:
        random.seed(seed)
    try:
        code = _compile(src, sub)
    except SyntaxError as e:
        raise UserCodeError(_format_user_tb(e), "syntax")
    ns = {"__name__": "__main__", "__builtins__": builtins}
    box = _Sandbox(inputs)
    try:
        with box:
            exec(code, ns)
    except BaseException as e:  # noqa
        if isinstance(e, (KeyboardInterrupt, SystemExit)) and not isinstance(e, StepLimit):
            raise
        err = UserCodeError(_format_user_tb(e), "runtime")
        err.partial = box.out.getvalue()
        raise err
    out = box.out.getvalue()
    _state["outs"].append(out)
    return ns, out


_last = {"out": ""}


def call(ns, name, *args, **kwargs):
    """Ruft eine Funktion/Klasse aus dem Code der Studierenden auf."""
    if name not in ns or not callable(ns[name]):
        raise TestFailure(_tr(f"Es gibt keine Funktion/Klasse namens `{name}`.",
                              f"There is no function/class named `{name}`."))
    box = _Sandbox()
    try:
        with box:
            res = ns[name](*args, **kwargs)
    except BaseException as e:  # noqa
        if isinstance(e, (KeyboardInterrupt, SystemExit)) and not isinstance(e, StepLimit):
            raise
        a = ", ".join([repr(x) for x in args] + [f"{k}={v!r}" for k, v in kwargs.items()])
        raise UserCodeError(_tr(f"Fehler beim Aufruf von {name}({a}):\n", f"Error when calling {name}({a}):\n")
                            + _format_user_tb(e), "runtime")
    _last["out"] = box.out.getvalue()
    return res


def method(obj, name, *args, **kwargs):
    """Ruft eine Methode eines Objekts auf (mit Schutz vor Endlosschleifen)."""
    if not hasattr(obj, name):
        raise TestFailure(_tr(f"Das Objekt hat keine Methode/kein Attribut `{name}`.",
                              f"The object has no method/attribute `{name}`."))
    box = _Sandbox()
    try:
        with box:
            m = getattr(obj, name)
            res = m(*args, **kwargs) if callable(m) else m
    except BaseException as e:  # noqa
        if isinstance(e, (KeyboardInterrupt, SystemExit)) and not isinstance(e, StepLimit):
            raise
        raise UserCodeError(_tr(f"Fehler in der Methode {name}():\n", f"Error in method {name}():\n")
                            + _format_user_tb(e), "runtime")
    _last["out"] = box.out.getvalue()
    return res


def safe(fn):
    """Führt beliebigen Ausdruck mit Studierenden-Code geschützt aus: safe(lambda: a + b)."""
    box = _Sandbox()
    try:
        with box:
            res = fn()
    except BaseException as e:  # noqa
        if isinstance(e, (KeyboardInterrupt, SystemExit)) and not isinstance(e, StepLimit):
            raise
        raise UserCodeError(_format_user_tb(e), "runtime")
    _last["out"] = box.out.getvalue()
    return res


def raises(exc_type, fn):
    """True, wenn fn() die Exception exc_type auslöst."""
    box = _Sandbox()
    try:
        with box:
            fn()
    except exc_type:
        return True
    except StepLimit as e:
        raise UserCodeError(_format_user_tb(e), "runtime")
    except Exception:
        return False
    finally:
        _last["out"] = box.out.getvalue()
    return False


def last_out():
    return _last["out"]


# ---------------------------------------------------------------- Test-Helfer

def check(cond, de, en=None):
    _state["checks"].append({"ok": bool(cond), "de": de, "en": en or de})
    return bool(cond)


def need(ns, *names):
    missing = [n for n in names if n not in ns]
    if missing:
        raise TestFailure(_tr("Variable(n) fehlt/fehlen: " + ", ".join(missing),
                              "Missing variable(s): " + ", ".join(missing)))
    return [ns[n] for n in names] if len(names) > 1 else ns[names[0]]


def approx(a, b, tol=1e-6):
    try:
        return abs(float(a) - float(b)) <= tol * max(1.0, abs(float(b)))
    except (TypeError, ValueError):
        return False


def nums(text):
    import re
    found = []
    for m in re.finditer(r"-?\d+(?:[.,]\d+)?(?:[eE][-+]?\d+)?", text):
        try:
            found.append(float(m.group().replace(",", ".")))
        except ValueError:
            pass
    return found


def has_num(text, value, tol=1e-6):
    return any(approx(x, value, tol) for x in nums(text))


def has(text, *words):
    t = text.lower()
    return all(w.lower() in t for w in words)


class Code:
    """Ersetzt in run(sub=...) die rechte Seite durch beliebigen Code: sub={"A": Code("np.eye(2)")}."""
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return self.text


def read_file(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


# ---------------------------------------------------------------- Konstrukte

CH_ORDER = ["4", "5", "6", "7", "8", "9", "10", "A", "B"]


def ch_idx(c):
    return CH_ORDER.index(c) if c in CH_ORDER else 99


# key: (kapitel oder None = nicht im Skript, Abschnitt, label_de, label_en)
C = {
    # Kapitel 4
    "print": ("4", "4.1", "print()", "print()"),
    "input": ("4", "4.3e", "input()", "input()"),
    "fstring": ("4", "4.3", "f-String", "f-string"),
    "arith": ("4", "4.2", "Rechenoperatoren", "arithmetic operators"),
    "assign_multi": ("4", "4.3", "Mehrfachzuweisung", "multiple assignment"),
    "augassign": ("4", "4.3", "erweiterte Zuweisung (+= …)", "augmented assignment (+= …)"),
    "compare": ("4", "4.4", "Vergleiche", "comparisons"),
    "boolop": ("4", "4.4", "and / or / not", "and / or / not"),
    "in": ("4", "4.4", "Operator in", "operator in"),
    "len": ("4", "4.5", "len()", "len()"),
    "round": ("4", "4.4", "round()", "round()"),
    # Kapitel 5
    "type": ("5", "5.1", "type()", "type()"),
    "cast": ("5", "5.2e", "Casting int()/float()/str()/bool()", "casting int()/float()/str()/bool()"),
    "list": ("5", "5.3", "Liste", "list"),
    "index": ("5", "5.3", "Indexzugriff", "indexing"),
    "list_methods": ("5", "5.3m", "Listen-Methoden", "list methods"),
    "is": ("5", "5.4s", "Operator is", "operator is"),
    "id": ("5", "5.4", "id()", "id()"),
    "none": ("5", "5.3m", "None", "None"),
    "numsys": ("5", "5.5", "bin()/hex()/ord()/chr()", "bin()/hex()/ord()/chr()"),
    "complex": ("5", "5.1", "complex / j", "complex / j"),
    "replace": ("5", "5.2e", ".replace()", ".replace()"),
    "import_math": ("5", "5.2e", "Modul math (floor, ceil, isclose)", "module math (floor, ceil, isclose)"),
    "math_more": ("9", "9.1", "weitere math-Funktionen (sqrt, pi, sin, …)", "further math functions (sqrt, pi, sin, …)"),
    # Kapitel 6
    "if": ("6", "6.1a", "if / elif / else", "if / elif / else"),
    "ifexp": ("6", "6.1b", "Conditional Expression", "conditional expression"),
    "while": ("6", "6.2a", "while-Schleife", "while loop"),
    "for": ("6", "6.2b", "for-Schleife", "for loop"),
    "range": ("6", "6.2b", "range()", "range()"),
    "break": ("6", "6.2c", "break / continue", "break / continue"),
    "abs": ("6", "6.1a", "abs()", "abs()"),
    "isdigit": ("6", "6.2c", ".isdigit()", ".isdigit()"),
    "import_random": ("6", "6.2c", "Modul random", "module random"),
    # Kapitel 7
    "def": ("7", "7.3", "eigene Funktionen (def)", "own functions (def)"),
    "return": ("7", "7.3r", "return", "return"),
    "default_arg": ("7", "7.3p", "Standardargumente", "default arguments"),
    "kwargs_call": ("7", "7.3k", "Keyword-Argumente", "keyword arguments"),
    "varargs": ("7", "7.5", "*args", "*args"),
    "global": ("7", "7.6g", "global", "global"),
    "isinstance": ("7", "7.4", "isinstance()", "isinstance()"),
    "seqfuncs": ("7", "7.2s", "sum()/max()/min()/sorted()", "sum()/max()/min()/sorted()"),
    "divmod": ("7", "7.3r", "divmod()/oct()/help()", "divmod()/oct()/help()"),
    "annot": ("7", "7.8", "Typ-Annotationen", "type annotations"),
    # Kapitel 8
    "slice": ("8", "8.1x", "Slicing", "slicing"),
    "set": ("8", "8.2", "Set", "set"),
    "dict": ("8", "8.3", "Dictionary", "dictionary"),
    "dict_methods": ("8", "8.3", "Dictionary-Methoden (get/items/…)", "dictionary methods (get/items/…)"),
    "set_methods": ("8", "8.2", "Set-Methoden", "set methods"),
    "tuple": ("8", "8.4", "Tupel / tuple()", "tuple / tuple()"),
    "listcomp": ("8", "8.8", "Comprehension", "comprehension"),
    "enumzip": ("8", "8.9", "enumerate() / zip()", "enumerate() / zip()"),
    "copy": ("8", "8.7", "Kopieren (copy)", "copying (copy)"),
    "unpack_for": ("8", "8.3", "Entpacken in for-Schleifen", "unpacking in for loops"),
    # Kapitel 9
    "import": ("9", "9.1", "import / from … import / as", "import / from … import / as"),
    "numpy": ("9", "9.2", "NumPy", "NumPy"),
    "pandas": ("9", "9.4", "pandas", "pandas"),
    "matmul": ("9", "9.2m", "Operator @", "operator @"),
    # Kapitel 10
    "class": ("10", "10.3", "Klassen", "classes"),
    "super": ("10", "10.5", "super()", "super()"),
    "magic": ("10", "10.7", "Magic Methods", "magic methods"),
    "abc": ("10", "10.8", "abstrakte Klassen (abc)", "abstract classes (abc)"),
    "pass": ("10", "10.6", "pass", "pass"),
    # Anhang A
    "with": ("A", "A.2", "with", "with"),
    "open": ("A", "A.2", "open()", "open()"),
    "file_methods": ("A", "A.3", "read/write/strip/split/startswith", "read/write/strip/split/startswith"),
    "csv": ("A", "A.4", "Modul csv", "module csv"),
    "pathlib": ("A", "A.1", "pathlib", "pathlib"),
    # Anhang B
    "try": ("B", "B.3", "try / except", "try / except"),
    "raise": ("B", "B.4", "raise", "raise"),
    # nicht im Skript
    "lambda": (None, None, "lambda", "lambda"),
    "loop_else": (None, None, "else-Zweig an Schleife", "else clause on a loop"),
    "match": (None, None, "match/case", "match/case"),
    "walrus": (None, None, "Walross-Operator :=", "walrus operator :="),
    "yield": (None, None, "yield / Generatorfunktion", "yield / generator function"),
    "nonlocal": (None, None, "nonlocal", "nonlocal"),
    "assert": (None, None, "assert", "assert"),
    "bitops": (None, None, "Bit-Operatoren (& | ^ ~ << >>)", "bitwise operators (& | ^ ~ << >>)"),
    "decorator": (None, None, "Decorator", "decorator"),
    "star_call": (None, None, "Entpacken beim Aufruf (*liste)", "unpacking in calls (*list)"),
    "kwargs_def": (None, None, "**kwargs", "**kwargs"),
    "del": (None, None, "del", "del"),
}

BUILTIN_MAP = {
    "print": "print", "input": "input", "len": "len", "round": "round",
    "type": "type", "int": "cast", "float": "cast", "str": "cast", "bool": "cast", "list": "list",
    "id": "id", "bin": "numsys", "hex": "numsys", "ord": "numsys", "chr": "numsys", "complex": "complex",
    "range": "range", "abs": "abs",
    "isinstance": "isinstance", "sum": "seqfuncs", "max": "seqfuncs", "min": "seqfuncs", "sorted": "seqfuncs",
    "oct": "divmod", "divmod": "divmod", "help": "divmod",
    "set": "set", "dict": "dict", "tuple": "tuple", "enumerate": "enumzip", "zip": "enumzip",
    "super": "super", "open": "open",
}
NOT_IN_SCRIPT_BUILTINS = {
    "map", "filter", "reduce", "any", "all", "reversed", "iter", "next", "eval", "exec", "getattr", "setattr",
    "hasattr", "pow", "format", "vars", "globals", "locals", "frozenset", "bytes", "bytearray", "callable",
    "hash", "memoryview", "property", "staticmethod", "classmethod", "slice", "object", "issubclass", "repr",
    "ascii", "compile", "dir", "exit", "quit",
}
METHOD_MAP = {
    "append": "list_methods", "pop": "list_methods", "index": "list_methods", "remove": "list_methods",
    "insert": "list_methods", "clear": "list_methods", "count": "list_methods", "sort": "list_methods",
    "reverse": "list_methods", "replace": "replace", "isdigit": "isdigit",
    "get": "dict_methods", "keys": "dict_methods", "values": "dict_methods", "items": "dict_methods",
    "add": "set_methods", "union": "set_methods", "intersection": "set_methods", "difference": "set_methods",
    "copy": "copy", "deepcopy": "copy",
    "read": "file_methods", "write": "file_methods", "readline": "file_methods", "strip": "file_methods",
    "split": "file_methods", "startswith": "file_methods", "read_text": "pathlib", "write_text": "pathlib",
}
NOT_IN_SCRIPT_METHODS = {
    "upper", "lower", "title", "capitalize", "join", "find", "rfind", "endswith", "format", "extend",
    "setdefault", "update", "lstrip", "rstrip", "isalpha", "isnumeric", "isdecimal", "isalnum", "zfill",
    "center", "ljust", "rjust", "swapcase", "casefold", "partition", "rpartition", "splitlines", "discard",
    "symmetric_difference", "issubset", "issuperset", "popitem", "fromkeys", "readlines", "writelines",
    "isupper", "islower", "isspace", "rsplit", "rindex", "expandtabs", "encode", "decode", "translate",
    "maketrans", "removeprefix", "removesuffix",
}
MODULES = {
    "math": "import_math", "random": "import_random", "copy": "copy", "numpy": "numpy", "pandas": "pandas",
    "matplotlib": "import", "abc": "abc", "datetime": "import", "time": "import", "csv": "csv",
    "pathlib": "pathlib", "sys": "import", "uuid": "import",
}
MAGIC = {"__str__", "__eq__", "__ne__", "__lt__", "__le__", "__gt__", "__ge__", "__add__", "__sub__",
         "__mul__", "__truediv__", "__floordiv__", "__mod__", "__pow__", "__abs__", "__len__", "__int__",
         "__float__", "__iadd__"}


def analyze(src):
    """Liefert {key: erste_zeile} für alle gefundenen Konstrukte."""
    tree = ast.parse(src)
    found = {}
    user_defs = set()
    for n in ast.walk(tree):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            user_defs.add(n.name)
        elif isinstance(n, ast.Attribute) and isinstance(n.ctx, ast.Store):
            user_defs.add(n.attr)

    def add(key, node):
        line = getattr(node, "lineno", 0)
        if key not in found or line < found[key]:
            found[key] = line

    math_names = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            for a in n.names:
                if a.name == "math":
                    math_names.add(a.asname or "math")
    for n in ast.walk(tree):
        if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name) and n.value.id in math_names:
            add("import_math" if n.attr in ("floor", "ceil", "isclose") else "math_more", n)
    for n in ast.walk(tree):
        t = type(n).__name__
        if isinstance(n, ast.If):
            add("if", n)
        elif isinstance(n, ast.IfExp):
            add("ifexp", n)
        elif isinstance(n, ast.While):
            add("while", n)
            if n.orelse:
                add("loop_else", n)
        elif isinstance(n, ast.For):
            add("for", n)
            if n.orelse:
                add("loop_else", n)
            if isinstance(n.target, (ast.Tuple, ast.List)):
                add("unpack_for", n)
        elif isinstance(n, (ast.Break, ast.Continue)):
            add("break", n)
        elif isinstance(n, ast.FunctionDef):
            add("def", n)
            a = n.args
            if a.defaults or a.kw_defaults and any(d is not None for d in a.kw_defaults):
                add("default_arg", n)
            if a.vararg:
                add("varargs", n)
            if a.kwarg:
                add("kwargs_def", n)
            if n.returns or any(x.annotation for x in a.args + a.kwonlyargs):
                add("annot", n)
            if n.name in MAGIC or (n.name.startswith("__") and n.name.endswith("__") and n.name != "__init__"):
                add("magic", n)
            for d in n.decorator_list:
                dn = d.id if isinstance(d, ast.Name) else (d.attr if isinstance(d, ast.Attribute) else "")
                if dn != "abstractmethod":
                    add("decorator", d)
        elif isinstance(n, ast.AsyncFunctionDef):
            add("yield", n)
        elif isinstance(n, ast.ClassDef):
            add("class", n)
            for b in n.bases:
                if isinstance(b, ast.Name) and b.id == "ABC":
                    add("abc", n)
        elif isinstance(n, ast.Return):
            add("return", n)
        elif isinstance(n, ast.Global):
            add("global", n)
        elif isinstance(n, ast.Nonlocal):
            add("nonlocal", n)
        elif isinstance(n, ast.Lambda):
            add("lambda", n)
        elif isinstance(n, (ast.Yield, ast.YieldFrom)):
            add("yield", n)
        elif isinstance(n, ast.NamedExpr):
            add("walrus", n)
        elif t == "Match":
            add("match", n)
        elif isinstance(n, ast.Assert):
            add("assert", n)
        elif isinstance(n, ast.Delete):
            add("del", n)
        elif isinstance(n, ast.Pass):
            add("pass", n)
        elif isinstance(n, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
            add("listcomp", n)
        elif isinstance(n, ast.Set):
            add("set", n)
        elif isinstance(n, ast.Dict):
            add("dict", n)
        elif isinstance(n, ast.List):
            add("list", n)
        elif isinstance(n, ast.Tuple) and isinstance(n.ctx, ast.Store):
            add("assign_multi", n)
        elif isinstance(n, ast.Subscript):
            if isinstance(n.slice, ast.Slice) or (isinstance(n.slice, ast.Tuple) and any(isinstance(e, ast.Slice) for e in n.slice.elts)):
                add("slice", n)
            else:
                add("index", n)
        elif isinstance(n, ast.JoinedStr):
            add("fstring", n)
        elif isinstance(n, ast.AugAssign):
            add("augassign", n)
            if isinstance(n.op, (ast.BitAnd, ast.BitOr, ast.BitXor, ast.LShift, ast.RShift)):
                add("bitops", n)
        elif isinstance(n, ast.BinOp):
            if isinstance(n.op, ast.MatMult):
                add("matmul", n)
            elif isinstance(n.op, (ast.BitAnd, ast.BitOr, ast.BitXor, ast.LShift, ast.RShift)):
                add("bitops", n)
            else:
                add("arith", n)
        elif isinstance(n, ast.UnaryOp):
            if isinstance(n.op, ast.Invert):
                add("bitops", n)
            elif isinstance(n.op, ast.Not):
                add("boolop", n)
        elif isinstance(n, ast.BoolOp):
            add("boolop", n)
        elif isinstance(n, ast.Compare):
            for op in n.ops:
                if isinstance(op, (ast.In, ast.NotIn)):
                    add("in", n)
                elif isinstance(op, (ast.Is, ast.IsNot)):
                    add("is", n)
                else:
                    add("compare", n)
        elif isinstance(n, ast.Constant):
            if n.value is None:
                add("none", n)
            elif isinstance(n.value, complex):
                add("complex", n)
        elif isinstance(n, ast.Try) or t == "TryStar":
            add("try", n)
        elif isinstance(n, ast.Raise):
            add("raise", n)
        elif isinstance(n, ast.With):
            add("with", n)
        elif isinstance(n, (ast.Import, ast.ImportFrom)):
            mods = [a.name for a in n.names] if isinstance(n, ast.Import) else [n.module or ""]
            for m in mods:
                root = m.split(".")[0]
                key = MODULES.get(root)
                if key is None:
                    found.setdefault("module:" + root, getattr(n, "lineno", 0))
                else:
                    add(key, n)
                    if root not in ("math", "random", "copy", "csv", "pathlib", "abc"):
                        add("import", n)
            if isinstance(n, ast.ImportFrom) or any(a.asname for a in n.names):
                add("import", n)
        elif isinstance(n, ast.Call):
            f = n.func
            if any(isinstance(a, ast.Starred) for a in n.args) or any(k.arg is None for k in n.keywords):
                add("star_call", n)
            if n.keywords and isinstance(f, ast.Name) and f.id in user_defs:
                add("kwargs_call", n)
            if isinstance(f, ast.Name):
                if f.id in BUILTIN_MAP and f.id not in user_defs:
                    add(BUILTIN_MAP[f.id], n)
                elif f.id in NOT_IN_SCRIPT_BUILTINS and f.id not in user_defs:
                    found.setdefault("builtin:" + f.id, n.lineno)
            elif isinstance(f, ast.Attribute):
                name = f.attr
                if name in user_defs:
                    continue
                base_is_module = isinstance(f.value, ast.Name) and f.value.id in ("math", "random", "np", "pd", "csv", "copy", "plt", "numpy", "pandas")
                if base_is_module:
                    continue
                if name in METHOD_MAP:
                    add(METHOD_MAP[name], n)
                elif name in NOT_IN_SCRIPT_METHODS:
                    found.setdefault("method:" + name, n.lineno)
    return found


def construct_report(src, chapter, require=None, forbid=None, off=None):
    """Bewertet die verwendeten Konstrukte relativ zum Kapitel der Aufgabe."""
    try:
        found = analyze(src)
    except SyntaxError:
        return {"items": [], "missing": [], "forbidden": []}
    limit = ch_idx(chapter)
    items = []
    for key, line in sorted(found.items(), key=lambda kv: kv[1]):
        if ":" in key:
            kind, name = key.split(":", 1)
            label = f".{name}()" if kind == "method" else (f"{name}()" if kind == "builtin" else f"import {name}")
            items.append({"key": key, "line": line, "status": "absent", "chapter": None, "section": None,
                          "de": label, "en": label})
            continue
        chap, sec, de, en = C[key]
        if key in (off or []):
            items.append({"key": key, "line": line, "status": "off", "chapter": chap, "section": sec, "de": de, "en": en})
        elif chap is None:
            items.append({"key": key, "line": line, "status": "absent", "chapter": None, "section": None, "de": de, "en": en})
        elif ch_idx(chap) > limit:
            items.append({"key": key, "line": line, "status": "later", "chapter": chap, "section": sec, "de": de, "en": en})
    missing = [{"key": k, "de": C[k][2], "en": C[k][3], "section": C[k][1]} for k in (require or []) if k not in found]
    forbidden = [{"key": k, "de": C[k][2] if k in C else k, "en": C[k][3] if k in C else k,
                  "line": found[k]} for k in (forbid or []) if k in found]
    return {"items": items, "missing": missing, "forbidden": forbidden}


# ---------------------------------------------------------------- API für JS

def api_run(code, stdin_text, lang="de", files=None):
    _state["code"] = code
    _state["lang"] = lang
    inputs = stdin_text.split("\n") if stdin_text else []
    if inputs and inputs[-1] == "":
        inputs.pop()
    try:
        ns, out = run(inputs=inputs, files=files)
        return json.dumps({"out": out, "error": None})
    except UserCodeError as e:
        return json.dumps({"out": e.partial if hasattr(e, "partial") else "", "error": e.text, "kind": e.kind})
    except Exception as e:  # interner Fehler
        return json.dumps({"out": "", "error": "Interner Fehler: " + repr(e), "kind": "internal"})


def api_check(code, tests, chapter, require=None, forbid=None, lang="de", off=None):
    _state["code"] = code
    _state["lang"] = lang
    _state["checks"] = []
    _state["outs"] = []
    error = None
    kind = None
    try:
        compile(code, USER_FILE, "exec")
    except SyntaxError as e:
        _register_source(code)
        return json.dumps({"checks": [], "error": _format_user_tb(e), "kind": "syntax",
                           "constructs": {"items": [], "missing": [], "forbidden": []}, "out": ""})
    env = {"run": run, "call": call, "method": method, "safe": safe, "raises": raises, "check": check,
           "need": need, "approx": approx, "nums": nums, "has": has, "has_num": has_num, "read_file": read_file,
           "last_out": last_out, "math": math, "TestFailure": TestFailure, "SOURCE": code, "Code": Code}
    cwd = os.getcwd()
    try:
        exec(tests, env)
    except UserCodeError as e:
        error, kind = e.text, e.kind
    except TestFailure as e:
        check(False, str(e), str(e))
    except Exception as e:
        error, kind = "Interner Testfehler: " + "".join(traceback.format_exception_only(type(e), e)).strip(), "internal"
    finally:
        try:
            os.chdir(cwd)
        except Exception:
            pass
    rep = construct_report(code, chapter, require, forbid, off)
    out = _state["outs"][0] if _state["outs"] else ""
    return json.dumps({"checks": _state["checks"], "error": error, "kind": kind, "constructs": rep, "out": out[:4000]})


def api_constructs(code, chapter, lang="de", off=None):
    return json.dumps(construct_report(code, chapter, off=off))
