from exlib import ex

# Kapitel 7, zweiter Satz: zusätzlich def, return, Standardargumente, Keyword-Argumente, *args, global,
# isinstance, sum/max/min/sorted, divmod, Docstrings, Typ-Annotationen.
# Kein Slicing, keine Dicts/Sets, keine Comprehensions, kein zip/enumerate.

# ------------------------------------------------------------------ Stufe 1
ex(id="k7-frequency", ch="7", lvl=1,
   title={"de": "Funktionen rund um die Frequenz", "en": "Functions around frequency"},
   task={"de": "Schreiben Sie drei Funktionen, die ihr Ergebnis **zurückgeben**:\n- `period(f)`: die Periodendauer $T = 1/f$ in s\n- `angular(f)`: die Kreisfrequenz $\\omega = 2\\pi f$ in 1/s (verwenden Sie die vorgegebene Konstante `PI`)\n- `wavelength(f, c=3e8)`: die Wellenlänge $\\lambda = c/f$; der optionale Parameter `c` ist die Ausbreitungsgeschwindigkeit (Standard: Licht im Vakuum)\n\nRufen Sie `wavelength` einmal mit dem Standardwert und einmal für Schall in Luft mit `c=343` als Keyword-Argument auf.",
         "en": "Write three functions that **return** their result:\n- `period(f)`: the period $T = 1/f$ in s\n- `angular(f)`: the angular frequency $\\omega = 2\\pi f$ in 1/s (use the given constant `PI`)\n- `wavelength(f, c=3e8)`: the wavelength $\\lambda = c/f$; the optional parameter `c` is the propagation speed (default: light in a vacuum)\n\nCall `wavelength` once with the default value and once for sound in air with `c=343` as a keyword argument."},
   starter={"de": "PI = 3.14159\n\ndef period(f):\n    ...\n", "en": "PI = 3.14159\n\ndef period(f):\n    ...\n"},
   solution='PI = 3.14159\n\ndef period(f):\n    return 1 / f\n\ndef angular(f):\n    return 2 * PI * f\n\ndef wavelength(f, c=3e8):\n    return c / f\n\nprint(period(50), angular(50), wavelength(100e6), wavelength(440, c=343))\n',
   tests='''
ns, out = run()
for f in [50, 1000, 2.4e9]:
    check(approx(call(ns, "period", f), 1 / f) and approx(call(ns, "angular", f), 2 * 3.14159 * f), f"f = {f:g} Hz: T = {1/f:.3g} s, ω = {2*3.14159*f:.4g} 1/s", f"f = {f:g} Hz: T = {1/f:.3g} s, ω = {2*3.14159*f:.4g} 1/s")
    check(approx(call(ns, "wavelength", f), 3e8 / f), f"wavelength({f:g}) = {3e8/f:.4g} m", f"wavelength({f:g}) = {3e8/f:.4g} m")
check(approx(call(ns, "wavelength", 440, c=343), 343 / 440), "wavelength(440, c=343) ≈ 0.78 m (Schall)", "wavelength(440, c=343) ≈ 0.78 m (sound)")
''',
   require=["def", "return", "default_arg"], refs=["7.3r", "7.3p"])

ex(id="k7-printbug", ch="7", lvl=1,
   title={"de": "Fehler finden: print statt return", "en": "Find the bug: print instead of return"},
   task={"de": "Die Funktion `kinetic_energy(m, v)` im Editor soll die Bewegungsenergie $E = \\frac{1}{2} m v^2$ eines Fahrzeugs (in J) liefern. Darauf aufbauend soll `braking_heat(m, v1, v2)` berechnen, wie viel Energie beim Abbremsen von `v1` auf `v2` in Wärme umgewandelt wird. Das Programm stürzt jedoch ab. Lesen Sie die Fehlermeldung, finden Sie die Ursache und korrigieren Sie **beide** Funktionen, sodass sie ihr Ergebnis zurückgeben.",
         "en": "The function `kinetic_energy(m, v)` in the editor is supposed to deliver the kinetic energy $E = \\frac{1}{2} m v^2$ of a vehicle (in J). Building on it, `braking_heat(m, v1, v2)` should compute how much energy is turned into heat when braking from `v1` to `v2`. However, the program crashes. Read the error message, find the cause and fix **both** functions so that they return their result."},
   starter={"de": "def kinetic_energy(m, v):\n    print(0.5 * m * v**2)\n\ndef braking_heat(m, v1, v2):\n    print(kinetic_energy(m, v1) - kinetic_energy(m, v2))\n\nbraking_heat(1500, 27.8, 13.9)\n", "en": "def kinetic_energy(m, v):\n    print(0.5 * m * v**2)\n\ndef braking_heat(m, v1, v2):\n    print(kinetic_energy(m, v1) - kinetic_energy(m, v2))\n\nbraking_heat(1500, 27.8, 13.9)\n"},
   solution='def kinetic_energy(m, v):\n    return 0.5 * m * v**2\n\ndef braking_heat(m, v1, v2):\n    return kinetic_energy(m, v1) - kinetic_energy(m, v2)\n\nprint(braking_heat(1500, 27.8, 13.9))\n',
   tests='''
ns, out = run()
for m, v in [(1500, 27.8), (80, 5.0), (2, 0.0)]:
    r = call(ns, "kinetic_energy", m, v)
    check(r is not None and approx(r, 0.5 * m * v * v), f"kinetic_energy({m}, {v}) gibt {0.5*m*v*v:g} J zurück", f"kinetic_energy({m}, {v}) returns {0.5*m*v*v:g} J")
for m, a, b in [(1500, 27.8, 13.9), (1000, 10.0, 0.0)]:
    r = call(ns, "braking_heat", m, a, b)
    check(r is not None and approx(r, 0.5 * m * (a * a - b * b)), f"braking_heat({m}, {a}, {b}) = {0.5*m*(a*a-b*b):g} J", f"braking_heat({m}, {a}, {b}) = {0.5*m*(a*a-b*b):g} J")
''',
   require=["def", "return"], refs=["7.3r"])

ex(id="k7-annotated", ch="7", lvl=1,
   title={"de": "Dokumentierte Funktion: Biegemoment", "en": "Documented function: bending moment"},
   task={"de": "Ein Kragarm der Länge `length` (m) trägt am Ende die Einzellast `force` (N) und zusätzlich über die ganze Länge die Streckenlast `q` (N/m). Das Biegemoment an der Einspannung ist $M = \\mathit{force} \\cdot \\mathit{length} + q \\cdot \\mathit{length}^2/2$.\n\nSchreiben Sie `clamp_moment(force: float, length: float, q: float = 0.0) -> float` mit genau diesen **Typ-Annotationen** und einem **Docstring**, der Parameter und Rückgabewert (mit Einheiten) beschreibt. Rufen Sie `help(clamp_moment)` auf, um sich Ihre Dokumentation anzusehen.",
         "en": "A cantilever of length `length` (m) carries the point load `force` (N) at its end and in addition the distributed load `q` (N/m) along its whole length. The bending moment at the clamped end is $M = \\mathit{force} \\cdot \\mathit{length} + q \\cdot \\mathit{length}^2/2$.\n\nWrite `clamp_moment(force: float, length: float, q: float = 0.0) -> float` with exactly these **type annotations** and a **docstring** describing parameters and return value (with units). Call `help(clamp_moment)` to look at your documentation."},
   starter={"de": "def clamp_moment(force, length, q=0.0):\n    ...\n", "en": "def clamp_moment(force, length, q=0.0):\n    ...\n"},
   solution='def clamp_moment(force: float, length: float, q: float = 0.0) -> float:\n    """Biegemoment an der Einspannung eines Kragarms.\n\n    Args:\n        force (float): Einzellast am freien Ende in N.\n        length (float): Länge des Kragarms in m.\n        q (float): Streckenlast in N/m (Standard: 0).\n\n    Returns:\n        float: Einspannmoment in Nm.\n    """\n    return force * length + q * length**2 / 2\n\nhelp(clamp_moment)\nprint(clamp_moment(500, 1.2, q=200))\n',
   tests='''
ns, out = run()
for F, L, q in [(500, 1.2, 200), (1000, 2.0, 0), (0, 3.0, 50)]:
    r = call(ns, "clamp_moment", F, L, q) if q else call(ns, "clamp_moment", F, L)
    check(approx(r, F * L + q * L * L / 2), f"F = {F} N, L = {L} m, q = {q} N/m: M = {F*L + q*L*L/2:g} Nm", f"F = {F} N, L = {L} m, q = {q} N/m: M = {F*L + q*L*L/2:g} Nm")
f = ns["clamp_moment"]
ann = getattr(f, "__annotations__", {})
check(ann.get("force") is float and ann.get("length") is float and ann.get("q") is float and ann.get("return") is float, "Typ-Annotationen für alle Parameter und den Rückgabewert", "Type annotations for all parameters and the return value")
doc = (f.__doc__ or "").strip()
check(len(doc) >= 30 and doc != "...", "Aussagekräftiger Docstring vorhanden", "Meaningful docstring present")
''',
   require=["def", "annot"], refs=["7.8", "7.3p"])

ex(id="k7-section", ch="7", lvl=1,
   title={"de": "Querschnittswerte als Rückgabewerte", "en": "Section properties as return values"},
   task={"de": "Schreiben Sie `rect_section(b, h)` für einen Rechteckquerschnitt (Maße in mm). Die Funktion gibt **zwei Werte** zurück: die Fläche $A = b h$ (mm²) und das Widerstandsmoment $W = b h^2/6$ (mm³).\n\nRufen Sie die Funktion mit **Keyword-Argumenten** in vertauschter Reihenfolge auf (`rect_section(h=…, b=…)`), entpacken Sie das Ergebnis in die Variablen `area` und `modulus` und berechnen Sie daraus die Biegespannung `sigma = M / W` für das Biegemoment `M` (Nmm).",
         "en": "Write `rect_section(b, h)` for a rectangular cross-section (dimensions in mm). The function returns **two values**: the area $A = b h$ (mm²) and the section modulus $W = b h^2/6$ (mm³).\n\nCall the function with **keyword arguments** in swapped order (`rect_section(h=…, b=…)`), unpack the result into the variables `area` and `modulus`, and compute from it the bending stress `sigma = M / W` for the bending moment `M` (Nmm)."},
   starter={"de": "M = 2.4e6   # Nmm\nb = 40      # mm\nh = 80      # mm\n\ndef rect_section(b, h):\n    ...\n", "en": "M = 2.4e6   # Nmm\nb = 40      # mm\nh = 80      # mm\n\ndef rect_section(b, h):\n    ...\n"},
   solution='M = 2.4e6\nb = 40\nh = 80\n\ndef rect_section(b, h):\n    return b * h, b * h**2 / 6\n\narea, modulus = rect_section(h=h, b=b)\nsigma = M / modulus\nprint(area, modulus, round(sigma, 1))\n',
   tests='''
ns, out = run()
for b, h in [(40, 80), (100, 10), (25, 25)]:
    r = call(ns, "rect_section", b, h)
    check(isinstance(r, tuple) and len(r) == 2 and approx(r[0], b * h) and approx(r[1], b * h * h / 6), f"rect_section({b}, {h}) = ({b*h}, {b*h*h/6:g})", f"rect_section({b}, {h}) = ({b*h}, {b*h*h/6:g})")
for M, b, h in [(2.4e6, 40, 80), (5e5, 20, 50)]:
    ns, out = run(sub={"M": M, "b": b, "h": h})
    a, w, s = need(ns, "area", "modulus", "sigma")
    check(approx(a, b * h) and approx(w, b * h * h / 6) and approx(s, M / (b * h * h / 6)), f"M = {M:g} Nmm, {b}×{h} mm: σ = {M / (b*h*h/6):.1f} N/mm²", f"M = {M:g} Nmm, {b}×{h} mm: σ = {M / (b*h*h/6):.1f} N/mm²")
''',
   require=["def", "return", "kwargs_call"], refs=["7.3r", "7.3k"])

ex(id="k7-loadprofile", ch="7", lvl=1,
   title={"de": "Lastgang eines Tages", "en": "Daily load profile"},
   task={"de": "Die Liste `load` enthält die mittlere Leistung (kW) für jede Stunde eines Tages, beginnend um 0 Uhr. Schreiben Sie mit den eingebauten Funktionen `max`, `min`, `sum` und der Methode `index`:\n- `peak_hour(load)`: die Stunde (Index), in der die Leistung am größten ist\n- `energy(load)`: die Energie des Tages in kWh (jede Stunde: Leistung · 1 h)\n- `spread(load)`: den Unterschied zwischen größter und kleinster Leistung\n\nAlle drei Funktionen geben ihr Ergebnis zurück.",
         "en": "The list `load` contains the mean power (kW) for each hour of a day, starting at midnight. Using the built-in functions `max`, `min`, `sum` and the method `index`, write:\n- `peak_hour(load)`: the hour (index) in which the power is greatest\n- `energy(load)`: the day's energy in kWh (each hour: power · 1 h)\n- `spread(load)`: the difference between the largest and the smallest power\n\nAll three functions return their result."},
   starter={"de": "load = [3.2, 2.9, 2.8, 2.8, 3.0, 4.1, 7.9, 9.6, 8.8, 8.1, 7.7, 8.4,\n        9.9, 9.2, 8.0, 7.6, 7.9, 8.8, 9.4, 8.1, 6.2, 5.0, 4.1, 3.5]\n\ndef peak_hour(load):\n    ...\n", "en": "load = [3.2, 2.9, 2.8, 2.8, 3.0, 4.1, 7.9, 9.6, 8.8, 8.1, 7.7, 8.4,\n        9.9, 9.2, 8.0, 7.6, 7.9, 8.8, 9.4, 8.1, 6.2, 5.0, 4.1, 3.5]\n\ndef peak_hour(load):\n    ...\n"},
   solution='load = [3.2, 2.9, 2.8, 2.8, 3.0, 4.1, 7.9, 9.6, 8.8, 8.1, 7.7, 8.4,\n        9.9, 9.2, 8.0, 7.6, 7.9, 8.8, 9.4, 8.1, 6.2, 5.0, 4.1, 3.5]\n\ndef peak_hour(load):\n    return load.index(max(load))\n\ndef energy(load):\n    return sum(load) * 1\n\ndef spread(load):\n    return max(load) - min(load)\n\nprint(peak_hour(load), round(energy(load), 1), round(spread(load), 1))\n',
   tests='''
ns, out = run()
for l in [[3.2, 2.9, 2.8, 2.8, 3.0, 4.1, 7.9, 9.6, 8.8, 8.1, 7.7, 8.4, 9.9, 9.2, 8.0, 7.6, 7.9, 8.8, 9.4, 8.1, 6.2, 5.0, 4.1, 3.5], [1.0, 5.0, 5.0, 2.0], [4.4]]:
    check(call(ns, "peak_hour", l) == l.index(max(l)), f"peak_hour = {l.index(max(l))}", f"peak_hour = {l.index(max(l))}")
    check(approx(call(ns, "energy", l), sum(l)) and approx(call(ns, "spread", l), max(l) - min(l)), f"energy = {sum(l):.1f} kWh, spread = {max(l) - min(l):.1f} kW", f"energy = {sum(l):.1f} kWh, spread = {max(l) - min(l):.1f} kW")
''',
   require=["def", "seqfuncs"], refs=["7.2s", "7.3r"])

# ------------------------------------------------------------------ Stufe 2
ex(id="k7-inplace", ch="7", lvl=2,
   title={"de": "Liste verändern oder neue Liste?", "en": "Change the list or a new list?"},
   task={"de": "Messwerte eines Dehnungsmessstreifens sollen mit einem Kalibrierfaktor `k` multipliziert werden. Schreiben Sie zwei Varianten:\n- `scale_inplace(values, k)`: verändert die **übergebene** Liste selbst (jeder Eintrag wird mit k multipliziert, Indexzugriff `values[i] = …`) und gibt **nichts** zurück.\n- `scaled(values, k)`: lässt die übergebene Liste unverändert und gibt eine **neue** Liste mit den skalierten Werten in derselben Reihenfolge zurück.\n\nProbieren Sie beide mit derselben Liste aus und beobachten Sie den Unterschied (Stichwort: Funktionsaufrufe mit mutable Datentypen).",
         "en": "Readings from a strain gauge are to be multiplied by a calibration factor `k`. Write two variants:\n- `scale_inplace(values, k)`: changes the list **passed in** itself (each entry is multiplied by k, indexing `values[i] = …`) and returns **nothing**.\n- `scaled(values, k)`: leaves the list passed in unchanged and returns a **new** list with the scaled values in the same order.\n\nTry both with the same list and observe the difference (keyword: function calls with mutable data types)."},
   starter={"de": "def scale_inplace(values, k):\n    ...\n\ndef scaled(values, k):\n    ...\n", "en": "def scale_inplace(values, k):\n    ...\n\ndef scaled(values, k):\n    ...\n"},
   solution='def scale_inplace(values, k):\n    for i in range(len(values)):\n        values[i] = values[i] * k\n\ndef scaled(values, k):\n    result = []\n    for v in values:\n        result.append(v * k)\n    return result\n\ndata = [1.0, 2.0, 3.0]\nnew = scaled(data, 2)\nprint(data, new)\nscale_inplace(data, 2)\nprint(data)\n',
   tests='''
ns, out = run()
for v, k in [([1.0, 2.0, 3.0], 2), ([0.5, -4.0], 0.1), ([], 3)]:
    a = list(v)
    r = call(ns, "scale_inplace", a, k)
    check(r is None and len(a) == len(v) and all(approx(x, y * k) for x, y in zip(a, v)), f"scale_inplace({v}, {k}) verändert die Liste und gibt None zurück", f"scale_inplace({v}, {k}) changes the list and returns None")
    b = list(v)
    r = call(ns, "scaled", b, k)
    check(b == v, f"scaled({v}, {k}) lässt die Liste unverändert", f"scaled({v}, {k}) leaves the list unchanged")
    check(isinstance(r, list) and r is not b and len(r) == len(v) and all(approx(x, y * k) for x, y in zip(r, v)), f"scaled liefert eine neue Liste {[y * k for y in v]}", f"scaled returns a new list {[y * k for y in v]}")
''',
   require=["def", "return"], refs=["7.7", "5.4s"])

ex(id="k7-weighted", ch="7", lvl=2,
   title={"de": "Gewichteter Mittelwert", "en": "Weighted mean"},
   task={"de": "Bei einer Mischung mehrerer Kühlmittelströme ergibt sich die Mischtemperatur als gewichteter Mittelwert: $T = \\dfrac{\\sum_i m_i T_i}{\\sum_i m_i}$ mit den Massenströmen $m_i$ als Gewichten.\n\nSchreiben Sie `weighted_mean(values, weights)`. Sie gibt `None` zurück, wenn die Listen unterschiedlich lang oder leer sind oder die Summe der Gewichte 0 ist. Sonst gibt sie den gewichteten Mittelwert zurück. Verwenden Sie eine Schleife über die Indizes (`zip` kommt erst in Kapitel 8).",
         "en": "When several coolant flows are mixed, the mixing temperature is the weighted mean: $T = \\dfrac{\\sum_i m_i T_i}{\\sum_i m_i}$ with the mass flows $m_i$ as weights.\n\nWrite `weighted_mean(values, weights)`. It returns `None` if the lists differ in length or are empty, or if the sum of the weights is 0. Otherwise it returns the weighted mean. Use a loop over the indices (`zip` only comes in chapter 8)."},
   starter={"de": "def weighted_mean(values, weights):\n    ...\n", "en": "def weighted_mean(values, weights):\n    ...\n"},
   solution='def weighted_mean(values, weights):\n    if len(values) != len(weights) or len(values) == 0:\n        return None\n    total_weight = sum(weights)\n    if total_weight == 0:\n        return None\n    total = 0\n    for i in range(len(values)):\n        total += values[i] * weights[i]\n    return total / total_weight\n\nprint(weighted_mean([20.0, 60.0], [3.0, 1.0]))\n',
   tests='''
ns, out = run()
for v, w in [([20.0, 60.0], [3.0, 1.0]), ([15.0, 25.0, 35.0], [1, 1, 2]), ([42.0], [0.5])]:
    e = sum(a * b for a, b in zip(v, w)) / sum(w)
    check(approx(call(ns, "weighted_mean", v, w), e), f"weighted_mean({v}, {w}) = {e:g}", f"weighted_mean({v}, {w}) = {e:g}")
check(call(ns, "weighted_mean", [1.0, 2.0], [1.0]) is None, "Unterschiedlich lange Listen → None", "Lists of different length → None")
check(call(ns, "weighted_mean", [], []) is None and call(ns, "weighted_mean", [5.0, 6.0], [0, 0]) is None, "Leere Listen oder Gewichtssumme 0 → None", "Empty lists or weight sum 0 → None")
''',
   require=["def", "return"], forbid=["enumzip"], refs=["7.3r", "6.2b"])

ex(id="k7-tomm", ch="7", lvl=2,
   title={"de": "Maßangaben vereinheitlichen", "en": "Unifying dimension entries"},
   task={"de": "In einer Stückliste stehen Längen teils als Zahl (bereits in mm), teils als Text wie `\"12,5\"` oder `\"40\"` (ebenfalls mm, eventuell mit Dezimalkomma). Schreiben Sie `to_mm(value)`:\n- Ist `value` ein `int` oder `float`, wird es als `float` zurückgegeben.\n- Ist `value` ein `str`, wird ein Komma durch einen Punkt ersetzt und in `float` umgewandelt.\n- Für alle anderen Typen (z.B. `None`, Listen) wird `None` zurückgegeben.\n\nPrüfen Sie die Typen mit `isinstance`. Schreiben Sie außerdem `total_length(items)`, die die Summe aller umwandelbaren Einträge einer Liste liefert (nicht umwandelbare werden übersprungen). Sie dürfen annehmen, dass Texte immer gültige Zahlen enthalten.",
         "en": "In a parts list, lengths are sometimes numbers (already in mm), sometimes text like `\"12,5\"` or `\"40\"` (also mm, possibly with a decimal comma). Write `to_mm(value)`:\n- If `value` is an `int` or `float`, it is returned as a `float`.\n- If `value` is a `str`, a comma is replaced by a dot and it is converted to `float`.\n- For all other types (e.g. `None`, lists) `None` is returned.\n\nCheck the types with `isinstance`. Also write `total_length(items)` that returns the sum of all convertible entries of a list (non-convertible ones are skipped). You may assume that texts always contain valid numbers."},
   starter={"de": "def to_mm(value):\n    ...\n", "en": "def to_mm(value):\n    ...\n"},
   solution='def to_mm(value):\n    if isinstance(value, int) or isinstance(value, float):\n        return float(value)\n    if isinstance(value, str):\n        return float(value.replace(",", "."))\n    return None\n\ndef total_length(items):\n    total = 0.0\n    for item in items:\n        mm = to_mm(item)\n        if mm is not None:\n            total += mm\n    return total\n\nprint(to_mm("12,5"), total_length([100, "12,5", None, 7.5]))\n',
   tests='''
ns, out = run()
for v, e in [(100, 100.0), (7.5, 7.5), ("12,5", 12.5), ("40", 40.0), ("-3,25", -3.25)]:
    r = call(ns, "to_mm", v)
    check(isinstance(r, float) and approx(r, e), f"to_mm({v!r}) = {e}", f"to_mm({v!r}) = {e}")
check(call(ns, "to_mm", None) is None and call(ns, "to_mm", [1, 2]) is None, "None und Listen → None", "None and lists → None")
check(approx(call(ns, "total_length", [100, "12,5", None, 7.5, [3]]), 120.0) and approx(call(ns, "total_length", []), 0), "total_length([100, '12,5', None, 7.5, [3]]) = 120.0", "total_length([100, '12,5', None, 7.5, [3]]) = 120.0")
''',
   require=["def", "isinstance"], refs=["7.4", "5.2e"])

ex(id="k7-cutplan", ch="7", lvl=2,
   title={"de": "Zuschnittplan mit divmod", "en": "Cutting plan with divmod"},
   task={"de": "Aus Rohrstangen sollen Stücke der Länge `piece` geschnitten werden (alle Längen in mm, ganze Zahlen; Sägeschnitt vernachlässigt).\n- `cut(length, piece)` gibt mit der eingebauten Funktion `divmod` das Tupel (Anzahl Stücke, Reststück) für **eine** Stange zurück.\n- `cut_plan(lengths, piece)` bekommt eine Liste von Stangenlängen und gibt **zwei Werte** zurück: die Gesamtzahl der Stücke und den gesamten Verschnitt (Summe der Reststücke). Nutzen Sie dafür `cut`.",
         "en": "Pieces of length `piece` are to be cut from pipe bars (all lengths in mm, integers; saw cut neglected).\n- `cut(length, piece)` uses the built-in function `divmod` to return the tuple (number of pieces, remainder) for **one** bar.\n- `cut_plan(lengths, piece)` receives a list of bar lengths and returns **two values**: the total number of pieces and the total waste (sum of the remainders). Use `cut` for it."},
   starter={"de": "def cut(length, piece):\n    ...\n", "en": "def cut(length, piece):\n    ...\n"},
   solution='def cut(length, piece):\n    return divmod(length, piece)\n\ndef cut_plan(lengths, piece):\n    pieces = 0\n    waste = 0\n    for length in lengths:\n        n, rest = cut(length, piece)\n        pieces += n\n        waste += rest\n    return pieces, waste\n\nprint(cut(6000, 850), cut_plan([6000, 6000, 3500], 850))\n',
   tests='''
ns, out = run()
for L, p in [(6000, 850), (1000, 250), (300, 400)]:
    check(call(ns, "cut", L, p) == divmod(L, p), f"cut({L}, {p}) = {divmod(L, p)}", f"cut({L}, {p}) = {divmod(L, p)}")
for ls, p in [([6000, 6000, 3500], 850), ([1000], 333), ([], 100)]:
    e = (sum(L // p for L in ls), sum(L % p for L in ls))
    r = call(ns, "cut_plan", ls, p)
    check(isinstance(r, tuple) and tuple(r) == e, f"cut_plan({ls}, {p}) = {e}", f"cut_plan({ls}, {p}) = {e}")
''',
   require=["def", "divmod"], refs=["7.3r", "7.2"])

ex(id="k7-logger", ch="7", lvl=2,
   title={"de": "Fehler im Datenlogger", "en": "Bug in the data logger"},
   task={"de": "Die Funktion `log_event(event, log=[])` im Editor soll ein Ereignis an ein Protokoll anhängen und das Protokoll zurückgeben. Wird kein Protokoll übergeben, soll ein **neues** angelegt werden. Doch beim zweiten Aufruf ohne Protokoll taucht plötzlich das Ereignis des ersten Aufrufs wieder auf!\n\nFinden Sie die Ursache und beheben Sie den Fehler (Tipp: Standardwert `None`). Die Funktion soll weiterhin auch mit einem übergebenen Protokoll funktionieren.",
         "en": "The function `log_event(event, log=[])` in the editor is supposed to append an event to a log and return the log. If no log is passed, a **new** one should be created. But on the second call without a log, the event of the first call suddenly reappears!\n\nFind the cause and fix the bug (tip: default value `None`). The function should still work with a log passed in."},
   starter={"de": "def log_event(event, log=[]):\n    log.append(event)\n    return log\n\nprint(log_event(\"Start Pumpe 1\"))\nprint(log_event(\"Start Pumpe 2\"))\n", "en": "def log_event(event, log=[]):\n    log.append(event)\n    return log\n\nprint(log_event(\"Start pump 1\"))\nprint(log_event(\"Start pump 2\"))\n"},
   solution='def log_event(event, log=None):\n    if log is None:\n        log = []\n    log.append(event)\n    return log\n\nprint(log_event("Start Pumpe 1"))\nprint(log_event("Start Pumpe 2"))\n',
   tests='''
ns, out = run()
a = call(ns, "log_event", "A")
b = call(ns, "log_event", "B")
check(a == ["A"] and b == ["B"], "Zwei Aufrufe ohne Protokoll liefern ['A'] und ['B']", "Two calls without a log return ['A'] and ['B']")
check(a is not b, "Jeder Aufruf ohne Protokoll erzeugt eine neue Liste", "Every call without a log creates a new list")
mine = ["X"]
r = call(ns, "log_event", "Y", mine)
check(r is mine and mine == ["X", "Y"], "Ein übergebenes Protokoll wird ergänzt und zurückgegeben", "A log passed in is extended and returned")
check(call(ns, "log_event", "Z", log=[]) == ["Z"], "Auch mit Keyword-Argument log=[]", "Also with keyword argument log=[]")
''',
   require=["def", "none"], refs=["7.7", "7.3p"])

# ------------------------------------------------------------------ Stufe 3
ex(id="k7-newtonpoly", ch="7", lvl=3,
   title={"de": "Newton-Verfahren als Funktion", "en": "Newton's method as a function"},
   task={"de": "Ein Polynom wird als Liste seiner Koeffizienten gespeichert, beginnend beim konstanten Glied: `[-1, -2, 1, 1]` steht für $x^3 + x^2 - 2x - 1$.\n- `poly(coeffs, x)`: Wert des Polynoms an der Stelle x\n- `dpoly(coeffs, x)`: Wert der Ableitung an der Stelle x (Ableitung von $c x^k$ ist $k c x^{k-1}$)\n- `newton(coeffs, x0, tol=1e-10, max_iter=50)`: sucht ausgehend von x0 eine Nullstelle mit $x \\leftarrow x - f(x)/f'(x)$. Sobald $|f(x)| < \\mathit{tol}$ ist, wird x zurückgegeben. Ist die Ableitung 0 oder wird nach `max_iter` Schritten keine Nullstelle gefunden, wird `None` zurückgegeben.",
         "en": "A polynomial is stored as a list of its coefficients, starting with the constant term: `[-1, -2, 1, 1]` means $x^3 + x^2 - 2x - 1$.\n- `poly(coeffs, x)`: value of the polynomial at x\n- `dpoly(coeffs, x)`: value of the derivative at x (the derivative of $c x^k$ is $k c x^{k-1}$)\n- `newton(coeffs, x0, tol=1e-10, max_iter=50)`: starting from x0, searches a root with $x \\leftarrow x - f(x)/f'(x)$. As soon as $|f(x)| < \\mathit{tol}$, x is returned. If the derivative is 0 or no root is found after `max_iter` steps, `None` is returned."},
   starter={"de": "def poly(coeffs, x):\n    ...\n", "en": "def poly(coeffs, x):\n    ...\n"},
   solution='def poly(coeffs, x):\n    total = 0\n    for k in range(len(coeffs)):\n        total += coeffs[k] * x**k\n    return total\n\ndef dpoly(coeffs, x):\n    total = 0\n    for k in range(1, len(coeffs)):\n        total += k * coeffs[k] * x**(k - 1)\n    return total\n\ndef newton(coeffs, x0, tol=1e-10, max_iter=50):\n    x = x0\n    for i in range(max_iter):\n        fx = poly(coeffs, x)\n        if abs(fx) < tol:\n            return x\n        d = dpoly(coeffs, x)\n        if d == 0:\n            return None\n        x = x - fx / d\n    if abs(poly(coeffs, x)) < tol:\n        return x\n    return None\n\nprint(newton([-1, -2, 1, 1], 1.0))\n',
   tests='''
ns, out = run()
P = [-1, -2, 1, 1]
for x in [0, 1.5, -2]:
    check(approx(call(ns, "poly", P, x), x**3 + x**2 - 2*x - 1) and approx(call(ns, "dpoly", P, x), 3*x**2 + 2*x - 2), f"poly/dpoly bei x = {x}", f"poly/dpoly at x = {x}")
for x0 in [1.0, -0.5, -2.0]:
    r = call(ns, "newton", P, x0)
    check(r is not None and abs(r**3 + r**2 - 2*r - 1) < 1e-8, f"newton(..., {x0}) findet eine Nullstelle", f"newton(..., {x0}) finds a root")
r = call(ns, "newton", [-2, 0, 1], 1.0)
check(r is not None and approx(r, 2**0.5, 1e-8), "x² − 2 = 0 mit Start 1.0 → √2", "x² − 2 = 0 starting at 1.0 → √2")
check(call(ns, "newton", [1, 0, 1], 0.0) is None, "x² + 1 hat keine reelle Nullstelle; Ableitung 0 bei x = 0 → None", "x² + 1 has no real root; derivative 0 at x = 0 → None")
check(call(ns, "newton", [1, 0, 1], 0.5, max_iter=20) is None, "Keine Konvergenz → None", "No convergence → None")
''',
   require=["def", "return", "default_arg"], refs=["6.3a", "7.3p", "7.3r"])

ex(id="k7-interpolate", ch="7", lvl=3,
   title={"de": "Kennlinie interpolieren", "en": "Interpolating a characteristic"},
   task={"de": "Die Kennlinie eines NTC-Temperatursensors ist als Tabelle gegeben: `temps` (°C, aufsteigend) und `resist` (kΩ). Für Werte zwischen den Stützstellen wird **linear interpoliert**: Liegt x zwischen $x_i$ und $x_{i+1}$, dann gilt $y = y_i + (y_{i+1} - y_i) \\cdot \\dfrac{x - x_i}{x_{i+1} - x_i}$.\n\nSchreiben Sie `interpolate(xs, ys, x)`, die den interpolierten Wert zurückgibt; genau auf einer Stützstelle wird deren Wert geliefert. Liegt x außerhalb der Tabelle, wird `None` zurückgegeben (keine Extrapolation!). Schreiben Sie dann `resistance_at(t)`, die mit Hilfe von `interpolate` den Widerstand bei der Temperatur t aus der vorgegebenen Tabelle liefert.",
         "en": "The characteristic of an NTC temperature sensor is given as a table: `temps` (°C, ascending) and `resist` (kΩ). For values between the data points, **linear interpolation** is used: if x lies between $x_i$ and $x_{i+1}$, then $y = y_i + (y_{i+1} - y_i) \\cdot \\dfrac{x - x_i}{x_{i+1} - x_i}$.\n\nWrite `interpolate(xs, ys, x)` that returns the interpolated value; exactly at a data point, its value is returned. If x lies outside the table, `None` is returned (no extrapolation!). Then write `resistance_at(t)` that uses `interpolate` to return the resistance at temperature t from the given table."},
   starter={"de": "temps = [-20, 0, 25, 50, 100]\nresist = [97.1, 32.7, 10.0, 3.6, 0.68]\n\ndef interpolate(xs, ys, x):\n    ...\n", "en": "temps = [-20, 0, 25, 50, 100]\nresist = [97.1, 32.7, 10.0, 3.6, 0.68]\n\ndef interpolate(xs, ys, x):\n    ...\n"},
   solution='temps = [-20, 0, 25, 50, 100]\nresist = [97.1, 32.7, 10.0, 3.6, 0.68]\n\ndef interpolate(xs, ys, x):\n    if x < xs[0] or x > xs[-1]:\n        return None\n    for i in range(len(xs) - 1):\n        if xs[i] <= x <= xs[i + 1]:\n            return ys[i] + (ys[i + 1] - ys[i]) * (x - xs[i]) / (xs[i + 1] - xs[i])\n    return ys[-1]\n\ndef resistance_at(t):\n    return interpolate(temps, resist, t)\n\nprint(resistance_at(37.5))\n',
   tests='''
def ref(xs, ys, x):
    if x < xs[0] or x > xs[-1]:
        return None
    for i in range(len(xs) - 1):
        if xs[i] <= x <= xs[i + 1]:
            return ys[i] + (ys[i + 1] - ys[i]) * (x - xs[i]) / (xs[i + 1] - xs[i])
ns, out = run()
X = [-20, 0, 25, 50, 100]; Y = [97.1, 32.7, 10.0, 3.6, 0.68]
for x in [37.5, -20, 100, 0, 10, 75.25]:
    check(approx(call(ns, "interpolate", X, Y, x), ref(X, Y, x)), f"interpolate bei {x} °C ≈ {ref(X, Y, x):.3f} kΩ", f"interpolate at {x} °C ≈ {ref(X, Y, x):.3f} kΩ")
check(call(ns, "interpolate", X, Y, -25) is None and call(ns, "interpolate", X, Y, 100.5) is None, "Außerhalb der Tabelle → None", "Outside the table → None")
check(approx(call(ns, "interpolate", [0, 10], [5, 25], 2.5), 10.0), "Funktioniert auch mit anderen Tabellen", "Works with other tables too")
check(approx(call(ns, "resistance_at", 37.5), ref(X, Y, 37.5)), "resistance_at nutzt die vorgegebene Tabelle", "resistance_at uses the given table")
''',
   require=["def", "return"], refs=["7.3r", "6.2c"])

ex(id="k7-e12", ch="7", lvl=3,
   title={"de": "Nächster Normwert (E12-Reihe)", "en": "Nearest preferred value (E12 series)"},
   task={"de": "Widerstände gibt es nur in Normwerten. Die E12-Reihe enthält pro Dekade die Werte `E12 = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]`, multipliziert mit einer Zehnerpotenz (z.B. $4.7\\,\\mathrm{k\\Omega} = 4.7 \\cdot 10^3\\,\\Omega$).\n\nSchreiben Sie `nearest_e12(r)` für r > 0:\n1. Bestimmen Sie mit `while`-Schleifen die Zehnerpotenz `decade` (z.B. 1000 für 4321 Ω), sodass r / decade zwischen 1 und 10 liegt.\n2. Suchen Sie unter den Werten `E12[i] · decade` **und** zusätzlich `10 · decade` (der erste Wert der nächsten Dekade) den mit dem kleinsten Abstand zu r (`abs`).\n3. Geben Sie diesen Wert mit `round(…, 6)` gerundet zurück – das entfernt winzige Rundungsfehler wie 4700.000000000001.\n\nSchreiben Sie außerdem `deviation(r)`: die relative Abweichung des Normwerts von r in Prozent.",
         "en": "Resistors only come in preferred values. Per decade, the E12 series contains the values `E12 = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]`, multiplied by a power of ten (e.g. $4.7\\,\\mathrm{k\\Omega} = 4.7 \\cdot 10^3\\,\\Omega$).\n\nWrite `nearest_e12(r)` for r > 0:\n1. Use `while` loops to determine the power of ten `decade` (e.g. 1000 for 4321 Ω) such that r / decade lies between 1 and 10.\n2. Among the values `E12[i] · decade` **and** additionally `10 · decade` (the first value of the next decade), find the one with the smallest distance to r (`abs`).\n3. Return that value rounded with `round(…, 6)` – this removes tiny rounding errors like 4700.000000000001.\n\nAlso write `deviation(r)`: the relative deviation of the preferred value from r in percent."},
   starter={"de": "E12 = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]\n\ndef nearest_e12(r):\n    ...\n", "en": "E12 = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]\n\ndef nearest_e12(r):\n    ...\n"},
   solution='E12 = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]\n\ndef nearest_e12(r):\n    decade = 1\n    while r / decade >= 10:\n        decade *= 10\n    while r / decade < 1:\n        decade /= 10\n    best = 10 * decade\n    for e in E12:\n        if abs(e * decade - r) < abs(best - r):\n            best = e * decade\n    return round(best, 6)\n\ndef deviation(r):\n    return (nearest_e12(r) - r) / r * 100\n\nprint(nearest_e12(4321), nearest_e12(95), round(deviation(4321), 2))\n',
   tests='''
E = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2, 10.0]
def ref(r):
    d = 1
    while r / d >= 10: d *= 10
    while r / d < 1: d /= 10
    best = None
    for e in E:
        if best is None or abs(e * d - r) < abs(best - r):
            best = e * d
    return round(best, 6)
ns, out = run()
for r in [4321, 95, 1000, 2.0, 160000, 5.0, 3.6, 7.5, 0.47, 0.0333]:
    check(approx(call(ns, "nearest_e12", r), ref(r)), f"nearest_e12({r}) = {ref(r):g} Ω", f"nearest_e12({r}) = {ref(r):g} Ω")
check(approx(call(ns, "deviation", 4321), (ref(4321) - 4321) / 4321 * 100), "deviation(4321) ≈ 8.77 %", "deviation(4321) ≈ 8.77 %")
''',
   require=["def", "while", "abs"], refs=["7.3r", "6.2a"])

ex(id="k7-gearpair", ch="7", lvl=3,
   title={"de": "Zähnezahlen für eine Übersetzung finden", "en": "Finding tooth counts for a ratio"},
   task={"de": "Für ein einstufiges Getriebe wird die Übersetzung `target` = z2 / z1 gesucht. Erlaubt sind Zähnezahlen von `z_min` bis `z_max` (jeweils einschließlich).\n\nSchreiben Sie `best_pair(target, z_min=17, z_max=80)`, die mit **verschachtelten Schleifen** alle Paare (z1, z2) durchprobiert und das Paar mit der kleinsten Abweichung $|z_2/z_1 - \\mathit{target}|$ als Tupel `(z1, z2)` zurückgibt. Bei gleicher Abweichung gewinnt das zuerst gefundene Paar (kleinstes z1, dann kleinstes z2). Schreiben Sie außerdem `ratio_error(target, z_min=17, z_max=80)`, die die relative Abweichung des besten Paares in Prozent zurückgibt.",
         "en": "For a single-stage gearbox, the ratio `target` = z2 / z1 is wanted. Tooth counts from `z_min` to `z_max` (both inclusive) are allowed.\n\nWrite `best_pair(target, z_min=17, z_max=80)` that uses **nested loops** to try all pairs (z1, z2) and returns the pair with the smallest deviation $|z_2/z_1 - \\mathit{target}|$ as the tuple `(z1, z2)`. With equal deviation, the pair found first wins (smallest z1, then smallest z2). Also write `ratio_error(target, z_min=17, z_max=80)` that returns the relative deviation of the best pair in percent."},
   starter={"de": "def best_pair(target, z_min=17, z_max=80):\n    ...\n", "en": "def best_pair(target, z_min=17, z_max=80):\n    ...\n"},
   solution='def best_pair(target, z_min=17, z_max=80):\n    best = None\n    best_err = None\n    for z1 in range(z_min, z_max + 1):\n        for z2 in range(z_min, z_max + 1):\n            err = abs(z2 / z1 - target)\n            if best_err is None or err < best_err:\n                best = (z1, z2)\n                best_err = err\n    return best\n\ndef ratio_error(target, z_min=17, z_max=80):\n    z1, z2 = best_pair(target, z_min, z_max)\n    return abs(z2 / z1 - target) / target * 100\n\nprint(best_pair(3.14159), ratio_error(3.14159))\n',
   tests='''
def ref(t, a=17, b=80):
    best = None; be = None
    for z1 in range(a, b + 1):
        for z2 in range(a, b + 1):
            e = abs(z2 / z1 - t)
            if be is None or e < be:
                best, be = (z1, z2), e
    return best
ns, out = run()
for t in [3.14159, 2.5, 1.0, 4.37, 0.2125, 0.2099, 4.8]:
    r = call(ns, "best_pair", t)
    check(tuple(r) == ref(t) if r is not None else False, f"best_pair({t}) = {ref(t)}", f"best_pair({t}) = {ref(t)}")
check(tuple(call(ns, "best_pair", 2.0, z_min=10, z_max=12)) == ref(2.0, 10, 12), "Eigene Grenzen z_min/z_max werden beachtet", "Custom limits z_min/z_max are respected")
z1, z2 = ref(3.14159)
check(approx(call(ns, "ratio_error", 3.14159), abs(z2 / z1 - 3.14159) / 3.14159 * 100) and approx(call(ns, "ratio_error", 0.2125), 0), "ratio_error stimmt (auch mit den Standardgrenzen 17 bis 80)", "ratio_error is correct (also with the default limits 17 to 80)")
''',
   require=["def", "for", "default_arg"], refs=["6.2d", "7.3p", "7.3r"])

ex(id="k7-tobase", ch="7", lvl=3,
   title={"de": "Zahlensysteme selbst umrechnen", "en": "Converting number systems yourself"},
   task={"de": "Schreiben Sie `to_base(n, base)`, die eine ganze Zahl $n \\ge 0$ in ein Zahlensystem mit der Basis 2 bis 16 umrechnet und als String zurückgibt (ohne Präfix, Großbuchstaben, z.B. `to_base(255, 16)` → `\"FF\"`). Verwenden Sie wiederholte Division mit `divmod` und die vorgegebene Liste `DIGITS` für die Ziffernzeichen. Für n = 0 ist das Ergebnis `\"0\"`. Bei einer ungültigen Basis wird `None` zurückgegeben.\n\nSchreiben Sie außerdem `check(n)`, die `True` zurückgibt, wenn Ihre Ergebnisse mit den eingebauten Funktionen übereinstimmen: `\"0b\" + to_base(n, 2)` muss gleich `bin(n)` sein und `\"0o\" + to_base(n, 8)` gleich `oct(n)`.",
         "en": "Write `to_base(n, base)` that converts an integer $n \\ge 0$ into a number system with base 2 to 16 and returns it as a string (without prefix, upper case, e.g. `to_base(255, 16)` → `\"FF\"`). Use repeated division with `divmod` and the given list `DIGITS` for the digit characters. For n = 0 the result is `\"0\"`. For an invalid base, return `None`.\n\nAlso write `check(n)` that returns `True` if your results agree with the built-in functions: `\"0b\" + to_base(n, 2)` must equal `bin(n)` and `\"0o\" + to_base(n, 8)` must equal `oct(n)`."},
   starter={"de": "DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']\n\ndef to_base(n, base):\n    ...\n", "en": "DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']\n\ndef to_base(n, base):\n    ...\n"},
   solution='DIGITS = [\'0\', \'1\', \'2\', \'3\', \'4\', \'5\', \'6\', \'7\', \'8\', \'9\', \'A\', \'B\', \'C\', \'D\', \'E\', \'F\']\n\ndef to_base(n, base):\n    if base < 2 or base > 16:\n        return None\n    if n == 0:\n        return "0"\n    result = ""\n    while n > 0:\n        n, rest = divmod(n, base)\n        result = DIGITS[rest] + result\n    return result\n\ndef check(n):\n    ok2 = "0b" + to_base(n, 2) == bin(n)\n    ok8 = "0o" + to_base(n, 8) == oct(n)\n    return ok2 and ok8\n\nprint(to_base(255, 16), to_base(10, 2), check(4711))\n',
   tests='''
def ref(n, b):
    s = "0123456789ABCDEF"; r = ""
    if n == 0: return "0"
    while n: n, k = divmod(n, b); r = s[k] + r
    return r
ns, out = run()
for n, b in [(255, 16), (10, 2), (0, 7), (4711, 8), (123456, 16), (35, 3)]:
    check(call(ns, "to_base", n, b) == ref(n, b), f"to_base({n}, {b}) = {ref(n, b)!r}", f"to_base({n}, {b}) = {ref(n, b)!r}")
check(call(ns, "to_base", 10, 1) is None and call(ns, "to_base", 10, 17) is None, "Ungültige Basis → None", "Invalid base → None")
check(call(ns, "check", 4711) is True and call(ns, "check", 0) is True, "check(4711) und check(0) sind True", "check(4711) and check(0) are True")
''',
   require=["def", "while", "divmod"], refs=["7.2", "5.5", "7.3r"])
