from exlib import ex

# Kapitel 5, zweiter Satz: zusätzlich type(), Casting, Listen + Methoden, Indexzugriff, is/id, None,
# bin/hex/ord/chr, int(text, basis), complex, .replace(), Modul math (floor, ceil, isclose).
# Kein if, keine Schleifen, kein abs/min/max/sum/sorted, kein Slicing.

# ------------------------------------------------------------------ Stufe 1
ex(id="k5-readings", ch="5", lvl=1,
   title={"de": "Messwerte sammeln", "en": "Collecting readings"},
   task={"de": "Ein Prüfer liest an einem Manometer nacheinander drei Drücke ab. Legen Sie die leere Liste `readings` an, lesen Sie die drei Werte mit `input()` ein (Kommazahlen mit Punkt), wandeln Sie sie in `float` um und hängen Sie sie mit `append` an. Bestimmen Sie danach\n- `n`: die Anzahl der Messwerte\n- `first` und `last`: den ersten und den letzten Wert\n- `mean`: den Mittelwert (die drei Werte per Indexzugriff addieren)",
         "en": "An inspector reads three pressures from a gauge one after the other. Create the empty list `readings`, read the three values with `input()` (decimal numbers with a dot), convert them to `float` and append them with `append`. Then determine\n- `n`: the number of readings\n- `first` and `last`: the first and the last value\n- `mean`: the mean (add the three values via indexing)"},
   starter={"de": "# Liste anlegen und drei Werte einlesen\n", "en": "# create the list and read three values\n"},
   solution='readings = []\nreadings.append(float(input("Druck 1 in bar: ")))\nreadings.append(float(input("Druck 2 in bar: ")))\nreadings.append(float(input("Druck 3 in bar: ")))\nn = len(readings)\nfirst = readings[0]\nlast = readings[-1]\nmean = (readings[0] + readings[1] + readings[2]) / 3\nprint(readings, n, first, last, round(mean, 2))\n',
   tests='''
for vals in [["4.2", "4.5", "4.1"], ["10", "12.5", "9.25"], ["0.5", "0.5", "0.5"]]:
    ns, out = run(inputs=vals)
    r, n, f, l, m = need(ns, "readings", "n", "first", "last", "mean")
    e = [float(v) for v in vals]
    check(r == e and all(isinstance(x, float) for x in r), f"readings = {e} (als float)", f"readings = {e} (as float)")
    check(n == 3 and f == e[0] and l == e[-1], "n, first und last stimmen", "n, first and last are correct")
    check(approx(m, (e[0] + e[1] + e[2]) / 3), f"Mittelwert = {(e[0] + e[1] + e[2]) / 3:.3f}", f"mean = {(e[0] + e[1] + e[2]) / 3:.3f}")
''',
   stdin="4.2\n4.5\n4.1\n", require=["cast", "list_methods"], refs=["5.3", "5.3m", "5.2e"])

ex(id="k5-register", ch="5", lvl=1,
   title={"de": "Modbus-Registeradresse", "en": "Modbus register address"},
   task={"de": "In Datenblättern von Feldgeräten stehen Registeradressen oft hexadezimal, z.B. `0x1F4`. Lesen Sie eine solche Adresse als Text ein und wandeln Sie sie mit `int(text, 16)` in die Dezimalzahl `address` um. Ein Messwert belegt zwei aufeinanderfolgende Register: Speichern Sie die Adresse des zweiten Registers dezimal in `next_address` und hexadezimal (als String) in `next_hex`. Geben Sie alle drei aus.",
         "en": "Datasheets of field devices often give register addresses in hexadecimal, e.g. `0x1F4`. Read such an address as text and convert it to the decimal number `address` with `int(text, 16)`. A measured value occupies two consecutive registers: store the address of the second register in decimal in `next_address` and in hexadecimal (as a string) in `next_hex`. Print all three."},
   starter={"de": "# Adresse einlesen (z.B. 0x1F4)\n", "en": "# read the address (e.g. 0x1F4)\n"},
   solution='text = input("Registeradresse (hex): ")\naddress = int(text, 16)\nnext_address = address + 1\nnext_hex = hex(next_address)\nprint(address, next_address, next_hex)\n',
   tests='''
for t in ["0x1F4", "0x0", "0xFFFE", "0x7d0"]:
    ns, out = run(inputs=[t])
    a, na, nh = need(ns, "address", "next_address", "next_hex")
    e = int(t, 16)
    check(a == e, f"{t} = {e}", f"{t} = {e}")
    check(na == e + 1 and nh == hex(e + 1), f"nächstes Register: {e + 1} = {hex(e + 1)}", f"next register: {e + 1} = {hex(e + 1)}")
''',
   stdin="0x1F4\n", require=["numsys", "cast"], refs=["5.5", "5.2e"])

ex(id="k5-phasor", ch="5", lvl=1,
   title={"de": "Ströme als komplexe Zahlen", "en": "Currents as complex numbers"},
   task={"de": "In einem Wechselstromknoten fließen zwei Ströme zusammen, die als komplexe Zahlen gegeben sind (Realteil + Imaginärteil·j, in A). Berechnen Sie\n- `I_total`: den Gesamtstrom I₁ + I₂\n- `U`: die Spannung an der Impedanz `Z` (Ω, ebenfalls komplex) nach dem ohmschen Gesetz U = Z · I_total\n- `kind`: den Datentyp von `U` (mit `type()`)\n\nGeben Sie `I_total` und `U` aus. Erinnerung: Die imaginäre Einheit schreibt man direkt hinter eine Zahl, z.B. `4j`.",
         "en": "Two currents meet at an AC node; they are given as complex numbers (real part + imaginary part·j, in A). Compute\n- `I_total`: the total current I₁ + I₂\n- `U`: the voltage across the impedance `Z` (Ω, also complex) according to Ohm's law U = Z · I_total\n- `kind`: the data type of `U` (using `type()`)\n\nPrint `I_total` and `U`. Reminder: the imaginary unit is written directly after a number, e.g. `4j`."},
   starter={"de": "I1 = 3 + 4j    # A\nI2 = 2 - 1j    # A\nZ = 10 + 5j    # Ohm\n\n# Ihr Code:\n", "en": "I1 = 3 + 4j    # A\nI2 = 2 - 1j    # A\nZ = 10 + 5j    # Ohm\n\n# your code:\n"},
   solution='I1 = 3 + 4j\nI2 = 2 - 1j\nZ = 10 + 5j\nI_total = I1 + I2\nU = Z * I_total\nkind = type(U)\nprint(I_total, U, kind)\n',
   tests='''
for i1, i2, z in [(3 + 4j, 2 - 1j, 10 + 5j), (1j, 1j, 2 + 0j), (-2.5 + 0.5j, 4 + 0j, 1 - 1j)]:
    ns, out = run(sub={"I1": i1, "I2": i2, "Z": z})
    it, U, k = need(ns, "I_total", "U", "kind")
    check(approx(it.real, (i1 + i2).real) and approx(it.imag, (i1 + i2).imag), f"I₁ + I₂ = {i1 + i2}", f"I₁ + I₂ = {i1 + i2}")
    eU = z * (i1 + i2)
    check(isinstance(U, complex) and approx(U.real, eU.real) and approx(U.imag, eU.imag), f"U = {eU}", f"U = {eU}")
    check(k is complex, "kind ist der Typ complex", "kind is the type complex")
''',
   require=["complex", "type"], refs=["5.1"])

ex(id="k5-sortbug", ch="5", lvl=1,
   title={"de": "Fehler finden: Messwerte weg", "en": "Find the bug: readings gone"},
   task={"de": "Der Code im Editor soll die Schwingungsmesswerte sortieren und danach den kleinsten Wert `lowest` und den größten Wert `highest` auslesen – stattdessen bricht er mit einem Fehler ab. Lesen Sie die Fehlermeldung, finden Sie die Ursache und korrigieren Sie den Code. Danach soll `values` die sortierte Liste sein.\n\nTipp: Was gibt die Methode `sort()` zurück?",
         "en": "The code in the editor is meant to sort the vibration readings and then read the smallest value `lowest` and the largest value `highest` – instead it stops with an error. Read the error message, find the cause and fix the code. Afterwards, `values` should be the sorted list.\n\nTip: what does the method `sort()` return?"},
   starter={"de": "values = [2.8, 1.4, 3.9, 0.7, 2.1]  # mm/s\nvalues = values.sort()\nlowest = values[0]\nhighest = values[-1]\nprint(values, lowest, highest)\n", "en": "values = [2.8, 1.4, 3.9, 0.7, 2.1]  # mm/s\nvalues = values.sort()\nlowest = values[0]\nhighest = values[-1]\nprint(values, lowest, highest)\n"},
   solution='values = [2.8, 1.4, 3.9, 0.7, 2.1]\nvalues.sort()\nlowest = values[0]\nhighest = values[-1]\nprint(values, lowest, highest)\n',
   tests='''
import ast as _ast
for v in [[2.8, 1.4, 3.9, 0.7, 2.1], [5.0, -1.0], [3.3]]:
    ns, out = run(sub={"values": list(v)})
    vals, lo, hi = need(ns, "values", "lowest", "highest")
    s = list(v); s.sort()
    check(vals == s, f"values ist sortiert: {s}", f"values is sorted: {s}")
    check(lo == s[0] and hi == s[-1], f"lowest = {s[0]}, highest = {s[-1]}", f"lowest = {s[0]}, highest = {s[-1]}")
check("= values.sort()" not in SOURCE.replace("  ", " "), "Das Ergebnis von sort() wird nicht mehr zugewiesen", "The result of sort() is no longer assigned")
''',
   require=["list_methods"], forbid=["seqfuncs"], refs=["5.3m"])

ex(id="k5-qualitycheck", ch="5", lvl=1,
   title={"de": "Wie viele Prüfungen bestanden?", "en": "How many checks passed?"},
   task={"de": "An einem Bauteil werden drei Merkmale geprüft:\n- Länge `length` im Bereich 99.8 bis 100.2 mm (Grenzen eingeschlossen)\n- Masse `mass` höchstens 250 g\n- Rauheit `roughness` kleiner als 1.6 µm\n\nSpeichern Sie die drei Ergebnisse als Wahrheitswerte in `c1`, `c2`, `c3`. Nutzen Sie dann **implizites Casting**: Wahrheitswerte verhalten sich beim Rechnen wie 1 und 0. Berechnen Sie damit `n_passed` (Anzahl bestandener Prüfungen) und `share` (Anteil in Prozent). Speichern Sie außerdem `all_ok`.",
         "en": "Three features of a part are checked:\n- length `length` within 99.8 to 100.2 mm (limits included)\n- mass `mass` at most 250 g\n- roughness `roughness` less than 1.6 µm\n\nStore the three results as booleans in `c1`, `c2`, `c3`. Then use **implicit casting**: booleans behave like 1 and 0 in arithmetic. Use that to compute `n_passed` (number of passed checks) and `share` (share in percent). Also store `all_ok`."},
   starter={"de": "length = 100.15    # mm\nmass = 252.0       # g\nroughness = 0.8    # µm\n\n# Ihr Code:\n", "en": "length = 100.15    # mm\nmass = 252.0       # g\nroughness = 0.8    # µm\n\n# your code:\n"},
   solution='length = 100.15\nmass = 252.0\nroughness = 0.8\nc1 = 99.8 <= length <= 100.2\nc2 = mass <= 250\nc3 = roughness < 1.6\nn_passed = c1 + c2 + c3\nshare = n_passed / 3 * 100\nall_ok = c1 and c2 and c3\nprint(n_passed, round(share, 1), all_ok)\n',
   tests='''
for L, m, r in [(100.15, 252.0, 0.8), (100.0, 250.0, 1.0), (99.7, 260.0, 2.0), (100.2, 100.0, 1.6), (100.3, 250.5, 1.5)]:
    ns, out = run(sub={"length": L, "mass": m, "roughness": r})
    c1, c2, c3, n, s, a = need(ns, "c1", "c2", "c3", "n_passed", "share", "all_ok")
    e = [99.8 <= L <= 100.2, m <= 250, r < 1.6]
    check([c1, c2, c3] == e, f"Länge {L}, Masse {m}, Rauheit {r}: {e}", f"length {L}, mass {m}, roughness {r}: {e}")
    check(n == sum(e) and approx(s, sum(e) / 3 * 100), f"n_passed = {sum(e)}, share = {sum(e) / 3 * 100:.1f} %", f"n_passed = {sum(e)}, share = {sum(e) / 3 * 100:.1f} %")
    check(a is all(e), f"all_ok = {all(e)}", f"all_ok = {all(e)}")
''',
   refs=["5.2", "4.4"])

# ------------------------------------------------------------------ Stufe 2
ex(id="k5-dip", ch="5", lvl=2,
   title={"de": "DIP-Schalter und D/A-Wandler", "en": "DIP switches and a D/A converter"},
   task={"de": "Mit acht DIP-Schaltern wird der Sollwert eines 8-Bit-D/A-Wandlers eingestellt. Lesen Sie die Schalterstellung als Text aus Nullen und Einsen ein, z.B. `10110010` (links das höchstwertige Bit). Bestimmen Sie\n- `code`: den Zahlenwert (`int(text, 2)`)\n- `code_hex`: die Hexadezimaldarstellung als String\n- `voltage`: die Ausgangsspannung bei der Referenzspannung `U_ref`: U = code / 255 · U_ref\n\nGeben Sie die Spannung mit drei Nachkommastellen aus.",
         "en": "Eight DIP switches set the value of an 8-bit D/A converter. Read the switch positions as a text of zeros and ones, e.g. `10110010` (most significant bit on the left). Determine\n- `code`: the numeric value (`int(text, 2)`)\n- `code_hex`: the hexadecimal representation as a string\n- `voltage`: the output voltage at the reference voltage `U_ref`: U = code / 255 · U_ref\n\nPrint the voltage with three decimals."},
   starter={"de": "U_ref = 5.0  # V\n\n# Schalterstellung einlesen\n", "en": "U_ref = 5.0  # V\n\n# read the switch positions\n"},
   solution='U_ref = 5.0\ntext = input("Schalterstellung (8 Bit): ")\ncode = int(text, 2)\ncode_hex = hex(code)\nvoltage = code / 255 * U_ref\nprint(f"Code {code} ({code_hex}): {voltage:.3f} V")\n',
   tests='''
for b in ["10110010", "00000000", "11111111", "00000001"]:
    ns, out = run(inputs=[b])
    c, h, u = need(ns, "code", "code_hex", "voltage")
    e = int(b, 2)
    check(c == e and h == hex(e), f"{b} = {e} = {hex(e)}", f"{b} = {e} = {hex(e)}")
    check(approx(u, e / 255 * 5.0), f"U = {e / 255 * 5.0:.3f} V", f"U = {e / 255 * 5.0:.3f} V")
    check(f"{e / 255 * 5.0:.3f}" in out, "Ausgabe mit drei Nachkommastellen", "Output with three decimals")
ns, out = run(inputs=["11111111"], sub={"U_ref": 3.3})
check(approx(ns.get("voltage"), 3.3), "Mit U_ref = 3.3 V liefert 11111111 genau 3.3 V", "With U_ref = 3.3 V, 11111111 gives exactly 3.3 V")
''',
   stdin="10110010\n", require=["numsys"], refs=["5.5", "5.5i"])

ex(id="k5-isclose", ch="5", lvl=2,
   title={"de": "Maßkette mit Gleitkommazahlen", "en": "Dimension chain with floats"},
   task={"de": "Drei Distanzscheiben mit den Dicken `t1`, `t2`, `t3` (mm) sollen zusammen genau das Sollmaß `target` ergeben. Berechnen Sie die Summe `total` und vergleichen Sie auf zwei Arten:\n- `exact`: Vergleich mit `==`\n- `close`: Vergleich mit `math.isclose`\n\nSpeichern Sie außerdem die Abweichung `diff = total - target`. Probieren Sie es mit den vorgegebenen Werten aus und erklären Sie das Ergebnis von `exact`!",
         "en": "Three spacer discs with thicknesses `t1`, `t2`, `t3` (mm) together should give exactly the target size `target`. Compute the sum `total` and compare in two ways:\n- `exact`: comparison with `==`\n- `close`: comparison with `math.isclose`\n\nAlso store the deviation `diff = total - target`. Try it with the given values and explain the result of `exact`!"},
   starter={"de": "import math\n\nt1 = 0.1\nt2 = 0.2\nt3 = 0.4\ntarget = 0.7\n\n# Ihr Code:\n", "en": "import math\n\nt1 = 0.1\nt2 = 0.2\nt3 = 0.4\ntarget = 0.7\n\n# your code:\n"},
   solution='import math\n\nt1 = 0.1\nt2 = 0.2\nt3 = 0.4\ntarget = 0.7\ntotal = t1 + t2 + t3\nexact = total == target\nclose = math.isclose(total, target)\ndiff = total - target\nprint(total, exact, close, diff)\n',
   tests='''
import math as _m
for a, b, c, t in [(0.1, 0.2, 0.4, 0.7), (0.5, 0.25, 0.25, 1.0), (1.1, 2.2, 3.3, 6.6), (0.1, 0.2, 0.3, 0.7)]:
    ns, out = run(sub={"t1": a, "t2": b, "t3": c, "target": t})
    tot, ex_, cl, d = need(ns, "total", "exact", "close", "diff")
    s = a + b + c
    check(tot == s and d == s - t, f"{a} + {b} + {c} = {s!r}", f"{a} + {b} + {c} = {s!r}")
    check(ex_ is (s == t) and cl is _m.isclose(s, t), f"exact = {s == t}, close = {_m.isclose(s, t)}", f"exact = {s == t}, close = {_m.isclose(s, t)}")
''',
   require=["import_math"], refs=["5.5f", "5.2e"])

ex(id="k5-magazine", ch="5", lvl=2,
   title={"de": "Werkzeugmagazin", "en": "Tool magazine"},
   task={"de": "Das Werkzeugmagazin einer Fräsmaschine ist eine Liste; leere Plätze sind mit `None` markiert. Die Spindel enthält das Werkzeug `spindle`.\n1. Lesen Sie den Platz `pos` (ganze Zahl, Index ab 0) des nächsten Werkzeugs ein.\n2. Entnehmen Sie es mit `pop(pos)` und speichern Sie es in `new_tool`.\n3. Das bisherige Spindelwerkzeug kommt an genau diesen Platz zurück (`insert`). Danach steckt `new_tool` in der Spindel (`spindle` neu zuweisen).\n4. Speichern Sie in `free` die Anzahl der leeren Plätze und in `pos_t5` den Platz von `'T5'`.",
         "en": "The tool magazine of a milling machine is a list; empty slots are marked with `None`. The spindle holds the tool `spindle`.\n1. Read the slot `pos` (integer, index from 0) of the next tool.\n2. Take it out with `pop(pos)` and store it in `new_tool`.\n3. The previous spindle tool goes back into exactly this slot (`insert`). Afterwards `new_tool` is in the spindle (reassign `spindle`).\n4. Store the number of empty slots in `free` and the slot of `'T5'` in `pos_t5`."},
   starter={"de": "magazine = ['T1', None, 'T3', 'T4', None, 'T5']\nspindle = 'T2'\n\n# Ihr Code:\n", "en": "magazine = ['T1', None, 'T3', 'T4', None, 'T5']\nspindle = 'T2'\n\n# your code:\n"},
   solution="magazine = ['T1', None, 'T3', 'T4', None, 'T5']\nspindle = 'T2'\npos = int(input('Platz des nächsten Werkzeugs: '))\nnew_tool = magazine.pop(pos)\nmagazine.insert(pos, spindle)\nspindle = new_tool\nfree = magazine.count(None)\npos_t5 = magazine.index('T5')\nprint(magazine, spindle, free, pos_t5)\n",
   tests='''
start = ['T1', None, 'T3', 'T4', None, 'T5']
for p in [2, 0, 3]:
    ns, out = run(inputs=[str(p)])
    m, s, nt, f, p5 = need(ns, "magazine", "spindle", "new_tool", "free", "pos_t5")
    e = list(start); ent = e.pop(p); e.insert(p, 'T2')
    check(nt == ent and s == ent, f"Platz {p}: {ent!r} wandert in die Spindel", f"slot {p}: {ent!r} goes into the spindle")
    check(m == e, f"Magazin danach: {e}", f"magazine afterwards: {e}")
    check(f == e.count(None) and p5 == e.index('T5'), f"free = {e.count(None)}, pos_t5 = {e.index('T5')}", f"free = {e.count(None)}, pos_t5 = {e.index('T5')}")
''',
   stdin="2\n", require=["list_methods", "none"], refs=["5.3m", "5.3"])

ex(id="k5-twos", ch="5", lvl=2,
   title={"de": "Zweierkomplement mit 8 Bit", "en": "Two's complement with 8 bits"},
   task={"de": "Ein Mikrocontroller speichert ganze Zahlen von −128 bis 127 als 8-Bit-Muster im Zweierkomplement. Für eine Zahl `n` aus diesem Bereich ergibt sich der gespeicherte Code (0 bis 255) aus `(n + 256) % 256` – probieren Sie nach, dass das für positive **und** negative Zahlen stimmt!\n\nLesen Sie `n` ein und bestimmen Sie\n- `code`: den gespeicherten Code\n- `bits`: dessen Binärdarstellung als String\n- `msb`: das höchstwertige Bit (0 oder 1) – es ist `code // 128`\n- `negative`: ob `msb` gleich 1 ist",
         "en": "A microcontroller stores integers from −128 to 127 as 8-bit patterns in two's complement. For a number `n` in this range, the stored code (0 to 255) is `(n + 256) % 256` – verify that this works for positive **and** negative numbers!\n\nRead `n` and determine\n- `code`: the stored code\n- `bits`: its binary representation as a string\n- `msb`: the most significant bit (0 or 1) – it is `code // 128`\n- `negative`: whether `msb` equals 1"},
   starter={"de": "# Zahl einlesen (-128 bis 127)\n", "en": "# read the number (-128 to 127)\n"},
   solution='n = int(input("Zahl (-128 bis 127): "))\ncode = (n + 256) % 256\nbits = bin(code)\nmsb = code // 128\nnegative = msb == 1\nprint(n, code, bits, msb, negative)\n',
   tests='''
for n in [-5, 5, -128, 127, 0, -1]:
    ns, out = run(inputs=[str(n)])
    c, b, m, neg = need(ns, "code", "bits", "msb", "negative")
    e = (n + 256) % 256
    check(c == e and b == bin(e), f"{n} → Code {e} = {bin(e)}", f"{n} → code {e} = {bin(e)}")
    check(m == e // 128 and neg is (n < 0), f"msb = {e // 128}, negative = {n < 0}", f"msb = {e // 128}, negative = {n < 0}")
''',
   stdin="-5\n", require=["numsys"], refs=["5.5i"])

ex(id="k5-protocol", ch="5", lvl=2,
   title={"de": "Messprotokoll als verschachtelte Liste", "en": "Measurement log as a nested list"},
   task={"de": "Ein Prüfprotokoll ist eine Liste von Einträgen; jeder Eintrag ist selbst eine Liste `[zeit_min, temperatur]`.\n1. Speichern Sie die Temperatur des zweiten Eintrags in `second_temp`.\n2. Lesen Sie eine neue Messung ein: zuerst die Zeit (ganze Zahl), dann die Temperatur (Kommazahl). Hängen Sie sie als neuen Eintrag an.\n3. Der erste Eintrag war eine Fehlmessung: Entfernen Sie ihn mit `pop(0)` und speichern Sie ihn in `removed`.\n4. Speichern Sie in `last_time` die Zeit des letzten Eintrags und in `n_entries` die Anzahl der Einträge.",
         "en": "A test log is a list of entries; each entry is itself a list `[time_min, temperature]`.\n1. Store the temperature of the second entry in `second_temp`.\n2. Read a new measurement: first the time (integer), then the temperature (decimal number). Append it as a new entry.\n3. The first entry was a faulty measurement: remove it with `pop(0)` and store it in `removed`.\n4. Store the time of the last entry in `last_time` and the number of entries in `n_entries`."},
   starter={"de": "protocol = [[0, 21.4], [5, 23.9], [10, 27.5]]\n\n# Ihr Code:\n", "en": "protocol = [[0, 21.4], [5, 23.9], [10, 27.5]]\n\n# your code:\n"},
   solution='protocol = [[0, 21.4], [5, 23.9], [10, 27.5]]\nsecond_temp = protocol[1][1]\nt = int(input("Zeit in min: "))\ntemp = float(input("Temperatur in °C: "))\nprotocol.append([t, temp])\nremoved = protocol.pop(0)\nlast_time = protocol[-1][0]\nn_entries = len(protocol)\nprint(protocol, removed, last_time, n_entries)\n',
   tests='''
for t, temp in [("15", "30.2"), ("120", "-4.5")]:
    ns, out = run(inputs=[t, temp])
    p, st, r, lt, n = need(ns, "protocol", "second_temp", "removed", "last_time", "n_entries")
    check(st == 23.9, "second_temp = 23.9", "second_temp = 23.9")
    check(p == [[5, 23.9], [10, 27.5], [int(t), float(temp)]], f"Protokoll danach: [[5, 23.9], [10, 27.5], [{int(t)}, {float(temp)}]]", f"log afterwards: [[5, 23.9], [10, 27.5], [{int(t)}, {float(temp)}]]")
    check(r == [0, 21.4] and lt == int(t) and n == 3, f"removed = [0, 21.4], last_time = {int(t)}, n_entries = 3", f"removed = [0, 21.4], last_time = {int(t)}, n_entries = 3")
ns, out = run(inputs=["7", "1.0"], sub={"protocol": [[1, 5.0], [2, 6.0]]})
check(ns.get("second_temp") == 6.0 and ns.get("n_entries") == 2 and ns.get("removed") == [1, 5.0], "Funktioniert auch mit einem anderen Protokoll", "Works with another log too")
''',
   stdin="15\n30.2\n", require=["index", "list_methods"], refs=["5.3", "5.3m"])

# ------------------------------------------------------------------ Stufe 3
ex(id="k5-utf8", ch="5", lvl=3,
   title={"de": "Wie viele Bytes braucht ein Zeichen?", "en": "How many bytes does a character need?"},
   task={"de": "In UTF-8 wird ein Zeichen je nach Codepunkt in 1 bis 4 Bytes gespeichert:\n- Codepunkt unter 0x80 (128): 1 Byte\n- ab 0x80: 2 Bytes, ab 0x800: 3 Bytes, ab 0x10000: 4 Bytes\n\nLesen Sie ein einzelnes Zeichen ein und bestimmen Sie\n- `cp`: den Codepunkt (`ord`) und `cp_hex`: dessen Hexadezimaldarstellung\n- `is_ascii`: ob das Zeichen im ASCII-Bereich liegt (Codepunkt kleiner als 128)\n- `n_bytes`: die Anzahl der UTF-8-Bytes – **ohne `if`**: Nutzen Sie, dass Vergleiche beim Rechnen als 1 bzw. 0 zählen (1 + (cp >= 0x80) + …).",
         "en": "In UTF-8, a character is stored in 1 to 4 bytes depending on its code point:\n- code point below 0x80 (128): 1 byte\n- from 0x80: 2 bytes, from 0x800: 3 bytes, from 0x10000: 4 bytes\n\nRead a single character and determine\n- `cp`: the code point (`ord`) and `cp_hex`: its hexadecimal representation\n- `is_ascii`: whether the character is in the ASCII range (code point less than 128)\n- `n_bytes`: the number of UTF-8 bytes – **without `if`**: use the fact that comparisons count as 1 or 0 in arithmetic (1 + (cp >= 0x80) + …)."},
   starter={"de": "# Zeichen einlesen\n", "en": "# read the character\n"},
   solution='c = input("Zeichen: ")\ncp = ord(c)\ncp_hex = hex(cp)\nis_ascii = cp < 128\nn_bytes = 1 + (cp >= 0x80) + (cp >= 0x800) + (cp >= 0x10000)\nprint(cp, cp_hex, is_ascii, n_bytes)\n',
   tests='''
for c in ["A", "ä", "€", "😊", "~", "ß", chr(127), chr(128), chr(2047), chr(2048), chr(65535), chr(65536)]:
    ns, out = run(inputs=[c])
    cp, h, a, n = need(ns, "cp", "cp_hex", "is_ascii", "n_bytes")
    check(cp == ord(c) and h == hex(ord(c)), f"{c!r}: Codepunkt {ord(c)} = {hex(ord(c))}", f"{c!r}: code point {ord(c)} = {hex(ord(c))}")
    check(a is (ord(c) < 128) and n == len(c.encode("utf-8")), f"{c!r}: ASCII = {ord(c) < 128}, {len(c.encode('utf-8'))} Byte(s)", f"{c!r}: ASCII = {ord(c) < 128}, {len(c.encode('utf-8'))} byte(s)")
''',
   stdin="€\n", require=["numsys"], forbid=["if"], refs=["5.5s", "5.2"])

ex(id="k5-adc", ch="5", lvl=3,
   title={"de": "Rohwert eines A/D-Wandlers", "en": "Raw value of an A/D converter"},
   task={"de": "Ein Sensor liefert über einen n-Bit-A/D-Wandler einen Rohwert, den die Diagnosesoftware hexadezimal anzeigt (z.B. `0x9C4`). Gegeben sind die Auflösung `n_bits` und die Referenzspannung `U_ref`. Bestimmen Sie\n- `max_code`: den größten darstellbaren Code 2ⁿ − 1\n- `lsb`: die Spannung eines Schritts U_ref / (2ⁿ − 1) in V\n- `raw`: den eingelesenen Rohwert als Zahl\n- `voltage`: die gemessene Spannung raw · lsb\n- `valid`: ob der Rohwert im darstellbaren Bereich liegt (0 bis max_code)\n- `percent`: die Aussteuerung in Prozent, gerundet auf eine Nachkommastelle",
         "en": "A sensor delivers a raw value through an n-bit A/D converter, which the diagnostic software shows in hexadecimal (e.g. `0x9C4`). The resolution `n_bits` and the reference voltage `U_ref` are given. Determine\n- `max_code`: the largest representable code 2ⁿ − 1\n- `lsb`: the voltage of one step U_ref / (2ⁿ − 1) in V\n- `raw`: the raw value read in, as a number\n- `voltage`: the measured voltage raw · lsb\n- `valid`: whether the raw value is within the representable range (0 to max_code)\n- `percent`: the level in percent, rounded to one decimal"},
   starter={"de": "n_bits = 12\nU_ref = 3.3  # V\n\n# Rohwert einlesen (hexadezimal)\n", "en": "n_bits = 12\nU_ref = 3.3  # V\n\n# read the raw value (hexadecimal)\n"},
   solution='n_bits = 12\nU_ref = 3.3\nmax_code = 2**n_bits - 1\nlsb = U_ref / max_code\nraw = int(input("Rohwert (hex): "), 16)\nvoltage = raw * lsb\nvalid = 0 <= raw <= max_code\npercent = round(raw / max_code * 100, 1)\nprint(f"{voltage:.4f} V, gültig: {valid}, {percent} %")\n',
   tests='''
for t, nb, ur in [("0x9C4", 12, 3.3), ("0xFFF", 12, 3.3), ("0x3FF", 10, 5.0), ("0x1000", 12, 3.3), ("0x80", 8, 2.5), ("0x0", 12, 3.3)]:
    ns, out = run(inputs=[t], sub={"n_bits": nb, "U_ref": ur})
    mc, l, r, u, v, p = need(ns, "max_code", "lsb", "raw", "voltage", "valid", "percent")
    emc = 2**nb - 1; er = int(t, 16)
    check(mc == emc and approx(l, ur / emc), f"{nb} Bit: max_code = {emc}, lsb = {ur / emc:.6f} V", f"{nb} bit: max_code = {emc}, lsb = {ur / emc:.6f} V")
    check(r == er and approx(u, er * ur / emc), f"{t} = {er} → {er * ur / emc:.4f} V", f"{t} = {er} → {er * ur / emc:.4f} V")
    check(v is (0 <= er <= emc) and approx(p, round(er / emc * 100, 1)), f"valid = {0 <= er <= emc}, {round(er / emc * 100, 1)} %", f"valid = {0 <= er <= emc}, {round(er / emc * 100, 1)} %")
''',
   stdin="0x9C4\n", require=["cast"], refs=["5.5", "5.5i", "5.2e"])

ex(id="k5-ean8", ch="5", lvl=3,
   title={"de": "EAN-8-Prüfziffer", "en": "EAN-8 check digit"},
   task={"de": "Ein EAN-8-Strichcode besteht aus 8 Ziffern; die letzte ist eine Prüfziffer. Sie berechnet sich aus den ersten sieben Ziffern d₀ … d₆: Gewichtete Summe s = 3·(d₀ + d₂ + d₄ + d₆) + (d₁ + d₃ + d₅), Prüfziffer = (10 − s % 10) % 10.\n\nLesen Sie den Code als Text ein. `list(code)` liefert die Liste der Zeichen; wandeln Sie die benötigten Zeichen per Indexzugriff mit `int()` in Ziffern um. Bestimmen Sie\n- `digits`: die Liste der 8 Zeichen\n- `weighted`: die gewichtete Summe s\n- `check_digit`: die berechnete Prüfziffer\n- `valid`: ob sie mit der letzten Ziffer des Codes übereinstimmt",
         "en": "An EAN-8 barcode consists of 8 digits; the last one is a check digit. It is computed from the first seven digits d₀ … d₆: weighted sum s = 3·(d₀ + d₂ + d₄ + d₆) + (d₁ + d₃ + d₅), check digit = (10 − s % 10) % 10.\n\nRead the code as text. `list(code)` gives the list of characters; convert the required characters into digits via indexing and `int()`. Determine\n- `digits`: the list of the 8 characters\n- `weighted`: the weighted sum s\n- `check_digit`: the computed check digit\n- `valid`: whether it matches the last digit of the code"},
   starter={"de": "# EAN-8-Code einlesen\n", "en": "# read the EAN-8 code\n"},
   solution='code = input("EAN-8: ")\ndigits = list(code)\nweighted = 3 * (int(digits[0]) + int(digits[2]) + int(digits[4]) + int(digits[6])) + int(digits[1]) + int(digits[3]) + int(digits[5])\ncheck_digit = (10 - weighted % 10) % 10\nvalid = check_digit == int(digits[7])\nprint(weighted, check_digit, valid)\n',
   tests='''
def ref(code):
    d = [int(c) for c in code]
    s = 3 * (d[0] + d[2] + d[4] + d[6]) + d[1] + d[3] + d[5]
    return s, (10 - s % 10) % 10
for c in ["96385074", "40170725", "12345670", "96385075", "00000000"]:
    ns, out = run(inputs=[c])
    dg, w, cd, v = need(ns, "digits", "weighted", "check_digit", "valid")
    es, ec = ref(c)
    check(dg == list(c), f"digits = {list(c)}", f"digits = {list(c)}")
    check(w == es and cd == ec, f"{c}: gewichtete Summe {es}, Prüfziffer {ec}", f"{c}: weighted sum {es}, check digit {ec}")
    check(v is (ec == int(c[7])), f"valid = {ec == int(c[7])}", f"valid = {ec == int(c[7])}")
''',
   stdin="96385074\n", require=["index", "cast"], forbid=["for", "while"], refs=["5.3", "5.2e"])

ex(id="k5-statusword", ch="5", lvl=3,
   title={"de": "Statuswort einer SPS auswerten", "en": "Decoding a PLC status word"},
   task={"de": "Eine SPS meldet den Zustand eines Antriebs als Statuswort, das hexadezimal angezeigt wird (z.B. `0x2D`). Jedes Bit hat eine Bedeutung:\n- Bit 0: bereit\n- Bit 2: Motor läuft\n- Bit 3: Warnung\n- Bit 5: Störung\n\nBit k einer Zahl x erhält man **ohne Bit-Operatoren** mit `(x // 2**k) % 2` – machen Sie sich klar, warum. Lesen Sie das Statuswort ein, speichern Sie es als Zahl in `status` und die Bits als Zahlen 0/1 in `ready`, `running`, `warning`, `fault`. Speichern Sie außerdem `bits` (Binärdarstellung als String) und `ok` = bereit und nicht gestört.",
         "en": "A PLC reports the state of a drive as a status word shown in hexadecimal (e.g. `0x2D`). Each bit has a meaning:\n- bit 0: ready\n- bit 2: motor running\n- bit 3: warning\n- bit 5: fault\n\nYou get bit k of a number x **without bitwise operators** via `(x // 2**k) % 2` – make sure you understand why. Read the status word, store it as a number in `status` and the bits as numbers 0/1 in `ready`, `running`, `warning`, `fault`. Also store `bits` (binary representation as a string) and `ok` = ready and not faulty."},
   starter={"de": "# Statuswort einlesen (hexadezimal)\n", "en": "# read the status word (hexadecimal)\n"},
   solution='status = int(input("Statuswort (hex): "), 16)\nbits = bin(status)\nready = (status // 2**0) % 2\nrunning = (status // 2**2) % 2\nwarning = (status // 2**3) % 2\nfault = (status // 2**5) % 2\nok = ready == 1 and fault == 0\nprint(bits, ready, running, warning, fault, ok)\n',
   tests='''
for t in ["0x2D", "0x05", "0x0", "0xFF", "0x21", "0x08", "0x61", "0x44"]:
    ns, out = run(inputs=[t])
    s, b, r, ru, w, f, ok = need(ns, "status", "bits", "ready", "running", "warning", "fault", "ok")
    x = int(t, 16); e = [(x >> k) & 1 for k in (0, 2, 3, 5)]
    check(s == x and b == bin(x), f"{t} = {x} = {bin(x)}", f"{t} = {x} = {bin(x)}")
    check([r, ru, w, f] == e, f"bereit/läuft/Warnung/Störung = {e}", f"ready/running/warning/fault = {e}")
    check(ok is (e[0] == 1 and e[3] == 0), f"ok = {e[0] == 1 and e[3] == 0}", f"ok = {e[0] == 1 and e[3] == 0}")
''',
   stdin="0x2D\n", require=["numsys"], forbid=["if", "bitops"], refs=["5.5i", "4.2"])

ex(id="k5-lowpass", ch="5", lvl=3,
   title={"de": "RC-Tiefpass", "en": "RC low-pass filter"},
   task={"de": "Ein RC-Tiefpass aus `R` (Ω) und `C` (F) dämpft hohe Frequenzen. Mit `pi = 3.14159` und Wurzeln über `** 0.5` gilt:\n- Grenzfrequenz f_g = 1 / (2π·R·C)\n- Verstärkung bei der Frequenz f: A = 1 / √(1 + (f / f_g)²)\n\nLesen Sie die Signalfrequenz `f` (Hz, Kommazahl) und die Eingangsamplitude `U_in` (V) ein. Bestimmen Sie `f_g`, `gain`, die Ausgangsamplitude `U_out` und `passband`: ob die Verstärkung mindestens 1/√2 beträgt (dann liegt f im Durchlassbereich). Geben Sie `f_g` auf eine und `U_out` auf drei Nachkommastellen aus.",
         "en": "An RC low-pass filter made of `R` (Ω) and `C` (F) attenuates high frequencies. With `pi = 3.14159` and roots via `** 0.5`:\n- cut-off frequency f_c = 1 / (2π·R·C)\n- gain at frequency f: A = 1 / √(1 + (f / f_c)²)\n\nRead the signal frequency `f` (Hz, decimal number) and the input amplitude `U_in` (V). Determine `f_g` (the cut-off frequency), `gain`, the output amplitude `U_out` and `passband`: whether the gain is at least 1/√2 (then f lies in the pass band). Print `f_g` with one and `U_out` with three decimals."},
   starter={"de": "pi = 3.14159\nR = 1000.0     # Ohm\nC = 100e-9     # F\n\n# Frequenz und Amplitude einlesen\n", "en": "pi = 3.14159\nR = 1000.0     # Ohm\nC = 100e-9     # F\n\n# read frequency and amplitude\n"},
   solution='pi = 3.14159\nR = 1000.0\nC = 100e-9\nf = float(input("Frequenz in Hz: "))\nU_in = float(input("Amplitude in V: "))\nf_g = 1 / (2 * pi * R * C)\ngain = 1 / (1 + (f / f_g)**2) ** 0.5\nU_out = gain * U_in\npassband = gain >= 1 / 2**0.5\nprint(f"f_g = {f_g:.1f} Hz, U_out = {U_out:.3f} V, Durchlassbereich: {passband}")\n',
   tests='''
P = 3.14159
for f, u, R, C in [("1000", "5", 1000.0, 100e-9), ("50000", "2.5", 1000.0, 100e-9), ("1591.55", "1", 1000.0, 100e-9), ("1860", "1", 1000.0, 100e-9), ("10", "10", 10000.0, 1e-6)]:
    ns, out = run(inputs=[f, u], sub={"R": R, "C": C})
    fg, g, uo, pb = need(ns, "f_g", "gain", "U_out", "passband")
    efg = 1 / (2 * P * R * C); eg = 1 / (1 + (float(f) / efg)**2) ** 0.5
    check(approx(fg, efg), f"R = {R:g} Ω, C = {C:g} F: f_g = {efg:.2f} Hz", f"R = {R:g} Ω, C = {C:g} F: f_g = {efg:.2f} Hz")
    check(approx(g, eg) and approx(uo, eg * float(u)), f"f = {f} Hz: A = {eg:.4f}, U_out = {eg * float(u):.3f} V", f"f = {f} Hz: A = {eg:.4f}, U_out = {eg * float(u):.3f} V")
    check(pb is (eg >= 1 / 2**0.5), f"passband = {eg >= 1 / 2**0.5}", f"passband = {eg >= 1 / 2**0.5}")
''',
   stdin="1000\n5\n", require=["cast"], refs=["5.2e", "4.2"])
