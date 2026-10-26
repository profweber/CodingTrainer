from exlib import ex

# Kapitel 10: Klassen, Attribute, Methoden, Vererbung, super(), protected/private, Getter/Setter, Magic Methods, abc.

ex(id="k10-motor", ch="10", lvl=1,
   title={"de": "Klasse Motor", "en": "Class Motor"},
   task={"de": "Schreiben Sie eine Klasse `Motor`. Der Konstruktor erhält die Nennleistung `power_kw` und die Nenndrehzahl `rpm` und speichert beide als Attribute gleichen Namens.\n- `torque()` gibt das Nennmoment M = P / ω in Nm zurück (P in W, ω = 2π·n/60).\n- `describe()` gibt einen Text wie `5.5 kW bei 1450 1/min` zurück (nicht ausgeben!).",
         "en": "Write a class `Motor`. The constructor receives the rated power `power_kw` and the rated speed `rpm` and stores both as attributes of the same name.\n- `torque()` returns the rated torque M = P / ω in Nm (P in W, ω = 2π·n/60).\n- `describe()` returns a text like `5.5 kW at 1450 1/min` (don't print it!)."},
   starter={"de": "import math\n\nclass Motor:\n    def __init__(self, power_kw, rpm):\n        ...\n", "en": "import math\n\nclass Motor:\n    def __init__(self, power_kw, rpm):\n        ...\n"},
   solution='import math\n\nclass Motor:\n    def __init__(self, power_kw, rpm):\n        self.power_kw = power_kw\n        self.rpm = rpm\n\n    def torque(self):\n        omega = 2 * math.pi * self.rpm / 60\n        return self.power_kw * 1000 / omega\n\n    def describe(self):\n        return f"{self.power_kw} kW bei {self.rpm} 1/min"\n\nm = Motor(5.5, 1450)\nprint(m.describe(), round(m.torque(), 1), "Nm")\n',
   tests='''
import math as _m
ns, out = run()
for P, n in [(5.5, 1450), (0.75, 2800), (22, 980)]:
    m = call(ns, "Motor", P, n)
    check(getattr(m, "power_kw", None) == P and getattr(m, "rpm", None) == n, f"Motor({P}, {n}) speichert power_kw und rpm", f"Motor({P}, {n}) stores power_kw and rpm")
    eM = P * 1000 / (2 * _m.pi * n / 60)
    check(approx(method(m, "torque"), eM), f"torque() ≈ {eM:.2f} Nm", f"torque() ≈ {eM:.2f} Nm")
    d = method(m, "describe")
    check(isinstance(d, str) and str(P) in d and str(n) in d, "describe() gibt einen Text mit Leistung und Drehzahl zurück", "describe() returns a text with power and speed")
''',
   require=["class"], refs=["10.3", "10.2"])

ex(id="k10-counter", ch="10", lvl=1,
   title={"de": "Stückzähler", "en": "Piece counter"},
   task={"de": "Schreiben Sie eine Klasse `PieceCounter` für eine Fertigungslinie. Ein neuer Zähler startet mit `good = 0` und `scrap = 0`.\n- `add_good(n=1)` und `add_scrap(n=1)` erhöhen den jeweiligen Zähler (Standardwert 1).\n- `total()` gibt die Gesamtzahl zurück.\n- `scrap_rate()` gibt den Ausschussanteil in Prozent zurück (0, solange noch nichts gezählt wurde).\n- `reset()` setzt beide Zähler auf 0.",
         "en": "Write a class `PieceCounter` for a production line. A new counter starts with `good = 0` and `scrap = 0`.\n- `add_good(n=1)` and `add_scrap(n=1)` increase the respective counter (default 1).\n- `total()` returns the total count.\n- `scrap_rate()` returns the scrap share in percent (0 as long as nothing has been counted).\n- `reset()` sets both counters to 0."},
   starter={"de": "class PieceCounter:\n    def __init__(self):\n        ...\n", "en": "class PieceCounter:\n    def __init__(self):\n        ...\n"},
   solution='class PieceCounter:\n    def __init__(self):\n        self.good = 0\n        self.scrap = 0\n\n    def add_good(self, n=1):\n        self.good += n\n\n    def add_scrap(self, n=1):\n        self.scrap += n\n\n    def total(self):\n        return self.good + self.scrap\n\n    def scrap_rate(self):\n        if self.total() == 0:\n            return 0\n        return self.scrap / self.total() * 100\n\n    def reset(self):\n        self.good = 0\n        self.scrap = 0\n\nc = PieceCounter()\nc.add_good(48)\nc.add_scrap(2)\nprint(c.total(), c.scrap_rate())\n',
   tests='''
ns, out = run()
c = call(ns, "PieceCounter")
check(getattr(c, "good", None) == 0 and getattr(c, "scrap", None) == 0 and approx(method(c, "scrap_rate"), 0), "Neuer Zähler: 0 / 0, Ausschussanteil 0", "New counter: 0 / 0, scrap rate 0")
method(c, "add_good"); method(c, "add_good", 47); method(c, "add_scrap", 2)
check(c.good == 48 and c.scrap == 2 and method(c, "total") == 50, "add_good(), add_good(47), add_scrap(2) → 48 gut, 2 Ausschuss, 50 gesamt", "add_good(), add_good(47), add_scrap(2) → 48 good, 2 scrap, 50 total")
check(approx(method(c, "scrap_rate"), 4.0), "Ausschussanteil 4 %", "scrap rate 4 %")
method(c, "add_scrap")
check(c.scrap == 3, "add_scrap() ohne Argument zählt 1", "add_scrap() without argument counts 1")
method(c, "reset")
check(c.good == 0 and c.scrap == 0 and method(c, "total") == 0, "reset() setzt alles auf 0", "reset() sets everything to 0")
''',
   require=["class", "default_arg"], refs=["10.3", "7.3p"])

ex(id="k10-measurement", ch="10", lvl=1,
   title={"de": "Messwert mit Einheit", "en": "Measurement with unit"},
   task={"de": "Schreiben Sie eine Klasse `Measurement(value, unit, uncertainty=0.0)`.\n- `__str__` liefert z.B. `12.5 V` bzw. mit Unsicherheit `12.5 ± 0.1 V` (nur wenn `uncertainty` größer als 0 ist).\n- `relative_uncertainty()` gibt die relative Unsicherheit in Prozent zurück (uncertainty / |value| · 100).\n\nTesten Sie mit `print(Measurement(12.5, \"V\", 0.1))`.",
         "en": "Write a class `Measurement(value, unit, uncertainty=0.0)`.\n- `__str__` returns e.g. `12.5 V`, or with uncertainty `12.5 ± 0.1 V` (only if `uncertainty` is greater than 0).\n- `relative_uncertainty()` returns the relative uncertainty in percent (uncertainty / |value| · 100).\n\nTest with `print(Measurement(12.5, \"V\", 0.1))`."},
   starter={"de": "class Measurement:\n    def __init__(self, value, unit, uncertainty=0.0):\n        ...\n", "en": "class Measurement:\n    def __init__(self, value, unit, uncertainty=0.0):\n        ...\n"},
   solution='class Measurement:\n    def __init__(self, value, unit, uncertainty=0.0):\n        self.value = value\n        self.unit = unit\n        self.uncertainty = uncertainty\n\n    def __str__(self):\n        if self.uncertainty > 0:\n            return f"{self.value} ± {self.uncertainty} {self.unit}"\n        return f"{self.value} {self.unit}"\n\n    def relative_uncertainty(self):\n        return self.uncertainty / abs(self.value) * 100\n\nprint(Measurement(12.5, "V", 0.1))\nprint(Measurement(3.3, "A"))\n',
   tests='''
ns, out = run()
m1 = call(ns, "Measurement", 12.5, "V", 0.1)
m2 = call(ns, "Measurement", 3.3, "A")
check(safe(lambda: str(m1)) == "12.5 ± 0.1 V", "str(Measurement(12.5, 'V', 0.1)) = '12.5 ± 0.1 V'", "str(Measurement(12.5, 'V', 0.1)) = '12.5 ± 0.1 V'")
check(safe(lambda: str(m2)) == "3.3 A", "str(Measurement(3.3, 'A')) = '3.3 A'", "str(Measurement(3.3, 'A')) = '3.3 A'")
check(approx(method(m1, "relative_uncertainty"), 0.8), "relative Unsicherheit 0.8 %", "relative uncertainty 0.8 %")
check(approx(method(call(ns, "Measurement", -50.0, "mV", 2.0), "relative_uncertainty"), 4.0), "Bei negativem Wert: Betrag verwenden (4 %)", "For a negative value: use the magnitude (4 %)")
''',
   require=["class", "magic"], refs=["10.7", "10.3"])

ex(id="k10-beams", ch="10", lvl=2,
   title={"de": "Profile und Polymorphie", "en": "Profiles and polymorphism"},
   task={"de": "Basisklasse `Profile(length)` (Länge in m) mit der Methode `weight(rho=7850)`: Masse in kg = Querschnittsfläche (m²) · Länge · Dichte. Die Fläche liefert die Methode `area()`, die in der Basisklasse `0` zurückgibt.\n\nAbgeleitete Klassen (Konstruktor mit `super().__init__(length)`), Maße in mm:\n- `RectProfile(length, b, h)`: Rechteck-Vollprofil\n- `TubeProfile(length, d_out, d_in)`: Rundrohr, A = π/4 · (D² − d²)\n\nBeide überschreiben nur `area()` (Ergebnis in m²!). `weight()` wird **nicht** überschrieben.",
         "en": "Base class `Profile(length)` (length in m) with the method `weight(rho=7850)`: mass in kg = cross-sectional area (m²) · length · density. The area comes from the method `area()`, which returns `0` in the base class.\n\nDerived classes (constructor with `super().__init__(length)`), dimensions in mm:\n- `RectProfile(length, b, h)`: solid rectangular profile\n- `TubeProfile(length, d_out, d_in)`: round tube, A = π/4 · (D² − d²)\n\nBoth override only `area()` (result in m²!). `weight()` is **not** overridden."},
   starter={"de": "import math\n\nclass Profile:\n    def __init__(self, length):\n        self.length = length\n", "en": "import math\n\nclass Profile:\n    def __init__(self, length):\n        self.length = length\n"},
   solution='import math\n\nclass Profile:\n    def __init__(self, length):\n        self.length = length\n\n    def area(self):\n        return 0\n\n    def weight(self, rho=7850):\n        return self.area() * self.length * rho\n\n\nclass RectProfile(Profile):\n    def __init__(self, length, b, h):\n        super().__init__(length)\n        self.b = b\n        self.h = h\n\n    def area(self):\n        return self.b * self.h / 1e6\n\n\nclass TubeProfile(Profile):\n    def __init__(self, length, d_out, d_in):\n        super().__init__(length)\n        self.d_out = d_out\n        self.d_in = d_in\n\n    def area(self):\n        return math.pi / 4 * (self.d_out**2 - self.d_in**2) / 1e6\n\nfor p in [RectProfile(2.0, 40, 20), TubeProfile(2.0, 48.3, 40.3)]:\n    print(type(p).__name__, round(p.weight(), 2), "kg")\n',
   tests='''
import math as _m
ns, out = run()
r = call(ns, "RectProfile", 2.0, 40, 20)
t = call(ns, "TubeProfile", 3.0, 48.3, 40.3)
check(isinstance(r, ns["Profile"]) and isinstance(t, ns["Profile"]), "Beide Klassen erben von Profile", "Both classes inherit from Profile")
check(getattr(r, "length", None) == 2.0 and getattr(t, "length", None) == 3.0, "length wird über super().__init__ gesetzt", "length is set via super().__init__")
check(approx(method(r, "area"), 0.0008) and approx(method(r, "weight"), 0.0008 * 2 * 7850), "Rechteck 40×20, 2 m: 12.56 kg", "Rectangle 40×20, 2 m: 12.56 kg")
eA = _m.pi / 4 * (48.3**2 - 40.3**2) / 1e6
check(approx(method(t, "area"), eA) and approx(method(t, "weight"), eA * 3 * 7850), f"Rohr 48.3×4, 3 m: {eA*3*7850:.2f} kg", f"Tube 48.3×4, 3 m: {eA*3*7850:.2f} kg")
check(approx(method(t, "weight", 2700), eA * 3 * 2700), "weight(2700) für Aluminium", "weight(2700) for aluminium")
check("weight" not in vars(ns["RectProfile"]) and "weight" not in vars(ns["TubeProfile"]), "weight() wird nur in der Basisklasse definiert", "weight() is only defined in the base class")
''',
   require=["class", "super"], refs=["10.5", "10.3"])

ex(id="k10-inventory", ch="10", lvl=2,
   title={"de": "Lagerverwaltung mit Objekten", "en": "Inventory with objects"},
   task={"de": "Zwei Klassen:\n- `Part(number, name, price, quantity)` mit der Methode `value()` = Preis · Menge.\n- `Inventory()` mit dem Attribut `parts` (leere Liste) und den Methoden\n  - `add(part)`: fügt ein `Part` hinzu\n  - `find(number)`: gibt das `Part` mit dieser Teilenummer zurück oder `None`\n  - `total_value()`: Gesamtwert des Lagers\n  - `low_stock(limit)`: Liste der Teilenummern aller Teile mit weniger als `limit` Stück",
         "en": "Two classes:\n- `Part(number, name, price, quantity)` with the method `value()` = price · quantity.\n- `Inventory()` with the attribute `parts` (empty list) and the methods\n  - `add(part)`: adds a `Part`\n  - `find(number)`: returns the `Part` with this part number or `None`\n  - `total_value()`: total value of the inventory\n  - `low_stock(limit)`: list of the part numbers of all parts with fewer than `limit` pieces"},
   starter={"de": "class Part:\n    def __init__(self, number, name, price, quantity):\n        ...\n\nclass Inventory:\n    def __init__(self):\n        ...\n", "en": "class Part:\n    def __init__(self, number, name, price, quantity):\n        ...\n\nclass Inventory:\n    def __init__(self):\n        ...\n"},
   solution="class Part:\n    def __init__(self, number, name, price, quantity):\n        self.number = number\n        self.name = name\n        self.price = price\n        self.quantity = quantity\n\n    def value(self):\n        return self.price * self.quantity\n\n\nclass Inventory:\n    def __init__(self):\n        self.parts = []\n\n    def add(self, part):\n        self.parts.append(part)\n\n    def find(self, number):\n        for part in self.parts:\n            if part.number == number:\n                return part\n        return None\n\n    def total_value(self):\n        total = 0\n        for part in self.parts:\n            total += part.value()\n        return total\n\n    def low_stock(self, limit):\n        return [p.number for p in self.parts if p.quantity < limit]\n\ninv = Inventory()\ninv.add(Part('M8-40', 'Schraube M8x40', 0.12, 500))\ninv.add(Part('L-6204', 'Kugellager 6204', 4.80, 6))\nprint(inv.total_value(), inv.low_stock(10))\n",
   tests='''
ns, out = run()
inv = call(ns, "Inventory")
check(getattr(inv, "parts", None) == [], "Neues Inventory hat eine leere Liste parts", "A new Inventory has an empty list parts")
p1 = call(ns, "Part", "M8-40", "Schraube M8x40", 0.12, 500)
p2 = call(ns, "Part", "L-6204", "Kugellager 6204", 4.80, 6)
p3 = call(ns, "Part", "D-35", "Dichtring", 1.50, 9)
check(approx(method(p2, "value"), 28.8), "Part.value() = Preis · Menge", "Part.value() = price · quantity")
for p in (p1, p2, p3):
    method(inv, "add", p)
check(method(inv, "find", "L-6204") is p2 and method(inv, "find", "X-1") is None, "find() liefert das Objekt bzw. None", "find() returns the object or None")
check(approx(method(inv, "total_value"), 60 + 28.8 + 13.5), "total_value() = 102.30", "total_value() = 102.30")
check(sorted(method(inv, "low_stock", 10)) == ["D-35", "L-6204"] and method(inv, "low_stock", 9) == ["L-6204"] and method(inv, "low_stock", 5) == [], "low_stock(10) = ['L-6204', 'D-35'], low_stock(9) = ['L-6204'], low_stock(5) = []", "low_stock(10) = ['L-6204', 'D-35'], low_stock(9) = ['L-6204'], low_stock(5) = []")
''',
   require=["class"], refs=["10.5", "10.3"])

ex(id="k10-resistor-ops", ch="10", lvl=3,
   title={"de": "Widerstände vergleichen und sortieren", "en": "Comparing and sorting resistors"},
   task={"de": "Erweitern Sie die Idee eines Widerstands-Objekts: Klasse `R(ohm)` mit\n- `__add__`: Reihenschaltung, Ergebnis ist ein neues `R`\n- `parallel(other)`: Parallelschaltung, Ergebnis ist ein neues `R`\n- `__eq__` und `__lt__`: Vergleich über den Widerstandswert (dann funktioniert auch `sorted()` mit einer Liste von `R`-Objekten!)\n- `__str__`: `470 Ω` bzw. ab 1000 Ω in kΩ mit einer Nachkommastelle, z.B. `4.7 kΩ`",
         "en": "Extend the idea of a resistor object: class `R(ohm)` with\n- `__add__`: series connection, result is a new `R`\n- `parallel(other)`: parallel connection, result is a new `R`\n- `__eq__` and `__lt__`: comparison by resistance value (then `sorted()` also works on a list of `R` objects!)\n- `__str__`: `470 Ω`, or from 1000 Ω on in kΩ with one decimal, e.g. `4.7 kΩ`"},
   starter={"de": "class R:\n    def __init__(self, ohm):\n        self.ohm = ohm\n", "en": "class R:\n    def __init__(self, ohm):\n        self.ohm = ohm\n"},
   solution='class R:\n    def __init__(self, ohm):\n        self.ohm = ohm\n\n    def __add__(self, other):\n        return R(self.ohm + other.ohm)\n\n    def parallel(self, other):\n        return R(self.ohm * other.ohm / (self.ohm + other.ohm))\n\n    def __eq__(self, other):\n        return isinstance(other, R) and self.ohm == other.ohm\n\n    def __lt__(self, other):\n        return self.ohm < other.ohm\n\n    def __str__(self):\n        if self.ohm >= 1000:\n            return f"{self.ohm / 1000:.1f} kΩ"\n        return f"{self.ohm} Ω"\n\nparts = [R(4700), R(220), R(1000)]\nprint([str(p) for p in sorted(parts)])\nprint(R(220) + R(250), R(100).parallel(R(100)))\n',
   tests='''
ns, out = run()
Rc = ns.get("R")
a = call(ns, "R", 220); b = call(ns, "R", 250)
s = safe(lambda: a + b)
check(isinstance(s, Rc) and s.ohm == 470, "R(220) + R(250) = R(470)", "R(220) + R(250) = R(470)")
p = method(call(ns, "R", 100), "parallel", call(ns, "R", 300))
check(isinstance(p, Rc) and approx(p.ohm, 75), "R(100) parallel R(300) = R(75)", "R(100) parallel R(300) = R(75)")
check(safe(lambda: a == call(ns, "R", 220)) is True and safe(lambda: a == b) is False, "== vergleicht die Werte", "== compares the values")
lst = [call(ns, "R", 4700), call(ns, "R", 220), call(ns, "R", 1000)]
srt = safe(lambda: sorted(lst))
check([x.ohm for x in srt] == [220, 1000, 4700], "sorted() sortiert nach Widerstand", "sorted() sorts by resistance")
check(safe(lambda: str(call(ns, "R", 470))) == "470 Ω" and safe(lambda: str(call(ns, "R", 4700))) == "4.7 kΩ" and safe(lambda: str(call(ns, "R", 1000))) == "1.0 kΩ", "str: '470 Ω', '4.7 kΩ' und '1.0 kΩ'", "str: '470 Ω', '4.7 kΩ' and '1.0 kΩ'")
''',
   require=["class", "magic"], refs=["10.7"])

ex(id="k10-polynomial", ch="10", lvl=3,
   title={"de": "Klasse Polynom", "en": "Class Polynomial"},
   task={"de": "Schreiben Sie `Polynomial(coeffs)`. `coeffs` ist eine Liste der Koeffizienten, beginnend beim konstanten Glied: `[1, 0, -2]` steht für 1 − 2x².\n- `evaluate(x)`: Wert an der Stelle x\n- `derivative()`: neues `Polynomial` der Ableitung (`[1, 0, -2]` → `[0, -4]`; die Ableitung einer Konstanten ist `[0]`)\n- `__add__`: Summe zweier Polynome (auch unterschiedlichen Grades)\n- `degree()`: Grad (Index des höchsten Koeffizienten ≠ 0; für das Nullpolynom 0)",
         "en": "Write `Polynomial(coeffs)`. `coeffs` is a list of coefficients starting with the constant term: `[1, 0, -2]` means 1 − 2x².\n- `evaluate(x)`: value at x\n- `derivative()`: new `Polynomial` of the derivative (`[1, 0, -2]` → `[0, -4]`; the derivative of a constant is `[0]`)\n- `__add__`: sum of two polynomials (even of different degree)\n- `degree()`: degree (index of the highest coefficient ≠ 0; 0 for the zero polynomial)"},
   starter={"de": "class Polynomial:\n    def __init__(self, coeffs):\n        self.coeffs = list(coeffs)\n", "en": "class Polynomial:\n    def __init__(self, coeffs):\n        self.coeffs = list(coeffs)\n"},
   solution='class Polynomial:\n    def __init__(self, coeffs):\n        self.coeffs = list(coeffs)\n\n    def evaluate(self, x):\n        total = 0\n        for k, c in enumerate(self.coeffs):\n            total += c * x**k\n        return total\n\n    def derivative(self):\n        if len(self.coeffs) <= 1:\n            return Polynomial([0])\n        return Polynomial([k * self.coeffs[k] for k in range(1, len(self.coeffs))])\n\n    def __add__(self, other):\n        n = max(len(self.coeffs), len(other.coeffs))\n        a = self.coeffs + [0] * (n - len(self.coeffs))\n        b = other.coeffs + [0] * (n - len(other.coeffs))\n        return Polynomial([x + y for x, y in zip(a, b)])\n\n    def degree(self):\n        d = 0\n        for k, c in enumerate(self.coeffs):\n            if c != 0:\n                d = k\n        return d\n\np = Polynomial([-1, -2, 1, 1])\nprint(p.evaluate(1.0), p.derivative().coeffs, p.degree())\n',
   tests='''
ns, out = run()
P = ns.get("Polynomial")
p = call(ns, "Polynomial", [1, 0, -2])
for x in [0, 1.5, -2]:
    check(approx(method(p, "evaluate", x), 1 - 2 * x * x), f"1 − 2x² bei x = {x}: {1 - 2*x*x}", f"1 − 2x² at x = {x}: {1 - 2*x*x}")
d = method(p, "derivative")
check(isinstance(d, P) and d.coeffs == [0, -4], "Ableitung von [1, 0, -2] ist [0, -4]", "Derivative of [1, 0, -2] is [0, -4]")
check(method(call(ns, "Polynomial", [5]), "derivative").coeffs == [0] and method(call(ns, "Polynomial", [3, 5]), "derivative").coeffs == [5], "Ableitung einer Konstanten ist [0], von 3 + 5x ist sie [5]", "Derivative of a constant is [0], of 3 + 5x it is [5]")
s = safe(lambda: call(ns, "Polynomial", [1, 2]) + call(ns, "Polynomial", [0, 1, 3]))
s2 = safe(lambda: call(ns, "Polynomial", [0, 1, 3]) + call(ns, "Polynomial", [1, 2]))
check(isinstance(s, P) and s.coeffs == [1, 3, 3] and isinstance(s2, P) and s2.coeffs == [1, 3, 3], "[1, 2] + [0, 1, 3] = [0, 1, 3] + [1, 2] = [1, 3, 3]", "[1, 2] + [0, 1, 3] = [0, 1, 3] + [1, 2] = [1, 3, 3]")
check(method(call(ns, "Polynomial", [-1, -2, 1, 1]), "degree") == 3 and method(call(ns, "Polynomial", [2, 0, 0]), "degree") == 0 and method(call(ns, "Polynomial", [0]), "degree") == 0, "degree(): 3 für x³+…, 0 für [2, 0, 0] und [0]", "degree(): 3 for x³+…, 0 for [2, 0, 0] and [0]")
''',
   require=["class", "magic"], refs=["10.7", "10.3"])
