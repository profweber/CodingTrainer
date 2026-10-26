from exlib import ex

# Kapitel 8: zusätzlich Slicing, Set, Dictionary (+ Methoden), Tupel, Comprehensions, enumerate/zip, copy.

ex(id="k8-tuple", ch="8", lvl=1,
   title={"de": "Messpunkt als Tupel", "en": "Measuring point as a tuple"},
   task={"de": "Ein Koordinatenmessgerät liefert den Punkt `point` als Tupel (x, y, z) in mm.\n- Entpacken Sie das Tupel in `x`, `y`, `z`.\n- Berechnen Sie den Abstand zum Ursprung `dist` = √(x² + y² + z²).\n- Der Taster war um `offset` mm in z-Richtung verschoben. Erzeugen Sie das **neue** Tupel `corrected` mit korrigiertem z-Wert (z − offset). Ein Tupel kann man nicht verändern!",
         "en": "A coordinate measuring machine delivers the point `point` as a tuple (x, y, z) in mm.\n- Unpack the tuple into `x`, `y`, `z`.\n- Compute the distance to the origin `dist` = √(x² + y² + z²).\n- The probe was offset by `offset` mm in z direction. Create the **new** tuple `corrected` with the corrected z value (z − offset). A tuple cannot be modified!"},
   starter={"de": "point = (12.0, -4.0, 3.5)\noffset = 0.5\n\n# Ihr Code:\n", "en": "point = (12.0, -4.0, 3.5)\noffset = 0.5\n\n# your code:\n"},
   solution='point = (12.0, -4.0, 3.5)\noffset = 0.5\nx, y, z = point\ndist = (x**2 + y**2 + z**2) ** 0.5\ncorrected = (x, y, z - offset)\nprint(dist, corrected)\n',
   tests='''
for p, o in [((12.0, -4.0, 3.5), 0.5), ((0.0, 0.0, 0.0), 1.0), ((3.0, 4.0, 12.0), -2.0)]:
    ns, out = run(sub={"point": p, "offset": o})
    x, y, z, d, c = need(ns, "x", "y", "z", "dist", "corrected")
    check((x, y, z) == p, f"Entpackt: x, y, z = {p}", f"Unpacked: x, y, z = {p}")
    check(approx(d, (p[0]**2 + p[1]**2 + p[2]**2) ** 0.5), f"Abstand ≈ {(p[0]**2 + p[1]**2 + p[2]**2) ** 0.5:.3f} mm", f"distance ≈ {(p[0]**2 + p[1]**2 + p[2]**2) ** 0.5:.3f} mm")
    check(isinstance(c, tuple) and len(c) == 3 and c[:2] == p[:2] and approx(c[2], p[2] - o), f"corrected = {(p[0], p[1], p[2] - o)} (als Tupel)", f"corrected = {(p[0], p[1], p[2] - o)} (as a tuple)")
    check(ns["point"] == p, "point bleibt unverändert", "point stays unchanged")
''',
   require=["assign_multi"], refs=["8.4"])

ex(id="k8-colorcode", ch="8", lvl=1,
   title={"de": "Widerstands-Farbcode", "en": "Resistor colour code"},
   task={"de": "Das Dictionary `colors` ordnet Farben ihre Ziffer zu. Ein Widerstand mit drei Ringen `band1`, `band2`, `band3` hat den Wert R = (10 · Ziffer1 + Ziffer2) · 10^Ziffer3.\n- Ermitteln Sie die drei Ziffern per Dictionary-Zugriff und berechnen Sie `R`.\n- Speichern Sie in `known` mit dem Operator `in`, ob die Farbe `test_color` im Dictionary vorkommt, und in `digit_or_minus1` ihre Ziffer – oder −1, falls unbekannt (mit `.get()`).",
         "en": "The dictionary `colors` maps colours to their digit. A resistor with three bands `band1`, `band2`, `band3` has the value R = (10 · digit1 + digit2) · 10^digit3.\n- Look up the three digits in the dictionary and compute `R`.\n- Store in `known` (using the operator `in`) whether the colour `test_color` is in the dictionary, and in `digit_or_minus1` its digit – or −1 if unknown (using `.get()`)."},
   starter={"de": "colors = {'schwarz': 0, 'braun': 1, 'rot': 2, 'orange': 3, 'gelb': 4,\n          'grün': 5, 'blau': 6, 'violett': 7, 'grau': 8, 'weiß': 9}\nband1, band2, band3 = 'gelb', 'violett', 'rot'\ntest_color = 'gold'\n\n# Ihr Code:\n",
            "en": "colors = {'schwarz': 0, 'braun': 1, 'rot': 2, 'orange': 3, 'gelb': 4,\n          'grün': 5, 'blau': 6, 'violett': 7, 'grau': 8, 'weiß': 9}\nband1, band2, band3 = 'gelb', 'violett', 'rot'\ntest_color = 'gold'\n\n# your code:\n"},
   solution="colors = {'schwarz': 0, 'braun': 1, 'rot': 2, 'orange': 3, 'gelb': 4,\n          'grün': 5, 'blau': 6, 'violett': 7, 'grau': 8, 'weiß': 9}\nband1, band2, band3 = 'gelb', 'violett', 'rot'\ntest_color = 'gold'\nR = (10 * colors[band1] + colors[band2]) * 10 ** colors[band3]\nknown = test_color in colors\ndigit_or_minus1 = colors.get(test_color, -1)\nprint(R, known, digit_or_minus1)\n",
   tests='''
C = {'schwarz': 0, 'braun': 1, 'rot': 2, 'orange': 3, 'gelb': 4, 'grün': 5, 'blau': 6, 'violett': 7, 'grau': 8, 'weiß': 9}
ns, out = run()
check(need(ns, "R") == 4700, "gelb-violett-rot = 4700 Ω", "yellow-violet-red = 4700 Ω")
check(ns.get("known") is False and ns.get("digit_or_minus1") == -1, "'gold' ist unbekannt → False und −1", "'gold' is unknown → False and −1")
for t in ["blau", "schwarz"]:
    ns, out = run(sub={"test_color": t})
    check(ns.get("known") is True and ns.get("digit_or_minus1") == C[t], f"{t!r} → True und {C[t]}", f"{t!r} → True and {C[t]}")
''',
   require=["dict_methods"], refs=["8.3"])

ex(id="k8-kelvin-comp", ch="8", lvl=1,
   title={"de": "Comprehensions für Temperaturen", "en": "Comprehensions for temperatures"},
   task={"de": "Erzeugen Sie aus der Liste `celsius` jeweils mit einer **List Comprehension**:\n- `kelvin`: alle Werte in Kelvin\n- `frost`: nur die Werte unter 0 °C\n- `labels`: für jeden Wert `'Frost'` (unter 0 °C) oder `'ok'`",
         "en": "From the list `celsius`, create with a **list comprehension** each:\n- `kelvin`: all values in kelvin\n- `frost`: only the values below 0 °C\n- `labels`: for every value `'Frost'` (below 0 °C) or `'ok'`"},
   starter={"de": "celsius = [3.5, -2.0, 0.0, -7.5, 12.1]\n\n# Ihr Code:\n", "en": "celsius = [3.5, -2.0, 0.0, -7.5, 12.1]\n\n# your code:\n"},
   solution="celsius = [3.5, -2.0, 0.0, -7.5, 12.1]\nkelvin = [t + 273.15 for t in celsius]\nfrost = [t for t in celsius if t < 0]\nlabels = ['Frost' if t < 0 else 'ok' for t in celsius]\nprint(kelvin, frost, labels)\n",
   tests='''
for c in [[3.5, -2.0, 0.0, -7.5, 12.1], [10.0, 20.0], [-1.0]]:
    ns, out = run(sub={"celsius": c})
    k, f, l = need(ns, "kelvin", "frost", "labels")
    check(len(k) == len(c) and all(approx(a, b + 273.15) for a, b in zip(k, c)), f"kelvin für {c}", f"kelvin for {c}")
    check(f == [t for t in c if t < 0], f"frost = {[t for t in c if t < 0]}", f"frost = {[t for t in c if t < 0]}")
    check(l == ['Frost' if t < 0 else 'ok' for t in c], "labels stimmen", "labels are correct")
''',
   require=["listcomp"], forbid=["for"], refs=["8.8"])

ex(id="k8-invert", ch="8", lvl=2,
   title={"de": "Teilekatalog umdrehen", "en": "Inverting a parts catalogue"},
   task={"de": "Das Dictionary `catalogue` ordnet Teilenummern eine Bezeichnung zu. Erzeugen Sie mit einer **Dictionary-Comprehension** das umgekehrte Dictionary `by_name` (Bezeichnung → Teilenummer). Erzeugen Sie außerdem `names`: die alphabetisch sortierte Liste aller Bezeichnungen, und `numbers_m`: die sortierte Liste aller Teilenummern, die mit `'M'` beginnen (Tipp: Indexzugriff auf das erste Zeichen).",
         "en": "The dictionary `catalogue` maps part numbers to a name. Use a **dictionary comprehension** to create the inverted dictionary `by_name` (name → part number). Also create `names`: the alphabetically sorted list of all names, and `numbers_m`: the sorted list of all part numbers starting with `'M'` (tip: index the first character)."},
   starter={"de": "catalogue = {'M8-40': 'Sechskantschraube M8x40', 'L-6204': 'Rillenkugellager 6204',\n             'M6-20': 'Zylinderschraube M6x20', 'D-35': 'Wellendichtring 35x52'}\n\n# Ihr Code:\n",
            "en": "catalogue = {'M8-40': 'Sechskantschraube M8x40', 'L-6204': 'Rillenkugellager 6204',\n             'M6-20': 'Zylinderschraube M6x20', 'D-35': 'Wellendichtring 35x52'}\n\n# your code:\n"},
   solution="catalogue = {'M8-40': 'Sechskantschraube M8x40', 'L-6204': 'Rillenkugellager 6204',\n             'M6-20': 'Zylinderschraube M6x20', 'D-35': 'Wellendichtring 35x52'}\nby_name = {name: number for number, name in catalogue.items()}\nnames = sorted(catalogue.values())\nnumbers_m = sorted([n for n in catalogue if n[0] == 'M'])\nprint(by_name, names, numbers_m)\n",
   tests='''
for cat in [{'M8-40': 'Sechskantschraube M8x40', 'L-6204': 'Rillenkugellager 6204', 'M6-20': 'Zylinderschraube M6x20', 'D-35': 'Wellendichtring 35x52'}, {'A1': 'Zahnrad', 'M2': 'Mutter'}]:
    ns, out = run(sub={"catalogue": dict(cat)})
    b, n, m = need(ns, "by_name", "names", "numbers_m")
    check(b == {v: k for k, v in cat.items()}, "by_name ist das umgekehrte Dictionary", "by_name is the inverted dictionary")
    check(n == sorted(cat.values()), f"names = {sorted(cat.values())}", f"names = {sorted(cat.values())}")
    check(m == sorted(k for k in cat if k[0] == 'M'), f"numbers_m = {sorted(k for k in cat if k[0] == 'M')}", f"numbers_m = {sorted(k for k in cat if k[0] == 'M')}")
''',
   require=["listcomp"], refs=["8.8", "8.3"])

ex(id="k8-group", ch="8", lvl=2,
   title={"de": "Messwerte nach Sensor gruppieren", "en": "Grouping readings by sensor"},
   task={"de": "Die Liste `readings` enthält Tupel `(sensor, wert)` in der Reihenfolge, in der sie eingetroffen sind. Erzeugen Sie\n- `grouped`: ein Dictionary Sensor → Liste seiner Werte (Reihenfolge beibehalten)\n- `means`: ein Dictionary Sensor → Mittelwert seiner Werte (auf zwei Stellen gerundet), mit einer Dictionary-Comprehension\n- `busiest`: den Sensor mit den meisten Messwerten (bei Gleichstand der alphabetisch erste)",
         "en": "The list `readings` contains tuples `(sensor, value)` in the order they arrived. Create\n- `grouped`: a dictionary sensor → list of its values (keep the order)\n- `means`: a dictionary sensor → mean of its values (rounded to two decimals), using a dictionary comprehension\n- `busiest`: the sensor with the most readings (on a tie, the alphabetically first)"},
   starter={"de": "readings = [('T1', 21.5), ('T2', 19.0), ('T1', 21.9), ('T3', 25.2), ('T2', 19.4), ('T1', 22.3)]\n\n# Ihr Code:\n",
            "en": "readings = [('T1', 21.5), ('T2', 19.0), ('T1', 21.9), ('T3', 25.2), ('T2', 19.4), ('T1', 22.3)]\n\n# your code:\n"},
   solution="readings = [('T1', 21.5), ('T2', 19.0), ('T1', 21.9), ('T3', 25.2), ('T2', 19.4), ('T1', 22.3)]\ngrouped = {}\nfor sensor, value in readings:\n    if sensor not in grouped:\n        grouped[sensor] = []\n    grouped[sensor].append(value)\nmeans = {s: round(sum(v) / len(v), 2) for s, v in grouped.items()}\nbusiest = None\nfor s in sorted(grouped):\n    if busiest is None or len(grouped[s]) > len(grouped[busiest]):\n        busiest = s\nprint(grouped, means, busiest)\n",
   tests='''
for r in [[('T1', 21.5), ('T2', 19.0), ('T1', 21.9), ('T3', 25.2), ('T2', 19.4), ('T1', 22.3)], [('B', 1.0), ('A', 2.0), ('B', 3.0), ('A', 4.0)]]:
    ns, out = run(sub={"readings": r})
    g, m, b = need(ns, "grouped", "means", "busiest")
    eg = {}
    for s, v in r:
        eg.setdefault(s, []).append(v)
    check(g == eg, f"grouped = {eg}", f"grouped = {eg}")
    em = {s: round(sum(v) / len(v), 2) for s, v in eg.items()}
    check(isinstance(m, dict) and set(m) == set(em) and all(approx(m[k], em[k], 1e-6) for k in em), f"means = {em}", f"means = {em}")
    eb = min(eg, key=lambda s: (-len(eg[s]), s))
    check(b == eb, f"busiest = {eb!r}", f"busiest = {eb!r}")
''',
   require=["dict", "listcomp"], refs=["8.3", "8.4", "8.8"])

ex(id="k8-deepcopy", ch="8", lvl=3,
   title={"de": "Parametersatz sicher kopieren", "en": "Copying a parameter set safely"},
   task={"de": "Der Parametersatz `base` einer Maschine enthält verschachtelte Listen und Dictionaries. Für eine Variante soll eine **völlig unabhängige** Kopie `variant` entstehen:\n- Erzeugen Sie die Kopie mit dem Modul `copy`.\n- Ändern Sie in `variant` die Drehzahl `'speed'` auf 1800, hängen Sie an die Werkzeugliste `'tools'` den Eintrag `'T7'` an und setzen Sie `variant['limits']['temp']` auf 95.\n- `base` darf sich dabei **nicht** verändern. Prüfen Sie mit `print`, warum `dict(base)` hier nicht reichen würde.",
         "en": "The machine parameter set `base` contains nested lists and dictionaries. For a variant, create a **completely independent** copy `variant`:\n- Create the copy with the module `copy`.\n- In `variant`, change the speed `'speed'` to 1800, append the entry `'T7'` to the tool list `'tools'` and set `variant['limits']['temp']` to 95.\n- `base` must **not** change. Use `print` to see why `dict(base)` would not be enough here."},
   starter={"de": "base = {'speed': 1500, 'tools': ['T1', 'T3'], 'limits': {'temp': 80, 'force': 12.5}}\n\n# Ihr Code:\n",
            "en": "base = {'speed': 1500, 'tools': ['T1', 'T3'], 'limits': {'temp': 80, 'force': 12.5}}\n\n# your code:\n"},
   solution="import copy\n\nbase = {'speed': 1500, 'tools': ['T1', 'T3'], 'limits': {'temp': 80, 'force': 12.5}}\nvariant = copy.deepcopy(base)\nvariant['speed'] = 1800\nvariant['tools'].append('T7')\nvariant['limits']['temp'] = 95\nprint(base)\nprint(variant)\n",
   tests='''
ns, out = run()
b, v = need(ns, "base", "variant")
check(b == {'speed': 1500, 'tools': ['T1', 'T3'], 'limits': {'temp': 80, 'force': 12.5}}, "base ist unverändert (auch die inneren Listen/Dicts)", "base is unchanged (inner lists/dicts too)")
check(v == {'speed': 1800, 'tools': ['T1', 'T3', 'T7'], 'limits': {'temp': 95, 'force': 12.5}}, "variant enthält die drei Änderungen", "variant contains the three changes")
check(v["tools"] is not b["tools"] and v["limits"] is not b["limits"], "Die inneren Listen/Dicts sind eigene Instanzen", "The inner lists/dicts are separate instances")
other = {'speed': 900, 'tools': [], 'limits': {'temp': 60, 'force': 3.0}}
ns, out = run(sub={"base": other})
check(ns.get("base") == other and ns.get("variant") == {'speed': 1800, 'tools': ['T7'], 'limits': {'temp': 95, 'force': 3.0}}, "Funktioniert auch mit einem anderen Parametersatz (Kopie, nicht abgetippt)", "Works with another parameter set too (copied, not typed in)")
''',
   require=["copy"], refs=["8.7", "8.6"])

ex(id="k8-matvec", ch="8", lvl=3,
   title={"de": "Matrix mal Vektor in einer Zeile", "en": "Matrix times vector in one line"},
   task={"de": "Im Kapitel *Kontrollstrukturen* wurde Matrix mal Vektor mit verschachtelten Schleifen berechnet. Berechnen Sie das Produkt `Mv` von `M` (verschachtelte Liste, beliebige Größe) und `v` jetzt in **einer Zeile** mit einer List Comprehension, `zip()` und `sum()`. Berechnen Sie ebenso die transponierte Matrix `MT` mit einer verschachtelten Comprehension.",
         "en": "In the chapter *control structures*, matrix times vector was computed with nested loops. Now compute the product `Mv` of `M` (nested list, any size) and `v` in **one line** using a list comprehension, `zip()` and `sum()`. Likewise compute the transposed matrix `MT` with a nested comprehension."},
   starter={"de": "M = [[1.0, 0.0, 1.0],\n     [0.0, -1.0, 0.0],\n     [2.0, 0.0, 0.0]]\nv = [1.0, -2.0, 1.5]\n\n# Ihr Code:\n", "en": "M = [[1.0, 0.0, 1.0],\n     [0.0, -1.0, 0.0],\n     [2.0, 0.0, 0.0]]\nv = [1.0, -2.0, 1.5]\n\n# your code:\n"},
   solution='M = [[1.0, 0.0, 1.0],\n     [0.0, -1.0, 0.0],\n     [2.0, 0.0, 0.0]]\nv = [1.0, -2.0, 1.5]\nMv = [sum([a * b for a, b in zip(row, v)]) for row in M]\nMT = [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]\nprint(Mv, MT)\n',
   tests='''
for M, v in [([[1.0, 0.0, 1.0], [0.0, -1.0, 0.0], [2.0, 0.0, 0.0]], [1.0, -2.0, 1.5]), ([[1, 2], [3, 4], [5, 6]], [10, -1]), ([[2.5, -1.0, 0.0, 4.0]], [1.0, 2.0, 3.0, 4.0])]:
    ns, out = run(sub={"M": M, "v": v})
    mv, mt = need(ns, "Mv", "MT")
    e = [sum(a * b for a, b in zip(r, v)) for r in M]
    check(len(mv) == len(e) and all(approx(a, b) for a, b in zip(mv, e)), f"M·v = {e}", f"M·v = {e}")
    check(mt == [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))], "Transponierte stimmt", "Transpose is correct")
''',
   require=["listcomp", "enumzip"], refs=["8.8", "8.9", "6.3b"])

ex(id="k8-bom", ch="8", lvl=3,
   title={"de": "Stückliste auflösen", "en": "Exploding a bill of materials"},
   task={"de": "`bom` beschreibt, aus welchen Teilen eine Baugruppe besteht: Baugruppe → {Teil: Stückzahl}. `order` gibt an, wie viele Baugruppen gebaut werden: Baugruppe → Anzahl.\n- Berechnen Sie `parts_needed`: Teil → Gesamtstückzahl über alle bestellten Baugruppen.\n- Berechnen Sie `shortage`: Teil → fehlende Menge für alle Teile, bei denen der Lagerbestand `stock` nicht reicht (Teile, die gar nicht im Lager sind, haben Bestand 0).",
         "en": "`bom` describes which parts an assembly consists of: assembly → {part: quantity}. `order` states how many assemblies are built: assembly → count.\n- Compute `parts_needed`: part → total quantity over all ordered assemblies.\n- Compute `shortage`: part → missing amount for all parts where the stock `stock` is not enough (parts not in stock at all have a stock of 0)."},
   starter={"de": "bom = {\n    'Pumpe':   {'Gehäuse': 1, 'Laufrad': 1, 'M8': 6, 'Dichtung': 2},\n    'Ventil':  {'Gehäuse': 1, 'M8': 4, 'Dichtung': 1, 'Feder': 1},\n}\norder = {'Pumpe': 3, 'Ventil': 5}\nstock = {'Gehäuse': 10, 'Laufrad': 2, 'M8': 40, 'Dichtung': 8}\n\n# Ihr Code:\n",
            "en": "bom = {\n    'Pumpe':   {'Gehäuse': 1, 'Laufrad': 1, 'M8': 6, 'Dichtung': 2},\n    'Ventil':  {'Gehäuse': 1, 'M8': 4, 'Dichtung': 1, 'Feder': 1},\n}\norder = {'Pumpe': 3, 'Ventil': 5}\nstock = {'Gehäuse': 10, 'Laufrad': 2, 'M8': 40, 'Dichtung': 8}\n\n# your code:\n"},
   solution="bom = {\n    'Pumpe':   {'Gehäuse': 1, 'Laufrad': 1, 'M8': 6, 'Dichtung': 2},\n    'Ventil':  {'Gehäuse': 1, 'M8': 4, 'Dichtung': 1, 'Feder': 1},\n}\norder = {'Pumpe': 3, 'Ventil': 5}\nstock = {'Gehäuse': 10, 'Laufrad': 2, 'M8': 40, 'Dichtung': 8}\nparts_needed = {}\nfor assembly, count in order.items():\n    for part, qty in bom[assembly].items():\n        parts_needed[part] = parts_needed.get(part, 0) + qty * count\nshortage = {p: n - stock.get(p, 0) for p, n in parts_needed.items() if n > stock.get(p, 0)}\nprint(parts_needed, shortage)\n",
   tests='''
def ref(bom, order, stock):
    need_ = {}
    for a, c in order.items():
        for p, q in bom[a].items():
            need_[p] = need_.get(p, 0) + q * c
    return need_, {p: n - stock.get(p, 0) for p, n in need_.items() if n > stock.get(p, 0)}
B = {'Pumpe': {'Gehäuse': 1, 'Laufrad': 1, 'M8': 6, 'Dichtung': 2}, 'Ventil': {'Gehäuse': 1, 'M8': 4, 'Dichtung': 1, 'Feder': 1}}
for o, s in [({'Pumpe': 3, 'Ventil': 5}, {'Gehäuse': 10, 'Laufrad': 2, 'M8': 40, 'Dichtung': 8}), ({'Ventil': 1}, {}), ({'Pumpe': 1}, {'Gehäuse': 5, 'Laufrad': 5, 'M8': 50, 'Dichtung': 5}), ({'Ventil': 1}, {'Gehäuse': 1, 'M8': 4, 'Dichtung': 1, 'Feder': 1})]:
    ns, out = run(sub={"order": dict(o), "stock": dict(s)})
    pn, sh = need(ns, "parts_needed", "shortage")
    en, es = ref(B, o, s)
    check(pn == en, f"Bestellung {o}: parts_needed = {en}", f"order {o}: parts_needed = {en}")
    check(sh == es, f"shortage = {es}", f"shortage = {es}")
''',
   require=["dict_methods"], refs=["8.5", "8.3"])
