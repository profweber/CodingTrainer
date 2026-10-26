from exlib import ex

# Kapitel 8, zweiter Satz: zusätzlich Slicing, Set, Dictionary (+ Methoden), Tupel, Comprehensions,
# enumerate/zip, copy.

# ------------------------------------------------------------------ Stufe 1
ex(id="k8-datasheet", ch="8", lvl=1,
   title={"de": "Datenblatt als Dictionary", "en": "Datasheet as a dictionary"},
   task={"de": "Das Dictionary `motor` enthält die Daten eines Typenschilds. Führen Sie nacheinander aus:\n1. Lesen Sie die Nennleistung (Schlüssel `'P_kW'`) in `power` aus.\n2. Ergänzen Sie den Schlüssel `'IE'` mit dem Wert `'IE3'` (Effizienzklasse).\n3. Korrigieren Sie die Drehzahl `'n_rpm'` auf 1455.\n4. Lesen Sie mit `.get()` den Leistungsfaktor `'cos_phi'` in `cos_phi` aus – fehlt er, soll 0.85 verwendet werden.\n5. Speichern Sie in `n_keys` die Anzahl der Einträge und in `keys` die alphabetisch sortierte Liste aller Schlüssel.",
         "en": "The dictionary `motor` contains the data of a nameplate. Perform in order:\n1. Read the rated power (key `'P_kW'`) into `power`.\n2. Add the key `'IE'` with the value `'IE3'` (efficiency class).\n3. Correct the speed `'n_rpm'` to 1455.\n4. Use `.get()` to read the power factor `'cos_phi'` into `cos_phi` – if it is missing, 0.85 should be used.\n5. Store the number of entries in `n_keys` and the alphabetically sorted list of all keys in `keys`."},
   starter={"de": "motor = {'Typ': 'DRN132S4', 'P_kW': 5.5, 'n_rpm': 1450, 'U_V': 400}\n\n# Ihr Code:\n", "en": "motor = {'Typ': 'DRN132S4', 'P_kW': 5.5, 'n_rpm': 1450, 'U_V': 400}\n\n# your code:\n"},
   solution="motor = {'Typ': 'DRN132S4', 'P_kW': 5.5, 'n_rpm': 1450, 'U_V': 400}\npower = motor['P_kW']\nmotor['IE'] = 'IE3'\nmotor['n_rpm'] = 1455\ncos_phi = motor.get('cos_phi', 0.85)\nn_keys = len(motor)\nkeys = sorted(motor)\nprint(motor, power, cos_phi, n_keys, keys)\n",
   tests='''
for m in [{'Typ': 'DRN132S4', 'P_kW': 5.5, 'n_rpm': 1450, 'U_V': 400}, {'Typ': 'X', 'P_kW': 0.75, 'n_rpm': 2800, 'cos_phi': 0.79}]:
    ns, out = run(sub={"motor": dict(m)})
    mo, p, c, n, k = need(ns, "motor", "power", "cos_phi", "n_keys", "keys")
    e = dict(m); e['IE'] = 'IE3'; e['n_rpm'] = 1455
    check(mo == e, f"motor danach: {e}", f"motor afterwards: {e}")
    check(p == m['P_kW'] and c == m.get('cos_phi', 0.85), f"power = {m['P_kW']}, cos_phi = {m.get('cos_phi', 0.85)}", f"power = {m['P_kW']}, cos_phi = {m.get('cos_phi', 0.85)}")
    check(n == len(e) and k == sorted(e), f"n_keys = {len(e)}, keys = {sorted(e)}", f"n_keys = {len(e)}, keys = {sorted(e)}")
''',
   require=["dict_methods"], refs=["8.3"])

ex(id="k8-duplicates", ch="8", lvl=1,
   title={"de": "Doppelte Seriennummern", "en": "Duplicate serial numbers"},
   task={"de": "Beim Wareneingang wurden die Seriennummern der gelieferten Geräte gescannt (`scans`). Manche Geräte wurden versehentlich doppelt gescannt. Ermitteln Sie mit einem Set\n- `unique`: die sortierte Liste der verschiedenen Seriennummern\n- `n_devices`: die Anzahl der tatsächlich gelieferten Geräte\n- `n_double`: wie viele Scans überzählig waren\n- `missing`: die sortierte Liste der Seriennummern aus dem Lieferschein `ordered`, die **nicht** gescannt wurden (Differenzmenge)",
         "en": "At goods receipt, the serial numbers of the delivered devices were scanned (`scans`). Some devices were accidentally scanned twice. Using a set, determine\n- `unique`: the sorted list of the different serial numbers\n- `n_devices`: the number of devices actually delivered\n- `n_double`: how many scans were superfluous\n- `missing`: the sorted list of the serial numbers from the delivery note `ordered` that were **not** scanned (set difference)"},
   starter={"de": "scans = ['SN-104', 'SN-101', 'SN-104', 'SN-107', 'SN-101', 'SN-102']\nordered = ['SN-101', 'SN-102', 'SN-103', 'SN-104', 'SN-107']\n\n# Ihr Code:\n", "en": "scans = ['SN-104', 'SN-101', 'SN-104', 'SN-107', 'SN-101', 'SN-102']\nordered = ['SN-101', 'SN-102', 'SN-103', 'SN-104', 'SN-107']\n\n# your code:\n"},
   solution="scans = ['SN-104', 'SN-101', 'SN-104', 'SN-107', 'SN-101', 'SN-102']\nordered = ['SN-101', 'SN-102', 'SN-103', 'SN-104', 'SN-107']\nscanned = set(scans)\nunique = sorted(scanned)\nn_devices = len(scanned)\nn_double = len(scans) - n_devices\nmissing = sorted(set(ordered).difference(scanned))\nprint(unique, n_devices, n_double, missing)\n",
   tests='''
for s, o in [(['SN-104', 'SN-101', 'SN-104', 'SN-107', 'SN-101', 'SN-102'], ['SN-101', 'SN-102', 'SN-103', 'SN-104', 'SN-107']), (['A', 'B'], ['A', 'B']), (['X', 'X', 'X'], ['Y', 'X', 'Z'])]:
    ns, out = run(sub={"scans": s, "ordered": o})
    u, nd, nb, m = need(ns, "unique", "n_devices", "n_double", "missing")
    check(u == sorted(set(s)) and nd == len(set(s)), f"unique = {sorted(set(s))}, n_devices = {len(set(s))}", f"unique = {sorted(set(s))}, n_devices = {len(set(s))}")
    check(nb == len(s) - len(set(s)), f"n_double = {len(s) - len(set(s))}", f"n_double = {len(s) - len(set(s))}")
    check(m == sorted(set(o) - set(s)), f"missing = {sorted(set(o) - set(s))}", f"missing = {sorted(set(o) - set(s))}")
''',
   require=["set"], refs=["8.2"])

ex(id="k8-alarms", ch="8", lvl=1,
   title={"de": "Alarmliste nummerieren", "en": "Numbering an alarm list"},
   task={"de": "Die Liste `alarms` enthält die Meldungen einer Anlage in zeitlicher Reihenfolge; kritische Meldungen beginnen mit `'CRIT'`. Geben Sie mit `enumerate(…, start=1)` eine nummerierte Liste aus, z.B. `1: WARN Druck niedrig`. Sammeln Sie dabei in `critical` die **Nummern** (ab 1) aller kritischen Meldungen. Speichern Sie außerdem in `last_three` die letzten drei Meldungen in zeitlicher Reihenfolge (Slicing).\n\nTipp: Ob eine Meldung mit `'CRIT'` beginnt, prüfen Sie mit Slicing: `text[:4] == 'CRIT'`.",
         "en": "The list `alarms` contains the messages of a plant in chronological order; critical messages start with `'CRIT'`. Use `enumerate(…, start=1)` to print a numbered list, e.g. `1: WARN Druck niedrig`. While doing so, collect in `critical` the **numbers** (from 1) of all critical messages. Also store the last three messages in `last_three` in chronological order (slicing).\n\nTip: check whether a message starts with `'CRIT'` using slicing: `text[:4] == 'CRIT'`."},
   starter={"de": "alarms = ['WARN Druck niedrig', 'INFO Pumpe 2 an', 'CRIT Motor überhitzt', 'INFO Kühlung an', 'CRIT Not-Aus']\n\n# Ihr Code:\n", "en": "alarms = ['WARN Druck niedrig', 'INFO Pumpe 2 an', 'CRIT Motor überhitzt', 'INFO Kühlung an', 'CRIT Not-Aus']\n\n# your code:\n"},
   solution="alarms = ['WARN Druck niedrig', 'INFO Pumpe 2 an', 'CRIT Motor überhitzt', 'INFO Kühlung an', 'CRIT Not-Aus']\ncritical = []\nfor number, text in enumerate(alarms, start=1):\n    print(f'{number}: {text}')\n    if text[:4] == 'CRIT':\n        critical.append(number)\nlast_three = alarms[-3:]\n",
   tests='''
_srt = lambda x: sorted(x) if isinstance(x, (list, tuple)) else x
for a in [['WARN Druck niedrig', 'INFO Pumpe 2 an', 'CRIT Motor überhitzt', 'INFO Kühlung an', 'CRIT Not-Aus'], ['CRIT A', 'INFO B'], ['INFO x']]:
    ns, out = run(sub={"alarms": a})
    c, l = need(ns, "critical", "last_three")
    ec = [i + 1 for i, t in enumerate(a) if t.startswith('CRIT')]
    check(_srt(c) == ec, f"critical = {ec}", f"critical = {ec}")
    check(l == a[-3:], f"last_three = {a[-3:]}", f"last_three = {a[-3:]}")
    check(all(f"{i + 1}: {t}" in out for i, t in enumerate(a)), "Nummerierte Ausgabe ab 1", "Numbered output starting at 1")
''',
   require=["enumzip", "slice"], refs=["8.9", "8.1x"])

ex(id="k8-cutlist", ch="8", lvl=1,
   title={"de": "Zuschnittliste aus Tupeln", "en": "Cutting list of tuples"},
   task={"de": "Die Zuschnittliste `cuts` enthält Tupel `(teil, länge_mm, anzahl)`. Ermitteln Sie\n- `total_mm`: die gesamte benötigte Länge (Länge · Anzahl, aufsummiert) – mit einer List Comprehension und `sum()`\n- `n_pieces`: die Gesamtzahl der Teile\n- `longest`: den Namen des Teils mit der größten Einzellänge (Schleife mit Entpacken der Tupel)\n- `bars`: wie viele 6-m-Stangen (6000 mm) man mindestens braucht, wenn man den Verschnitt vernachlässigt (`math.ceil`)",
         "en": "The cutting list `cuts` contains tuples `(part, length_mm, quantity)`. Determine\n- `total_mm`: the total length required (length · quantity, summed up) – with a list comprehension and `sum()`\n- `n_pieces`: the total number of parts\n- `longest`: the name of the part with the largest single length (loop that unpacks the tuples)\n- `bars`: how many 6 m bars (6000 mm) are needed at least if the waste is neglected (`math.ceil`)"},
   starter={"de": "import math\n\ncuts = [('Strebe', 1250, 4), ('Riegel', 880, 6), ('Pfosten', 2400, 2)]\n\n# Ihr Code:\n", "en": "import math\n\ncuts = [('Strebe', 1250, 4), ('Riegel', 880, 6), ('Pfosten', 2400, 2)]\n\n# your code:\n"},
   solution="import math\n\ncuts = [('Strebe', 1250, 4), ('Riegel', 880, 6), ('Pfosten', 2400, 2)]\ntotal_mm = sum([length * n for part, length, n in cuts])\nn_pieces = sum([n for part, length, n in cuts])\nlongest = None\nbest = 0\nfor part, length, n in cuts:\n    if length > best:\n        best = length\n        longest = part\nbars = math.ceil(total_mm / 6000)\nprint(total_mm, n_pieces, longest, bars)\n",
   tests='''
import math as _m
for c in [[('Strebe', 1250, 4), ('Riegel', 880, 6), ('Pfosten', 2400, 2)], [('A', 6000, 1)], [('B', 100, 3), ('C', 300, 1)], [('D', 2500, 2), ('E', 1001, 1)]]:
    ns, out = run(sub={"cuts": c})
    t, n, l, b = need(ns, "total_mm", "n_pieces", "longest", "bars")
    et = sum(x * k for _, x, k in c)
    check(t == et and n == sum(k for _, _, k in c), f"total_mm = {et}, n_pieces = {sum(k for _, _, k in c)}", f"total_mm = {et}, n_pieces = {sum(k for _, _, k in c)}")
    check(l == max(c, key=lambda z: z[1])[0], f"longest = {max(c, key=lambda z: z[1])[0]!r}", f"longest = {max(c, key=lambda z: z[1])[0]!r}")
    check(b == _m.ceil(et / 6000), f"bars = {_m.ceil(et / 6000)}", f"bars = {_m.ceil(et / 6000)}")
''',
   require=["listcomp", "unpack_for"], refs=["8.4", "8.8"])

ex(id="k8-ranking", ch="8", lvl=1,
   title={"de": "Rangliste der Prüflinge", "en": "Ranking of test specimens"},
   task={"de": "Die Bruchkräfte von Prüflingen (in kN) stehen in `forces`. Erzeugen Sie\n- `ranking`: eine **neue** Liste, absteigend sortiert (größte Kraft zuerst) – das Original bleibt unverändert (`sorted(…, reverse=True)`)\n- `top3`: die drei größten Werte, absteigend (Slicing von `ranking`)\n- `weakest`: die zwei kleinsten Werte, beginnend mit dem kleinsten (Slicing einer sortierten Liste)\n- `place`: den Platz (ab 1) des Prüflings mit der Kraft `my_force` in der Rangliste",
         "en": "The breaking forces of test specimens (in kN) are in `forces`. Create\n- `ranking`: a **new** list sorted in descending order (largest force first) – the original stays unchanged (`sorted(…, reverse=True)`)\n- `top3`: the three largest values, in descending order (slicing of `ranking`)\n- `weakest`: the two smallest values, starting with the smallest (slicing of a sorted list)\n- `place`: the place (from 1) of the specimen with force `my_force` in the ranking"},
   starter={"de": "forces = [42.1, 39.8, 45.6, 41.0, 38.2, 44.9]  # kN\nmy_force = 41.0\n\n# Ihr Code:\n", "en": "forces = [42.1, 39.8, 45.6, 41.0, 38.2, 44.9]  # kN\nmy_force = 41.0\n\n# your code:\n"},
   solution='forces = [42.1, 39.8, 45.6, 41.0, 38.2, 44.9]\nmy_force = 41.0\nranking = sorted(forces, reverse=True)\ntop3 = ranking[:3]\nweakest = sorted(forces)[:2]\nplace = ranking.index(my_force) + 1\nprint(ranking, top3, weakest, place)\n',
   tests='''
for f, m in [([42.1, 39.8, 45.6, 41.0, 38.2, 44.9], 41.0), ([5.0, 1.0, 3.0], 5.0), ([2.0, 7.5, 7.0, 1.5], 1.5)]:
    orig = list(f)
    ns, out = run(sub={"forces": list(f), "my_force": m})
    r, t, w, p = need(ns, "ranking", "top3", "weakest", "place")
    er = sorted(f, reverse=True)
    check(r == er and ns["forces"] == orig, f"ranking = {er}, forces unverändert", f"ranking = {er}, forces unchanged")
    check(t == er[:3] and w == sorted(f)[:2], f"top3 = {er[:3]}, weakest = {sorted(f)[:2]}", f"top3 = {er[:3]}, weakest = {sorted(f)[:2]}")
    check(p == er.index(m) + 1, f"place von {m} = {er.index(m) + 1}", f"place of {m} = {er.index(m) + 1}")
''',
   require=["slice", "seqfuncs"], refs=["8.1s", "8.1x"])

# ------------------------------------------------------------------ Stufe 2
ex(id="k8-errorindex", ch="8", lvl=2,
   title={"de": "Welche Maschine hatte welchen Fehler?", "en": "Which machine had which error?"},
   task={"de": "Das Dictionary `errors` ordnet jeder Maschine die Liste ihrer Fehlercodes des Tages zu (Codes können mehrfach vorkommen). Für die Instandhaltung soll die Sicht umgedreht werden:\n- `by_code`: ein Dictionary Fehlercode → **Set** der Maschinen, bei denen er auftrat\n- `shared`: die sortierte Liste der Fehlercodes, die an mindestens zwei Maschinen auftraten\n- `clean`: die sortierte Liste der Maschinen ohne Fehler\n- `n_codes`: die Anzahl verschiedener Fehlercodes insgesamt",
         "en": "The dictionary `errors` maps each machine to the list of its error codes of the day (codes may occur several times). For maintenance, the view should be inverted:\n- `by_code`: a dictionary error code → **set** of machines where it occurred\n- `shared`: the sorted list of error codes that occurred on at least two machines\n- `clean`: the sorted list of machines without errors\n- `n_codes`: the number of different error codes in total"},
   starter={"de": "errors = {\n    'Fräse 1': ['E12', 'E40', 'E12'],\n    'Fräse 2': ['E40'],\n    'Drehbank': [],\n    'Presse': ['E07', 'E12'],\n}\n\n# Ihr Code:\n", "en": "errors = {\n    'Fräse 1': ['E12', 'E40', 'E12'],\n    'Fräse 2': ['E40'],\n    'Drehbank': [],\n    'Presse': ['E07', 'E12'],\n}\n\n# your code:\n"},
   solution="errors = {\n    'Fräse 1': ['E12', 'E40', 'E12'],\n    'Fräse 2': ['E40'],\n    'Drehbank': [],\n    'Presse': ['E07', 'E12'],\n}\nby_code = {}\nfor machine, codes in errors.items():\n    for code in codes:\n        if code not in by_code:\n            by_code[code] = set()\n        by_code[code].add(machine)\nshared = sorted([c for c, machines in by_code.items() if len(machines) >= 2])\nclean = sorted([m for m, codes in errors.items() if len(codes) == 0])\nn_codes = len(by_code)\nprint(by_code, shared, clean, n_codes)\n",
   tests='''
for err in [{'Fräse 1': ['E12', 'E40', 'E12'], 'Fräse 2': ['E40'], 'Drehbank': [], 'Presse': ['E07', 'E12']}, {'A': [], 'B': []}, {'X': ['E1', 'E2'], 'Y': ['E2', 'E1']}]:
    ns, out = run(sub={"errors": err})
    bc, sh, cl, nc = need(ns, "by_code", "shared", "clean", "n_codes")
    e = {}
    for m, cs in err.items():
        for c in cs:
            e.setdefault(c, set()).add(m)
    check(bc == e and all(isinstance(v, set) for v in bc.values()), f"by_code = {e}", f"by_code = {e}")
    check(sh == sorted(c for c, ms in e.items() if len(ms) >= 2), f"shared = {sorted(c for c, ms in e.items() if len(ms) >= 2)}", f"shared = {sorted(c for c, ms in e.items() if len(ms) >= 2)}")
    check(cl == sorted(m for m, cs in err.items() if not cs) and nc == len(e), f"clean = {sorted(m for m, cs in err.items() if not cs)}, n_codes = {len(e)}", f"clean = {sorted(m for m, cs in err.items() if not cs)}, n_codes = {len(e)}")
''',
   require=["dict", "set_methods"], refs=["8.3", "8.2"])

ex(id="k8-deviations", ch="8", lvl=2,
   title={"de": "Soll-Ist-Vergleich", "en": "Target/actual comparison"},
   task={"de": "Ein Messprotokoll enthält die Sollmaße `nominal` und die gemessenen Istmaße `actual` (mm, gleiche Reihenfolge) sowie die Toleranz `tol` (± mm).\n- `deviations`: Liste der Abweichungen Ist − Soll in der Reihenfolge der Maße, auf drei Stellen gerundet – mit `zip()` und einer List Comprehension\n- `out_of_tol`: Liste der **Positionen** (Index ab 0) aller Maße außerhalb der Toleranz – mit `enumerate()`\n- `report`: Dictionary Position → Abweichung, nur für die Maße außerhalb der Toleranz (Dictionary-Comprehension)\n- `max_dev`: die betragsmäßig größte Abweichung (mit Vorzeichen!)",
         "en": "A measurement report contains the nominal dimensions `nominal` and the measured actual dimensions `actual` (mm, same order) as well as the tolerance `tol` (± mm).\n- `deviations`: list of the deviations actual − nominal in the order of the dimensions, rounded to three decimals – using `zip()` and a list comprehension\n- `out_of_tol`: list of the **positions** (index from 0) of all dimensions outside the tolerance – using `enumerate()`\n- `report`: dictionary position → deviation, only for the dimensions outside the tolerance (dictionary comprehension)\n- `max_dev`: the deviation with the largest magnitude (keep its sign!)"},
   starter={"de": "nominal = [25.0, 40.0, 12.5, 60.0, 8.0]\nactual = [25.02, 39.91, 12.53, 60.0, 8.06]\ntol = 0.05\n\n# Ihr Code:\n", "en": "nominal = [25.0, 40.0, 12.5, 60.0, 8.0]\nactual = [25.02, 39.91, 12.53, 60.0, 8.06]\ntol = 0.05\n\n# your code:\n"},
   solution='nominal = [25.0, 40.0, 12.5, 60.0, 8.0]\nactual = [25.02, 39.91, 12.53, 60.0, 8.06]\ntol = 0.05\ndeviations = [round(a - n, 3) for n, a in zip(nominal, actual)]\nout_of_tol = [i for i, d in enumerate(deviations) if abs(d) > tol]\nreport = {i: deviations[i] for i in out_of_tol}\nmax_dev = 0\nfor d in deviations:\n    if abs(d) > abs(max_dev):\n        max_dev = d\nprint(deviations, out_of_tol, report, max_dev)\n',
   tests='''
_srt = lambda x: sorted(x) if isinstance(x, (list, tuple)) else x
for n, a, t in [([25.0, 40.0, 12.5, 60.0, 8.0], [25.02, 39.91, 12.53, 60.0, 8.06], 0.05), ([1.0, 2.0], [1.0, 2.0], 0.01), ([10.0, 10.0, 10.0], [10.2, 9.7, 10.1], 0.15), ([5.0, 5.0], [5.05, 4.9], 0.05)]:
    ns, out = run(sub={"nominal": n, "actual": a, "tol": t})
    d, o, r, m = need(ns, "deviations", "out_of_tol", "report", "max_dev")
    ed = [round(y - x, 3) for x, y in zip(n, a)]
    eo = [i for i, v in enumerate(ed) if abs(v) > t]
    check(len(d) == len(ed) and all(approx(x, y) for x, y in zip(d, ed)), f"deviations = {ed}", f"deviations = {ed}")
    check(_srt(o) == eo and r == {i: ed[i] for i in eo}, f"out_of_tol = {eo}, report = {({i: ed[i] for i in eo})}", f"out_of_tol = {eo}, report = {({i: ed[i] for i in eo})}")
    em = max(ed, key=abs) if any(ed) else 0
    check(approx(m, em), f"max_dev = {em}", f"max_dev = {em}")
''',
   require=["enumzip", "listcomp"], refs=["8.9", "8.8"])

ex(id="k8-submatrix", ch="8", lvl=2,
   title={"de": "Teilmatrizen ausschneiden", "en": "Cutting out submatrices"},
   task={"de": "Ein Wärmebild ist als verschachtelte Liste `img` gespeichert (Zeilen = Bildzeilen, Werte in °C). Erzeugen Sie mit Slicing und List Comprehensions\n- `row2`: die dritte Zeile (Index 2)\n- `col1`: die zweite Spalte (Index 1) als Liste, von oben nach unten\n- `center`: den Bildausschnitt aus den mittleren Zeilen und Spalten – also ohne die erste und letzte Zeile und ohne die erste und letzte Spalte (verschachtelte Liste)\n- `hottest`: den größten Wert im ganzen Bild\n- `hot_rows`: die Indizes der Zeilen, in denen mindestens ein Wert über `limit` liegt",
         "en": "A thermal image is stored as a nested list `img` (rows = image rows, values in °C). Using slicing and list comprehensions, create\n- `row2`: the third row (index 2)\n- `col1`: the second column (index 1) as a list, top to bottom\n- `center`: the image section of the middle rows and columns – i.e. without the first and last row and without the first and last column (nested list)\n- `hottest`: the largest value in the whole image\n- `hot_rows`: the indices of the rows in which at least one value is above `limit`"},
   starter={"de": "img = [[21.0, 21.5, 22.0, 21.2],\n       [21.8, 35.2, 48.9, 22.1],\n       [22.0, 41.3, 62.4, 23.0],\n       [21.1, 22.4, 23.1, 21.6]]\nlimit = 45.0\n\n# Ihr Code:\n", "en": "img = [[21.0, 21.5, 22.0, 21.2],\n       [21.8, 35.2, 48.9, 22.1],\n       [22.0, 41.3, 62.4, 23.0],\n       [21.1, 22.4, 23.1, 21.6]]\nlimit = 45.0\n\n# your code:\n"},
   solution='img = [[21.0, 21.5, 22.0, 21.2],\n       [21.8, 35.2, 48.9, 22.1],\n       [22.0, 41.3, 62.4, 23.0],\n       [21.1, 22.4, 23.1, 21.6]]\nlimit = 45.0\nrow2 = img[2]\ncol1 = [row[1] for row in img]\ncenter = [row[1:-1] for row in img[1:-1]]\nhottest = max([max(row) for row in img])\nhot_rows = [i for i, row in enumerate(img) if max(row) > limit]\nprint(row2, col1, center, hottest, hot_rows)\n',
   tests='''
_srt = lambda x: sorted(x) if isinstance(x, (list, tuple)) else x
for im, lim in [([[21.0, 21.5, 22.0, 21.2], [21.8, 35.2, 48.9, 22.1], [22.0, 41.3, 62.4, 23.0], [21.1, 22.4, 23.1, 21.6]], 45.0),
                ([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]], 10), ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 6)]:
    ns, out = run(sub={"img": im, "limit": lim})
    r2, c1, ce, h, hr = need(ns, "row2", "col1", "center", "hottest", "hot_rows")
    check(r2 == im[2] and c1 == [r[1] for r in im], f"row2 = {im[2]}, col1 = {[r[1] for r in im]}", f"row2 = {im[2]}, col1 = {[r[1] for r in im]}")
    check(ce == [r[1:-1] for r in im[1:-1]], f"center = {[r[1:-1] for r in im[1:-1]]}", f"center = {[r[1:-1] for r in im[1:-1]]}")
    check(h == max(max(r) for r in im) and _srt(hr) == [i for i, r in enumerate(im) if max(r) > lim], f"hottest = {max(max(r) for r in im)}, hot_rows = {[i for i, r in enumerate(im) if max(r) > lim]}", f"hottest = {max(max(r) for r in im)}, hot_rows = {[i for i, r in enumerate(im) if max(r) > lim]}")
''',
   require=["slice", "listcomp"], refs=["8.1x", "8.8", "6.3b"])

ex(id="k8-pricelist", ch="8", lvl=2,
   title={"de": "Preisliste mit Mengenrabatt", "en": "Price list with volume discount"},
   task={"de": "Das Dictionary `prices` ordnet Artikeln ihren Stückpreis (€) zu, `order` die bestellte Menge. Ab einem Bestellwert von `discount_from` € pro Position gibt es `discount` Prozent Rabatt auf diese Position.\n- `line_totals`: Dictionary Artikel → Positionswert (Preis · Menge, nach Rabatt, auf Cent gerundet) – Dictionary-Comprehension\n- `discounted`: sortierte Liste der Artikel, die Rabatt bekommen haben\n- `total`: der Gesamtbetrag (auf Cent gerundet)\n- `unknown`: sortierte Liste der bestellten Artikel, die nicht in der Preisliste stehen – sie werden bei den Summen **ignoriert**",
         "en": "The dictionary `prices` maps items to their unit price (€), `order` to the ordered quantity. From an order value of `discount_from` € per line, there is a discount of `discount` percent on that line.\n- `line_totals`: dictionary item → line value (price · quantity, after discount, rounded to cents) – dictionary comprehension\n- `discounted`: sorted list of the items that received a discount\n- `total`: the total amount (rounded to cents)\n- `unknown`: sorted list of ordered items that are not in the price list – they are **ignored** in the sums"},
   starter={"de": "prices = {'Kugellager': 4.80, 'Dichtring': 1.20, 'Schraube M8': 0.12, 'Zahnriemen': 18.50}\norder = {'Kugellager': 30, 'Schraube M8': 500, 'Zahnriemen': 2, 'Kupplung': 1}\ndiscount_from = 100.0\ndiscount = 5\n\n# Ihr Code:\n", "en": "prices = {'Kugellager': 4.80, 'Dichtring': 1.20, 'Schraube M8': 0.12, 'Zahnriemen': 18.50}\norder = {'Kugellager': 30, 'Schraube M8': 500, 'Zahnriemen': 2, 'Kupplung': 1}\ndiscount_from = 100.0\ndiscount = 5\n\n# your code:\n"},
   solution="prices = {'Kugellager': 4.80, 'Dichtring': 1.20, 'Schraube M8': 0.12, 'Zahnriemen': 18.50}\norder = {'Kugellager': 30, 'Schraube M8': 500, 'Zahnriemen': 2, 'Kupplung': 1}\ndiscount_from = 100.0\ndiscount = 5\nraw = {item: prices[item] * qty for item, qty in order.items() if item in prices}\nline_totals = {item: round(v * (1 - discount / 100), 2) if v >= discount_from else round(v, 2) for item, v in raw.items()}\ndiscounted = sorted([item for item, v in raw.items() if v >= discount_from])\ntotal = round(sum(line_totals.values()), 2)\nunknown = sorted([item for item in order if item not in prices])\nprint(line_totals, discounted, total, unknown)\n",
   tests='''
P = {'Kugellager': 4.80, 'Dichtring': 1.20, 'Schraube M8': 0.12, 'Zahnriemen': 18.50}
for o, df, d in [({'Kugellager': 30, 'Schraube M8': 500, 'Zahnriemen': 2, 'Kupplung': 1}, 100.0, 5), ({'Dichtring': 10}, 5.0, 10), ({'X': 3}, 1.0, 50), ({'Zahnriemen': 2, 'Dichtring': 1}, 37.0, 10)]:
    ns, out = run(sub={"order": dict(o), "discount_from": df, "discount": d})
    lt, ds, t, u = need(ns, "line_totals", "discounted", "total", "unknown")
    raw = {k: P[k] * q for k, q in o.items() if k in P}
    e = {k: round(v * (1 - d / 100), 2) if v >= df else round(v, 2) for k, v in raw.items()}
    check(isinstance(lt, dict) and set(lt) == set(e) and all(approx(lt[k], e[k]) for k in e), f"line_totals = {e}", f"line_totals = {e}")
    check(ds == sorted(k for k, v in raw.items() if v >= df) and u == sorted(k for k in o if k not in P), f"discounted = {sorted(k for k, v in raw.items() if v >= df)}, unknown = {sorted(k for k in o if k not in P)}", f"discounted = {sorted(k for k, v in raw.items() if v >= df)}, unknown = {sorted(k for k in o if k not in P)}")
    check(approx(t, round(sum(e.values()), 2)), f"total = {round(sum(e.values()), 2)} €", f"total = {round(sum(e.values()), 2)} €")
''',
   require=["listcomp", "dict_methods"], refs=["8.8", "8.3"])

ex(id="k8-polyline", ch="8", lvl=2,
   title={"de": "Länge einer Fräsbahn", "en": "Length of a milling path"},
   task={"de": "Eine Fräsbahn ist als Liste von Punkten `path` gegeben; jeder Punkt ist ein Tupel `(x, y)` in mm. Berechnen Sie\n- `segments`: die Liste der Einzellängen zwischen aufeinanderfolgenden Punkten in der Reihenfolge der Bahn – Tipp: `zip(path, path[1:])` liefert Paare benachbarter Punkte; Länge = $\\sqrt{\\Delta x^2 + \\Delta y^2}$\n- `length`: die Gesamtlänge der Bahn\n- `bbox`: das Tupel `(x_min, y_min, x_max, y_max)` der kleinsten umschließenden Rechteckfläche (Bounding Box) – mit List Comprehensions für die x- und y-Werte\n- `closed`: ob die Bahn wieder am Startpunkt endet",
         "en": "A milling path is given as a list of points `path`; each point is a tuple `(x, y)` in mm. Compute\n- `segments`: the list of the individual lengths between consecutive points in the order of the path – tip: `zip(path, path[1:])` gives pairs of neighbouring points; length = $\\sqrt{\\Delta x^2 + \\Delta y^2}$\n- `length`: the total length of the path\n- `bbox`: the tuple `(x_min, y_min, x_max, y_max)` of the smallest enclosing rectangle (bounding box) – using list comprehensions for the x and y values\n- `closed`: whether the path ends at the starting point again"},
   starter={"de": "path = [(0, 0), (40, 0), (40, 30), (10, 30), (0, 0)]\n\n# Ihr Code:\n", "en": "path = [(0, 0), (40, 0), (40, 30), (10, 30), (0, 0)]\n\n# your code:\n"},
   solution='path = [(0, 0), (40, 0), (40, 30), (10, 30), (0, 0)]\nsegments = [((x2 - x1)**2 + (y2 - y1)**2) ** 0.5 for (x1, y1), (x2, y2) in zip(path, path[1:])]\nlength = sum(segments)\nxs = [p[0] for p in path]\nys = [p[1] for p in path]\nbbox = (min(xs), min(ys), max(xs), max(ys))\nclosed = path[0] == path[-1]\nprint(segments, round(length, 2), bbox, closed)\n',
   tests='''
for p in [[(0, 0), (40, 0), (40, 30), (10, 30), (0, 0)], [(5, 5), (8, 9)], [(-2.0, 1.0), (3.0, 1.0), (3.0, -4.0)]]:
    ns, out = run(sub={"path": p})
    s, l, b, c = need(ns, "segments", "length", "bbox", "closed")
    es = [((q[0] - r[0])**2 + (q[1] - r[1])**2) ** 0.5 for r, q in zip(p, p[1:])]
    check(len(s) == len(es) and all(approx(x, y) for x, y in zip(s, es)), f"segments = {[round(x, 3) for x in es]}", f"segments = {[round(x, 3) for x in es]}")
    check(approx(l, sum(es)), f"length = {sum(es):.3f} mm", f"length = {sum(es):.3f} mm")
    eb = (min(x for x, _ in p), min(y for _, y in p), max(x for x, _ in p), max(y for _, y in p))
    check(tuple(b) == eb and isinstance(b, tuple) and c is (p[0] == p[-1]), f"bbox = {eb}, closed = {p[0] == p[-1]}", f"bbox = {eb}, closed = {p[0] == p[-1]}")
''',
   require=["enumzip", "slice"], refs=["8.9", "8.4", "8.1x"])

# ------------------------------------------------------------------ Stufe 3
ex(id="k8-network", ch="8", lvl=3,
   title={"de": "Erreichbare Knoten im Leitungsnetz", "en": "Reachable nodes in a pipe network"},
   task={"de": "Ein Fernwärmenetz ist als Dictionary `network` gespeichert: Knoten → Liste der direkt verbundenen Knoten. Durch einen Schaden sind die Leitungen in `broken` (Liste von Tupeln `(a, b)`) gesperrt – in beiden Richtungen.\n\nBestimmen Sie, welche Knoten vom Heizwerk `start` aus noch erreichbar sind:\n- Arbeiten Sie mit einer Liste `todo` (noch zu besuchende Knoten, anfangs `[start]`) und einem Set `reachable`.\n- Nehmen Sie solange Knoten aus `todo` (`pop`), bis die Liste leer ist, und fügen Sie alle Nachbarn hinzu, die über eine **nicht** gesperrte Leitung erreichbar und noch nicht in `reachable` sind.\n\nSpeichern Sie `reachable` (Set, inklusive `start`) und `cut_off`: die sortierte Liste der Knoten, die nicht mehr erreichbar sind.",
         "en": "A district heating network is stored as a dictionary `network`: node → list of directly connected nodes. Due to damage, the pipes in `broken` (list of tuples `(a, b)`) are blocked – in both directions.\n\nDetermine which nodes can still be reached from the heating plant `start`:\n- Work with a list `todo` (nodes still to visit, initially `[start]`) and a set `reachable`.\n- Keep taking nodes from `todo` (`pop`) until the list is empty, and add all neighbours that can be reached via a pipe that is **not** blocked and are not yet in `reachable`.\n\nStore `reachable` (set, including `start`) and `cut_off`: the sorted list of nodes that can no longer be reached."},
   starter={"de": "network = {\n    'HW': ['A', 'B'],\n    'A': ['HW', 'C'],\n    'B': ['HW', 'C', 'D'],\n    'C': ['A', 'B', 'E'],\n    'D': ['B'],\n    'E': ['C'],\n}\nbroken = [('B', 'D'), ('A', 'C')]\nstart = 'HW'\n\n# Ihr Code:\n", "en": "network = {\n    'HW': ['A', 'B'],\n    'A': ['HW', 'C'],\n    'B': ['HW', 'C', 'D'],\n    'C': ['A', 'B', 'E'],\n    'D': ['B'],\n    'E': ['C'],\n}\nbroken = [('B', 'D'), ('A', 'C')]\nstart = 'HW'\n\n# your code:\n"},
   solution="network = {\n    'HW': ['A', 'B'],\n    'A': ['HW', 'C'],\n    'B': ['HW', 'C', 'D'],\n    'C': ['A', 'B', 'E'],\n    'D': ['B'],\n    'E': ['C'],\n}\nbroken = [('B', 'D'), ('A', 'C')]\nstart = 'HW'\nblocked = set()\nfor a, b in broken:\n    blocked.add((a, b))\n    blocked.add((b, a))\nreachable = {start}\ntodo = [start]\nwhile len(todo) > 0:\n    node = todo.pop()\n    for neighbour in network[node]:\n        if (node, neighbour) not in blocked and neighbour not in reachable:\n            reachable.add(neighbour)\n            todo.append(neighbour)\ncut_off = sorted(set(network).difference(reachable))\nprint(sorted(reachable), cut_off)\n",
   tests='''
def ref(net, br, s):
    bl = set(br) | {(b, a) for a, b in br}
    seen, todo = {s}, [s]
    while todo:
        n = todo.pop()
        for m in net[n]:
            if (n, m) not in bl and m not in seen:
                seen.add(m); todo.append(m)
    return seen, sorted(set(net) - seen)
N = {'HW': ['A', 'B'], 'A': ['HW', 'C'], 'B': ['HW', 'C', 'D'], 'C': ['A', 'B', 'E'], 'D': ['B'], 'E': ['C']}
for br, s in [([('B', 'D'), ('A', 'C')], 'HW'), ([], 'HW'), ([('HW', 'A'), ('B', 'HW')], 'HW'), ([('C', 'B')], 'D')]:
    ns, out = run(sub={"broken": br, "start": s})
    r, c = need(ns, "reachable", "cut_off")
    er, ec = ref(N, br, s)
    check(isinstance(r, set) and r == er, f"gesperrt {br}, Start {s}: erreichbar {sorted(er)}", f"blocked {br}, start {s}: reachable {sorted(er)}")
    check(c == ec, f"cut_off = {ec}", f"cut_off = {ec}")
''',
   require=["set", "dict"], refs=["8.2", "8.3", "8.4"])

ex(id="k8-sparse", ch="8", lvl=3,
   title={"de": "Dünnbesetzte Matrix", "en": "Sparse matrix"},
   task={"de": "Steifigkeitsmatrizen aus der FEM sind riesig, enthalten aber fast nur Nullen. Man speichert deshalb nur die Einträge ≠ 0 – in einem Dictionary mit **Tupeln als Schlüsseln**: `{(zeile, spalte): wert}`. Die Größe der Matrix ist `n` × `n`.\n- `dense`: die vollständige Matrix als verschachtelte Liste (fehlende Einträge sind 0.0) – verschachtelte List Comprehension mit `.get()`\n- `Kv`: das Produkt Matrix · Vektor `v`, berechnet **nur über die gespeicherten Einträge** (Schleife über `.items()`, Ergebnis als Liste mit n Einträgen)\n- `density`: der Anteil der gespeicherten Einträge an allen $n^2$ Einträgen in Prozent\n- `symmetric`: ob für jeden gespeicherten Eintrag (i, j) auch (j, i) mit demselben Wert existiert",
         "en": "Stiffness matrices from FEM are huge but contain almost only zeros. Therefore only the entries ≠ 0 are stored – in a dictionary with **tuples as keys**: `{(row, column): value}`. The size of the matrix is `n` × `n`.\n- `dense`: the complete matrix as a nested list (missing entries are 0.0) – nested list comprehension with `.get()`\n- `Kv`: the product matrix · vector `v`, computed **only over the stored entries** (loop over `.items()`, result as a list with n entries)\n- `density`: the share of the stored entries in all $n^2$ entries in percent\n- `symmetric`: whether for every stored entry (i, j) there is also (j, i) with the same value"},
   starter={"de": "n = 4\nK = {(0, 0): 2.0, (0, 1): -1.0, (1, 0): -1.0, (1, 1): 2.0, (1, 2): -1.0,\n     (2, 1): -1.0, (2, 2): 2.0, (2, 3): -1.0, (3, 2): -1.0, (3, 3): 1.0}\nv = [1.0, 2.0, 3.0, 4.0]\n\n# Ihr Code:\n", "en": "n = 4\nK = {(0, 0): 2.0, (0, 1): -1.0, (1, 0): -1.0, (1, 1): 2.0, (1, 2): -1.0,\n     (2, 1): -1.0, (2, 2): 2.0, (2, 3): -1.0, (3, 2): -1.0, (3, 3): 1.0}\nv = [1.0, 2.0, 3.0, 4.0]\n\n# your code:\n"},
   solution='n = 4\nK = {(0, 0): 2.0, (0, 1): -1.0, (1, 0): -1.0, (1, 1): 2.0, (1, 2): -1.0,\n     (2, 1): -1.0, (2, 2): 2.0, (2, 3): -1.0, (3, 2): -1.0, (3, 3): 1.0}\nv = [1.0, 2.0, 3.0, 4.0]\ndense = [[K.get((i, j), 0.0) for j in range(n)] for i in range(n)]\nKv = [0.0 for i in range(n)]\nfor (i, j), value in K.items():\n    Kv[i] += value * v[j]\ndensity = len(K) / n**2 * 100\nsymmetric = True\nfor (i, j), value in K.items():\n    if K.get((j, i)) != value:\n        symmetric = False\nprint(dense, Kv, density, symmetric)\n',
   tests='''
K1 = {(0, 0): 2.0, (0, 1): -1.0, (1, 0): -1.0, (1, 1): 2.0, (1, 2): -1.0, (2, 1): -1.0, (2, 2): 2.0, (2, 3): -1.0, (3, 2): -1.0, (3, 3): 1.0}
for n, K, v in [(4, K1, [1.0, 2.0, 3.0, 4.0]), (3, {(0, 2): 5.0, (1, 1): 1.0}, [1.0, 1.0, 2.0]), (2, {}, [3.0, 4.0])]:
    ns, out = run(sub={"n": n, "K": K, "v": v})
    d, kv, de, sy = need(ns, "dense", "Kv", "density", "symmetric")
    ed = [[K.get((i, j), 0.0) for j in range(n)] for i in range(n)]
    ekv = [sum(ed[i][j] * v[j] for j in range(n)) for i in range(n)]
    check(d == ed, f"n = {n}: dense = {ed}", f"n = {n}: dense = {ed}")
    check(len(kv) == n and all(approx(a, b) for a, b in zip(kv, ekv)), f"K·v = {ekv}", f"K·v = {ekv}")
    es = all(K.get((j, i)) == x for (i, j), x in K.items())
    check(approx(de, len(K) / n**2 * 100) and sy is es, f"density = {len(K) / n**2 * 100:.1f} %, symmetric = {es}", f"density = {len(K) / n**2 * 100:.1f} %, symmetric = {es}")
''',
   require=["listcomp", "dict_methods"], refs=["8.4", "8.3", "8.8", "6.3b"])

ex(id="k8-merge", ch="8", lvl=3,
   title={"de": "Zwei Messreihen zusammenführen", "en": "Merging two measurement series"},
   task={"de": "Zwei Temperatursensoren haben unabhängig voneinander gemessen; manche Zeitpunkte fehlen bei einem der beiden. Die Daten liegen als Dictionaries Zeit (min) → Temperatur vor: `s1` und `s2`.\n- `times`: die sortierte Liste **aller** Zeitpunkte, an denen mindestens ein Sensor gemessen hat (Vereinigungsmenge)\n- `both`: die sortierte Liste der Zeitpunkte, an denen beide gemessen haben\n- `merged`: Dictionary Zeit → Temperatur: der Mittelwert, wenn beide gemessen haben, sonst der vorhandene Wert\n- `max_diff`: die größte Abweichung $|s_1 - s_2|$ an den gemeinsamen Zeitpunkten (0, wenn es keine gibt)\n- `gaps`: Liste von Tupeln `(zeit, sensorname)` für jeden fehlenden Messwert, z.B. `(10, 's2')`, sortiert nach der Zeit",
         "en": "Two temperature sensors measured independently; some points in time are missing for one of them. The data are dictionaries time (min) → temperature: `s1` and `s2`.\n- `times`: the sorted list of **all** points in time at which at least one sensor measured (union)\n- `both`: the sorted list of the points in time at which both measured\n- `merged`: dictionary time → temperature: the mean if both measured, otherwise the available value\n- `max_diff`: the largest deviation $|s_1 - s_2|$ at the common points in time (0 if there are none)\n- `gaps`: list of tuples `(time, sensorname)` for every missing reading, e.g. `(10, 's2')`, sorted by time"},
   starter={"de": "s1 = {0: 20.1, 5: 21.4, 10: 22.9, 20: 25.0}\ns2 = {0: 20.4, 5: 21.0, 15: 24.1, 20: 25.6}\n\n# Ihr Code:\n", "en": "s1 = {0: 20.1, 5: 21.4, 10: 22.9, 20: 25.0}\ns2 = {0: 20.4, 5: 21.0, 15: 24.1, 20: 25.6}\n\n# your code:\n"},
   solution="s1 = {0: 20.1, 5: 21.4, 10: 22.9, 20: 25.0}\ns2 = {0: 20.4, 5: 21.0, 15: 24.1, 20: 25.6}\ntimes = sorted(set(s1).union(set(s2)))\nboth = sorted(set(s1).intersection(set(s2)))\nmerged = {}\ngaps = []\nfor t in times:\n    if t in s1 and t in s2:\n        merged[t] = (s1[t] + s2[t]) / 2\n    elif t in s1:\n        merged[t] = s1[t]\n        gaps.append((t, 's2'))\n    else:\n        merged[t] = s2[t]\n        gaps.append((t, 's1'))\nmax_diff = 0\nfor t in both:\n    if abs(s1[t] - s2[t]) > max_diff:\n        max_diff = abs(s1[t] - s2[t])\nprint(times, both, merged, round(max_diff, 2), gaps)\n",
   tests='''
for a, b in [({0: 20.1, 5: 21.4, 10: 22.9, 20: 25.0}, {0: 20.4, 5: 21.0, 15: 24.1, 20: 25.6}), ({1: 5.0}, {2: 6.0}), ({0: 1.0, 1: 2.0}, {0: 1.5, 1: 1.0}), ({0: 3.0, 1: 2.0}, {0: 1.0, 1: 2.1})]:
    ns, out = run(sub={"s1": a, "s2": b})
    t, bo, m, md, g = need(ns, "times", "both", "merged", "max_diff", "gaps")
    et = sorted(set(a) | set(b)); eb = sorted(set(a) & set(b))
    em = {k: (a[k] + b[k]) / 2 if k in a and k in b else a.get(k, b.get(k)) for k in et}
    check(t == et and bo == eb, f"times = {et}, both = {eb}", f"times = {et}, both = {eb}")
    check(isinstance(m, dict) and set(m) == set(em) and all(approx(m[k], em[k]) for k in em), f"merged = {em}", f"merged = {em}")
    emd = max([abs(a[k] - b[k]) for k in eb], default=0)
    eg = [(k, 's2' if k in a else 's1') for k in et if not (k in a and k in b)]
    check(approx(md, emd) and g == eg, f"max_diff = {emd:.2f}, gaps = {eg}", f"max_diff = {emd:.2f}, gaps = {eg}")
''',
   require=["set_methods", "dict"], refs=["8.2", "8.3", "8.4"])

ex(id="k8-bomdiff", ch="8", lvl=3,
   title={"de": "Stücklistenversionen vergleichen", "en": "Comparing BOM versions"},
   task={"de": "Nach einer Konstruktionsänderung gibt es eine neue Version der Stückliste. Beide Versionen sind Dictionaries Teil → Stückzahl: `old` und `new`. Erstellen Sie den Änderungsbericht:\n- `added`: sortierte Liste der Teile, die neu hinzugekommen sind\n- `removed`: sortierte Liste der Teile, die weggefallen sind\n- `changed`: Dictionary Teil → Tupel `(alt, neu)` für alle Teile, die in beiden Versionen vorkommen, deren Stückzahl sich aber geändert hat (Dictionary-Comprehension über die Schnittmenge)\n- `n_changes`: die Gesamtzahl der Änderungen (hinzugefügt + entfernt + geändert)\n\nBerechnen Sie außerdem `delta`: Dictionary Teil → Mengenänderung (neu − alt) für **alle** Teile aus beiden Versionen, wobei fehlende Teile als 0 Stück zählen; Teile mit Änderung 0 werden weggelassen.",
         "en": "After a design change, there is a new version of the bill of materials. Both versions are dictionaries part → quantity: `old` and `new`. Create the change report:\n- `added`: sorted list of the parts that were added\n- `removed`: sorted list of the parts that were removed\n- `changed`: dictionary part → tuple `(old, new)` for all parts present in both versions whose quantity changed (dictionary comprehension over the intersection)\n- `n_changes`: the total number of changes (added + removed + changed)\n\nAlso compute `delta`: dictionary part → quantity change (new − old) for **all** parts from both versions, where missing parts count as 0 pieces; parts with a change of 0 are left out."},
   starter={"de": "old = {'Gehäuse': 1, 'Deckel': 1, 'M6x20': 8, 'Dichtung': 1, 'Federring': 8}\nnew = {'Gehäuse': 1, 'Deckel': 1, 'M6x20': 6, 'Dichtung': 2, 'Sensor': 1}\n\n# Ihr Code:\n", "en": "old = {'Gehäuse': 1, 'Deckel': 1, 'M6x20': 8, 'Dichtung': 1, 'Federring': 8}\nnew = {'Gehäuse': 1, 'Deckel': 1, 'M6x20': 6, 'Dichtung': 2, 'Sensor': 1}\n\n# your code:\n"},
   solution="old = {'Gehäuse': 1, 'Deckel': 1, 'M6x20': 8, 'Dichtung': 1, 'Federring': 8}\nnew = {'Gehäuse': 1, 'Deckel': 1, 'M6x20': 6, 'Dichtung': 2, 'Sensor': 1}\nadded = sorted(set(new).difference(set(old)))\nremoved = sorted(set(old).difference(set(new)))\ncommon = set(old).intersection(set(new))\nchanged = {p: (old[p], new[p]) for p in common if old[p] != new[p]}\nn_changes = len(added) + len(removed) + len(changed)\ndelta = {}\nfor p in set(old).union(set(new)):\n    d = new.get(p, 0) - old.get(p, 0)\n    if d != 0:\n        delta[p] = d\nprint(added, removed, changed, n_changes, delta)\n",
   tests='''
for o, n in [({'Gehäuse': 1, 'Deckel': 1, 'M6x20': 8, 'Dichtung': 1, 'Federring': 8}, {'Gehäuse': 1, 'Deckel': 1, 'M6x20': 6, 'Dichtung': 2, 'Sensor': 1}), ({'A': 1}, {'A': 1}), ({}, {'X': 3})]:
    ns, out = run(sub={"old": o, "new": n})
    a, r, c, nc, d = need(ns, "added", "removed", "changed", "n_changes", "delta")
    ea, er = sorted(set(n) - set(o)), sorted(set(o) - set(n))
    ec = {p: (o[p], n[p]) for p in set(o) & set(n) if o[p] != n[p]}
    check(a == ea and r == er, f"added = {ea}, removed = {er}", f"added = {ea}, removed = {er}")
    check(c == ec and nc == len(ea) + len(er) + len(ec), f"changed = {ec}, n_changes = {len(ea) + len(er) + len(ec)}", f"changed = {ec}, n_changes = {len(ea) + len(er) + len(ec)}")
    ed = {p: n.get(p, 0) - o.get(p, 0) for p in set(o) | set(n) if n.get(p, 0) != o.get(p, 0)}
    check(d == ed, f"delta = {ed}", f"delta = {ed}")
''',
   require=["set_methods", "dict_methods", "listcomp"], refs=["8.2", "8.3", "8.8"])

ex(id="k8-pivot", ch="8", lvl=3,
   title={"de": "Messdaten nach Tagen ordnen", "en": "Organising readings by day"},
   task={"de": "Ein Datenlogger liefert die Liste `readings` mit Tupeln `(tag, stunde, temperatur)` in beliebiger Reihenfolge. Erzeugen Sie\n- `by_day`: ein verschachteltes Dictionary Tag → {Stunde: Temperatur}\n- `daily_max`: Dictionary Tag → höchste Temperatur des Tages (`max` über die Werte)\n- `daily_mean`: Dictionary Tag → Tagesmittel, auf eine Nachkommastelle gerundet (Dictionary-Comprehension)\n- `widest`: den Tag mit der größten Spanne zwischen höchster und niedrigster Temperatur (bei Gleichstand der alphabetisch erste Tag)\n- `hours_complete`: sortierte Liste der Tage, für die alle Stunden aus `required_hours` vorliegen",
         "en": "A data logger delivers the list `readings` of tuples `(day, hour, temperature)` in arbitrary order. Create\n- `by_day`: a nested dictionary day → {hour: temperature}\n- `daily_max`: dictionary day → highest temperature of the day (`max` over the values)\n- `daily_mean`: dictionary day → daily mean, rounded to one decimal (dictionary comprehension)\n- `widest`: the day with the largest spread between highest and lowest temperature (on a tie, the alphabetically first day)\n- `hours_complete`: sorted list of the days for which all hours from `required_hours` are present"},
   starter={"de": "readings = [('Mo', 8, 14.2), ('Di', 8, 11.0), ('Mo', 12, 19.8), ('Mo', 16, 17.1),\n            ('Di', 12, 13.5), ('Mi', 8, 9.4), ('Di', 16, 12.2), ('Mi', 12, 18.9)]\nrequired_hours = [8, 12, 16]\n\n# Ihr Code:\n", "en": "readings = [('Mo', 8, 14.2), ('Di', 8, 11.0), ('Mo', 12, 19.8), ('Mo', 16, 17.1),\n            ('Di', 12, 13.5), ('Mi', 8, 9.4), ('Di', 16, 12.2), ('Mi', 12, 18.9)]\nrequired_hours = [8, 12, 16]\n\n# your code:\n"},
   solution="readings = [('Mo', 8, 14.2), ('Di', 8, 11.0), ('Mo', 12, 19.8), ('Mo', 16, 17.1),\n            ('Di', 12, 13.5), ('Mi', 8, 9.4), ('Di', 16, 12.2), ('Mi', 12, 18.9)]\nrequired_hours = [8, 12, 16]\nby_day = {}\nfor day, hour, temp in readings:\n    if day not in by_day:\n        by_day[day] = {}\n    by_day[day][hour] = temp\ndaily_max = {day: max(values.values()) for day, values in by_day.items()}\ndaily_mean = {day: round(sum(values.values()) / len(values), 1) for day, values in by_day.items()}\nwidest = None\nfor day in sorted(by_day):\n    spread = max(by_day[day].values()) - min(by_day[day].values())\n    if widest is None or spread > max(by_day[widest].values()) - min(by_day[widest].values()):\n        widest = day\nhours_complete = sorted([day for day, values in by_day.items() if set(required_hours).difference(set(values)) == set()])\nprint(by_day, daily_max, daily_mean, widest, hours_complete)\n",
   tests='''
R1 = [('Mo', 8, 14.2), ('Di', 8, 11.0), ('Mo', 12, 19.8), ('Mo', 16, 17.1), ('Di', 12, 13.5), ('Mi', 8, 9.4), ('Di', 16, 12.2), ('Mi', 12, 18.9)]
for r, req in [(R1, [8, 12, 16]), (R1, [8]), ([('B', 1, 5.0), ('A', 1, 5.0), ('A', 2, 7.0), ('B', 2, 7.0)], [1, 2, 3])]:
    ns, out = run(sub={"readings": r, "required_hours": req})
    bd, dm, dme, w, hc = need(ns, "by_day", "daily_max", "daily_mean", "widest", "hours_complete")
    eb = {}
    for d, h, t in r:
        eb.setdefault(d, {})[h] = t
    check(bd == eb, f"by_day = {eb}", f"by_day = {eb}")
    check(dm == {d: max(v.values()) for d, v in eb.items()} and all(approx(dme[d], round(sum(v.values()) / len(v), 1)) for d, v in eb.items()), "daily_max und daily_mean stimmen", "daily_max and daily_mean are correct")
    ew = min(sorted(eb), key=lambda d: -(max(eb[d].values()) - min(eb[d].values())))
    check(w == ew and hc == sorted(d for d, v in eb.items() if set(req) <= set(v)), f"widest = {ew!r}, hours_complete = {sorted(d for d, v in eb.items() if set(req) <= set(v))}", f"widest = {ew!r}, hours_complete = {sorted(d for d, v in eb.items() if set(req) <= set(v))}")
''',
   require=["dict", "listcomp", "unpack_for"], refs=["8.5", "8.4", "8.8"])
