from exlib import ex

# Kapitel 6, zweiter Satz: zusätzlich if/elif/else, Conditional Expression, while, for, range,
# break/continue, abs, isdigit, random. Keine eigenen Funktionen, kein sum/min/max/sorted, kein Slicing,
# keine Dicts/Sets/Tupel-Funktionen, kein enumerate/zip.

# ------------------------------------------------------------------ Stufe 1
ex(id="k6-pallet", ch="6", lvl=1,
   title={"de": "Palette beladen", "en": "Loading a pallet"},
   task={"de": "Die Kisten aus der Liste `boxes` (Gewichte in kg) sollen auf eine Palette geladen werden. Addieren Sie die Gewichte mit einer `for`-Schleife zu `total` auf (ohne `sum()`). Die Palette trägt höchstens `max_load` kg: Speichern Sie in `overloaded`, ob sie überladen ist, und geben Sie mit `if`/`else` entweder `Überladen um 12.5 kg` oder `Noch 30.0 kg frei` aus (eine Nachkommastelle).",
         "en": "The boxes from the list `boxes` (weights in kg) are to be loaded onto a pallet. Add up the weights with a `for` loop into `total` (without `sum()`). The pallet carries at most `max_load` kg: store in `overloaded` whether it is overloaded and use `if`/`else` to print either `Overloaded by 12.5 kg` or `30.0 kg left` (one decimal)."},
   starter={"de": "boxes = [120.5, 98.0, 210.0, 156.5, 85.0]  # kg\nmax_load = 700.0\n\n# Ihr Code:\n", "en": "boxes = [120.5, 98.0, 210.0, 156.5, 85.0]  # kg\nmax_load = 700.0\n\n# your code:\n"},
   solution='boxes = [120.5, 98.0, 210.0, 156.5, 85.0]\nmax_load = 700.0\ntotal = 0\nfor b in boxes:\n    total += b\noverloaded = total > max_load\nif overloaded:\n    print(f"Überladen um {total - max_load:.1f} kg")\nelse:\n    print(f"Noch {max_load - total:.1f} kg frei")\n',
   tests='''
for b, m in [([120.5, 98.0, 210.0, 156.5, 85.0], 700.0), ([300.0, 450.0], 700.0), ([10.0], 10.0)]:
    ns, out = run(sub={"boxes": b, "max_load": m})
    t, o = need(ns, "total", "overloaded")
    e = 0
    for x in b:
        e += x
    check(approx(t, e), f"Gesamtgewicht {e:g} kg", f"total weight {e:g} kg")
    check(o is (e > m), f"overloaded = {e > m}", f"overloaded = {e > m}")
    check(f"{abs(e - m):.1f}" in out, f"Ausgabe nennt {abs(e - m):.1f} kg", f"Output states {abs(e - m):.1f} kg")
''',
   require=["for", "if"], forbid=["seqfuncs"], refs=["6.2b", "6.1a"])

ex(id="k6-switches", ch="6", lvl=1,
   title={"de": "Schaltzustände anzeigen", "en": "Showing switch states"},
   task={"de": "Die Liste `levels` enthält die Spannungen (V) an den Eingängen einer Steuerung. Ein Eingang gilt als eingeschaltet, wenn die Spannung mindestens `threshold` V beträgt. Erzeugen Sie mit einer `for`-Schleife die Liste `states` mit `'AN'` bzw. `'AUS'` für jeden Eingang – verwenden Sie dafür eine **Conditional Expression** (`… if … else …`). Zählen Sie außerdem die eingeschalteten Eingänge in `n_on` und geben Sie für jeden Eingang eine Zeile wie `Eingang 0: AN` aus.",
         "en": "The list `levels` contains the voltages (V) at the inputs of a controller. An input counts as on if the voltage is at least `threshold` V. Use a `for` loop to create the list `states` with `'AN'` (on) or `'AUS'` (off) for each input – use a **conditional expression** (`… if … else …`) for it. Also count the inputs that are on in `n_on` and print a line like `Input 0: AN` for every input."},
   starter={"de": "levels = [23.8, 0.4, 12.1, 24.2, 3.0]  # V\nthreshold = 11.0\nstates = []\n\n# Ihr Code:\n", "en": "levels = [23.8, 0.4, 12.1, 24.2, 3.0]  # V\nthreshold = 11.0\nstates = []\n\n# your code:\n"},
   solution='levels = [23.8, 0.4, 12.1, 24.2, 3.0]\nthreshold = 11.0\nstates = []\nn_on = 0\nfor i in range(len(levels)):\n    state = "AN" if levels[i] >= threshold else "AUS"\n    states.append(state)\n    if state == "AN":\n        n_on += 1\n    print(f"Eingang {i}: {state}")\n',
   tests='''
for l, t in [([23.8, 0.4, 12.1, 24.2, 3.0], 11.0), ([5.0, 5.0], 5.0), ([0.0, 1.0, 2.0], 10.0)]:
    ns, out = run(sub={"levels": l, "threshold": t})
    s, n = need(ns, "states", "n_on")
    e = ["AN" if x >= t else "AUS" for x in l]
    check(s == e, f"states = {e}", f"states = {e}")
    check(n == e.count("AN"), f"n_on = {e.count('AN')}", f"n_on = {e.count('AN')}")
    check(out.count("AN") + out.count("AUS") >= len(l), "Für jeden Eingang wird eine Zeile ausgegeben", "A line is printed for every input")
''',
   require=["ifexp", "for"], refs=["6.1b", "6.2b"])

ex(id="k6-boltcircle", ch="6", lvl=1,
   title={"de": "Lochkreis", "en": "Bolt circle"},
   task={"de": "Auf einem Flansch sollen `n` Bohrungen gleichmäßig auf einem Kreis verteilt werden. Die erste liegt bei 0°. Berechnen Sie mit einer `for`-Schleife über `range(n)` den Winkel jeder Bohrung (360° / n Abstand) und hängen Sie ihn an die Liste `angles` an. Geben Sie jede Bohrung als Zeile aus, z.B. `Bohrung 1: 0.0°` (Nummerierung ab 1, eine Nachkommastelle).",
         "en": "`n` holes are to be evenly spaced on a circle on a flange. The first one is at 0°. Use a `for` loop over `range(n)` to compute the angle of each hole (360° / n apart) and append it to the list `angles`. Print each hole as a line, e.g. `Hole 1: 0.0°` (numbering from 1, one decimal)."},
   starter={"de": "n = 6\nangles = []\n\n# Ihr Code:\n", "en": "n = 6\nangles = []\n\n# your code:\n"},
   solution='n = 6\nangles = []\nfor i in range(n):\n    angle = i * 360 / n\n    angles.append(angle)\n    print(f"Bohrung {i + 1}: {angle:.1f}°")\n',
   tests='''
for n in [6, 8, 5, 1]:
    ns, out = run(sub={"n": n})
    a = need(ns, "angles")
    e = [i * 360 / n for i in range(n)]
    check(len(a) == n and all(approx(x, y) for x, y in zip(a, e)), f"n = {n}: angles = {[round(x, 1) for x in e]}", f"n = {n}: angles = {[round(x, 1) for x in e]}")
    check(f"{n}:" in out and f"{e[-1]:.1f}" in out, "Nummerierung bis n und letzter Winkel in der Ausgabe", "Numbering up to n and the last angle in the output")
''',
   require=["for", "range"], refs=["6.2b"])

ex(id="k6-dice", ch="6", lvl=1,
   title={"de": "Würfeltest mit random", "en": "Dice test with random"},
   task={"de": "Ein Prüfstand testet einen elektronischen Würfel. Simulieren Sie ihn mit `random.randint(1, 6)`: Würfeln Sie mit einer `while`-Schleife so lange, bis eine 6 fällt. Speichern Sie die Anzahl der Würfe in `throws` und alle gewürfelten Augenzahlen der Reihe nach in der Liste `results`. Geben Sie `6 nach 4 Würfen` aus.\n\nDas Modul `random` müssen Sie zuerst importieren.",
         "en": "A test bench tests an electronic die. Simulate it with `random.randint(1, 6)`: use a `while` loop to roll until a 6 comes up. Store the number of throws in `throws` and all rolled numbers in order in the list `results`. Print `6 after 4 throws`.\n\nYou need to import the module `random` first."},
   starter={"de": "results = []\nthrows = 0\n\n# Ihr Code:\n", "en": "results = []\nthrows = 0\n\n# your code:\n"},
   solution='import random\n\nresults = []\nthrows = 0\nroll = 0\nwhile roll != 6:\n    roll = random.randint(1, 6)\n    results.append(roll)\n    throws += 1\nprint(f"6 nach {throws} Würfen")\n',
   tests='''
for seed in [1, 2, 3, 42]:
    ns, out = run(seed=seed)
    t, r = need(ns, "throws", "results")
    check(len(r) == t and t >= 1, f"Seed {seed}: throws passt zur Länge von results", f"seed {seed}: throws matches the length of results")
    check(r[-1] == 6 and 6 not in r[:-1] and all(1 <= x <= 6 for x in r), f"Seed {seed}: nur der letzte Wurf ist eine 6", f"seed {seed}: only the last throw is a 6")
    check(str(t) in out, "Die Anzahl der Würfe wird ausgegeben", "The number of throws is printed")
    import random as _r
    _r.seed(seed); er = [_r.randint(1, 6)]
    while er[-1] != 6:
        er.append(_r.randint(1, 6))
    check(r == er, f"Seed {seed}: Würfe stammen von random.randint(1, 6) (erwartet {er})", f"seed {seed}: throws come from random.randint(1, 6) (expected {er})")
''',
   require=["while", "import_random"], refs=["6.2a", "6.2c"])

ex(id="k6-inputcheck", ch="6", lvl=1,
   title={"de": "Stückzahl prüfen", "en": "Checking a quantity"},
   task={"de": "An einem Terminal wird die produzierte Stückzahl eingegeben. Lesen Sie die Eingabe als Text in `text` ein. Prüfen Sie mit `.isdigit()`, ob nur Ziffern eingegeben wurden:\n- Wenn ja: Wandeln Sie in `int` um (`count`) und geben Sie `Gebucht: 120 Stück` aus.\n- Wenn nein: Setzen Sie `count = None` und geben Sie `Ungültige Eingabe` aus.\n\nZusätzlich: Mehr als 10000 Stück pro Schicht sind unplausibel – geben Sie in diesem Fall statt „Gebucht“ die Meldung `Unplausibel` aus und setzen Sie ebenfalls `count = None`.",
         "en": "The quantity produced is entered at a terminal. Read the input as text into `text`. Use `.isdigit()` to check whether only digits were entered:\n- If so: convert to `int` (`count`) and print `Booked: 120 pieces`.\n- If not: set `count = None` and print `Invalid input`.\n\nAdditionally: more than 10000 pieces per shift are implausible – in that case print `Implausible` instead of “Booked” and also set `count = None`."},
   starter={"de": "text = input(\"Stückzahl: \")\n\n# Ihr Code:\n", "en": "text = input(\"Quantity: \")\n\n# your code:\n"},
   solution='text = input("Stückzahl: ")\nif text.isdigit():\n    count = int(text)\n    if count > 10000:\n        count = None\n        print("Unplausibel")\n    else:\n        print(f"Gebucht: {count} Stück")\nelse:\n    count = None\n    print("Ungültige Eingabe")\n',
   tests='''
for t, e in [("120", 120), ("abc", None), ("-5", None), ("12.5", None), ("10000", 10000), ("10001", None), ("", None)]:
    ns, out = run(inputs=[t])
    c = need(ns, "count")
    check(c == e and (e is None) == (c is None), f"Eingabe {t!r}: count = {e}", f"input {t!r}: count = {e}")
ns, out = run(inputs=["10001"])
o = out.lower()
check("unplausib" in o or "implausib" in o, "Für 10001 erscheint die Meldung 'Unplausibel'", "For 10001 the message 'Implausible' appears")
''',
   stdin="120\n", require=["isdigit", "if"], refs=["6.2c", "6.1b"])

# ------------------------------------------------------------------ Stufe 2
ex(id="k6-hysteresis", ch="6", lvl=2,
   title={"de": "Zweipunktregler mit Hysterese", "en": "Two-point controller with hysteresis"},
   task={"de": "Eine Heizung wird von einem Zweipunktregler mit Hysterese gesteuert: Sie schaltet **ein**, wenn die Temperatur unter `setpoint - h` fällt, und **aus**, wenn sie über `setpoint + h` steigt. Dazwischen bleibt der bisherige Zustand erhalten (sonst würde sie ständig schalten). Zu Beginn ist die Heizung aus.\n\nGehen Sie die Messwerte `temps` der Reihe nach durch, speichern Sie den Zustand nach jedem Messwert als Wahrheitswert in der Liste `heater` und zählen Sie in `switches`, wie oft geschaltet wurde (ein **und** aus).",
         "en": "A heater is controlled by a two-point controller with hysteresis: it switches **on** when the temperature falls below `setpoint - h` and **off** when it rises above `setpoint + h`. In between, the previous state is kept (otherwise it would switch constantly). At the start, the heater is off.\n\nGo through the readings `temps` in order, store the state after each reading as a boolean in the list `heater`, and count in `switches` how often it switched (on **and** off)."},
   starter={"de": "temps = [21.0, 19.4, 19.6, 20.5, 21.2, 20.8, 19.9, 19.2]\nsetpoint = 20.0\nh = 0.5\n\n# Ihr Code:\n", "en": "temps = [21.0, 19.4, 19.6, 20.5, 21.2, 20.8, 19.9, 19.2]\nsetpoint = 20.0\nh = 0.5\n\n# your code:\n"},
   solution='temps = [21.0, 19.4, 19.6, 20.5, 21.2, 20.8, 19.9, 19.2]\nsetpoint = 20.0\nh = 0.5\nheater = []\nswitches = 0\non = False\nfor t in temps:\n    if not on and t < setpoint - h:\n        on = True\n        switches += 1\n    elif on and t > setpoint + h:\n        on = False\n        switches += 1\n    heater.append(on)\nprint(heater, switches)\n',
   tests='''
def ref(ts, sp, h):
    on, out, sw = False, [], 0
    for t in ts:
        if not on and t < sp - h:
            on = True; sw += 1
        elif on and t > sp + h:
            on = False; sw += 1
        out.append(on)
    return out, sw
for ts, sp, h in [([21.0, 19.4, 19.6, 20.5, 21.2, 20.8, 19.9, 19.2], 20.0, 0.5), ([18.0, 18.0, 25.0, 15.0], 20.0, 1.0), ([20.0, 20.4, 19.6], 20.0, 0.5)]:
    ns, out = run(sub={"temps": ts, "setpoint": sp, "h": h})
    he, sw = need(ns, "heater", "switches")
    eh, es = ref(ts, sp, h)
    check(he == eh, f"Sollwert {sp} ± {h}: heater = {eh}", f"setpoint {sp} ± {h}: heater = {eh}")
    check(sw == es, f"switches = {es}", f"switches = {es}")
''',
   require=["for", "if"], refs=["6.1c", "6.2b"])

ex(id="k6-gears", ch="6", lvl=2,
   title={"de": "Jagende Verzahnung (ggT)", "en": "Hunting tooth (gcd)"},
   task={"de": "Damit sich ein Zahnradpaar gleichmäßig abnutzt, sollen sich die Zähnezahlen `z1` und `z2` möglichst nicht teilen – ideal ist ein größter gemeinsamer Teiler (ggT) von 1 („jagende Verzahnung“).\n\nBerechnen Sie den ggT mit dem euklidischen Algorithmus in einer `while`-Schleife: Solange b ≠ 0: (a, b) = (b, a % b); am Ende ist a der ggT. Speichern Sie\n- `gcd`: den ggT\n- `hunting`: ob der ggT 1 ist\n- `turns`: nach wie vielen Umdrehungen von Rad 1 derselbe Zahn wieder in dieselbe Lücke greift: kgV(z1, z2) / z1, mit kgV = z1·z2 // ggT\n\n`math.gcd` steht nicht im Skript – programmieren Sie es selbst. Die Eingaben `z1`, `z2` dürfen nicht verändert werden.",
         "en": "For a pair of gears to wear evenly, the tooth counts `z1` and `z2` should share as few factors as possible – ideally a greatest common divisor (gcd) of 1 (“hunting tooth”).\n\nCompute the gcd with the Euclidean algorithm in a `while` loop: while b ≠ 0: (a, b) = (b, a % b); at the end, a is the gcd. Store\n- `gcd`: the gcd\n- `hunting`: whether the gcd is 1\n- `turns`: after how many revolutions of gear 1 the same tooth meets the same gap again: lcm(z1, z2) / z1, with lcm = z1·z2 // gcd\n\n`math.gcd` isn't in the notes – program it yourself. The inputs `z1`, `z2` must not be changed."},
   starter={"de": "z1 = 18\nz2 = 42\n\n# Ihr Code:\n", "en": "z1 = 18\nz2 = 42\n\n# your code:\n"},
   solution='z1 = 18\nz2 = 42\na, b = z1, z2\nwhile b != 0:\n    a, b = b, a % b\ngcd = a\nhunting = gcd == 1\nlcm = z1 * z2 // gcd\nturns = lcm // z1\nprint(gcd, hunting, turns)\n',
   tests='''
import math as _m
for a, b in [(18, 42), (17, 43), (20, 20), (12, 35), (64, 24)]:
    ns, out = run(sub={"z1": a, "z2": b})
    g, h, t = need(ns, "gcd", "hunting", "turns")
    eg = _m.gcd(a, b)
    check(g == eg and h is (eg == 1), f"z1 = {a}, z2 = {b}: ggT = {eg}, jagend = {eg == 1}", f"z1 = {a}, z2 = {b}: gcd = {eg}, hunting = {eg == 1}")
    check(t == a * b // eg // a, f"turns = {a * b // eg // a}", f"turns = {a * b // eg // a}")
    check(ns["z1"] == a and ns["z2"] == b, "z1 und z2 bleiben unverändert", "z1 and z2 stay unchanged")
check("gcd(" not in SOURCE, "ggT selbst programmiert (ohne math.gcd)", "gcd programmed yourself (without math.gcd)")
''',
   require=["while"], refs=["6.2a", "4.3"])

ex(id="k6-powertable", ch="6", lvl=2,
   title={"de": "Leistungstabelle", "en": "Power table"},
   task={"de": "Für ein Datenblatt soll eine Tabelle der elektrischen Leistung P = U · I erstellt werden. Die Zeilen sind die Spannungen aus `voltages`, die Spalten die Ströme 1, 2, …, `i_max` A.\n- Erzeugen Sie mit **verschachtelten Schleifen** die verschachtelte Liste `table`: eine Zeile (Liste) pro Spannung.\n- Geben Sie jede Zeile aus, z.B. `12 V: 12 24 36 48` (Werte durch Leerzeichen getrennt; Tipp: `print(…, end=\" \")` und danach ein leeres `print()`).\n- Speichern Sie in `n_over` die Anzahl der Tabellenwerte über `p_limit` W.",
         "en": "For a datasheet, a table of the electric power P = U · I is to be created. The rows are the voltages from `voltages`, the columns the currents 1, 2, …, `i_max` A.\n- Use **nested loops** to create the nested list `table`: one row (list) per voltage.\n- Print each row, e.g. `12 V: 12 24 36 48` (values separated by spaces; tip: `print(…, end=\" \")` and then an empty `print()`).\n- Store in `n_over` the number of table values above `p_limit` W."},
   starter={"de": "voltages = [12, 24, 48]\ni_max = 4\np_limit = 100\n\n# Ihr Code:\n", "en": "voltages = [12, 24, 48]\ni_max = 4\np_limit = 100\n\n# your code:\n"},
   solution='voltages = [12, 24, 48]\ni_max = 4\np_limit = 100\ntable = []\nn_over = 0\nfor u in voltages:\n    row = []\n    print(f"{u} V:", end=" ")\n    for i in range(1, i_max + 1):\n        p = u * i\n        row.append(p)\n        print(p, end=" ")\n        if p > p_limit:\n            n_over += 1\n    print()\n    table.append(row)\n',
   tests='''
for v, im, pl in [([12, 24, 48], 4, 100), ([230], 3, 500), ([5, 10], 2, 0), ([10], 3, 20)]:
    ns, out = run(sub={"voltages": v, "i_max": im, "p_limit": pl})
    t, n = need(ns, "table", "n_over")
    e = [[u * i for i in range(1, im + 1)] for u in v]
    check(t == e, f"table = {e}", f"table = {e}")
    check(n == len([x for r in e for x in r if x > pl]), f"n_over = {len([x for r in e for x in r if x > pl])}", f"n_over = {len([x for r in e for x in r if x > pl])}")
    lines = [l for l in out.split("\\n") if l.strip()]
    check(len(lines) == len(v) and all(" ".join(str(x) for x in r) in l for r, l in zip(e, lines)), "Eine Ausgabezeile pro Spannung mit allen Werten", "One output line per voltage with all values")
''',
   require=["for", "range"], refs=["6.2d", "4.1"])

ex(id="k6-reorder", ch="6", lvl=2,
   title={"de": "Lagersimulation mit Nachbestellung", "en": "Stock simulation with reordering"},
   task={"de": "Simulieren Sie den Bestand eines Ersatzteils über mehrere Tage. Die Liste `demand` enthält den Verbrauch pro Tag. Startbestand ist `stock`.\n- Jeden Tag wird zuerst der Verbrauch abgezogen. Reicht der Bestand nicht, wird nur abgegeben, was da ist, und die Fehlmenge in `missing` aufaddiert.\n- Fällt der Bestand danach unter den Meldebestand `reorder_point`, wird `order_qty` nachbestellt; die Lieferung ist sofort am Ende des Tages da. Merken Sie sich den Tagesindex (ab 0) jeder Bestellung in der Liste `order_days`.\n- Speichern Sie den Bestand am Ende jedes Tages in `history`.",
         "en": "Simulate the stock of a spare part over several days. The list `demand` contains the consumption per day. The initial stock is `stock`.\n- Each day, the consumption is subtracted first. If the stock isn't enough, only what's there is handed out and the shortfall is added up in `missing`.\n- If the stock then falls below the reorder point `reorder_point`, `order_qty` is reordered; the delivery arrives immediately at the end of the day. Remember the day index (from 0) of every order in the list `order_days`.\n- Store the stock at the end of each day in `history`."},
   starter={"de": "demand = [12, 30, 8, 25, 40, 5, 18]\nstock = 50\nreorder_point = 20\norder_qty = 40\n\n# Ihr Code:\n", "en": "demand = [12, 30, 8, 25, 40, 5, 18]\nstock = 50\nreorder_point = 20\norder_qty = 40\n\n# your code:\n"},
   solution='demand = [12, 30, 8, 25, 40, 5, 18]\nstock = 50\nreorder_point = 20\norder_qty = 40\nmissing = 0\norder_days = []\nhistory = []\nfor day in range(len(demand)):\n    d = demand[day]\n    if d > stock:\n        missing += d - stock\n        stock = 0\n    else:\n        stock -= d\n    if stock < reorder_point:\n        stock += order_qty\n        order_days.append(day)\n    history.append(stock)\nprint(history, order_days, missing)\n',
   tests='''
def ref(dem, st, rp, oq):
    miss, od, hist = 0, [], []
    for day, d in enumerate(dem):
        if d > st:
            miss += d - st; st = 0
        else:
            st -= d
        if st < rp:
            st += oq; od.append(day)
        hist.append(st)
    return hist, od, miss
for dem, st, rp, oq in [([12, 30, 8, 25, 40, 5, 18], 50, 20, 40), ([100, 5], 30, 10, 20), ([1, 1, 1], 10, 0, 5), ([10, 10], 30, 20, 5)]:
    ns, out = run(sub={"demand": dem, "stock": st, "reorder_point": rp, "order_qty": oq})
    h, o, m = need(ns, "history", "order_days", "missing")
    eh, eo, em = ref(dem, st, rp, oq)
    check(h == eh, f"history = {eh}", f"history = {eh}")
    check(o == eo and m == em, f"order_days = {eo}, missing = {em}", f"order_days = {eo}, missing = {em}")
''',
   require=["for", "if"], refs=["6.2b", "6.1b"])

ex(id="k6-tobinary", ch="6", lvl=2,
   title={"de": "Dezimal nach binär – selbst gerechnet", "en": "Decimal to binary – done by hand"},
   task={"de": "Im Kapitel *Datentypen* wurde das Verfahren beschrieben, mit dem man eine Dezimalzahl ins Binärsystem umrechnet: wiederholt durch 2 teilen, die Reste von unten nach oben lesen. Setzen Sie es mit einer `while`-Schleife um:\n- Lesen Sie eine ganze Zahl `n` ≥ 0 ein.\n- Bauen Sie den String `bits` aus den Resten auf (neue Reste kommen **vorne** dazu: `str(rest) + bits`).\n- Für n = 0 soll `bits` den Wert `\"0\"` haben.\n- Speichern Sie in `steps` die Anzahl der Divisionen und in `matches`, ob `\"0b\" + bits` mit `bin(n)` übereinstimmt.",
         "en": "The chapter *data types* described how to convert a decimal number to binary: divide by 2 repeatedly and read the remainders from bottom to top. Implement it with a `while` loop:\n- Read an integer `n` ≥ 0.\n- Build the string `bits` from the remainders (new remainders go to the **front**: `str(remainder) + bits`).\n- For n = 0, `bits` should be `\"0\"`.\n- Store the number of divisions in `steps` and in `matches` whether `\"0b\" + bits` equals `bin(n)`."},
   starter={"de": "n = int(input(\"n = \"))\nbits = \"\"\n\n# Ihr Code:\n", "en": "n = int(input(\"n = \"))\nbits = \"\"\n\n# your code:\n"},
   solution='n = int(input("n = "))\nbits = ""\nsteps = 0\nx = n\nwhile x > 0:\n    bits = str(x % 2) + bits\n    x = x // 2\n    steps += 1\nif bits == "":\n    bits = "0"\nmatches = "0b" + bits == bin(n)\nprint(bits, steps, matches)\n',
   tests='''
for n in [13, 0, 1, 255, 1000, 2**20]:
    ns, out = run(inputs=[str(n)])
    b, s, m = need(ns, "bits", "steps", "matches")
    check(b == bin(n)[2:], f"{n} = {bin(n)[2:]} (binär)", f"{n} = {bin(n)[2:]} (binary)")
    check(s == len(bin(n)[2:]) - (n == 0) and m is True, f"{n}: {len(bin(n)[2:]) - (n == 0)} Divisionen, matches = True", f"{n}: {len(bin(n)[2:]) - (n == 0)} divisions, matches = True")
check("bin(n)[" not in SOURCE, "Ohne Abschneiden von bin(n) gelöst", "Solved without cutting up bin(n)")
''',
   stdin="13\n", require=["while"], refs=["6.2a", "5.5"])

# ------------------------------------------------------------------ Stufe 3
ex(id="k6-bubblesort", ch="6", lvl=3,
   title={"de": "Sortieren ohne sort()", "en": "Sorting without sort()"},
   task={"de": "Sortieren Sie die Liste `values` aufsteigend mit dem **Bubble-Sort**-Verfahren – ohne `sort()` und `sorted()`: Gehen Sie die Liste immer wieder durch und vertauschen Sie benachbarte Elemente, die in der falschen Reihenfolge stehen (Tausch mit Mehrfachzuweisung: `a[j], a[j + 1] = a[j + 1], a[j]`). Wenn bei einem Durchlauf nichts mehr vertauscht wurde, ist die Liste sortiert – brechen Sie dann ab.\n\nSortieren Sie `values` direkt (in-place), zählen Sie die Vertauschungen in `swaps` und die Durchläufe in `passes`.",
         "en": "Sort the list `values` in ascending order with **bubble sort** – without `sort()` and `sorted()`: go through the list again and again and swap neighbouring elements that are in the wrong order (swap with multiple assignment: `a[j], a[j + 1] = a[j + 1], a[j]`). If nothing was swapped in a pass, the list is sorted – stop then.\n\nSort `values` directly (in place), count the swaps in `swaps` and the passes in `passes`."},
   starter={"de": "values = [5.2, 1.8, 4.4, 9.1, 0.3, 4.4]\n\n# Ihr Code:\n", "en": "values = [5.2, 1.8, 4.4, 9.1, 0.3, 4.4]\n\n# your code:\n"},
   solution='values = [5.2, 1.8, 4.4, 9.1, 0.3, 4.4]\nswaps = 0\npasses = 0\nswapped = True\nwhile swapped:\n    swapped = False\n    passes += 1\n    for j in range(len(values) - 1):\n        if values[j] > values[j + 1]:\n            values[j], values[j + 1] = values[j + 1], values[j]\n            swaps += 1\n            swapped = True\nprint(values, swaps, passes)\n',
   tests='''
def inversions(v):
    return len([1 for i in range(len(v)) for j in range(i + 1, len(v)) if v[i] > v[j]])
for v in [[5.2, 1.8, 4.4, 9.1, 0.3, 4.4], [1, 2, 3], [3, 2, 1], [7]]:
    ns, out = run(sub={"values": list(v)})
    vals, s, p = need(ns, "values", "swaps")+[ns.get("passes")]
    check(vals == sorted(v), f"{v} → {sorted(v)}", f"{v} → {sorted(v)}")
    check(s == inversions(v), f"Anzahl Vertauschungen = {inversions(v)}", f"number of swaps = {inversions(v)}")
    check(isinstance(p, int) and 1 <= p <= len(v), "passes ist plausibel (mindestens 1, höchstens Länge der Liste)", "passes is plausible (at least 1, at most the list length)")
check("sort(" not in SOURCE and "sorted(" not in SOURCE, "Ohne sort() und sorted() gelöst", "Solved without sort() and sorted()")
''',
   require=["while", "for", "assign_multi"], refs=["6.2d", "6.2a", "4.3"])

ex(id="k6-euler", ch="6", lvl=3,
   title={"de": "Kondensator laden (Euler-Verfahren)", "en": "Charging a capacitor (Euler method)"},
   task={"de": "Ein Kondensator C wird über einen Widerstand R an die Spannung `U0` gelegt. Für die Kondensatorspannung gilt dU/dt = (U0 − U) / (R·C). Lösen Sie die Gleichung numerisch mit dem **Euler-Verfahren**: Ausgehend von U = 0 und t = 0 wird in jedem Zeitschritt `dt`\n\n  U = U + dt · (U0 − U) / (R·C)  und  t = t + dt\n\nberechnet. Wiederholen Sie das in einer `while`-Schleife, bis U mindestens 63.2 % von U0 erreicht hat. Speichern Sie die Zeit in `t63` (in s) und die Anzahl der Schritte in `steps`. Die Theorie sagt: t₆₃ ≈ R·C. Speichern Sie die relative Abweichung |t63 − R·C| / (R·C) in Prozent in `error_percent`. Probieren Sie anschließend kleinere Werte für `dt` aus – was beobachten Sie?",
         "en": "A capacitor C is connected to the voltage `U0` through a resistor R. For the capacitor voltage, dU/dt = (U0 − U) / (R·C). Solve the equation numerically with the **Euler method**: starting with U = 0 and t = 0, in every time step `dt`\n\n  U = U + dt · (U0 − U) / (R·C)  and  t = t + dt\n\nare computed. Repeat this in a `while` loop until U has reached at least 63.2 % of U0. Store the time in `t63` (in s) and the number of steps in `steps`. Theory says: t₆₃ ≈ R·C. Store the relative deviation |t63 − R·C| / (R·C) in percent in `error_percent`. Afterwards, try smaller values for `dt` – what do you observe?"},
   starter={"de": "U0 = 12.0     # V\nR = 10e3      # Ohm\nC = 100e-6    # F\ndt = 0.03     # s\n\n# Ihr Code:\n", "en": "U0 = 12.0     # V\nR = 10e3      # Ohm\nC = 100e-6    # F\ndt = 0.03     # s\n\n# your code:\n"},
   solution='U0 = 12.0\nR = 10e3\nC = 100e-6\ndt = 0.03\nU = 0.0\nt = 0.0\nsteps = 0\nwhile U < 0.632 * U0:\n    U = U + dt * (U0 - U) / (R * C)\n    t = t + dt\n    steps += 1\nt63 = t\nerror_percent = abs(t63 - R * C) / (R * C) * 100\nprint(f"t63 = {t63:.3f} s nach {steps} Schritten, Abweichung {error_percent:.2f} %")\n',
   tests='''
def ref(U0, R, C, dt):
    U = t = 0.0; n = 0
    while U < 0.632 * U0:
        U = U + dt * (U0 - U) / (R * C); t = t + dt; n += 1
    return t, n
for U0, R, C, dt in [(12.0, 10e3, 100e-6, 0.03), (5.0, 1e3, 1e-3, 0.07), (230.0, 4.7e3, 10e-6, 0.004), (12.0, 10e3, 100e-6, 0.01)]:
    ns, out = run(sub={"U0": U0, "R": R, "C": C, "dt": dt})
    t, n, e = need(ns, "t63", "steps", "error_percent")
    et, en = ref(U0, R, C, dt)
    check(approx(t, et) and n == en, f"R·C = {R * C:g} s, dt = {dt}: t63 = {et:.4f} s nach {en} Schritten", f"R·C = {R * C:g} s, dt = {dt}: t63 = {et:.4f} s after {en} steps")
    check(approx(e, abs(et - R * C) / (R * C) * 100), f"Abweichung {abs(et - R * C) / (R * C) * 100:.2f} %", f"deviation {abs(et - R * C) / (R * C) * 100:.2f} %")
''',
   require=["while", "abs"], refs=["6.2a", "6.3a"])

ex(id="k6-runs", ch="6", lvl=3,
   title={"de": "Laufzeiten einer Maschine", "en": "Run times of a machine"},
   task={"de": "Eine Maschine meldet jede Minute ihren Zustand: 1 = läuft, 0 = steht. Werten Sie die Liste `log` aus:\n- `starts`: wie oft die Maschine **angelaufen** ist (Wechsel von 0 auf 1; läuft sie schon in der ersten Minute, zählt das als Start)\n- `longest_run`: die längste ununterbrochene Laufzeit in Minuten\n- `runtime_percent`: der Anteil der Minuten, in denen sie lief, in Prozent (eine Nachkommastelle)\n\nVerwenden Sie eine Schleife und merken Sie sich den vorherigen Zustand und die Länge des aktuellen Laufs.",
         "en": "A machine reports its state every minute: 1 = running, 0 = stopped. Evaluate the list `log`:\n- `starts`: how often the machine **started** (change from 0 to 1; if it is already running in the first minute, that counts as a start)\n- `longest_run`: the longest uninterrupted run time in minutes\n- `runtime_percent`: the share of minutes in which it ran, in percent (one decimal)\n\nUse a loop and remember the previous state and the length of the current run."},
   starter={"de": "log = [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0]\n\n# Ihr Code:\n", "en": "log = [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0]\n\n# your code:\n"},
   solution='log = [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0]\nstarts = 0\nlongest_run = 0\ncurrent = 0\nprevious = 0\nminutes_on = 0\nfor state in log:\n    if state == 1:\n        minutes_on += 1\n        current += 1\n        if previous == 0:\n            starts += 1\n        if current > longest_run:\n            longest_run = current\n    else:\n        current = 0\n    previous = state\nruntime_percent = round(minutes_on / len(log) * 100, 1)\nprint(starts, longest_run, runtime_percent)\n',
   tests='''
def ref(log):
    starts = longest = cur = prev = on = 0
    for s in log:
        if s == 1:
            on += 1; cur += 1
            if prev == 0: starts += 1
            longest = longest if longest > cur else cur
        else:
            cur = 0
        prev = s
    return starts, longest, round(on / len(log) * 100, 1)
for lg in [[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0], [1, 1, 0, 1], [0, 0, 0], [1, 1, 1, 1, 1]]:
    ns, out = run(sub={"log": lg})
    s, l, r = need(ns, "starts", "longest_run", "runtime_percent")
    es, el, er = ref(lg)
    check(s == es, f"{lg}: starts = {es}", f"{lg}: starts = {es}")
    check(l == el and approx(r, er), f"longest_run = {el}, runtime_percent = {er}", f"longest_run = {el}, runtime_percent = {er}")
''',
   require=["for", "if"], forbid=["seqfuncs"], refs=["6.2b", "6.1b"])

ex(id="k6-movingavg", ch="6", lvl=3,
   title={"de": "Gleitender Mittelwert", "en": "Moving average"},
   task={"de": "Ein verrauschtes Drucksignal `signal` soll geglättet werden. Der gleitende Mittelwert mit der Fensterbreite `k` ist an der Position i der Mittelwert der Werte i, i+1, …, i+k−1. Es gibt also len(signal) − k + 1 solche Mittelwerte.\n\nBerechnen Sie die Liste `smooth` mit **verschachtelten Schleifen** (die innere Schleife summiert das Fenster; Slicing und `sum()` kommen erst später). Runden Sie jeden Mittelwert auf zwei Nachkommastellen. Speichern Sie außerdem in `max_jump` die größte Änderung zwischen zwei **aufeinanderfolgenden** geglätteten Werten (Betrag). Ist `k` größer als die Signallänge, ist `smooth` leer und `max_jump` gleich 0.",
         "en": "A noisy pressure signal `signal` is to be smoothed. The moving average with window width `k` at position i is the mean of the values i, i+1, …, i+k−1. So there are len(signal) − k + 1 such means.\n\nCompute the list `smooth` with **nested loops** (the inner loop sums the window; slicing and `sum()` come later). Round each mean to two decimals. Also store in `max_jump` the largest change between two **consecutive** smoothed values (magnitude). If `k` is greater than the signal length, `smooth` is empty and `max_jump` is 0."},
   starter={"de": "signal = [2.1, 2.5, 1.9, 2.8, 3.6, 3.1, 3.9, 4.4]\nk = 3\n\n# Ihr Code:\n", "en": "signal = [2.1, 2.5, 1.9, 2.8, 3.6, 3.1, 3.9, 4.4]\nk = 3\n\n# your code:\n"},
   solution='signal = [2.1, 2.5, 1.9, 2.8, 3.6, 3.1, 3.9, 4.4]\nk = 3\nsmooth = []\nfor i in range(len(signal) - k + 1):\n    window = 0\n    for j in range(i, i + k):\n        window += signal[j]\n    smooth.append(round(window / k, 2))\nmax_jump = 0\nfor i in range(len(smooth) - 1):\n    jump = abs(smooth[i + 1] - smooth[i])\n    if jump > max_jump:\n        max_jump = jump\nprint(smooth, round(max_jump, 2))\n',
   tests='''
def ref(s, k):
    sm = [round(sum(s[i:i + k]) / k, 2) for i in range(len(s) - k + 1)]
    mj = 0
    for i in range(len(sm) - 1):
        mj = max(mj, abs(sm[i + 1] - sm[i]))
    return sm, mj
for s, k in [([2.1, 2.5, 1.9, 2.8, 3.6, 3.1, 3.9, 4.4], 3), ([1.0, 2.0, 3.0, 4.0], 2), ([5.0, 5.0], 5), ([7.0, 1.0, 7.0], 1), ([1.0, 1.0, 1.0, 5.0], 1)]:
    ns, out = run(sub={"signal": s, "k": k})
    sm, mj = need(ns, "smooth", "max_jump")
    esm, emj = ref(s, k)
    check(len(sm) == len(esm) and all(approx(a, b) for a, b in zip(sm, esm)), f"k = {k}: smooth = {esm}", f"k = {k}: smooth = {esm}")
    check(approx(mj, emj), f"max_jump = {emj:.2f}", f"max_jump = {emj:.2f}")
''',
   require=["for"], forbid=["seqfuncs", "slice"], refs=["6.2d", "6.2b"])

ex(id="k6-binsearch", ch="6", lvl=3,
   title={"de": "Sollwert per Intervallhalbierung finden", "en": "Finding a setpoint by halving the interval"},
   task={"de": "Bei der Inbetriebnahme sucht ein Techniker den Drehzahlsollwert (ganze Zahl von 0 bis 100 %), bei dem eine Pumpe genau den geforderten Druck liefert. Simuliert wird das mit einer geheimen Zahl `secret`, die eingelesen wird. Das Programm „rät“ immer die Mitte des noch möglichen Bereichs: guess = (low + high) // 2. Ist der Rateversuch zu klein, wird `low = guess + 1`, ist er zu groß, `high = guess - 1`.\n\nSpeichern Sie alle Rateversuche der Reihe nach in der Liste `guesses` und brechen Sie die `while`-Schleife ab, sobald `secret` getroffen ist (`break`). Speichern Sie in `tries` die Anzahl der Versuche. Bei 101 möglichen Werten sollten nie mehr als 7 Versuche nötig sein – warum?",
         "en": "During commissioning, a technician looks for the speed setpoint (integer from 0 to 100 %) at which a pump delivers exactly the required pressure. This is simulated with a secret number `secret` that is read in. The program always “guesses” the middle of the remaining range: guess = (low + high) // 2. If the guess is too small, `low = guess + 1`; if it is too large, `high = guess - 1`.\n\nStore all guesses in order in the list `guesses` and leave the `while` loop as soon as `secret` is hit (`break`). Store the number of tries in `tries`. With 101 possible values, never more than 7 tries should be needed – why?"},
   starter={"de": "secret = int(input(\"Geheimer Sollwert (0-100): \"))\nlow = 0\nhigh = 100\nguesses = []\n\n# Ihr Code:\n", "en": "secret = int(input(\"Secret setpoint (0-100): \"))\nlow = 0\nhigh = 100\nguesses = []\n\n# your code:\n"},
   solution='secret = int(input("Geheimer Sollwert (0-100): "))\nlow = 0\nhigh = 100\nguesses = []\nwhile low <= high:\n    guess = (low + high) // 2\n    guesses.append(guess)\n    if guess == secret:\n        break\n    elif guess < secret:\n        low = guess + 1\n    else:\n        high = guess - 1\ntries = len(guesses)\nprint(guesses, tries)\n',
   tests='''
def ref(s):
    lo, hi, g = 0, 100, []
    while lo <= hi:
        m = (lo + hi) // 2; g.append(m)
        if m == s: break
        if m < s: lo = m + 1
        else: hi = m - 1
    return g
worst = 0
for s in [37, 50, 0, 100, 1, 99, 63]:
    ns, out = run(inputs=[str(s)])
    g, t = need(ns, "guesses", "tries")
    e = ref(s)
    check(g == e and t == len(e), f"secret = {s}: Versuche {e}", f"secret = {s}: guesses {e}")
    worst = max(worst, t if isinstance(t, int) else 99)
check(worst <= 7, "Nie mehr als 7 Versuche", "Never more than 7 tries")
''',
   stdin="37\n", require=["while", "break"], refs=["6.2c", "6.2a"])
