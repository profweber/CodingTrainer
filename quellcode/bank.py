# Aufgabenbank des CodingTrainers. Jede Aufgabe verwendet nur Konstrukte bis zu ihrem Kapitel.
# Felder: id, ch, lvl (1-3), title{de,en}, task{de,en}, starter{de,en}, solution, tests, refs, require, forbid, stdin
from exlib import EX, ex


# =================================================================== Kapitel 4
ex(id="k4-ohm", ch="4", lvl=1,
   title={"de": "Ohmsches Gesetz", "en": "Ohm's law"},
   task={"de": "Die Spannung `U` (in V) und der Widerstand `R` (in Ω) sind vorgegeben. Berechnen Sie den Strom `I = U / R` und speichern Sie ihn in der Variable `I`. Geben Sie ihn anschließend mit zwei Nachkommastellen aus, z.B. `I = 4.89 A`.",
         "en": "Voltage `U` (in V) and resistance `R` (in Ω) are given. Compute the current `I = U / R`, store it in the variable `I` and print it with two decimal places, e.g. `I = 4.89 A`."},
   starter={"de": "U = 230.0  # Spannung in V\nR = 47.0   # Widerstand in Ohm\n\n# Ihr Code:\n",
            "en": "U = 230.0  # voltage in V\nR = 47.0   # resistance in Ohm\n\n# your code:\n"},
   solution='U = 230.0\nR = 47.0\nI = U / R\nprint(f"I = {I:.2f} A")\n',
   tests='''
ns, out = run()
I = need(ns, "I")
check(approx(I, 230/47), "I wird korrekt aus U und R berechnet", "I is computed correctly from U and R")
check("4.89" in out, "Ausgabe enthält den Strom mit zwei Nachkommastellen (4.89)", "Output shows the current with two decimals (4.89)")
ns, out = run(sub={"U": 12.0, "R": 4.0})
check(approx(ns.get("I"), 3.0), "Mit U = 12 V und R = 4 Ω ergibt sich I = 3 A (keine festen Zahlen verwenden!)", "With U = 12 V and R = 4 Ω the result is I = 3 A (don't hard-code numbers!)")
check("3.00" in out, "Ausgabe für U = 12 V, R = 4 Ω lautet ‚3.00‘", "Output for U = 12 V, R = 4 Ω shows '3.00'")
''',
   refs=["4.2", "4.3"])

ex(id="k4-temp", ch="4", lvl=1,
   title={"de": "Temperatur umrechnen", "en": "Converting temperatures"},
   task={"de": "Gegeben ist eine Temperatur `celsius`. Berechnen Sie `fahrenheit` ($\\vartheta_\\mathrm{F} = \\vartheta_\\mathrm{C} \\cdot \\frac{9}{5} + 32$) und `kelvin` ($T = \\vartheta_\\mathrm{C} + 273.15$). Geben Sie beides in einer Zeile aus, z.B. `21.5 °C = 70.7 °F = 294.65 K` (Fahrenheit mit einer, Kelvin mit zwei Nachkommastellen).",
         "en": "A temperature `celsius` is given. Compute `fahrenheit` ($\\vartheta_\\mathrm{F} = \\vartheta_\\mathrm{C} \\cdot \\frac{9}{5} + 32$) and `kelvin` ($T = \\vartheta_\\mathrm{C} + 273.15$). Print both in one line, e.g. `21.5 °C = 70.7 °F = 294.65 K` (Fahrenheit with one, Kelvin with two decimals)."},
   starter={"de": "celsius = 21.5\n\n# Ihr Code:\n", "en": "celsius = 21.5\n\n# your code:\n"},
   solution='celsius = 21.5\nfahrenheit = celsius * 9 / 5 + 32\nkelvin = celsius + 273.15\nprint(f"{celsius} °C = {fahrenheit:.1f} °F = {kelvin:.2f} K")\n',
   tests='''
for c in [21.5, -40.0, 100.0]:
    ns, out = run(sub={"celsius": c})
    f, k = need(ns, "fahrenheit", "kelvin")
    check(approx(f, c * 9 / 5 + 32), f"fahrenheit stimmt für {c} °C", f"fahrenheit is correct for {c} °C")
    check(approx(k, c + 273.15), f"kelvin stimmt für {c} °C", f"kelvin is correct for {c} °C")
    check(f"{c*9/5+32:.1f}" in out and f"{c+273.15:.2f}" in out, f"Ausgabe für {c} °C ist korrekt formatiert", f"Output for {c} °C is formatted correctly")
''',
   refs=["4.2", "4.3"])

ex(id="k4-time", ch="4", lvl=2,
   title={"de": "Messdauer zerlegen", "en": "Splitting a measurement duration"},
   task={"de": "Ein Datenlogger hat `seconds` Sekunden lang gemessen. Zerlegen Sie die Dauer mit Ganzzahl-Division `//` und Modulo `%` in Stunden `h`, Minuten `m` und Sekunden `s` und geben Sie z.B. `2 h 3 min 4 s` aus.",
         "en": "A data logger measured for `seconds` seconds. Use integer division `//` and modulo `%` to split the duration into hours `h`, minutes `m` and seconds `s`, and print e.g. `2 h 3 min 4 s`."},
   starter={"de": "seconds = 7384\n\n# Ihr Code:\n", "en": "seconds = 7384\n\n# your code:\n"},
   solution='seconds = 7384\nh = seconds // 3600\nm = seconds % 3600 // 60\ns = seconds % 60\nprint(f"{h} h {m} min {s} s")\n',
   tests='''
for sec in [7384, 59, 3600, 86399]:
    ns, out = run(sub={"seconds": sec})
    h, m, s = need(ns, "h", "m", "s")
    eh, em, es = sec // 3600, sec % 3600 // 60, sec % 60
    check((h, m, s) == (eh, em, es), f"{sec} s = {eh} h {em} min {es} s", f"{sec} s = {eh} h {em} min {es} s")
    check(f"{eh} h {em} min {es} s" in out, f"Ausgabe für {sec} s lautet ‚{eh} h {em} min {es} s‘", f"Output for {sec} s is '{eh} h {em} min {es} s'")
''',
   refs=["4.2", "4.3"])

ex(id="k4-tol", ch="4", lvl=2,
   title={"de": "Toleranzprüfung", "en": "Tolerance check"},
   task={"de": "Eine Welle hat das Nennmaß `nominal` (mm) und die Toleranz `tol` (± mm). Speichern Sie in `in_tolerance` den Wahrheitswert, ob das Messmaß `measured` innerhalb der Toleranz liegt (Grenzen eingeschlossen). Nutzen Sie dafür eine Comparison Chain. Geben Sie `Maß in Toleranz: True` bzw. `False` aus.",
         "en": "A shaft has the nominal size `nominal` (mm) and tolerance `tol` (± mm). Store in `in_tolerance` whether the measured size `measured` lies within the tolerance (limits included). Use a comparison chain. Print `In tolerance: True` or `False`."},
   starter={"de": "nominal = 25.0   # mm\ntol = 0.05       # mm\nmeasured = 25.03 # mm\n\n# Ihr Code:\n",
            "en": "nominal = 25.0   # mm\ntol = 0.05       # mm\nmeasured = 25.03 # mm\n\n# your code:\n"},
   solution='nominal = 25.0\ntol = 0.05\nmeasured = 25.03\nin_tolerance = nominal - tol <= measured <= nominal + tol\nprint("Maß in Toleranz:", in_tolerance)\n',
   tests='''
cases = [(25.03, True), (24.96, True), (25.06, False), (24.90, False), (25.0, True)]
for m, exp in cases:
    ns, out = run(sub={"measured": m})
    v = need(ns, "in_tolerance")
    check(v is exp, f"Für {m} mm ist das Ergebnis {exp}", f"For {m} mm the result is {exp}")
    check(str(exp) in out, f"Ausgabe für {m} mm enthält {exp}", f"Output for {m} mm contains {exp}")
''',
   refs=["4.4"])

ex(id="k4-brake", ch="4", lvl=3,
   title={"de": "Anhalteweg", "en": "Stopping distance"},
   task={"de": "Faustformeln der Fahrschule ($v$ in km/h): Reaktionsweg = $(v/10) \\cdot 3$, Bremsweg = $(v/10)^2$. Berechnen Sie `reaction`, `braking` und `total` (Summe, in m). Speichern Sie in `safe`, ob `total` kleiner als der Abstand `distance` zum Hindernis ist. Ausgabe mit dem Anhalteweg auf eine Nachkommastelle, z.B.: `Anhalteweg: 40.0 m, sicher: True`.",
         "en": "Driving-school rules of thumb ($v$ in km/h): reaction distance = $(v/10) \\cdot 3$, braking distance = $(v/10)^2$. Compute `reaction`, `braking` and `total` (sum, in m). Store in `safe` whether `total` is less than `distance` to the obstacle. Output with the stopping distance to one decimal, e.g.: `Stopping distance: 40.0 m, safe: True`."},
   starter={"de": "v = 50          # km/h\ndistance = 45.0 # m\n\n# Ihr Code:\n", "en": "v = 50          # km/h\ndistance = 45.0 # m\n\n# your code:\n"},
   solution='v = 50\ndistance = 45.0\nreaction = (v / 10) * 3\nbraking = (v / 10) ** 2\ntotal = reaction + braking\nsafe = total < distance\nprint(f"Anhalteweg: {total:.1f} m, sicher: {safe}")\n',
   tests='''
for v, d in [(50, 45.0), (100, 120.0), (30, 20.0)]:
    ns, out = run(sub={"v": v, "distance": d})
    r, b, t, s = need(ns, "reaction", "braking", "total", "safe")
    er, eb = v / 10 * 3, (v / 10) ** 2
    check(approx(r, er) and approx(b, eb), f"Reaktions- und Bremsweg stimmen für v = {v}", f"Reaction and braking distance correct for v = {v}")
    check(approx(t, er + eb), f"Anhalteweg für v = {v} km/h ist {er+eb:.1f} m", f"Stopping distance for v = {v} km/h is {er+eb:.1f} m")
    check(s is (er + eb < d), f"safe ist korrekt für Abstand {d} m", f"safe is correct for distance {d} m")
    check(f"{er+eb:.1f}" in out, f"Ausgabe zeigt {er+eb:.1f} m", f"Output shows {er+eb:.1f} m")
''',
   refs=["4.2", "4.4"])

ex(id="k4-pq", ch="4", lvl=3,
   title={"de": "p-q-Formel", "en": "Quadratic formula"},
   task={"de": "Lösen Sie $x^2 + p x + q = 0$ mit der p-q-Formel $x_{1,2} = -\\frac{p}{2} \\pm \\sqrt{\\frac{p^2}{4} - q}$. Die Wurzel berechnen Sie mit `** 0.5`. Speichern Sie die Lösungen in `x1` (mit +) und `x2` (mit −) und geben Sie beide auf drei Nachkommastellen aus. Achten Sie auf die Klammern! Sie dürfen voraussetzen, dass es zwei reelle Lösungen gibt.",
         "en": "Solve $x^2 + p x + q = 0$ with the p-q formula $x_{1,2} = -\\frac{p}{2} \\pm \\sqrt{\\frac{p^2}{4} - q}$. Compute the root with `** 0.5`. Store the solutions in `x1` (with +) and `x2` (with −) and print both with three decimals. Mind the parentheses! You may assume that two real solutions exist."},
   starter={"de": "p = -3.0\nq = 2.0\n\n# Ihr Code:\n", "en": "p = -3.0\nq = 2.0\n\n# your code:\n"},
   solution='p = -3.0\nq = 2.0\nroot = (p**2 / 4 - q) ** 0.5\nx1 = -p / 2 + root\nx2 = -p / 2 - root\nprint(f"x1 = {x1:.3f}, x2 = {x2:.3f}")\n',
   tests='''
for p, q in [(-3.0, 2.0), (2.0, -8.0), (1.5, -1.0)]:
    ns, out = run(sub={"p": p, "q": q})
    x1, x2 = need(ns, "x1", "x2")
    r = (p * p / 4 - q) ** 0.5
    check(approx(x1, -p / 2 + r) and approx(x2, -p / 2 - r), f"Lösungen für p = {p}, q = {q} stimmen", f"Solutions for p = {p}, q = {q} are correct")
    check(f"{-p/2+r:.3f}" in out and f"{-p/2-r:.3f}" in out, f"Ausgabe mit drei Nachkommastellen für p = {p}, q = {q}", f"Output with three decimals for p = {p}, q = {q}")
''',
   refs=["4.2", "4.3"])

# =================================================================== Kapitel 5
ex(id="k5-profile", ch="5", lvl=1,
   title={"de": "Profilstahl bestellen", "en": "Ordering steel sections"},
   task={"de": "Ein Händler verkauft Stahlprofile nach Gewicht. Lesen Sie mit `input()` die benötigte Länge in m und die Masse pro Meter in kg/m ein (Punkt als Dezimalzeichen) und wandeln Sie beide in `float` um. Berechnen Sie die Masse `mass_kg` und den Preis `price` beim Kilopreis `price_per_kg`. Ausgabe: `Masse: 73.20 kg, Preis: 135.42 €` (zwei Nachkommastellen).\n\nTipp: Eingaben für „Ausführen“ tragen Sie im Feld *Eingaben für input()* ein, eine pro Zeile.",
         "en": "A dealer sells steel sections by weight. Use `input()` to read the required length in m and the mass per metre in kg/m (dot as decimal separator) and convert both to `float`. Compute the mass `mass_kg` and the price `price` at the price per kilogram `price_per_kg`. Output: `Mass: 73.20 kg, price: 135.42 €` (two decimals).\n\nTip: inputs for “Run” go into the field *Input for input()*, one per line."},
   starter={"de": "price_per_kg = 1.85  # € pro kg\n\n# Länge und Masse pro Meter einlesen\n", "en": "price_per_kg = 1.85  # € per kg\n\n# read length and mass per metre\n"},
   solution='price_per_kg = 1.85\nlength = float(input("Länge in m: "))\nmass_per_m = float(input("Masse pro Meter in kg/m: "))\nmass_kg = length * mass_per_m\nprice = mass_kg * price_per_kg\nprint(f"Masse: {mass_kg:.2f} kg, Preis: {price:.2f} €")\n',
   tests='''
for l, mpm in [("6", "12.2"), ("2.5", "4.04"), ("12", "0.89")]:
    ns, out = run(inputs=[l, mpm])
    m, p = need(ns, "mass_kg", "price")
    em = float(l) * float(mpm); ep = em * 1.85
    check(approx(m, em), f"{l} m × {mpm} kg/m = {em:.2f} kg", f"{l} m × {mpm} kg/m = {em:.2f} kg")
    check(approx(p, ep), f"Preis = {ep:.2f} €", f"price = {ep:.2f} €")
    check(f"{em:.2f}" in out and f"{ep:.2f}" in out, "Ausgabe mit zwei Nachkommastellen", "Output with two decimals")
''',
   stdin="6\n12.2\n", require=["cast"], refs=["4.3e", "5.2e"])

ex(id="k5-list", ch="5", lvl=1,
   title={"de": "Bauteilliste bearbeiten", "en": "Editing a parts list"},
   task={"de": "Bearbeiten Sie die Liste `parts` mit Listen-Methoden, und zwar in dieser Reihenfolge:\n1. Hängen Sie `'Mutter M8'` an.\n2. Entfernen Sie `'Unterlegscheibe'`.\n3. Fügen Sie `'Schraube M8'` ganz vorne ein.\n4. Sortieren Sie die Liste.\n5. Speichern Sie die Anzahl der Einträge in `n` und geben Sie Liste und Anzahl aus.",
         "en": "Edit the list `parts` with list methods, in this order:\n1. Append `'Mutter M8'`.\n2. Remove `'Unterlegscheibe'`.\n3. Insert `'Schraube M8'` at the very front.\n4. Sort the list.\n5. Store the number of entries in `n` and print list and count."},
   starter={"de": "parts = ['Lager 6204', 'Unterlegscheibe', 'Dichtring', 'Passfeder']\n\n# Ihr Code:\n",
            "en": "parts = ['Lager 6204', 'Unterlegscheibe', 'Dichtring', 'Passfeder']\n\n# your code:\n"},
   solution="parts = ['Lager 6204', 'Unterlegscheibe', 'Dichtring', 'Passfeder']\nparts.append('Mutter M8')\nparts.remove('Unterlegscheibe')\nparts.insert(0, 'Schraube M8')\nparts.sort()\nn = len(parts)\nprint(parts, n)\n",
   tests='''
ns, out = run()
p, n = need(ns, "parts", "n")
check("Mutter M8" in p, "'Mutter M8' ist in der Liste", "'Mutter M8' is in the list")
check("Unterlegscheibe" not in p, "'Unterlegscheibe' wurde entfernt", "'Unterlegscheibe' was removed")
check("Schraube M8" in p, "'Schraube M8' ist in der Liste", "'Schraube M8' is in the list")
check(p == sorted(['Lager 6204', 'Dichtring', 'Passfeder', 'Mutter M8', 'Schraube M8']), "Die Liste ist sortiert", "The list is sorted")
check(n == 5, "n = 5", "n = 5")
ns2, _ = run(sub={"parts": ['Unterlegscheibe', 'Zahnrad']})
check(ns2.get("n") == 3, "Funktioniert auch mit einer anderen Ausgangsliste (n berechnet, nicht fest)", "Works with another starting list too (n is computed, not fixed)")
''',
   require=["list_methods"], refs=["5.3", "5.3m"])

ex(id="k5-comma", ch="5", lvl=2,
   title={"de": "Eingabe mit Dezimalkomma", "en": "Input with decimal comma"},
   task={"de": "Lesen Sie einen Messwert ein, den Nutzer oft mit deutschem Komma eingeben (z.B. `12,7`). Ersetzen Sie das Komma durch einen Punkt und wandeln Sie in `float` um (`value`). Speichern Sie außerdem `truncated = int(value)` und `rounded = round(value)` und geben Sie alle drei Werte aus. Was ist der Unterschied?",
         "en": "Read a measurement that users often type with a German decimal comma (e.g. `12,7`). Replace the comma by a dot and convert to `float` (`value`). Also store `truncated = int(value)` and `rounded = round(value)` and print all three values. What's the difference?"},
   starter={"de": "# Messwert einlesen\n", "en": "# read the measurement\n"},
   solution='text = input("Messwert: ")\nvalue = float(text.replace(",", "."))\ntruncated = int(value)\nrounded = round(value)\nprint(value, truncated, rounded)\n',
   tests='''
for t in ["12,7", "3.2", "-2,6", "8"]:
    ns, out = run(inputs=[t])
    v, tr, ro = need(ns, "value", "truncated", "rounded")
    e = float(t.replace(",", "."))
    check(approx(v, e), f"Eingabe ‚{t}‘ ergibt value = {e}", f"Input '{t}' gives value = {e}")
    check(tr == int(e) and ro == round(e), f"truncated = {int(e)}, rounded = {round(e)} für ‚{t}‘", f"truncated = {int(e)}, rounded = {round(e)} for '{t}'")
''',
   stdin="12,7\n", require=["replace"], refs=["5.2e", "4.3e"])

ex(id="k5-numsys", ch="5", lvl=2,
   title={"de": "Zahlensysteme", "en": "Number systems"},
   task={"de": "Lesen Sie eine ganze Zahl `n` ein. Speichern Sie ihre Binärdarstellung in `b` und ihre Hexadezimaldarstellung in `h` (jeweils als String, z.B. `'0b101010'`). Wandeln Sie `b` anschließend mit `int(..., 2)` zurück in `back`. Geben Sie alles aus.",
         "en": "Read an integer `n`. Store its binary representation in `b` and its hexadecimal one in `h` (as strings, e.g. `'0b101010'`). Then convert `b` back with `int(..., 2)` into `back`. Print everything."},
   starter={"de": "# Zahl einlesen\n", "en": "# read the number\n"},
   solution='n = int(input("Zahl: "))\nb = bin(n)\nh = hex(n)\nback = int(b, 2)\nprint(n, b, h, back)\n',
   tests='''
for t in ["42", "255", "1000"]:
    ns, out = run(inputs=[t])
    n, b, h, back = need(ns, "n", "b", "h", "back")
    e = int(t)
    check(n == e and isinstance(n, int), f"n ist die ganze Zahl {e}", f"n is the integer {e}")
    check(b == bin(e) and h == hex(e), f"b = {bin(e)}, h = {hex(e)}", f"b = {bin(e)}, h = {hex(e)}")
    check(back == e, f"back = {e}", f"back = {e}")
''',
   stdin="42\n", require=["numsys"], refs=["5.5", "5.5i"])

ex(id="k5-ref", ch="5", lvl=2,
   title={"de": "Seiteneffekte vermeiden", "en": "Avoiding side effects"},
   task={"de": "Bevor die Messreihe `values` sortiert und ihr größter Wert entfernt wird, soll eine **unabhängige** Sicherung `backup` angelegt werden. `backup = values` reicht nicht – warum? Erzeugen Sie die Sicherung mit `list(...)`. Sortieren Sie danach `values`, entfernen Sie mit `pop()` den größten Wert und geben Sie beide Listen aus.",
         "en": "Before the measurement series `values` is sorted and its largest value removed, create an **independent** backup `backup`. `backup = values` is not enough – why? Create the backup with `list(...)`. Then sort `values`, remove the largest value with `pop()` and print both lists."},
   starter={"de": "values = [3.2, 1.5, 9.9, 2.8, 4.1]\n\n# Ihr Code:\n", "en": "values = [3.2, 1.5, 9.9, 2.8, 4.1]\n\n# your code:\n"},
   solution='values = [3.2, 1.5, 9.9, 2.8, 4.1]\nbackup = list(values)\nvalues.sort()\nvalues.pop()\nprint(values, backup)\n',
   tests='''
ns, out = run()
v, b = need(ns, "values", "backup")
check(b == [3.2, 1.5, 9.9, 2.8, 4.1], "backup enthält die Originalreihenfolge", "backup holds the original order")
check(b is not v, "backup ist eine eigene Instanz (kein Seiteneffekt)", "backup is a separate instance (no side effect)")
check(v == [1.5, 2.8, 3.2, 4.1], "values ist sortiert und ohne den größten Wert", "values is sorted and without its largest value")
ns, out = run(sub={"values": [5.0, 7.0, 1.0]})
check(ns.get("values") == [1.0, 5.0] and ns.get("backup") == [5.0, 7.0, 1.0], "Funktioniert auch mit anderen Messwerten", "Works with other measurements too")
''',
   refs=["5.4s", "5.4m", "5.3m"])

ex(id="k5-chars", ch="5", lvl=3,
   title={"de": "Caesar-Code für ein Zeichen", "en": "Caesar code for one character"},
   task={"de": "Lesen Sie einen Großbuchstaben `c` (A–Z) und eine Verschiebung `k` ein. Berechnen Sie mit `ord()` und `chr()` den um `k` Stellen verschobenen Buchstaben `shifted`; nach Z geht es wieder bei A los (Tipp: Modulo 26 auf die Position im Alphabet). Geben Sie `shifted` aus.",
         "en": "Read an upper-case letter `c` (A–Z) and a shift `k`. Use `ord()` and `chr()` to compute the letter `shifted`, moved by `k` positions; after Z it wraps around to A (tip: modulo 26 on the position in the alphabet). Print `shifted`."},
   starter={"de": "# Buchstabe und Verschiebung einlesen\n", "en": "# read letter and shift\n"},
   solution='c = input("Buchstabe: ")\nk = int(input("Verschiebung: "))\nshifted = chr((ord(c) - ord("A") + k) % 26 + ord("A"))\nprint(shifted)\n',
   tests='''
for c, k in [("A", 3), ("X", 5), ("M", 13), ("B", 27)]:
    ns, out = run(inputs=[c, str(k)])
    s = need(ns, "shifted")
    e = chr((ord(c) - 65 + k) % 26 + 65)
    check(s == e, f"{c} um {k} verschoben ergibt {e}", f"{c} shifted by {k} gives {e}")
''',
   stdin="X\n5\n", require=["numsys"], refs=["5.5s", "4.2"])

# =================================================================== Kapitel 6
ex(id="k6-breaker", ch="6", lvl=1,
   title={"de": "Leitungsschutzschalter", "en": "Circuit breaker"},
   task={"de": "Ein Leitungsschutzschalter mit dem Nennstrom `I_n` reagiert (vereinfacht) je nach Verhältnis $r = I / I_n$ unterschiedlich. Lesen Sie den Strom `I` in A ein und speichern Sie die Stufe als Zahl in `stage`:\n- $r \\le 1$: Stufe 0, Meldung `normal`\n- $1 < r \\le 1.45$: Stufe 1, `Überlast – Auslösung nach Minuten`\n- $1.45 < r \\le 5$: Stufe 2, `Überlast – Auslösung nach Sekunden`\n- $r > 5$: Stufe 3, `Kurzschluss – sofortige Auslösung`\n\nGeben Sie die passende Meldung aus.",
         "en": "A circuit breaker with rated current `I_n` reacts (simplified) depending on the ratio $r = I / I_n$. Read the current `I` in A and store the stage as a number in `stage`:\n- $r \\le 1$: stage 0, message `normal`\n- $1 < r \\le 1.45$: stage 1, `Overload – trips after minutes`\n- $1.45 < r \\le 5$: stage 2, `Overload – trips after seconds`\n- $r > 5$: stage 3, `Short circuit – trips instantly`\n\nPrint the matching message."},
   starter={"de": "I_n = 16.0  # A\nI = float(input(\"Strom in A: \"))\n\n# Ihr Code:\n", "en": "I_n = 16.0  # A\nI = float(input(\"Current in A: \"))\n\n# your code:\n"},
   solution='I_n = 16.0\nI = float(input("Strom in A: "))\nr = I / I_n\nif r <= 1:\n    stage = 0\n    print("normal")\nelif r <= 1.45:\n    stage = 1\n    print("Überlast – Auslösung nach Minuten")\nelif r <= 5:\n    stage = 2\n    print("Überlast – Auslösung nach Sekunden")\nelse:\n    stage = 3\n    print("Kurzschluss – sofortige Auslösung")\n',
   tests='''
def exp(r):
    return 0 if r <= 1 else 1 if r <= 1.45 else 2 if r <= 5 else 3
for I in [10.0, 16.0, 16.5, 23.2, 23.5, 80.0, 81.0, 300.0]:
    ns, out = run(inputs=[str(I)])
    check(need(ns, "stage") == exp(I / 16), f"I = {I} A bei I_n = 16 A: Stufe {exp(I / 16)}", f"I = {I} A with I_n = 16 A: stage {exp(I / 16)}")
ns, out = run(inputs=["30"], sub={"I_n": 10.0})
check(ns.get("stage") == 2, "Mit I_n = 10 A und I = 30 A: Stufe 2 (I_n wird verwendet, nicht 16 fest eingetippt)", "With I_n = 10 A and I = 30 A: stage 2 (I_n is used, not a hard-coded 16)")
o = out.lower()
check("sekund" in o or "second" in o, "Für Stufe 2 wird die passende Meldung ausgegeben", "The matching message is printed for stage 2")
''',
   stdin="20\n", require=["if"], refs=["6.1b"])

ex(id="k6-rms", ch="6", lvl=1,
   title={"de": "Effektivwert einer Wechselspannung", "en": "RMS value of an AC voltage"},
   task={"de": "Für Wechselspannungen ist der Effektivwert wichtig: $U_\\mathrm{eff} = \\sqrt{\\dfrac{u_1^2 + u_2^2 + \\dots + u_n^2}{n}}$. Berechnen Sie mit einer `for`-Schleife die Summe der Quadrate `sum_sq` der Abtastwerte `samples` und daraus `u_rms` (Wurzel mit `** 0.5`). Verwenden Sie **nicht** `sum()` – die Schleife ist hier das Ziel. Geben Sie `u_rms` mit einer Nachkommastelle aus.\n\nZur Kontrolle: Bei einer Sinusspannung ist $U_\\mathrm{eff} \\approx \\hat{U} / \\sqrt{2}$, für $\\hat{U} = 325\\,\\mathrm{V}$ also etwa 230 V.",
         "en": "For AC voltages, the RMS value matters: $U_\\mathrm{rms} = \\sqrt{\\dfrac{u_1^2 + u_2^2 + \\dots + u_n^2}{n}}$. Use a `for` loop to compute the sum of squares `sum_sq` of the samples `samples`, and from it `u_rms` (root with `** 0.5`). Do **not** use `sum()` – the loop is the point here. Print `u_rms` with one decimal.\n\nCheck: for a sine voltage, $U_\\mathrm{rms} \\approx \\hat{U} / \\sqrt{2}$, i.e. about 230 V for $\\hat{U} = 325\\,\\mathrm{V}$."},
   starter={"de": "samples = [0.0, 229.8, 325.0, 229.8, 0.0, -229.8, -325.0, -229.8]  # V\nsum_sq = 0\n\n# Ihr Code:\n", "en": "samples = [0.0, 229.8, 325.0, 229.8, 0.0, -229.8, -325.0, -229.8]  # V\nsum_sq = 0\n\n# your code:\n"},
   solution='samples = [0.0, 229.8, 325.0, 229.8, 0.0, -229.8, -325.0, -229.8]\nsum_sq = 0\nfor u in samples:\n    sum_sq += u**2\nu_rms = (sum_sq / len(samples)) ** 0.5\nprint(f"U_eff = {u_rms:.1f} V")\n',
   tests='''
for s in [[0.0, 229.8, 325.0, 229.8, 0.0, -229.8, -325.0, -229.8], [12.0, -12.0], [3.0, 4.0, 0.0, 5.0]]:
    ns, out = run(sub={"samples": s})
    sq, r = need(ns, "sum_sq", "u_rms")
    esq = sum(x * x for x in s); er = (esq / len(s)) ** 0.5
    check(approx(sq, esq), f"Summe der Quadrate = {esq:g}", f"sum of squares = {esq:g}")
    check(approx(r, er), f"U_eff ≈ {er:.2f} V", f"U_rms ≈ {er:.2f} V")
    check(f"{er:.1f}" in out, f"Ausgabe zeigt {er:.1f}", f"Output shows {er:.1f}")
''',
   require=["for"], forbid=["seqfuncs"], refs=["6.2b"])

ex(id="k6-leap", ch="6", lvl=2,
   title={"de": "Schaltjahr", "en": "Leap year"},
   task={"de": "Ein Jahr ist ein Schaltjahr, wenn es durch 4 teilbar ist, aber nicht durch 100 – es sei denn, es ist durch 400 teilbar. Lesen Sie ein Jahr ein, speichern Sie das Ergebnis als Wahrheitswert in `leap` und geben Sie `2024 ist ein Schaltjahr.` bzw. `2023 ist kein Schaltjahr.` aus.",
         "en": "A year is a leap year if it is divisible by 4 but not by 100 – unless it is divisible by 400. Read a year, store the result as a boolean in `leap` and print `2024 is a leap year.` or `2023 is not a leap year.`"},
   starter={"de": "year = int(input(\"Jahr: \"))\n\n# Ihr Code:\n", "en": "year = int(input(\"Year: \"))\n\n# your code:\n"},
   solution='year = int(input("Jahr: "))\nleap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)\nif leap:\n    print(year, "ist ein Schaltjahr.")\nelse:\n    print(year, "ist kein Schaltjahr.")\n',
   tests='''
for y in [2024, 2023, 1900, 2000, 2100, 1996]:
    ns, out = run(inputs=[str(y)])
    e = y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
    check(need(ns, "leap") == e, f"{y}: leap = {e}", f"{y}: leap = {e}")
    neg = ("kein" in out.lower()) or (" not " in out.lower())
    check(neg != e, f"{y}: Ausgabe passt zum Ergebnis", f"{y}: output matches the result")
''',
   stdin="2024\n", refs=["6.1c", "6.1a"])

ex(id="k6-cool", ch="6", lvl=2,
   title={"de": "Abkühlung simulieren", "en": "Simulating cooling"},
   task={"de": "Ein Bauteil hat die Temperatur `T = 90.0` °C, die Umgebung `T_env = 20.0` °C. Pro Minute sinkt die Temperatur um 10 % der Differenz zur Umgebung: `T -= 0.1 * (T - T_env)`. Zählen Sie mit einer `while`-Schleife die Minuten `minutes`, bis `T` unter `limit` fällt, und geben Sie Minuten und Endtemperatur aus.",
         "en": "A part has temperature `T = 90.0` °C, the environment `T_env = 20.0` °C. Each minute the temperature drops by 10 % of the difference to the environment: `T -= 0.1 * (T - T_env)`. Use a `while` loop to count the `minutes` until `T` falls below `limit`, and print minutes and final temperature."},
   starter={"de": "T = 90.0\nT_env = 20.0\nlimit = 40.0\n\n# Ihr Code:\n", "en": "T = 90.0\nT_env = 20.0\nlimit = 40.0\n\n# your code:\n"},
   solution='T = 90.0\nT_env = 20.0\nlimit = 40.0\nminutes = 0\nwhile T >= limit:\n    T -= 0.1 * (T - T_env)\n    minutes += 1\nprint(minutes, round(T, 2))\n',
   tests='''
def ref(T, env, lim):
    m = 0
    while T >= lim:
        T -= 0.1 * (T - env)
        m += 1
    return m, T
for T0, lim in [(90.0, 40.0), (90.0, 25.0), (35.0, 40.0), (40.0, 40.0)]:
    ns, out = run(sub={"T": T0, "limit": lim})
    em, eT = ref(T0, 20.0, lim)
    check(need(ns, "minutes") == em, f"Start {T0} °C, Grenze {lim} °C: {em} Minuten", f"Start {T0} °C, limit {lim} °C: {em} minutes")
    check(approx(ns["T"], eT), f"Endtemperatur ≈ {eT:.2f} °C", f"Final temperature ≈ {eT:.2f} °C")
''',
   require=["while"], refs=["6.2a"])

ex(id="k6-newton", ch="6", lvl=3,
   title={"de": "Wurzel mit dem Newton-Verfahren", "en": "Square root via Newton's method"},
   task={"de": "Berechnen Sie $\\sqrt{a}$ mit dem Newton-Verfahren: Start `x = a`, Iteration `x = (x + a / x) / 2`. Brechen Sie ab, sobald `abs(x*x - a) < 1e-10`, spätestens aber nach 100 Iterationen. Speichern Sie das Ergebnis in `x`, die Anzahl der benötigten Iterationen in `iterations`, und geben Sie beides aus. `** 0.5` ist hier nicht erlaubt.",
         "en": "Compute $\\sqrt{a}$ with Newton's method: start `x = a`, iteration `x = (x + a / x) / 2`. Stop as soon as `abs(x*x - a) < 1e-10`, but after 100 iterations at the latest. Store the result in `x`, the number of iterations used in `iterations`, and print both. `** 0.5` is not allowed here."},
   starter={"de": "a = float(input(\"a = \"))\n\n# Ihr Code:\n", "en": "a = float(input(\"a = \"))\n\n# your code:\n"},
   solution='a = float(input("a = "))\nx = a\niterations = 0\nfor i in range(100):\n    if abs(x * x - a) < 1e-10:\n        break\n    x = (x + a / x) / 2\n    iterations += 1\nprint(x, iterations)\n',
   tests='''
import math as _m
for a in [2.0, 10.0, 1e6, 0.25]:
    ns, out = run(inputs=[str(a)])
    x, it = need(ns, "x", "iterations")
    check(approx(x, _m.sqrt(a), 1e-9), f"√{a} ≈ {_m.sqrt(a):.6f}", f"√{a} ≈ {_m.sqrt(a):.6f}")
    ex_, eit = a, 0
    while abs(ex_ * ex_ - a) >= 1e-10 and eit < 100:
        ex_ = (ex_ + a / ex_) / 2; eit += 1
    check(it == eit, f"a = {a}: {eit} Iterationen bis |x·x − a| < 1e-10", f"a = {a}: {eit} iterations until |x·x − a| < 1e-10")
check("**0.5" not in SOURCE.replace(" ", "") and "sqrt" not in SOURCE, "Ohne ** 0.5 und ohne sqrt gelöst", "Solved without ** 0.5 and without sqrt")
''',
   stdin="2\n", refs=["6.3a", "6.2c"])

ex(id="k6-diagdom", ch="6", lvl=3,
   title={"de": "Diagonaldominanz prüfen", "en": "Checking diagonal dominance"},
   task={"de": "Iterative Gleichungslöser (z.B. das Jacobi-Verfahren) konvergieren sicher, wenn die Matrix **streng diagonaldominant** ist: In jeder Zeile ist der Betrag des Diagonalelements größer als die Summe der Beträge aller anderen Elemente dieser Zeile. Bestimmen Sie für die quadratische Matrix `M` (verschachtelte Liste)\n- `trace`: die Spur (Summe der Diagonalelemente)\n- `row_ok`: eine Liste mit einem Wahrheitswert pro Zeile (in der Reihenfolge der Zeilen), ob die Bedingung dort erfüllt ist\n- `dominant`: ob die Bedingung in allen Zeilen erfüllt ist\n\nVerwenden Sie verschachtelte Schleifen und `abs()`; `sum()` kommt erst in Kapitel 7.",
         "en": "Iterative equation solvers (e.g. the Jacobi method) are guaranteed to converge if the matrix is **strictly diagonally dominant**: in every row, the magnitude of the diagonal element is greater than the sum of the magnitudes of all other elements in that row. For the square matrix `M` (nested list) determine\n- `trace`: the trace (sum of the diagonal elements)\n- `row_ok`: a list with one boolean per row (in the order of the rows), whether the condition holds there\n- `dominant`: whether the condition holds in every row\n\nUse nested loops and `abs()`; `sum()` only comes in chapter 7."},
   starter={"de": "M = [[10.0, -1.0, 2.0],\n     [-1.0, 11.0, -1.0],\n     [2.0, -1.0, 10.0]]\n\n# Ihr Code:\n", "en": "M = [[10.0, -1.0, 2.0],\n     [-1.0, 11.0, -1.0],\n     [2.0, -1.0, 10.0]]\n\n# your code:\n"},
   solution='M = [[10.0, -1.0, 2.0],\n     [-1.0, 11.0, -1.0],\n     [2.0, -1.0, 10.0]]\nn = len(M)\ntrace = 0\nrow_ok = []\nfor i in range(n):\n    trace += M[i][i]\n    others = 0\n    for j in range(n):\n        if j != i:\n            others += abs(M[i][j])\n    row_ok.append(abs(M[i][i]) > others)\ndominant = True\nfor ok in row_ok:\n    if not ok:\n        dominant = False\nprint(trace, row_ok, dominant)\n',
   tests='''
def ref(M):
    n = len(M)
    rows = [abs(M[i][i]) > sum(abs(M[i][j]) for j in range(n) if j != i) for i in range(n)]
    return sum(M[i][i] for i in range(n)), rows, all(rows)
for M in [[[10.0, -1.0, 2.0], [-1.0, 11.0, -1.0], [2.0, -1.0, 10.0]], [[1.0, 2.0], [3.0, 4.0]], [[4.0, -2.0, 1.0], [1.0, -5.0, 3.0], [0.5, 0.5, 2.0]], [[-7.0]], [[2.0, 1.0, -1.0], [0.0, 3.0, 0.0], [1.0, 1.0, 3.0]]]:
    ns, out = run(sub={"M": M})
    tr, ro, d = need(ns, "trace", "row_ok", "dominant")
    et, er, ed = ref(M)
    check(approx(tr, et), f"Spur von {M} = {et:g}", f"trace of {M} = {et:g}")
    check(ro == er and d is ed, f"row_ok = {er}, dominant = {ed}", f"row_ok = {er}, dominant = {ed}")
''',
   require=["for", "abs"], forbid=["seqfuncs"], refs=["6.2d", "6.3b"])

ex(id="k6-primes", ch="6", lvl=3,
   title={"de": "Primzahlen", "en": "Prime numbers"},
   task={"de": "Lesen Sie eine Zahl `n` ein und sammeln Sie alle Primzahlen von 2 bis einschließlich `n` in der Liste `primes`. Prüfen Sie für jede Zahl mit einer inneren Schleife, ob sie einen Teiler hat; verlassen Sie die innere Schleife mit `break`, sobald ein Teiler gefunden ist.",
         "en": "Read a number `n` and collect all primes from 2 up to and including `n` in the list `primes`. For each number, use an inner loop to check for a divisor; leave the inner loop with `break` as soon as a divisor is found."},
   starter={"de": "n = int(input(\"n = \"))\nprimes = []\n\n# Ihr Code:\n", "en": "n = int(input(\"n = \"))\nprimes = []\n\n# your code:\n"},
   solution='n = int(input("n = "))\nprimes = []\nfor k in range(2, n + 1):\n    is_prime = True\n    for d in range(2, k):\n        if k % d == 0:\n            is_prime = False\n            break\n    if is_prime:\n        primes.append(k)\nprint(primes)\n',
   tests='''
def ref(n):
    return [k for k in range(2, n + 1) if all(k % d for d in range(2, k))]
for n in [10, 2, 1, 50]:
    ns, out = run(inputs=[str(n)])
    check(need(ns, "primes") == ref(n), f"Primzahlen bis {n}: {ref(n)}", f"Primes up to {n}: {ref(n)}")
''',
   stdin="30\n", require=["for", "break"], refs=["6.2d", "6.2c"])

# =================================================================== Kapitel 7
ex(id="k7-bmi", ch="7", lvl=1,
   title={"de": "Leistung und Energie", "en": "Power and energy"},
   task={"de": "Schreiben Sie eine Funktion `power(u, i)`, die die elektrische Leistung $P = U \\cdot I$ **zurückgibt** (nicht ausgibt!), und eine Funktion `energy_kwh(p, hours)`, die aus Leistung in W und Dauer in h die Energie in kWh zurückgibt. Testen Sie beide mit `print`.",
         "en": "Write a function `power(u, i)` that **returns** (not prints!) the electric power $P = U \\cdot I$, and a function `energy_kwh(p, hours)` that returns the energy in kWh from power in W and duration in h. Test both with `print`."},
   starter={"de": "def power(u, i):\n    # Ihr Code\n    ...\n\n", "en": "def power(u, i):\n    # your code\n    ...\n\n"},
   solution='def power(u, i):\n    return u * i\n\ndef energy_kwh(p, hours):\n    return p * hours / 1000\n\nprint(power(230, 2.5))\nprint(energy_kwh(power(230, 2.5), 3))\n',
   tests='''
ns, out = run()
for u, i in [(230, 2.5), (12, 0.5), (0, 3)]:
    r = call(ns, "power", u, i)
    check(r is not None and approx(r, u * i), f"power({u}, {i}) gibt {u*i} zurück", f"power({u}, {i}) returns {u*i}")
for p, h in [(1000, 1), (575.0, 3), (60, 24)]:
    r = call(ns, "energy_kwh", p, h)
    check(r is not None and approx(r, p * h / 1000), f"energy_kwh({p}, {h}) gibt {p*h/1000} zurück", f"energy_kwh({p}, {h}) returns {p*h/1000}")
''',
   require=["def", "return"], refs=["7.3", "7.3r"])

ex(id="k7-junction", ch="7", lvl=2,
   title={"de": "Sperrschichttemperatur", "en": "Junction temperature"},
   task={"de": "Ein Leistungshalbleiter erzeugt die Verlustleistung `p_loss` (W). Mit dem Wärmewiderstand `r_th` (K/W) gilt für die Sperrschichttemperatur $T_j = t_\\mathrm{amb} + p_\\mathrm{loss} \\cdot r_\\mathrm{th}$. Schreiben Sie `junction_temp(p_loss, r_th, t_amb=25.0, t_max=150.0)`, die **zwei Werte** zurückgibt: $T_j$ und die verbleibende Reserve $t_\\mathrm{max} - T_j$ (negativ, wenn die Grenze überschritten ist).\n\nRufen Sie die Funktion einmal mit den Standardwerten und einmal für einen warmen Schaltschrank mit `t_amb=45.0` als Keyword-Argument auf.",
         "en": "A power semiconductor produces the power loss `p_loss` (W). With the thermal resistance `r_th` (K/W), the junction temperature is $T_j = t_\\mathrm{amb} + p_\\mathrm{loss} \\cdot r_\\mathrm{th}$. Write `junction_temp(p_loss, r_th, t_amb=25.0, t_max=150.0)` that returns **two values**: $T_j$ and the remaining margin $t_\\mathrm{max} - T_j$ (negative if the limit is exceeded).\n\nCall the function once with the default values and once for a warm control cabinet with `t_amb=45.0` as a keyword argument."},
   starter={"de": "def junction_temp(p_loss, r_th, t_amb=25.0, t_max=150.0):\n    ...\n", "en": "def junction_temp(p_loss, r_th, t_amb=25.0, t_max=150.0):\n    ...\n"},
   solution='def junction_temp(p_loss, r_th, t_amb=25.0, t_max=150.0):\n    t_j = t_amb + p_loss * r_th\n    margin = t_max - t_j\n    return t_j, margin\n\nprint(junction_temp(40, 2.5))\nprint(junction_temp(40, 2.5, t_amb=45.0))\n',
   tests='''
ns, out = run()
for P, R in [(40, 2.5), (10, 1.2), (70, 2.0)]:
    r = call(ns, "junction_temp", P, R)
    ok = isinstance(r, tuple) and len(r) == 2
    check(ok and approx(r[0], 25 + P * R) and approx(r[1], 150 - 25 - P * R), f"junction_temp({P}, {R}) = ({25 + P*R:g}, {150 - 25 - P*R:g})", f"junction_temp({P}, {R}) = ({25 + P*R:g}, {150 - 25 - P*R:g})")
r = call(ns, "junction_temp", 40, 2.5, t_amb=45.0)
check(isinstance(r, tuple) and approx(r[0], 145.0) and approx(r[1], 5.0), "Mit t_amb=45.0: T_j = 145 °C, Reserve 5 K", "With t_amb=45.0: T_j = 145 °C, margin 5 K")
r = call(ns, "junction_temp", 40, 2.5, t_max=125.0)
check(isinstance(r, tuple) and approx(r[1], 0.0), "Mit t_max=125.0 ist die Reserve 0 K", "With t_max=125.0 the margin is 0 K")
''',
   require=["default_arg", "return"], refs=["7.3p", "7.3r", "7.3k"])

ex(id="k7-stats", ch="7", lvl=2,
   title={"de": "Beliebig viele Messwerte", "en": "Any number of measurements"},
   task={"de": "Schreiben Sie `stats(*values)`, die beliebig viele Messwerte entgegennimmt und das Tupel `(mittelwert, spannweite)` zurückgibt (Spannweite = Maximum − Minimum). Nutzen Sie `sum`, `max`, `min` und `len`. Werden gar keine Werte übergeben, soll `None` zurückgegeben werden.",
         "en": "Write `stats(*values)` that accepts any number of measurements and returns the tuple `(mean, range)` (range = maximum − minimum). Use `sum`, `max`, `min` and `len`. If no values are passed at all, return `None`."},
   starter={"de": "def stats(*values):\n    ...\n", "en": "def stats(*values):\n    ...\n"},
   solution='def stats(*values):\n    if len(values) == 0:\n        return None\n    mean = sum(values) / len(values)\n    span = max(values) - min(values)\n    return mean, span\n\nprint(stats(2.0, 4.0, 9.0))\n',
   tests='''
ns, out = run()
for vals in [(2.0, 4.0, 9.0), (5,), (-1.5, 1.5, 0.0, 3.0)]:
    r = call(ns, "stats", *vals)
    e = (sum(vals) / len(vals), max(vals) - min(vals))
    check(isinstance(r, tuple) and len(r) == 2 and approx(r[0], e[0]) and approx(r[1], e[1]), f"stats{vals} = {e}", f"stats{vals} = {e}")
check(call(ns, "stats") is None, "stats() ohne Argumente gibt None zurück", "stats() without arguments returns None")
''',
   require=["varargs"], refs=["7.5", "7.2s"])

ex(id="k7-normalize", ch="7", lvl=3,
   title={"de": "Normieren ohne Seiteneffekt", "en": "Normalising without side effects"},
   task={"de": "Schreiben Sie `normalize(values)`, die eine **neue** Liste zurückgibt, in der jeder Wert (in derselben Reihenfolge) durch das Maximum der Beträge geteilt ist (größter Betrag wird 1.0). Die übergebene Liste darf **nicht** verändert werden! Ist die Liste leer oder sind alle Werte 0, wird eine Kopie der Liste zurückgegeben.",
         "en": "Write `normalize(values)` that returns a **new** list in which each value (in the same order) is divided by the maximum absolute value (largest magnitude becomes 1.0). The list passed in must **not** be modified! If the list is empty or all values are 0, return a copy of the list."},
   starter={"de": "def normalize(values):\n    ...\n", "en": "def normalize(values):\n    ...\n"},
   solution='def normalize(values):\n    biggest = 0\n    for v in values:\n        if abs(v) > biggest:\n            biggest = abs(v)\n    result = []\n    for v in values:\n        if biggest == 0:\n            result.append(v)\n        else:\n            result.append(v / biggest)\n    return result\n\ndata = [2.0, -4.0, 1.0]\nprint(normalize(data), data)\n',
   tests='''
ns, out = run()
for d in [[2.0, -4.0, 1.0], [5, 10, 2.5], [0, 0], []]:
    original = list(d)
    arg = list(d)
    r = call(ns, "normalize", arg)
    m = max([abs(x) for x in d], default=0)
    e = [x / m for x in d] if m else list(d)
    check(isinstance(r, list) and len(r) == len(e) and all(approx(a, b) for a, b in zip(r, e)), f"normalize({original}) = {e}", f"normalize({original}) = {e}")
    check(arg == original, f"Die Liste {original} bleibt unverändert", f"The list {original} stays unchanged")
    check(r is not arg, "Es wird eine neue Liste zurückgegeben", "A new list is returned")
''',
   require=["def", "return"], refs=["7.7", "5.4s"])

ex(id="k7-resist", ch="7", lvl=3,
   title={"de": "Widerstandsnetzwerk", "en": "Resistor network"},
   task={"de": "Schreiben Sie `total_resistance(resistors, mode=\"series\")`. `resistors` ist eine Liste von Widerständen in Ω. Bei `mode=\"series\"` wird die Summe zurückgegeben, bei `mode=\"parallel\"` der Wert $\\dfrac{1}{1/R_1 + 1/R_2 + \\dots}$. Bei einem anderen `mode` oder einer leeren Liste soll `None` zurückgegeben werden. Dokumentieren Sie die Funktion mit einem Docstring.",
         "en": "Write `total_resistance(resistors, mode=\"series\")`. `resistors` is a list of resistances in Ω. For `mode=\"series\"` return the sum, for `mode=\"parallel\"` the value $\\dfrac{1}{1/R_1 + 1/R_2 + \\dots}$. For any other `mode` or an empty list, return `None`. Document the function with a docstring."},
   starter={"de": "def total_resistance(resistors, mode=\"series\"):\n    \"\"\"...\"\"\"\n    ...\n", "en": "def total_resistance(resistors, mode=\"series\"):\n    \"\"\"...\"\"\"\n    ...\n"},
   solution='def total_resistance(resistors, mode="series"):\n    """Gesamtwiderstand einer Reihen- oder Parallelschaltung.\n\n    Args:\n        resistors (list): Widerstände in Ohm.\n        mode (str): "series" oder "parallel".\n    Returns:\n        float: Gesamtwiderstand oder None bei ungültiger Eingabe.\n    """\n    if len(resistors) == 0:\n        return None\n    if mode == "series":\n        return sum(resistors)\n    elif mode == "parallel":\n        inverse = 0\n        for r in resistors:\n            inverse += 1 / r\n        return 1 / inverse\n    return None\n\nprint(total_resistance([100, 220]), total_resistance([100, 100], mode="parallel"))\n',
   tests='''
ns, out = run()
for rs in [[100, 220], [47.0], [10, 20, 30]]:
    check(approx(call(ns, "total_resistance", list(rs)), sum(rs)), f"Reihe {rs} = {sum(rs)} Ω", f"Series {rs} = {sum(rs)} Ω")
    ep = 1 / sum(1 / r for r in rs)
    check(approx(call(ns, "total_resistance", list(rs), mode="parallel"), ep), f"Parallel {rs} ≈ {ep:.3f} Ω", f"Parallel {rs} ≈ {ep:.3f} Ω")
check(call(ns, "total_resistance", [10, 20], mode="stern") is None, "Unbekannter mode liefert None", "Unknown mode returns None")
check(call(ns, "total_resistance", []) is None, "Leere Liste liefert None", "Empty list returns None")
check(bool(ns["total_resistance"].__doc__) and "..." != ns["total_resistance"].__doc__.strip(), "Die Funktion hat einen Docstring", "The function has a docstring")
''',
   require=["default_arg"], refs=["7.3p", "7.8"])

# =================================================================== Kapitel 8
ex(id="k8-slice", ch="8", lvl=1,
   title={"de": "Messreihe zerschneiden", "en": "Slicing a measurement series"},
   task={"de": "Erzeugen Sie aus `temps` nur mit Slicing:\n- `first3`: die ersten drei Werte\n- `last3`: die letzten drei Werte\n- `every2`: jeden zweiten Wert, beginnend beim ersten\n- `backwards`: die ganze Liste rückwärts",
         "en": "Using only slicing, create from `temps`:\n- `first3`: the first three values\n- `last3`: the last three values\n- `every2`: every second value, starting with the first\n- `backwards`: the whole list reversed"},
   starter={"de": "temps = [22.5, 23.1, 21.8, 24.0, 22.5, 21.8, 25.3]\n\n# Ihr Code:\n", "en": "temps = [22.5, 23.1, 21.8, 24.0, 22.5, 21.8, 25.3]\n\n# your code:\n"},
   solution='temps = [22.5, 23.1, 21.8, 24.0, 22.5, 21.8, 25.3]\nfirst3 = temps[:3]\nlast3 = temps[-3:]\nevery2 = temps[::2]\nbackwards = temps[::-1]\nprint(first3, last3, every2, backwards)\n',
   tests='''
for t in [[22.5, 23.1, 21.8, 24.0, 22.5, 21.8, 25.3], [1, 2, 3, 4, 5, 6]]:
    ns, out = run(sub={"temps": t})
    a, b, c, d = need(ns, "first3", "last3", "every2", "backwards")
    check(a == t[:3], f"first3 = {t[:3]}", f"first3 = {t[:3]}")
    check(b == t[-3:], f"last3 = {t[-3:]}", f"last3 = {t[-3:]}")
    check(c == t[::2], f"every2 = {t[::2]}", f"every2 = {t[::2]}")
    check(d == t[::-1], f"backwards = {t[::-1]}", f"backwards = {t[::-1]}")
''',
   require=["slice"], forbid=["for"], refs=["8.1x"])

ex(id="k8-set", ch="8", lvl=1,
   title={"de": "Gemeinsame Messwerte", "en": "Common measurements"},
   task={"de": "Zwei Sensoren liefern die Messreihen `a` und `b`. Ermitteln Sie mit Sets:\n- `unique_a`: Anzahl verschiedener Werte in `a`\n- `common`: die Werte, die in beiden Reihen vorkommen, als **sortierte Liste**\n- `only_a`: die Werte, die nur in `a` vorkommen, als sortierte Liste",
         "en": "Two sensors deliver the series `a` and `b`. Using sets, determine:\n- `unique_a`: number of distinct values in `a`\n- `common`: the values present in both series, as a **sorted list**\n- `only_a`: the values present only in `a`, as a sorted list"},
   starter={"de": "a = [19.6, 20.1, 20.4, 20.1, 21.0, 19.6]\nb = [20.4, 20.9, 19.6, 22.3, 20.2]\n\n# Ihr Code:\n", "en": "a = [19.6, 20.1, 20.4, 20.1, 21.0, 19.6]\nb = [20.4, 20.9, 19.6, 22.3, 20.2]\n\n# your code:\n"},
   solution='a = [19.6, 20.1, 20.4, 20.1, 21.0, 19.6]\nb = [20.4, 20.9, 19.6, 22.3, 20.2]\nset_a = set(a)\nset_b = set(b)\nunique_a = len(set_a)\ncommon = sorted(set_a.intersection(set_b))\nonly_a = sorted(set_a.difference(set_b))\nprint(unique_a, common, only_a)\n',
   tests='''
for a, b in [([19.6, 20.1, 20.4, 20.1, 21.0, 19.6], [20.4, 20.9, 19.6, 22.3, 20.2]), ([1, 1, 2], [3, 4])]:
    ns, out = run(sub={"a": a, "b": b})
    u, c, o = need(ns, "unique_a", "common", "only_a")
    check(u == len(set(a)), f"unique_a = {len(set(a))}", f"unique_a = {len(set(a))}")
    check(c == sorted(set(a) & set(b)), f"common = {sorted(set(a) & set(b))}", f"common = {sorted(set(a) & set(b))}")
    check(o == sorted(set(a) - set(b)), f"only_a = {sorted(set(a) - set(b))}", f"only_a = {sorted(set(a) - set(b))}")
''',
   require=["set"], refs=["8.2"])

ex(id="k8-stock", ch="8", lvl=2,
   title={"de": "Lagerbestand als Dictionary", "en": "Stock as a dictionary"},
   task={"de": "Der Lagerbestand `stock` ordnet Bauteilen eine Stückzahl zu. Die Liste `deliveries` enthält Tupel `(bauteil, anzahl)`. Buchen Sie alle Lieferungen ein (neue Bauteile werden angelegt – nutzen Sie `.get(..., 0)`). Erzeugen Sie danach `low` = sortierte Liste aller Bauteile mit weniger als 10 Stück.",
         "en": "The stock `stock` maps parts to quantities. The list `deliveries` contains tuples `(part, quantity)`. Book all deliveries (new parts are created – use `.get(..., 0)`). Then create `low` = sorted list of all parts with fewer than 10 pieces."},
   starter={"de": "stock = {'M8': 120, 'M6': 4, 'Lager': 9}\ndeliveries = [('M6', 50), ('Dichtung', 3), ('M8', 10)]\n\n# Ihr Code:\n", "en": "stock = {'M8': 120, 'M6': 4, 'Lager': 9}\ndeliveries = [('M6', 50), ('Dichtung', 3), ('M8', 10)]\n\n# your code:\n"},
   solution="stock = {'M8': 120, 'M6': 4, 'Lager': 9}\ndeliveries = [('M6', 50), ('Dichtung', 3), ('M8', 10)]\nfor part, qty in deliveries:\n    stock[part] = stock.get(part, 0) + qty\nlow = sorted([p for p, q in stock.items() if q < 10])\nprint(stock, low)\n",
   tests='''
for st, dl in [({'M8': 120, 'M6': 4, 'Lager': 9}, [('M6', 50), ('Dichtung', 3), ('M8', 10)]), ({}, [('A', 1), ('A', 2), ('B', 20)]), ({'X': 7, 'Y': 9}, [('X', 3)])]:
    ns, out = run(sub={"stock": dict(st), "deliveries": list(dl)})
    s, l = need(ns, "stock", "low")
    e = dict(st)
    for p, q in dl:
        e[p] = e.get(p, 0) + q
    check(s == e, f"Bestand nach Lieferung: {e}", f"Stock after delivery: {e}")
    el = sorted(p for p, q in e.items() if q < 10)
    check(l == el, f"low = {el}", f"low = {el}")
''',
   require=["dict_methods"], refs=["8.3", "8.4"])

ex(id="k8-comp", ch="8", lvl=2,
   title={"de": "Widerstände aussortieren", "en": "Sorting out resistors"},
   task={"de": "Gemessene Widerstände (Nennwert 220 Ω, Toleranz ±5 %) stehen in `measured`. Erzeugen Sie jeweils mit einer **List Comprehension** (Reihenfolge wie in `measured`):\n- `good`: alle Werte innerhalb der Toleranz\n- `deviation`: für jeden Messwert die Abweichung in Prozent, auf eine Nachkommastelle gerundet\n- `labels`: für jeden Messwert `'ok'` oder `'Ausschuss'`",
         "en": "Measured resistors (nominal 220 Ω, tolerance ±5 %) are in `measured`. Using a **list comprehension** each time, create (same order as in `measured`):\n- `good`: all values within tolerance\n- `deviation`: for every value the deviation in percent, rounded to one decimal\n- `labels`: for every value `'ok'` or `'scrap'`"},
   starter={"de": "nominal = 220\nmeasured = [218.0, 231.5, 209.0, 225.4, 240.1, 220.0]\n\n# Ihr Code:\n", "en": "nominal = 220\nmeasured = [218.0, 231.5, 209.0, 225.4, 240.1, 220.0]\n\n# your code:\n"},
   solution="nominal = 220\nmeasured = [218.0, 231.5, 209.0, 225.4, 240.1, 220.0]\ngood = [r for r in measured if abs(r - nominal) <= 0.05 * nominal]\ndeviation = [round((r - nominal) / nominal * 100, 1) for r in measured]\nlabels = ['ok' if abs(r - nominal) <= 0.05 * nominal else 'Ausschuss' for r in measured]\nprint(good, deviation, labels)\n",
   tests='''
_srt = lambda x: sorted(x) if isinstance(x, (list, tuple)) else x
for m in [[218.0, 231.5, 209.0, 225.4, 240.1, 220.0], [200.0, 230.0]]:
    ns, out = run(sub={"measured": m})
    g, d, l = need(ns, "good", "deviation", "labels")
    ok = [abs(r - 220) <= 11 for r in m]
    check(_srt(g) == sorted(r for r, o in zip(m, ok) if o), "good enthält genau die Werte in Toleranz", "good contains exactly the values within tolerance")
    ed = [round((r - 220) / 220 * 100, 1) for r in m]
    check(len(d) == len(ed) and all(approx(a, b, 1e-3) for a, b in zip(d, ed)), f"deviation = {ed}", f"deviation = {ed}")
    check(len(l) == len(m) and all((x == "ok") == o for x, o in zip(l, ok)), "labels markiert jeden Wert richtig", "labels marks every value correctly")
''',
   require=["listcomp"], refs=["8.8"])

ex(id="k8-zip", ch="8", lvl=2,
   title={"de": "Zeitreihe mit zip und enumerate", "en": "Time series with zip and enumerate"},
   task={"de": "Erzeugen Sie aus `times` (Minuten) und `temps` (°C) mit `zip()` und `dict()` das Dictionary `series` (Zeit → Temperatur). Ermitteln Sie `t_max`, die Zeit der höchsten Temperatur. Geben Sie anschließend mit `enumerate(..., start=1)` eine nummerierte Liste aus: `1: t = 0 min, 18.2 °C` usw.",
         "en": "From `times` (minutes) and `temps` (°C) create the dictionary `series` (time → temperature) using `zip()` and `dict()`. Determine `t_max`, the time of the highest temperature. Then print a numbered list using `enumerate(..., start=1)`: `1: t = 0 min, 18.2 °C` etc."},
   starter={"de": "times = [0, 10, 20, 30, 40]\ntemps = [18.2, 24.6, 31.0, 29.4, 26.1]\n\n# Ihr Code:\n", "en": "times = [0, 10, 20, 30, 40]\ntemps = [18.2, 24.6, 31.0, 29.4, 26.1]\n\n# your code:\n"},
   solution='times = [0, 10, 20, 30, 40]\ntemps = [18.2, 24.6, 31.0, 29.4, 26.1]\nseries = dict(zip(times, temps))\nt_max = times[temps.index(max(temps))]\nfor number, t in enumerate(times, start=1):\n    print(f"{number}: t = {t} min, {series[t]} °C")\n',
   tests='''
for ti, te in [([0, 10, 20, 30, 40], [18.2, 24.6, 31.0, 29.4, 26.1]), ([1, 2, 3], [9.0, 3.0, 1.0])]:
    ns, out = run(sub={"times": ti, "temps": te})
    s, tm = need(ns, "series", "t_max")
    check(s == dict(zip(ti, te)), f"series = {dict(zip(ti, te))}", f"series = {dict(zip(ti, te))}")
    check(tm == ti[te.index(max(te))], f"t_max = {ti[te.index(max(te))]}", f"t_max = {ti[te.index(max(te))]}")
    check(all(f"{i}:" in out for i in range(1, len(ti) + 1)) and "0:" not in out.replace("10:", "").replace("20:", ""), "Nummerierung beginnt bei 1", "Numbering starts at 1")
''',
   require=["enumzip"], refs=["8.9", "8.3"])

ex(id="k8-nested", ch="8", lvl=3,
   title={"de": "Mehrere Sensoren auswerten", "en": "Evaluating several sensors"},
   task={"de": "`data` ist ein verschachteltes Dictionary: Sensorname → {Zeitstempel → (Temperatur, Luftfeuchte)}. Erzeugen Sie\n- `mean_temp`: Dictionary Sensorname → mittlere Temperatur (auf 2 Stellen gerundet)\n- `humid_sensor`: Name des Sensors, an dem die höchste einzelne Luftfeuchte gemessen wurde.",
         "en": "`data` is a nested dictionary: sensor name → {timestamp → (temperature, humidity)}. Create\n- `mean_temp`: dictionary sensor name → mean temperature (rounded to 2 decimals)\n- `humid_sensor`: name of the sensor that measured the highest single humidity."},
   starter={"de": 'data = {\n    "Halle1": {"08:00": (19.5, 48), "09:00": (20.3, 51)},\n    "Halle2": {"08:00": (22.1, 39), "09:00": (22.8, 63), "10:00": (23.0, 58)},\n    "Lager": {"08:00": (14.2, 71)}\n}\n\n# Ihr Code:\n',
            "en": 'data = {\n    "Halle1": {"08:00": (19.5, 48), "09:00": (20.3, 51)},\n    "Halle2": {"08:00": (22.1, 39), "09:00": (22.8, 63), "10:00": (23.0, 58)},\n    "Lager": {"08:00": (14.2, 71)}\n}\n\n# your code:\n'},
   solution='data = {\n    "Halle1": {"08:00": (19.5, 48), "09:00": (20.3, 51)},\n    "Halle2": {"08:00": (22.1, 39), "09:00": (22.8, 63), "10:00": (23.0, 58)},\n    "Lager": {"08:00": (14.2, 71)}\n}\nmean_temp = {}\nhumid_sensor = None\nbest = -1\nfor sensor, readings in data.items():\n    temps = [m[0] for m in readings.values()]\n    mean_temp[sensor] = round(sum(temps) / len(temps), 2)\n    for temp, hum in readings.values():\n        if hum > best:\n            best = hum\n            humid_sensor = sensor\nprint(mean_temp, humid_sensor)\n',
   tests='''
cases = [{"Halle1": {"08:00": (19.5, 48), "09:00": (20.3, 51)}, "Halle2": {"08:00": (22.1, 39), "09:00": (22.8, 63), "10:00": (23.0, 58)}, "Lager": {"08:00": (14.2, 71)}},
         {"A": {"t1": (10.0, 90)}, "B": {"t1": (30.0, 20), "t2": (20.0, 30)}}]
for d in cases:
    ns, out = run(sub={"data": d})
    mt, hs = need(ns, "mean_temp", "humid_sensor")
    e = {s: round(sum(v[0] for v in r.values()) / len(r), 2) for s, r in d.items()}
    check(isinstance(mt, dict) and set(mt) == set(e) and all(approx(mt[k], e[k], 1e-4) for k in e), f"mean_temp = {e}", f"mean_temp = {e}")
    eh = max(d, key=lambda s: max(v[1] for v in d[s].values()))
    check(hs == eh, f"humid_sensor = {eh!r}", f"humid_sensor = {eh!r}")
''',
   refs=["8.5", "8.3", "8.4"])

ex(id="k8-mode", ch="8", lvl=3,
   title={"de": "Häufigster Messwert", "en": "Most frequent measurement"},
   task={"de": "Zählen Sie mit einem Dictionary, wie oft jeder Wert in `readings` vorkommt (`counts`, Wert → Anzahl). Ermitteln Sie `mode`, den häufigsten Wert (bei Gleichstand den kleinsten), und `once`, die sortierte Liste aller Werte, die genau einmal vorkommen. `Counter` aus `collections` steht nicht im Skript – bauen Sie es selbst.",
         "en": "Use a dictionary to count how often each value appears in `readings` (`counts`, value → count). Determine `mode`, the most frequent value (on a tie, the smallest), and `once`, the sorted list of all values that appear exactly once. `Counter` from `collections` is not in the script – build it yourself."},
   starter={"de": "readings = [3, 5, 3, 7, 5, 3, 9, 7, 1]\n\n# Ihr Code:\n", "en": "readings = [3, 5, 3, 7, 5, 3, 9, 7, 1]\n\n# your code:\n"},
   solution='readings = [3, 5, 3, 7, 5, 3, 9, 7, 1]\ncounts = {}\nfor r in readings:\n    counts[r] = counts.get(r, 0) + 1\nmode = None\nfor value in sorted(counts):\n    if mode is None or counts[value] > counts[mode]:\n        mode = value\nonce = sorted([v for v, c in counts.items() if c == 1])\nprint(counts, mode, once)\n',
   tests='''
for r in [[3, 5, 3, 7, 5, 3, 9, 7, 1], [4, 2, 4, 2, 8], [6]]:
    ns, out = run(sub={"readings": r})
    c, m, o = need(ns, "counts", "mode", "once")
    ec = {}
    for x in r:
        ec[x] = ec.get(x, 0) + 1
    em = min(ec, key=lambda v: (-ec[v], v))
    check(c == ec, f"counts = {ec}", f"counts = {ec}")
    check(m == em, f"mode = {em}", f"mode = {em}")
    check(o == sorted(v for v, k in ec.items() if k == 1), "once stimmt", "once is correct")
''',
   require=["dict"], refs=["8.3"])

# =================================================================== Kapitel 9
ex(id="k9-incline", ch="9", lvl=1,
   title={"de": "Schiefe Ebene mit math", "en": "Inclined plane with math"},
   task={"de": "Ein Körper der Masse `m` (kg) liegt auf einer schiefen Ebene mit Neigungswinkel `alpha_deg` (Grad). Importieren Sie `math`, rechnen Sie den Winkel ins Bogenmaß um (`* math.pi / 180`) und berechnen Sie Hangabtriebskraft `F_H = m·g·sin(α)` und Normalkraft `F_N = m·g·cos(α)` mit $g = 9.81\\,\\mathrm{m/s^2}$.",
         "en": "A body of mass `m` (kg) rests on an inclined plane with angle `alpha_deg` (degrees). Import `math`, convert the angle to radians (`* math.pi / 180`) and compute the downhill force `F_H = m·g·sin(α)` and the normal force `F_N = m·g·cos(α)` with $g = 9.81\\,\\mathrm{m/s^2}$."},
   starter={"de": "m = 12.0          # kg\nalpha_deg = 30.0  # Grad\n\n# Ihr Code:\n", "en": "m = 12.0          # kg\nalpha_deg = 30.0  # degrees\n\n# your code:\n"},
   solution='import math\n\nm = 12.0\nalpha_deg = 30.0\nalpha = alpha_deg * math.pi / 180\nF_H = m * 9.81 * math.sin(alpha)\nF_N = m * 9.81 * math.cos(alpha)\nprint(f"F_H = {F_H:.1f} N, F_N = {F_N:.1f} N")\n',
   tests='''
import math as _m
for m, a in [(12.0, 30.0), (5.0, 45.0), (80.0, 10.0)]:
    ns, out = run(sub={"m": m, "alpha_deg": a})
    fh, fn = need(ns, "F_H", "F_N")
    r = a * _m.pi / 180
    check(approx(fh, m * 9.81 * _m.sin(r), 1e-4), f"F_H für m = {m} kg, α = {a}° ≈ {m*9.81*_m.sin(r):.2f} N", f"F_H for m = {m} kg, α = {a}° ≈ {m*9.81*_m.sin(r):.2f} N")
    check(approx(fn, m * 9.81 * _m.cos(r), 1e-4), f"F_N ≈ {m*9.81*_m.cos(r):.2f} N", f"F_N ≈ {m*9.81*_m.cos(r):.2f} N")
''',
   refs=["9.1"])

ex(id="k9-vec", ch="9", lvl=2,
   title={"de": "Bewegung vektorisiert", "en": "Vectorised motion"},
   task={"de": "Importieren Sie NumPy als `np`. Erzeugen Sie mit `np.linspace` das Array `t` mit 101 Zeitpunkten von 0 bis 10 s. Berechnen Sie **ohne Schleife** die Positionen `x = x0 + v0·t + ½·a·t²` für `x0 = 2`, `v0 = 1.5`, `a = 0.8` als Array `x` und geben Sie die Position bei t = 10 s aus.",
         "en": "Import NumPy as `np`. Use `np.linspace` to create the array `t` with 101 time points from 0 to 10 s. Compute **without a loop** the positions `x = x0 + v0·t + ½·a·t²` for `x0 = 2`, `v0 = 1.5`, `a = 0.8` as the array `x` and print the position at t = 10 s."},
   starter={"de": "x0 = 2.0\nv0 = 1.5\na = 0.8\n\n# Ihr Code:\n", "en": "x0 = 2.0\nv0 = 1.5\na = 0.8\n\n# your code:\n"},
   solution='import numpy as np\n\nx0 = 2.0\nv0 = 1.5\na = 0.8\nt = np.linspace(0, 10, 101)\nx = x0 + v0 * t + 0.5 * a * t**2\nprint(x[-1])\n',
   tests='''
ns, out = run()
t, x = need(ns, "t", "x")
check(type(t).__name__ == "ndarray" and len(t) == 101 and approx(t[0], 0) and approx(t[-1], 10), "t ist ein Array mit 101 Werten von 0 bis 10", "t is an array of 101 values from 0 to 10")
check(type(x).__name__ == "ndarray" and len(x) == 101, "x ist ein Array gleicher Länge", "x is an array of the same length")
check(approx(x[-1], 2 + 15 + 40) and approx(x[50], 2 + 7.5 + 10), "Positionen stimmen (x(10 s) = 57 m)", "Positions are correct (x(10 s) = 57 m)")
ns, out = run(sub={"a": 0.0})
check(approx(ns["x"][-1], 17), "Mit a = 0 ergibt sich x(10 s) = 17 m", "With a = 0, x(10 s) = 17 m")
''',
   require=["numpy"], forbid=["for", "while"], refs=["9.2", "9.2v"])

ex(id="k9-rod", ch="9", lvl=2,
   title={"de": "Temperatur in einem Stab", "en": "Temperature in a rod"},
   task={"de": "Ein Stab wird links auf `T_left` und rechts auf `T_right` gehalten (°C). Teilt man ihn in vier gleiche Abschnitte, gilt für die drei inneren Temperaturen $T_1, T_2, T_3$ im stationären Zustand: Jeder innere Wert ist der Mittelwert seiner Nachbarn. Umgestellt ergibt das\n\n$$\\begin{aligned} -2T_1 + T_2 &= -T_\\mathrm{left} \\\\ T_1 - 2T_2 + T_3 &= 0 \\\\ T_2 - 2T_3 &= -T_\\mathrm{right} \\end{aligned}$$\n\nLegen Sie die Koeffizientenmatrix `A` und die rechte Seite `b` als NumPy-Arrays an, lösen Sie mit `np.linalg.solve` nach `T` und speichern Sie in `ok`, ob `A @ T` mit `b` übereinstimmt (`np.allclose`).",
         "en": "A rod is held at `T_left` on the left and `T_right` on the right (°C). Dividing it into four equal sections, the three inner temperatures $T_1, T_2, T_3$ satisfy in the steady state: each inner value is the mean of its neighbours. Rearranged, this gives\n\n$$\\begin{aligned} -2T_1 + T_2 &= -T_\\mathrm{left} \\\\ T_1 - 2T_2 + T_3 &= 0 \\\\ T_2 - 2T_3 &= -T_\\mathrm{right} \\end{aligned}$$\n\nCreate the coefficient matrix `A` and the right-hand side `b` as NumPy arrays, solve for `T` with `np.linalg.solve` and store in `ok` whether `A @ T` matches `b` (`np.allclose`)."},
   starter={"de": "import numpy as np\n\nT_left = 100.0\nT_right = 20.0\n\n# Ihr Code:\n", "en": "import numpy as np\n\nT_left = 100.0\nT_right = 20.0\n\n# your code:\n"},
   solution='import numpy as np\n\nT_left = 100.0\nT_right = 20.0\nA = np.array([[-2.0, 1.0, 0.0],\n              [1.0, -2.0, 1.0],\n              [0.0, 1.0, -2.0]])\nb = np.array([-T_left, 0.0, -T_right])\nT = np.linalg.solve(A, b)\nok = np.allclose(A @ T, b)\nprint(T, ok)\n',
   tests='''
for tl, tr in [(100.0, 20.0), (0.0, 80.0), (-10.0, -10.0)]:
    ns, out = run(sub={"T_left": tl, "T_right": tr})
    A, b, T, ok = need(ns, "A", "b", "T", "ok")
    e = [tl + (tr - tl) * k / 4 for k in (1, 2, 3)]
    check(getattr(A, "shape", None) == (3, 3) and getattr(b, "shape", None) == (3,), "A ist 3×3, b hat 3 Einträge", "A is 3×3, b has 3 entries")
    check(len(T) == 3 and all(approx(T[k], e[k]) for k in range(3)), f"T_left = {tl}, T_right = {tr}: T = {[round(x, 2) for x in e]}", f"T_left = {tl}, T_right = {tr}: T = {[round(x, 2) for x in e]}")
    check(bool(ok) is True, "Probe ok = True", "Check ok = True")
''',
   require=["numpy", "matmul"], refs=["9.2m"])

ex(id="k9-pandas", ch="9", lvl=3,
   title={"de": "Prüfstandsdaten mit pandas", "en": "Test-bench data with pandas"},
   task={"de": "Erzeugen Sie aus dem Dictionary `data` ein DataFrame `df`. Fügen Sie die Spalte `P_W` (Leistung = Spannung · Strom) hinzu. Speichern Sie die mittlere Leistung in `P_mean` (`.mean()`) und die höchste Temperatur in `T_max` – dafür genügt die eingebaute Funktion `max()`, angewendet auf die Spalte.",
         "en": "Create a DataFrame `df` from the dictionary `data`. Add the column `P_W` (power = voltage · current). Store the mean power in `P_mean` (`.mean()`) and the highest temperature in `T_max` – the built-in function `max()`, applied to the column, does the job."},
   starter={"de": "import pandas as pd\n\ndata = {\n    'zeit_s': [0, 2, 4, 6],\n    'spannung_V': [400.4, 400.8, 400.4, 400.7],\n    'strom_A': [10.2, 10.6, 9.7, 11.2],\n    'temperatur_C': [24.6, 25.3, 25.7, 25.9]\n}\n\n# Ihr Code:\n",
            "en": "import pandas as pd\n\ndata = {\n    'zeit_s': [0, 2, 4, 6],\n    'spannung_V': [400.4, 400.8, 400.4, 400.7],\n    'strom_A': [10.2, 10.6, 9.7, 11.2],\n    'temperatur_C': [24.6, 25.3, 25.7, 25.9]\n}\n\n# your code:\n"},
   solution="import pandas as pd\n\ndata = {\n    'zeit_s': [0, 2, 4, 6],\n    'spannung_V': [400.4, 400.8, 400.4, 400.7],\n    'strom_A': [10.2, 10.6, 9.7, 11.2],\n    'temperatur_C': [24.6, 25.3, 25.7, 25.9]\n}\ndf = pd.DataFrame(data)\ndf['P_W'] = df['spannung_V'] * df['strom_A']\nP_mean = df['P_W'].mean()\nT_max = max(df['temperatur_C'])\nprint(df.head())\nprint(P_mean, T_max)\n",
   tests='''
ns, out = run()
df, pm, tm = need(ns, "df", "P_mean", "T_max")
check(type(df).__name__ == "DataFrame" and "P_W" in df.columns, "df ist ein DataFrame mit Spalte P_W", "df is a DataFrame with column P_W")
u = [400.4, 400.8, 400.4, 400.7]; i = [10.2, 10.6, 9.7, 11.2]
check(approx(pm, sum(a * b for a, b in zip(u, i)) / 4), "P_mean stimmt", "P_mean is correct")
check(approx(tm, 25.9), "T_max = 25.9 °C", "T_max = 25.9 °C")
''',
   require=["pandas"], refs=["9.4"])

# =================================================================== Kapitel 10
ex(id="k10-resistor", ch="10", lvl=1,
   title={"de": "Klasse Resistor", "en": "Class Resistor"},
   task={"de": "Schreiben Sie eine Klasse `Resistor`. Der Konstruktor erhält den Widerstand `r` (Ω) und speichert ihn im Attribut `r`. Die Methode `current(u)` gibt den Strom $I = U/R$ zurück, die Methode `power(u)` die Leistung $P = U^2/R$.",
         "en": "Write a class `Resistor`. The constructor receives the resistance `r` (Ω) and stores it in the attribute `r`. The method `current(u)` returns the current $I = U/R$, the method `power(u)` the power $P = U^2/R$."},
   starter={"de": "class Resistor:\n    def __init__(self, r):\n        ...\n", "en": "class Resistor:\n    def __init__(self, r):\n        ...\n"},
   solution='class Resistor:\n    def __init__(self, r):\n        self.r = r\n\n    def current(self, u):\n        return u / self.r\n\n    def power(self, u):\n        return u**2 / self.r\n\nr1 = Resistor(100)\nprint(r1.current(12), r1.power(12))\n',
   tests='''
ns, out = run()
for r in [100, 4.7, 1000]:
    obj = call(ns, "Resistor", r)
    check(getattr(obj, "r", None) == r, f"Resistor({r}).r == {r}", f"Resistor({r}).r == {r}")
    check(approx(method(obj, "current", 12), 12 / r), f"current(12) = {12/r:.4g} A", f"current(12) = {12/r:.4g} A")
    check(approx(method(obj, "power", 12), 144 / r), f"power(12) = {144/r:.4g} W", f"power(12) = {144/r:.4g} W")
''',
   require=["class"], refs=["10.3"])

ex(id="k10-sensor", ch="10", lvl=2,
   title={"de": "Vererbung: Sensoren", "en": "Inheritance: sensors"},
   task={"de": "Basisklasse `Sensor(name)` mit Attributen `name` und `values` (leere Liste), Methoden `add(value)` und `mean()` (Mittelwert, bei leerer Liste `None`).\n\nAbgeleitete Klasse `TemperatureSensor(name, unit=\"C\")`: ruft mit `super().__init__(name)` den Basiskonstruktor auf, speichert `unit` und hat die Methode `mean_fahrenheit()`, die den Mittelwert in °F liefert (bei unit `\"C\"`). Ist `unit` schon `\"F\"`, wird der Mittelwert unverändert zurückgegeben.",
         "en": "Base class `Sensor(name)` with attributes `name` and `values` (empty list), methods `add(value)` and `mean()` (mean, `None` for an empty list).\n\nDerived class `TemperatureSensor(name, unit=\"C\")`: calls the base constructor with `super().__init__(name)`, stores `unit` and has the method `mean_fahrenheit()` returning the mean in °F (for unit `\"C\"`). If `unit` is already `\"F\"`, the mean is returned unchanged."},
   starter={"de": "class Sensor:\n    def __init__(self, name):\n        ...\n\nclass TemperatureSensor(Sensor):\n    ...\n", "en": "class Sensor:\n    def __init__(self, name):\n        ...\n\nclass TemperatureSensor(Sensor):\n    ...\n"},
   solution='class Sensor:\n    def __init__(self, name):\n        self.name = name\n        self.values = []\n\n    def add(self, value):\n        self.values.append(value)\n\n    def mean(self):\n        if len(self.values) == 0:\n            return None\n        return sum(self.values) / len(self.values)\n\n\nclass TemperatureSensor(Sensor):\n    def __init__(self, name, unit="C"):\n        super().__init__(name)\n        self.unit = unit\n\n    def mean_fahrenheit(self):\n        m = self.mean()\n        if m is None or self.unit == "F":\n            return m\n        return m * 9 / 5 + 32\n\nt = TemperatureSensor("T1")\nt.add(20.0)\nt.add(22.0)\nprint(t.mean(), t.mean_fahrenheit())\n',
   tests='''
ns, out = run()
s = call(ns, "Sensor", "S1")
check(getattr(s, "name", None) == "S1" and getattr(s, "values", None) == [], "Sensor hat name und leere values", "Sensor has name and empty values")
check(method(s, "mean") is None, "mean() einer leeren Messreihe ist None", "mean() of an empty series is None")
method(s, "add", 2.0); method(s, "add", 4.0)
check(approx(method(s, "mean"), 3.0), "mean() nach add(2), add(4) = 3.0", "mean() after add(2), add(4) = 3.0")
t = call(ns, "TemperatureSensor", "T1")
check(isinstance(t, ns["Sensor"]), "TemperatureSensor erbt von Sensor", "TemperatureSensor inherits from Sensor")
check(getattr(t, "name", None) == "T1" and getattr(t, "values", None) == [] and getattr(t, "unit", None) == "C", "Konstruktor setzt name, values und unit", "Constructor sets name, values and unit")
method(t, "add", 20.0); method(t, "add", 22.0)
check(approx(method(t, "mean_fahrenheit"), 69.8), "mean_fahrenheit() = 69.8 °F für 21 °C", "mean_fahrenheit() = 69.8 °F for 21 °C")
f = call(ns, "TemperatureSensor", "T2", unit="F")
method(f, "add", 50.0)
check(approx(method(f, "mean_fahrenheit"), 50.0), "Bei unit='F' bleibt der Wert unverändert", "With unit='F' the value stays unchanged")
''',
   require=["class", "super"], refs=["10.3", "10.5"])

ex(id="k10-tank", ch="10", lvl=2,
   title={"de": "Kapselung: Wassertank", "en": "Encapsulation: water tank"},
   task={"de": "Klasse `Tank(capacity)` mit dem **protected** Attribut `_level` (Startwert 0).\n- `get_level()` gibt den Füllstand zurück.\n- `fill(amount)` füllt auf, höchstens bis `capacity`, und gibt die **übergelaufene** Menge zurück (0, wenn nichts überläuft).\n- `set_level(value)` setzt den Füllstand nur, wenn `0 <= value <= capacity`, und gibt `True`/`False` zurück, je nachdem ob gesetzt wurde.",
         "en": "Class `Tank(capacity)` with the **protected** attribute `_level` (initial value 0).\n- `get_level()` returns the level.\n- `fill(amount)` fills up, at most to `capacity`, and returns the **overflowing** amount (0 if nothing overflows).\n- `set_level(value)` sets the level only if `0 <= value <= capacity` and returns `True`/`False` depending on whether it was set."},
   starter={"de": "class Tank:\n    def __init__(self, capacity):\n        ...\n", "en": "class Tank:\n    def __init__(self, capacity):\n        ...\n"},
   solution='class Tank:\n    def __init__(self, capacity):\n        self.capacity = capacity\n        self._level = 0\n\n    def get_level(self):\n        return self._level\n\n    def fill(self, amount):\n        self._level += amount\n        overflow = 0\n        if self._level > self.capacity:\n            overflow = self._level - self.capacity\n            self._level = self.capacity\n        return overflow\n\n    def set_level(self, value):\n        if 0 <= value <= self.capacity:\n            self._level = value\n            return True\n        return False\n\ntank = Tank(80)\nprint(tank.fill(50), tank.fill(50), tank.get_level())\n',
   tests='''
ns, out = run()
t = call(ns, "Tank", 80)
check(hasattr(t, "_level") and method(t, "get_level") == 0, "Neuer Tank: _level = 0", "New tank: _level = 0")
check(approx(method(t, "fill", 50), 0) and approx(method(t, "get_level"), 50), "fill(50) → kein Überlauf, Füllstand 50", "fill(50) → no overflow, level 50")
check(approx(method(t, "fill", 50), 20) and approx(method(t, "get_level"), 80), "fill(50) → 20 laufen über, Füllstand 80", "fill(50) → 20 overflow, level 80")
check(method(t, "set_level", 100) is False and approx(method(t, "get_level"), 80), "set_level(100) wird abgelehnt", "set_level(100) is rejected")
check(method(t, "set_level", -1) is False, "set_level(-1) wird abgelehnt", "set_level(-1) is rejected")
check(method(t, "set_level", 30) is True and approx(method(t, "get_level"), 30), "set_level(30) setzt den Füllstand", "set_level(30) sets the level")
check(method(t, "set_level", 0) is True and method(t, "set_level", 80) is True and approx(method(t, "get_level"), 80), "Die Grenzen 0 und capacity sind erlaubt", "The limits 0 and capacity are allowed")
''',
   require=["class"], refs=["10.6", "10.6g"])

ex(id="k10-dimension", ch="10", lvl=3,
   title={"de": "Maße mit Abmaßen", "en": "Dimensions with tolerances"},
   task={"de": "In technischen Zeichnungen werden Maße mit Abmaßen angegeben, z.B. $25^{+0.05}_{-0.02}$ mm. Schreiben Sie die Klasse `Dimension(nominal, upper, lower)` (`upper` ≥ 0, `lower` ≤ 0):\n- `max_size()` und `min_size()`: Höchst- und Mindestmaß\n- `fits(measured)`: ob ein Messwert im zulässigen Bereich liegt (Grenzen eingeschlossen)\n- `__add__`: Maßkette – Nennmaße, obere und untere Abmaße werden jeweils addiert; das Ergebnis ist eine neue `Dimension`\n- `__str__`: z.B. `25.00 +0.05/-0.02` (zwei Nachkommastellen, Vorzeichen immer angeben; Tipp: die Formatangabe `:+.2f` erzwingt ein Vorzeichen)",
         "en": "Technical drawings give dimensions with tolerances, e.g. $25^{+0.05}_{-0.02}$ mm. Write the class `Dimension(nominal, upper, lower)` (`upper` ≥ 0, `lower` ≤ 0):\n- `max_size()` and `min_size()`: maximum and minimum size\n- `fits(measured)`: whether a measurement lies within the permitted range (limits included)\n- `__add__`: dimension chain – nominal sizes, upper and lower deviations are added separately; the result is a new `Dimension`\n- `__str__`: e.g. `25.00 +0.05/-0.02` (two decimals, always show the sign; tip: the format spec `:+.2f` forces a sign)"},
   starter={"de": "class Dimension:\n    def __init__(self, nominal, upper, lower):\n        self.nominal = nominal\n        self.upper = upper\n        self.lower = lower\n", "en": "class Dimension:\n    def __init__(self, nominal, upper, lower):\n        self.nominal = nominal\n        self.upper = upper\n        self.lower = lower\n"},
   solution='class Dimension:\n    def __init__(self, nominal, upper, lower):\n        self.nominal = nominal\n        self.upper = upper\n        self.lower = lower\n\n    def max_size(self):\n        return self.nominal + self.upper\n\n    def min_size(self):\n        return self.nominal + self.lower\n\n    def fits(self, measured):\n        return self.min_size() <= measured <= self.max_size()\n\n    def __add__(self, other):\n        return Dimension(self.nominal + other.nominal, self.upper + other.upper, self.lower + other.lower)\n\n    def __str__(self):\n        return f"{self.nominal:.2f} {self.upper:+.2f}/{self.lower:+.2f}"\n\nshaft = Dimension(25, 0.05, -0.02)\nring = Dimension(40, 0.1, 0.0)\nprint(shaft, "|", shaft + ring, "|", shaft.fits(25.03))\n',
   tests='''
ns, out = run()
D = ns.get("Dimension")
d = call(ns, "Dimension", 25, 0.05, -0.02)
check(approx(method(d, "max_size"), 25.05) and approx(method(d, "min_size"), 24.98), "25 +0.05/-0.02: Höchstmaß 25.05, Mindestmaß 24.98", "25 +0.05/-0.02: max 25.05, min 24.98")
check(method(d, "fits", 25.0) is True and method(d, "fits", 24.99) is True and method(d, "fits", 25.06) is False and method(d, "fits", 24.97) is False, "fits() prüft den zulässigen Bereich", "fits() checks the permitted range")
s = safe(lambda: d + call(ns, "Dimension", 40, 0.1, 0.0))
check(isinstance(s, D) and approx(s.nominal, 65) and approx(s.upper, 0.15) and approx(s.lower, -0.02), "Maßkette: 25 +0.05/-0.02 + 40 +0.10/+0.00 = 65 +0.15/-0.02", "Chain: 25 +0.05/-0.02 + 40 +0.10/+0.00 = 65 +0.15/-0.02")
s2 = safe(lambda: d + call(ns, "Dimension", 10, 0.02, -0.03))
check(isinstance(s2, D) and approx(s2.nominal, 35) and approx(s2.upper, 0.07) and approx(s2.lower, -0.05), "Maßkette: 25 +0.05/-0.02 + 10 +0.02/-0.03 = 35 +0.07/-0.05", "Chain: 25 +0.05/-0.02 + 10 +0.02/-0.03 = 35 +0.07/-0.05")
check(safe(lambda: str(d)) == "25.00 +0.05/-0.02", "str() = '25.00 +0.05/-0.02'", "str() = '25.00 +0.05/-0.02'")
check(safe(lambda: str(call(ns, "Dimension", 12.5, 0.0, -0.1))) == "12.50 +0.00/-0.10", "str() = '12.50 +0.00/-0.10'", "str() = '12.50 +0.00/-0.10'")
''',
   require=["class", "magic"], refs=["10.7", "10.3"])

ex(id="k10-abstract", ch="10", lvl=3,
   title={"de": "Abstrakte Klasse: Lasten", "en": "Abstract class: loads"},
   task={"de": "Definieren Sie die abstrakte Klasse `Load(ABC)` mit der abstrakten Methode `force()` (Kraft in N). Leiten Sie davon ab:\n- `PointLoad(f)`: Einzellast, `force()` gibt `f` zurück\n- `LineLoad(q, length)`: Streckenlast q (N/m) über die Länge (m), `force()` gibt `q * length` zurück\n\nSchreiben Sie außerdem die Funktion `total_force(loads)`, die die Summe der Kräfte einer Liste von Lasten liefert.",
         "en": "Define the abstract class `Load(ABC)` with the abstract method `force()` (force in N). Derive from it:\n- `PointLoad(f)`: point load, `force()` returns `f`\n- `LineLoad(q, length)`: distributed load q (N/m) over the length (m), `force()` returns `q * length`\n\nAlso write the function `total_force(loads)` returning the sum of the forces of a list of loads."},
   starter={"de": "from abc import ABC, abstractmethod\n\nclass Load(ABC):\n    ...\n", "en": "from abc import ABC, abstractmethod\n\nclass Load(ABC):\n    ...\n"},
   solution='from abc import ABC, abstractmethod\n\nclass Load(ABC):\n    @abstractmethod\n    def force(self):\n        pass\n\nclass PointLoad(Load):\n    def __init__(self, f):\n        self._f = f\n\n    def force(self):\n        return self._f\n\nclass LineLoad(Load):\n    def __init__(self, q, length):\n        self._q = q\n        self._length = length\n\n    def force(self):\n        return self._q * self._length\n\ndef total_force(loads):\n    total = 0\n    for load in loads:\n        total += load.force()\n    return total\n\nprint(total_force([PointLoad(500), LineLoad(200, 3)]))\n',
   tests='''
ns, out = run()
check(raises(TypeError, lambda: ns["Load"]()), "Load selbst kann nicht instanziiert werden (abstrakt)", "Load itself cannot be instantiated (abstract)")
p = call(ns, "PointLoad", 500); l = call(ns, "LineLoad", 200, 3)
check(isinstance(p, ns["Load"]) and isinstance(l, ns["Load"]), "PointLoad und LineLoad erben von Load", "PointLoad and LineLoad inherit from Load")
check(approx(method(p, "force"), 500) and approx(method(l, "force"), 600), "force(): 500 N bzw. 600 N", "force(): 500 N and 600 N")
check(approx(call(ns, "total_force", [p, l, call(ns, "PointLoad", 50)]), 1150), "total_force(...) = 1150 N", "total_force(...) = 1150 N")
check(approx(call(ns, "total_force", []), 0), "total_force([]) = 0", "total_force([]) = 0")
''',
   require=["abc", "class"], refs=["10.8"])

# =================================================================== Anhang A
ex(id="kA-write", ch="A", lvl=1,
   title={"de": "Messprotokoll schreiben", "en": "Writing a measurement log"},
   task={"de": "Schreiben Sie die Messreihe in die Datei `data/protokoll.txt` (Encoding `utf-8`, `with`-Anweisung). Erste Zeile: `# Zeit [min];Temperatur [°C]`, danach eine Zeile pro Messung in der Reihenfolge der Messreihe, im Format `0;21.4`.",
         "en": "Write the measurement series to the file `data/protokoll.txt` (encoding `utf-8`, `with` statement). First line: `# Zeit [min];Temperatur [°C]`, then one line per measurement in the order of the series, in the format `0;21.4`."},
   starter={"de": "times = [0, 10, 20, 30]\ntemps = [18.6, 22.4, 25.9, 27.3]\n\n# Ihr Code:\n", "en": "times = [0, 10, 20, 30]\ntemps = [18.6, 22.4, 25.9, 27.3]\n\n# your code:\n"},
   solution='times = [0, 10, 20, 30]\ntemps = [18.6, 22.4, 25.9, 27.3]\nwith open("data/protokoll.txt", "w", encoding="utf-8") as f:\n    f.write("# Zeit [min];Temperatur [°C]\\n")\n    for t, temp in zip(times, temps):\n        f.write(f"{t};{temp}\\n")\n',
   tests='''
for ti, te in [([0, 10, 20, 30], [18.6, 22.4, 25.9, 27.3]), ([1, 2], [-3.5, 0.0])]:
    ns, out = run(sub={"times": ti, "temps": te})
    try:
        content = read_file("data/protokoll.txt")
    except FileNotFoundError:
        raise TestFailure("Die Datei data/protokoll.txt wurde nicht angelegt. / The file data/protokoll.txt was not created.")
    lines = [l for l in content.split("\\n") if l.strip() != ""]
    check(lines[0].strip() == "# Zeit [min];Temperatur [°C]", "Kopfzeile ist korrekt", "Header line is correct")
    check([l.strip() for l in lines[1:]] == [f"{a};{b}" for a, b in zip(ti, te)], f"Datenzeilen für {ti} stimmen", f"Data lines for {ti} are correct")
''',
   require=["with", "open"], refs=["A.2"])

ex(id="kA-read", ch="A", lvl=2,
   title={"de": "Messdatei einlesen", "en": "Reading a measurement file"},
   task={"de": "Die Datei `data/messwerte.txt` enthält Kommentarzeilen (beginnen mit `#`), Leerzeilen und Zeilen der Form `zeit,wert`. Lesen Sie sie zeilenweise ein, überspringen Sie Kommentare und Leerzeilen, und sammeln Sie die Werte als `float` in der Liste `values`. Berechnen Sie `mean` und `peak` (Maximum).\n\nZum Ausprobieren wird beim Ausführen eine Beispieldatei angelegt.",
         "en": "The file `data/messwerte.txt` contains comment lines (starting with `#`), blank lines and lines of the form `zeit,wert` (time,value). Read it line by line, skip comments and blank lines, and collect the values as `float` in the list `values`. Compute `mean` and `peak` (maximum).\n\nFor trying it out, a sample file is created when you run your code."},
   starter={"de": "values = []\n\n# Ihr Code:\n", "en": "values = []\n\n# your code:\n"},
   solution='values = []\nwith open("data/messwerte.txt", encoding="utf-8") as f:\n    for line in f:\n        line = line.strip()\n        if line == "" or line.startswith("#"):\n            continue\n        t_str, v_str = line.split(",")\n        values.append(float(v_str))\nmean = sum(values) / len(values)\npeak = max(values)\nprint(values, mean, peak)\n',
   tests='''
f1 = "# Sensor T2\\n# zeit,wert\\n0,18.6\\n10,22.4\\n\\n20,25.9\\n30,27.3\\n"
f2 = "#x\\n1,5.0\\n2,-1.0\\n"
for content, vals in [(f1, [18.6, 22.4, 25.9, 27.3]), (f2, [5.0, -1.0])]:
    ns, out = run(files={"data/messwerte.txt": content})
    v, m, p = need(ns, "values", "mean", "peak")
    check(v == vals, f"values = {vals}", f"values = {vals}")
    check(approx(m, sum(vals) / len(vals)) and approx(p, max(vals)), "mean und peak stimmen", "mean and peak are correct")
''',
   require=["with", "file_methods"], refs=["A.3"],
   files={"data/messwerte.txt": "# Sensor T2\n# zeit,wert\n0,18.6\n10,22.4\n\n20,25.9\n30,27.3\n"})

ex(id="kA-overheat", ch="A", lvl=3,
   title={"de": "Überhitzung in CSV-Daten finden", "en": "Finding overheating in CSV data"},
   task={"de": "Lesen Sie `data/kuehlung.csv` (Spalten `zeit_s`, `temperatur_C`, `strom_A`) mit `csv.DictReader` ein. Ermitteln Sie\n- `hot_times`: die Liste der Zeitpunkte (als `int`), an denen die Temperatur über `limit` liegt\n- `first_hot`: den ersten dieser Zeitpunkte oder `None`, falls es keinen gibt\n- `max_current`: den größten Strom (als `float`)\n\nDenken Sie daran: Auch das Modul `csv` liefert nur Strings.",
         "en": "Read `data/kuehlung.csv` (columns `zeit_s`, `temperatur_C`, `strom_A`) with `csv.DictReader`. Determine\n- `hot_times`: the list of times (as `int`) at which the temperature is above `limit`\n- `first_hot`: the first of these times, or `None` if there is none\n- `max_current`: the largest current (as `float`)\n\nRemember: the module `csv` also delivers strings only."},
   starter={"de": "import csv\n\nlimit = 60.0\nhot_times = []\n\n# Ihr Code:\n", "en": "import csv\n\nlimit = 60.0\nhot_times = []\n\n# your code:\n"},
   solution='import csv\n\nlimit = 60.0\nhot_times = []\nmax_current = None\nwith open("data/kuehlung.csv", encoding="utf-8", newline="") as f:\n    for row in csv.DictReader(f):\n        t = int(row["zeit_s"])\n        temp = float(row["temperatur_C"])\n        current = float(row["strom_A"])\n        if temp > limit:\n            hot_times.append(t)\n        if max_current is None or current > max_current:\n            max_current = current\nfirst_hot = hot_times[0] if hot_times else None\nprint(hot_times, first_hot, max_current)\n',
   tests='''
F1 = "zeit_s,temperatur_C,strom_A\\n0,24.5,10.2\\n60,48.9,10.8\\n120,61.3,11.9\\n180,63.0,12.4\\n240,58.7,11.1\\n"
F2 = "zeit_s,temperatur_C,strom_A\\n0,30.0,5.5\\n10,31.0,4.0\\n"
for content, lim in [(F1, 60.0), (F2, 60.0), (F1, 50.0), (F1, 63.0)]:
    rows = [l.split(",") for l in content.strip().split("\\n")[1:]]
    eh = [int(r[0]) for r in rows if float(r[1]) > lim]
    ec = max(float(r[2]) for r in rows)
    ns, out = run(files={"data/kuehlung.csv": content}, sub={"limit": lim})
    h, f, c = need(ns, "hot_times", "first_hot", "max_current")
    check(h == eh, f"Grenze {lim} °C: hot_times = {eh}", f"limit {lim} °C: hot_times = {eh}")
    check(f == (eh[0] if eh else None), f"first_hot = {eh[0] if eh else None}", f"first_hot = {eh[0] if eh else None}")
    check(approx(c, ec), f"max_current = {ec}", f"max_current = {ec}")
''',
   require=["csv", "with"], refs=["A.4"],
   files={"data/kuehlung.csv": "zeit_s,temperatur_C,strom_A\n0,24.5,10.2\n60,48.9,10.8\n120,61.3,11.9\n180,63.0,12.4\n240,58.7,11.1\n"})

# =================================================================== Anhang B
ex(id="kB-float", ch="B", lvl=1,
   title={"de": "Sicher umwandeln", "en": "Converting safely"},
   task={"de": "Schreiben Sie `safe_float(text)`, die `text` in eine Zahl umwandelt und zurückgibt. Ein Dezimalkomma soll erlaubt sein (`\"22,8\"` → 22.8). Ist die Umwandlung nicht möglich, wird der `ValueError` abgefangen und `None` zurückgegeben.",
         "en": "Write `safe_float(text)` that converts `text` into a number and returns it. A decimal comma should be accepted (`\"22,8\"` → 22.8). If conversion is impossible, catch the `ValueError` and return `None`."},
   starter={"de": "def safe_float(text):\n    ...\n", "en": "def safe_float(text):\n    ...\n"},
   solution='def safe_float(text):\n    try:\n        return float(text.replace(",", "."))\n    except ValueError:\n        return None\n\nprint(safe_float("22,8"), safe_float("abc"))\n',
   tests='''
ns, out = run()
for t, e in [("22,8", 22.8), ("3.5", 3.5), ("-7", -7.0), ("abc", None), ("", None), ("1,2,3", None)]:
    r = call(ns, "safe_float", t)
    check((r is None and e is None) or (e is not None and approx(r, e)), f"safe_float({t!r}) = {e}", f"safe_float({t!r}) = {e}")
''',
   require=["try"], refs=["B.3"])

ex(id="kB-raise", ch="B", lvl=2,
   title={"de": "Eigene Fehler auslösen", "en": "Raising your own errors"},
   task={"de": "Schreiben Sie `wire_resistance(rho, length, area)` für den Widerstand eines Drahts $R = \\rho \\cdot l / A$. Lösen Sie aus:\n- `TypeError`, wenn eines der Argumente keine Zahl (`int` oder `float`) ist,\n- `ValueError`, wenn `length` oder `area` nicht positiv ist.\nGeben Sie den Fehlern eine aussagekräftige Meldung.",
         "en": "Write `wire_resistance(rho, length, area)` for the resistance of a wire $R = \\rho \\cdot l / A$. Raise:\n- `TypeError` if one of the arguments is not a number (`int` or `float`),\n- `ValueError` if `length` or `area` is not positive.\nGive the errors a meaningful message."},
   starter={"de": "def wire_resistance(rho, length, area):\n    ...\n", "en": "def wire_resistance(rho, length, area):\n    ...\n"},
   solution='def wire_resistance(rho, length, area):\n    for x in (rho, length, area):\n        if not isinstance(x, (int, float)):\n            raise TypeError(f"Zahl erwartet, nicht {x!r}")\n    if length <= 0 or area <= 0:\n        raise ValueError("Länge und Querschnitt müssen positiv sein.")\n    return rho * length / area\n\nprint(wire_resistance(0.0178, 10, 1.5))\n',
   tests='''
ns, out = run()
f = ns.get("wire_resistance")
if f is None:
    raise TestFailure("Es gibt keine Funktion wire_resistance. / There is no function wire_resistance.")
check(approx(call(ns, "wire_resistance", 0.0178, 10, 1.5), 0.0178 * 10 / 1.5) and approx(call(ns, "wire_resistance", 0.0178, 0.5, 0.75), 0.0178 * 0.5 / 0.75), "Kupferdraht 10 m, 1.5 mm²: R ≈ 0.119 Ω (auch 0.5 m, 0.75 mm²)", "Copper wire 10 m, 1.5 mm²: R ≈ 0.119 Ω (also 0.5 m, 0.75 mm²)")
check(raises(ValueError, lambda: f(0.0178, -10, 1.5)), "Negative Länge → ValueError", "Negative length → ValueError")
check(raises(ValueError, lambda: f(0.0178, 10, 0)) and raises(ValueError, lambda: f(0.0178, 0, 1.5)), "Querschnitt 0 bzw. Länge 0 → ValueError", "Area 0 or length 0 → ValueError")
check(raises(TypeError, lambda: f("0.0178", 10, 1.5)), "rho als String → TypeError", "rho as string → TypeError")
check(raises(TypeError, lambda: f(0.0178, [10], 1.5)), "Länge als Liste → TypeError", "Length as list → TypeError")
''',
   require=["raise"], refs=["B.4", "7.4"])

ex(id="kB-retry", ch="B", lvl=3,
   title={"de": "Robuste Eingabe", "en": "Robust input"},
   task={"de": "Fragen Sie in einer Schleife so lange nach einer ganzen Zahl zwischen 1 und 10, bis eine gültige Eingabe kommt. Bei Text (`ValueError`) geben Sie `Keine Zahl!` aus, bei Zahlen außerhalb des Bereichs `Nicht zwischen 1 und 10!`. Speichern Sie die gültige Zahl in `choice` und zählen Sie die Fehlversuche in `errors`.",
         "en": "In a loop, keep asking for an integer between 1 and 10 until a valid input arrives. For text (`ValueError`) print `Not a number!`, for numbers outside the range print `Not between 1 and 10!`. Store the valid number in `choice` and count the failed attempts in `errors`."},
   starter={"de": "errors = 0\n\n# Ihr Code:\n", "en": "errors = 0\n\n# your code:\n"},
   solution='errors = 0\nwhile True:\n    try:\n        choice = int(input("Zahl (1-10): "))\n    except ValueError:\n        print("Keine Zahl!")\n        errors += 1\n        continue\n    if 1 <= choice <= 10:\n        break\n    print("Nicht zwischen 1 und 10!")\n    errors += 1\nprint("Gewählt:", choice)\n',
   tests='''
for inp, ec, ee in [(["abc", "12", "7"], 7, 2), (["3"], 3, 0), (["", "x", "0", "11", "10"], 10, 4), (["1"], 1, 0)]:
    ns, out = run(inputs=inp)
    c, e = need(ns, "choice", "errors")
    check(c == ec, f"Eingaben {inp}: choice = {ec}", f"Inputs {inp}: choice = {ec}")
    check(e == ee, f"Eingaben {inp}: errors = {ee}", f"Inputs {inp}: errors = {ee}")
ns, out = run(inputs=["abc", "12", "7"])
o = out.lower()
check(("keine zahl" in o or "not a number" in o) and ("zwischen 1 und 10" in o or "between 1 and 10" in o), "Beide Fehlermeldungen werden ausgegeben", "Both error messages are printed")
''',
   stdin="abc\n12\n7\n", require=["try", "while"], refs=["B.3", "6.2c"])


# ------------------------------------------------------------------ Erweiterungen
import bank_k4, bank_k5, bank_k6, bank_k7, bank_k8, bank_k9, bank_k10, bank_kAB  # noqa: E402,F401
import bank2_k4, bank2_k5, bank2_k6, bank2_k7, bank2_k8, bank2_k9, bank2_k10, bank2_kAB  # noqa: E402,F401
import bank3  # noqa: E402,F401
import bank4  # noqa: E402,F401

_ORDER = ["4", "5", "6", "7", "8", "9", "10", "A", "B"]
EX.sort(key=lambda e: (_ORDER.index(e["ch"]), e["lvl"]))
