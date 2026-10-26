import re, json, sys
sys.path.insert(0, ".")
import harness, bank

tpl = open("template.html", encoding="utf-8").read()
SEC = {m.group(1): m.group(2) for m in re.finditer(r'\["([0-9AB]+\.[0-9]+[a-z]?)", "([0-9AB]+)", "', tpl)}
ORDER = harness.CH_ORDER
problems = []
def flag(e, msg): problems.append(f"{e['id']}: {msg}")

titles = {}
for e in bank.EX:
    ch = e["ch"]
    # 1. Startcode
    for lang in ("de", "en"):
        rep = harness.construct_report(e["starter"][lang], ch)
        if rep["items"]:
            flag(e, f"Startcode {lang} nutzt {[i['key'] for i in rep['items']]}")
    # 2. Verweise
    if not e.get("refs"):
        flag(e, "keine Skriptverweise")
    for r in e.get("refs", []):
        if r not in SEC:
            flag(e, f"unbekannter Verweis {r}")
        elif ORDER.index(SEC[r]) > ORDER.index(ch):
            flag(e, f"Verweis {r} liegt nach Kapitel {ch}")
    # 3. stdin
    uses_input = "input(" in e["solution"]
    if uses_input and not e.get("stdin"):
        flag(e, "nutzt input(), aber keine Beispiel-Eingaben")
    if e.get("stdin") and not uses_input:
        flag(e, "Beispiel-Eingaben ohne input()")
    # 4. DE/EN-Bezeichner
    def idents(txt):
        out = set()
        for m in re.finditer(r"`([^`]+)`", txt):
            for w in re.findall(r"[A-Za-z_][A-Za-z0-9_]*", m.group(1)):
                out.add(w)
        return out
    de, en = idents(e["task"]["de"]), idents(e["task"]["en"])
    # Wörter, die bewusst übersetzt werden (Ausgabetexte), ignorieren wir, wenn sie in Anführungszeichen stehen
    diff = (de ^ en)
    diff = {w for w in diff if not re.search(r"[\"'][^\"'`]*\b" + re.escape(w) + r"\b", e["task"]["de"] + e["task"]["en"])}
    if diff:
        flag(e, f"DE/EN-Bezeichner unterschiedlich: {sorted(diff)}")
    # 5. Variablen im Text existieren in Lösung
    for w in sorted(de & en):
        if re.fullmatch(r"[a-z_][a-z0-9_]*", w) and len(w) > 1 and w not in e["solution"] and w not in ("int", "float", "str", "bool", "list", "dict", "set", "tuple", "if", "for", "while", "with", "utf", "csv", "self", "e", "j", "x"):
            flag(e, f"Bezeichner `{w}` aus dem Text kommt in der Musterlösung nicht vor")
    # 6. Robustheit der Tests
    t = e["tests"]
    varied = ("for " in t) or t.count("run(") >= 2 or "call(" in t or "sub=" in t or "inputs=" in t or "files=" in t
    if not varied:
        flag(e, "Tests prüfen nur einen einzigen Fall (fest eingetippte Lösung möglich?)")
    # 7. Titel doppelt
    for lang in ("de", "en"):
        key = (lang, e["title"][lang])
        if key in titles:
            flag(e, f"Titel doppelt mit {titles[key]}")
        titles[key] = e["id"]
    # 8. Leere/kurze Texte
    for lang in ("de", "en"):
        if len(e["task"][lang]) < 80:
            flag(e, f"Aufgabentext {lang} sehr kurz")
    # 9. Funktionen/Attribute aus Modulen, die nicht im Skript stehen (Musterlösung)
    import ast
    ALLOWED = {
        "math": {"sqrt", "cos", "sin", "pi", "factorial", "floor", "ceil", "isclose"},
        "random": {"randint"},
        "np": {"array", "zeros", "ones", "arange", "linspace", "dot", "cross", "transpose", "linalg", "sqrt", "exp",
               "sin", "cos", "pi", "isclose", "allclose", "std"},
        "linalg": {"solve", "eig", "eigvals"},
        "pd": {"DataFrame", "read_csv"},
        "csv": {"DictReader", "writer"},
        "copy": {"deepcopy", "copy"},
    }
    BAD_ATTRS = {"real", "imag", "conjugate", "max", "min", "sum", "idxmax", "idxmin", "iloc", "loc", "mean_", "tolist",
                 "astype", "reshape", "flatten", "argmax", "argmin", "cumsum", "round", "abs", "median", "sort_values"}
    try:
        tree = ast.parse(e["solution"])
    except SyntaxError:
        tree = None
    if tree:
        for n in ast.walk(tree):
            if isinstance(n, ast.Attribute):
                base = n.value
                bname = base.id if isinstance(base, ast.Name) else (base.attr if isinstance(base, ast.Attribute) else None)
                if bname in ALLOWED and n.attr not in ALLOWED[bname]:
                    flag(e, f"{bname}.{n.attr} steht nicht im Skript")
                elif n.attr in BAD_ATTRS and bname not in ALLOWED and bname != "self":
                    flag(e, f".{n.attr} steht nicht im Skript")
print("\n".join(problems) or "keine Auffälligkeiten")
print(len(problems), "Hinweise")
