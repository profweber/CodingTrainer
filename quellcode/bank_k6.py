from exlib import ex

# Kapitel 6: zusätzlich if/elif/else, Conditional Expression, while, for, range, break/continue, abs, isdigit, random.
# Keine Funktionen, kein sum/min/max/sorted, kein Slicing, keine Dicts/Sets/Tupel-Funktionen, kein enumerate/zip.

ex(id="k6-divider", ch="6", lvl=1,
   title={"de": "Spannungsteiler-Tabelle", "en": "Voltage divider table"},
   task={"de": "Ein Spannungsteiler aus `R1` und einem veränderlichen `R2` liegt an der Spannung `U`. Durchlaufen Sie mit einer `for`-Schleife und `range()` die Werte R2 = 100, 200, …, 1000 Ω. Berechnen Sie jeweils U₂ = U · R2 / (R1 + R2), hängen Sie den Wert an die Liste `u2_values` an und geben Sie eine Zeile wie `R2 = 100 Ohm: U2 = 0.83 V` aus.",
         "en": "A voltage divider made of `R1` and a variable `R2` is connected to voltage `U`. Use a `for` loop and `range()` to go through R2 = 100, 200, …, 1000 Ω. For each, compute U₂ = U · R2 / (R1 + R2), append the value to the list `u2_values` and print a line like `R2 = 100 Ohm: U2 = 0.83 V`."},
   starter={"de": "U = 5.0     # V\nR1 = 500.0  # Ohm\nu2_values = []\n\n# Ihr Code:\n", "en": "U = 5.0     # V\nR1 = 500.0  # Ohm\nu2_values = []\n\n# your code:\n"},
   solution='U = 5.0\nR1 = 500.0\nu2_values = []\nfor R2 in range(100, 1001, 100):\n    U2 = U * R2 / (R1 + R2)\n    u2_values.append(U2)\n    print(f"R2 = {R2} Ohm: U2 = {U2:.2f} V")\n',
   tests='''
for U, R1 in [(5.0, 500.0), (12.0, 1000.0)]:
    ns, out = run(sub={"U": U, "R1": R1})
    v = need(ns, "u2_values")
    e = [U * r / (R1 + r) for r in range(100, 1001, 100)]
    check(len(v) == 10 and all(approx(a, b) for a, b in zip(v, e)), f"u2_values für U = {U} V, R1 = {R1} Ω (10 Werte)", f"u2_values for U = {U} V, R1 = {R1} Ω (10 values)")
    check(f"{e[0]:.2f}" in out and f"{e[-1]:.2f}" in out and out.count("\\n") >= 10, "Für jedes R2 wird eine Zeile ausgegeben", "One line is printed for every R2")
''',
   require=["for", "range"], refs=["6.2b"])

ex(id="k6-battery", ch="6", lvl=1,
   title={"de": "Akkuanzeige", "en": "Battery indicator"},
   task={"de": "Lesen Sie den Ladezustand eines Akkus in Prozent ein (ganze Zahl) und geben Sie aus:\n- unter 5: `kritisch`\n- 5 bis unter 20: `niedrig`\n- 20 bis unter 80: `ok`\n- ab 80: `voll`\n- Werte unter 0 oder über 100: `ungültig`\n\nAchten Sie auf die Reihenfolge der Bedingungen.",
         "en": "Read a battery's state of charge in percent (integer) and print:\n- below 5: `critical`\n- 5 to below 20: `low`\n- 20 to below 80: `ok`\n- 80 or more: `full`\n- values below 0 or above 100: `invalid`\n\nMind the order of the conditions."},
   starter={"de": "soc = int(input(\"Ladezustand in %: \"))\n\n# Ihr Code:\n", "en": "soc = int(input(\"State of charge in %: \"))\n\n# your code:\n"},
   solution='soc = int(input("Ladezustand in %: "))\nif soc < 0 or soc > 100:\n    print("ungültig")\nelif soc < 5:\n    print("kritisch")\nelif soc < 20:\n    print("niedrig")\nelif soc < 80:\n    print("ok")\nelse:\n    print("voll")\n',
   tests='''
words = {"ungültig": "invalid", "kritisch": "critical", "niedrig": "low", "ok": "ok", "voll": "full"}
def exp(s):
    return "ungültig" if s < 0 or s > 100 else "kritisch" if s < 5 else "niedrig" if s < 20 else "ok" if s < 80 else "voll"
for s in [-3, 0, 4, 5, 19, 20, 79, 80, 100, 101]:
    ns, out = run(inputs=[str(s)])
    o = (out.split("\\n", 1)[1] if "\\n" in out else out).lower()
    e = exp(s)
    found = [w for w in words if w in o or words[w] in o]
    check(found == [e], f"{s} %: genau die Meldung '{e}'", f"{s} %: exactly the message '{words[e]}'")
''',
   stdin="57\n", require=["if"], refs=["6.1b"])

ex(id="k6-count", ch="6", lvl=1,
   title={"de": "Grenzwertüberschreitungen zählen", "en": "Counting limit violations"},
   task={"de": "Zählen Sie mit einer `for`-Schleife, wie viele Werte in `noise_db` (Lärmpegel in dB) über dem Grenzwert `limit` liegen (`n_over`), und sammeln Sie diese Werte in der Liste `over`. Geben Sie anschließend den Anteil der Überschreitungen in Prozent aus (`share`, auf eine Nachkommastelle gerundet).",
         "en": "Use a `for` loop to count how many values in `noise_db` (noise levels in dB) are above the limit `limit` (`n_over`), and collect those values in the list `over`. Then compute the share of violations in percent (`share`, rounded to one decimal)."},
   starter={"de": "noise_db = [62.5, 71.0, 85.3, 68.2, 90.1, 79.9, 80.0, 84.7]\nlimit = 80.0\nn_over = 0\nover = []\n\n# Ihr Code:\n", "en": "noise_db = [62.5, 71.0, 85.3, 68.2, 90.1, 79.9, 80.0, 84.7]\nlimit = 80.0\nn_over = 0\nover = []\n\n# your code:\n"},
   solution='noise_db = [62.5, 71.0, 85.3, 68.2, 90.1, 79.9, 80.0, 84.7]\nlimit = 80.0\nn_over = 0\nover = []\nfor level in noise_db:\n    if level > limit:\n        n_over += 1\n        over.append(level)\nshare = round(n_over / len(noise_db) * 100, 1)\nprint(n_over, over, share)\n',
   tests='''
for d, lim in [([62.5, 71.0, 85.3, 68.2, 90.1, 79.9, 80.0, 84.7], 80.0), ([50.0, 55.0], 60.0), ([90.0, 91.0, 70.0], 85.0)]:
    ns, out = run(sub={"noise_db": d, "limit": lim})
    n, o, s = need(ns, "n_over", "over", "share")
    eo = [x for x in d if x > lim]
    check(n == len(eo) and o == eo, f"Grenzwert {lim} dB: {len(eo)} Überschreitungen {eo}", f"limit {lim} dB: {len(eo)} violations {eo}")
    check(approx(s, round(len(eo) / len(d) * 100, 1)), f"Anteil = {round(len(eo)/len(d)*100, 1)} %", f"share = {round(len(eo)/len(d)*100, 1)} %")
''',
   require=["for", "if"], refs=["6.2b", "6.1a"])

ex(id="k6-argmax", ch="6", lvl=2,
   title={"de": "Spitzenwert und Zeitpunkt", "en": "Peak value and time"},
   task={"de": "Finden Sie in der Messreihe `force` (in kN, ein Wert pro Sekunde) den größten Wert `peak` und seinen Index `t_peak` – **ohne** `max()`, mit einer Schleife über `range(len(force))`. Kommt das Maximum mehrfach vor, zählt das erste Auftreten. Geben Sie `Maximale Kraft 12.4 kN nach 3 s` aus.",
         "en": "Find the largest value `peak` in the series `force` (in kN, one value per second) and its index `t_peak` – **without** `max()`, using a loop over `range(len(force))`. If the maximum occurs more than once, the first occurrence counts. Print `Maximum force 12.4 kN after 3 s`."},
   starter={"de": "force = [2.1, 5.8, 9.7, 12.4, 11.0, 12.4, 6.3]\n\n# Ihr Code:\n", "en": "force = [2.1, 5.8, 9.7, 12.4, 11.0, 12.4, 6.3]\n\n# your code:\n"},
   solution='force = [2.1, 5.8, 9.7, 12.4, 11.0, 12.4, 6.3]\npeak = force[0]\nt_peak = 0\nfor i in range(len(force)):\n    if force[i] > peak:\n        peak = force[i]\n        t_peak = i\nprint(f"Maximale Kraft {peak} kN nach {t_peak} s")\n',
   tests='''
for f in [[2.1, 5.8, 9.7, 12.4, 11.0, 12.4, 6.3], [-3.0, -1.0, -2.0], [7.0], [4.0, 4.0, 1.0]]:
    ns, out = run(sub={"force": f})
    p, t = need(ns, "peak", "t_peak")
    check(p == max(f) and t == f.index(max(f)), f"{f}: peak = {max(f)} bei Index {f.index(max(f))}", f"{f}: peak = {max(f)} at index {f.index(max(f))}")
''',
   require=["for", "range"], forbid=["seqfuncs"], refs=["6.2b", "6.1a"])

ex(id="k6-checkdigit", ch="6", lvl=2,
   title={"de": "Quersumme und Prüfziffer", "en": "Digit sum and check digit"},
   task={"de": "Lesen Sie eine Artikelnummer als ganze Zahl ein. Berechnen Sie mit einer `while`-Schleife ihre Quersumme `digit_sum` (letzte Ziffer mit `% 10`, abschneiden mit `// 10`). Die Prüfziffer `check_digit` ist die Zahl, die man zur Quersumme addieren muss, um das nächste Vielfache von 10 zu erreichen (0, wenn die Quersumme schon durch 10 teilbar ist).",
         "en": "Read an article number as an integer. Use a `while` loop to compute its digit sum `digit_sum` (last digit with `% 10`, cut it off with `// 10`). The check digit `check_digit` is the number you must add to the digit sum to reach the next multiple of 10 (0 if the digit sum is already divisible by 10)."},
   starter={"de": "number = int(input(\"Artikelnummer: \"))\n\n# Ihr Code:\n", "en": "number = int(input(\"Article number: \"))\n\n# your code:\n"},
   solution='number = int(input("Artikelnummer: "))\ndigit_sum = 0\nn = number\nwhile n > 0:\n    digit_sum += n % 10\n    n = n // 10\ncheck_digit = (10 - digit_sum % 10) % 10\nprint(digit_sum, check_digit)\n',
   tests='''
for n in [40317, 55, 9, 1000000, 123456789]:
    ns, out = run(inputs=[str(n)])
    ds, cd = need(ns, "digit_sum", "check_digit")
    eds = sum(int(c) for c in str(n))
    check(ds == eds, f"{n}: Quersumme {eds}", f"{n}: digit sum {eds}")
    check(cd == (10 - eds % 10) % 10, f"{n}: Prüfziffer {(10 - eds % 10) % 10}", f"{n}: check digit {(10 - eds % 10) % 10}")
''',
   stdin="40317\n", require=["while"], refs=["6.2a", "4.2"])

ex(id="k6-energy", ch="6", lvl=2,
   title={"de": "Energiezähler mit Abschaltung", "en": "Energy meter with cut-off"},
   task={"de": "Ein Leistungsmesser liefert alle 15 Minuten einen Leistungswert in kW (`power_kw`). Summieren Sie die Energie in kWh auf (jeder Wert × 0.25 h) und speichern Sie den Zwischenstand nach jedem Intervall in der Liste `cumulative`. Sobald die Energie das Budget `budget_kwh` **überschreitet**, soll die Schleife mit `break` abbrechen. Speichern Sie in `cutoff` den Index des Intervalls, in dem das passiert ist (`None`, falls das Budget nie überschritten wird).",
         "en": "A power meter delivers a power value in kW every 15 minutes (`power_kw`). Sum up the energy in kWh (each value × 0.25 h) and store the running total after each interval in the list `cumulative`. As soon as the energy **exceeds** the budget `budget_kwh`, leave the loop with `break`. Store in `cutoff` the index of the interval where that happened (`None` if the budget is never exceeded)."},
   starter={"de": "power_kw = [3.2, 4.8, 6.1, 5.5, 7.9, 2.0, 1.5]\nbudget_kwh = 5.0\ncumulative = []\ncutoff = None\n\n# Ihr Code:\n", "en": "power_kw = [3.2, 4.8, 6.1, 5.5, 7.9, 2.0, 1.5]\nbudget_kwh = 5.0\ncumulative = []\ncutoff = None\n\n# your code:\n"},
   solution='power_kw = [3.2, 4.8, 6.1, 5.5, 7.9, 2.0, 1.5]\nbudget_kwh = 5.0\ncumulative = []\ncutoff = None\nenergy = 0\nfor i in range(len(power_kw)):\n    energy += power_kw[i] * 0.25\n    cumulative.append(energy)\n    if energy > budget_kwh:\n        cutoff = i\n        break\nprint(cumulative, cutoff)\n',
   tests='''
def ref(p, b):
    c, e = [], 0
    for i, x in enumerate(p):
        e += x * 0.25; c.append(e)
        if e > b:
            return c, i
    return c, None
for p, b in [([3.2, 4.8, 6.1, 5.5, 7.9, 2.0, 1.5], 5.0), ([1.0, 1.0, 1.0], 10.0), ([30.0, 1.0], 2.0), ([4.0, 4.0, 4.0], 2.0)]:
    ns, out = run(sub={"power_kw": p, "budget_kwh": b})
    c, k = need(ns, "cumulative", "cutoff")
    ec, ek = ref(p, b)
    check(len(c) == len(ec) and all(approx(x, y) for x, y in zip(c, ec)), f"Budget {b} kWh: cumulative = {[round(x, 3) for x in ec]}", f"budget {b} kWh: cumulative = {[round(x, 3) for x in ec]}")
    check(k == ek, f"cutoff = {ek}", f"cutoff = {ek}")
''',
   require=["break"], refs=["6.2c", "6.2b"])

ex(id="k6-bisection", ch="6", lvl=3,
   title={"de": "Bisektionsverfahren", "en": "Bisection method"},
   task={"de": "Bestimmen Sie die Nullstelle von f(x) = x³ − 2x − 5 im Intervall [`a`, `b`] mit dem Bisektionsverfahren:\n1. Mittelpunkt m = (a + b) / 2 berechnen.\n2. Haben f(a) und f(m) unterschiedliche Vorzeichen (f(a)·f(m) < 0), liegt die Nullstelle links: b = m. Sonst: a = m.\n3. Wiederholen, solange die Intervallbreite b − a größer als `tol` ist.\n\nSpeichern Sie die Näherung (Mittelpunkt des letzten Intervalls) in `root` und die Anzahl der Halbierungen in `steps`.",
         "en": "Find the root of f(x) = x³ − 2x − 5 in the interval [`a`, `b`] with the bisection method:\n1. Compute the midpoint m = (a + b) / 2.\n2. If f(a) and f(m) have different signs (f(a)·f(m) < 0), the root is on the left: b = m. Otherwise: a = m.\n3. Repeat while the interval width b − a is greater than `tol`.\n\nStore the approximation (midpoint of the last interval) in `root` and the number of halvings in `steps`."},
   starter={"de": "a = 2.0\nb = 3.0\ntol = 1e-6\n\n# Ihr Code:\n", "en": "a = 2.0\nb = 3.0\ntol = 1e-6\n\n# your code:\n"},
   solution='a = 2.0\nb = 3.0\ntol = 1e-6\nsteps = 0\nwhile b - a > tol:\n    m = (a + b) / 2\n    fa = a**3 - 2 * a - 5\n    fm = m**3 - 2 * m - 5\n    if fa * fm < 0:\n        b = m\n    else:\n        a = m\n    steps += 1\nroot = (a + b) / 2\nprint(root, steps)\n',
   tests='''
import math as _m
for a, b, tol in [(2.0, 3.0, 1e-6), (0.0, 5.0, 1e-9), (2.0, 2.5, 1e-3)]:
    ns, out = run(sub={"a": a, "b": b, "tol": tol})
    r, s = need(ns, "root", "steps")
    es = _m.ceil(_m.log2((b - a) / tol))
    check(abs(r - 2.0945514815423265) <= tol, f"Intervall [{a}, {b}], tol = {tol}: root ≈ 2.094551", f"interval [{a}, {b}], tol = {tol}: root ≈ 2.094551")
    check(s == es, f"Anzahl Halbierungen = {es}", f"number of halvings = {es}")
''',
   require=["while", "if"], refs=["6.2a", "6.3a"])

ex(id="k6-histogram", ch="6", lvl=3,
   title={"de": "Histogramm in der Konsole", "en": "Histogram in the console"},
   task={"de": "Teilen Sie die Messwerte `values` in `n_bins` Klassen der Breite `width` ein, beginnend bei `start` (Klasse k umfasst start + k·width ≤ x < start + (k+1)·width). Werte außerhalb aller Klassen werden in `outside` gezählt.\n- Legen Sie die Liste `counts` mit `n_bins` Nullen an (z.B. mit einer Schleife und `append`) und zählen Sie hoch.\n- Geben Sie für jede Klasse eine Zeile wie `20.0 - 22.0 | **` aus (ein `*` pro Wert; Tipp: `\"*\" * 3` ergibt `\"***\"`).",
         "en": "Sort the measurements `values` into `n_bins` classes of width `width`, starting at `start` (class k covers start + k·width ≤ x < start + (k+1)·width). Values outside all classes are counted in `outside`.\n- Create the list `counts` with `n_bins` zeros (e.g. with a loop and `append`) and count up.\n- For each class, print a line like `20.0 - 22.0 | **` (one `*` per value; tip: `\"*\" * 3` gives `\"***\"`)."},
   starter={"de": "values = [21.3, 23.8, 22.1, 25.6, 20.4, 23.1, 24.9, 22.7, 29.9, 18.2]\nstart = 20.0\nwidth = 2.0\nn_bins = 3\n\n# Ihr Code:\n", "en": "values = [21.3, 23.8, 22.1, 25.6, 20.4, 23.1, 24.9, 22.7, 29.9, 18.2]\nstart = 20.0\nwidth = 2.0\nn_bins = 3\n\n# your code:\n"},
   solution='values = [21.3, 23.8, 22.1, 25.6, 20.4, 23.1, 24.9, 22.7, 29.9, 18.2]\nstart = 20.0\nwidth = 2.0\nn_bins = 3\ncounts = []\nfor k in range(n_bins):\n    counts.append(0)\noutside = 0\nfor x in values:\n    k = int((x - start) // width)\n    if 0 <= k < n_bins:\n        counts[k] += 1\n    else:\n        outside += 1\nfor k in range(n_bins):\n    lo = start + k * width\n    print(f"{lo:.1f} - {lo + width:.1f} | " + "*" * counts[k])\n',
   tests='''
def ref(v, s, w, n):
    c = [0] * n; o = 0
    for x in v:
        k = int((x - s) // w)
        if 0 <= k < n: c[k] += 1
        else: o += 1
    return c, o
for v, s, w, n in [([21.3, 23.8, 22.1, 25.6, 20.4, 23.1, 24.9, 22.7, 29.9, 18.2], 20.0, 2.0, 3), ([1.0, 1.5, 2.0, 2.5, 3.9, 4.0], 1.0, 1.0, 3), ([5.0], 0.0, 10.0, 1)]:
    ns, out = run(sub={"values": v, "start": s, "width": w, "n_bins": n})
    c, o = need(ns, "counts", "outside")
    ec, eo = ref(v, s, w, n)
    check(c == ec, f"counts = {ec}", f"counts = {ec}")
    check(o == eo, f"outside = {eo}", f"outside = {eo}")
    lines = [l for l in out.split("\\n") if "|" in l]
    check(len(lines) == n and all(l.count("*") == ec[i] for i, l in enumerate(lines)), "Pro Klasse eine Zeile mit der richtigen Anzahl Sterne", "One line per class with the right number of stars")
    check(len(lines) == n and all(has_num(l, s + i * w) and has_num(l, s + (i + 1) * w) for i, l in enumerate(lines)), f"Jede Zeile nennt die Klassengrenzen, z.B. {s:.1f} - {s + w:.1f}", f"Every line shows the class limits, e.g. {s:.1f} - {s + w:.1f}")
''',
   require=["for", "if"], refs=["6.2b", "6.1a"])
