from exlib import ex

# Kapitel 5: zusätzlich type(), Casting, Listen + Methoden, Indexzugriff, is/id, None, bin/hex/ord/chr,
# complex, .replace(), Modul math. Kein if, keine Schleifen, kein abs/min/max/sum/sorted, kein Slicing.

ex(id="k5-cells", ch="5", lvl=1,
   title={"de": "Batteriepack", "en": "Battery pack"},
   task={"de": "Lesen Sie mit `input()` die Spannung einer Zelle in V (Kommazahl) und die Anzahl der in Reihe geschalteten Zellen (ganze Zahl) ein. Berechnen Sie die Gesamtspannung `u_total`. Bauen Sie den Text `text = \"Gesamtspannung: \" + ... + \" V\"` mit `str()` zusammen (kein f-String!) und geben Sie ihn aus.",
         "en": "Use `input()` to read the voltage of one cell in V (decimal number) and the number of cells connected in series (integer). Compute the total voltage `u_total`. Build the text `text = \"Total voltage: \" + ... + \" V\"` using `str()` (no f-string!) and print it."},
   starter={"de": "# Zellspannung und Anzahl einlesen\n", "en": "# read cell voltage and count\n"},
   solution='u_cell = float(input("Zellspannung in V: "))\nn = int(input("Anzahl Zellen: "))\nu_total = u_cell * n\ntext = "Gesamtspannung: " + str(u_total) + " V"\nprint(text)\n',
   tests='''
for u, n in [("3.7", "4"), ("1.2", "10"), ("3.2", "16")]:
    ns, out = run(inputs=[u, n])
    ut, tx = need(ns, "u_total", "text")
    e = float(u) * int(n)
    check(approx(ut, e), f"{n} Zellen à {u} V ergeben {e:g} V", f"{n} cells of {u} V give {e:g} V")
    check(isinstance(tx, str) and str(ut) in tx and tx.strip().endswith("V"), "text enthält die Gesamtspannung und endet mit 'V'", "text contains the total voltage and ends with 'V'")
''',
   stdin="3.7\n4\n", require=["cast"], forbid=["fstring"], refs=["5.2e", "4.3e"])

ex(id="k5-index", ch="5", lvl=1,
   title={"de": "Indexzugriff auf Messwerte", "en": "Indexing measurements"},
   task={"de": "Aus der Messreihe `values` sollen Sie nur per Indexzugriff ermitteln:\n- `first`: den ersten Wert\n- `last`: den letzten Wert (negativer Index)\n- `second_last`: den vorletzten Wert\n- `n`: die Anzahl der Werte\n- `middle`: den Wert in der Mitte, also beim Index `n // 2`",
         "en": "From the series `values`, determine using indexing only:\n- `first`: the first value\n- `last`: the last value (negative index)\n- `second_last`: the second-to-last value\n- `n`: the number of values\n- `middle`: the value in the middle, i.e. at index `n // 2`"},
   starter={"de": "values = [12.1, 12.4, 13.0, 12.8, 12.9, 13.3, 13.1]\n\n# Ihr Code:\n", "en": "values = [12.1, 12.4, 13.0, 12.8, 12.9, 13.3, 13.1]\n\n# your code:\n"},
   solution='values = [12.1, 12.4, 13.0, 12.8, 12.9, 13.3, 13.1]\nfirst = values[0]\nlast = values[-1]\nsecond_last = values[-2]\nn = len(values)\nmiddle = values[n // 2]\nprint(first, last, second_last, n, middle)\n',
   tests='''
for v in [[12.1, 12.4, 13.0, 12.8, 12.9, 13.3, 13.1], [1, 2, 3, 4], [5.5, 6.6]]:
    ns, out = run(sub={"values": v})
    f, l, s, n, m = need(ns, "first", "last", "second_last", "n", "middle")
    check((f, l, s) == (v[0], v[-1], v[-2]), f"first/last/second_last für {v}", f"first/last/second_last for {v}")
    check(n == len(v) and m == v[len(v) // 2], f"n = {len(v)}, middle = {v[len(v)//2]}", f"n = {len(v)}, middle = {v[len(v)//2]}")
''',
   require=["index"], refs=["5.3"])

ex(id="k5-rounding", ch="5", lvl=1,
   title={"de": "Rohre bestellen", "en": "Ordering pipes"},
   task={"de": "Für eine Leitung werden `needed` Meter Rohr benötigt (Eingabe, Kommazahl mit Punkt). Rohre gibt es nur in Stangen zu 6 m. Importieren Sie das Modul `math` und berechnen Sie\n- `full_bars`: wie viele ganze Stangen vollständig verbraucht werden (`math.floor`)\n- `bars_to_buy`: wie viele Stangen gekauft werden müssen (`math.ceil`)\n- `leftover`: wie viele Meter übrig bleiben, auf zwei Stellen gerundet (`round`)\n- `exact`: ob die Länge genau ein Vielfaches von 6 m ist – vergleichen Sie `needed / 6` und `full_bars` mit `math.isclose` statt mit `==`.",
         "en": "A pipeline needs `needed` metres of pipe (input, decimal number with a dot). Pipes only come in 6 m bars. Import the module `math` and compute\n- `full_bars`: how many whole bars are used up completely (`math.floor`)\n- `bars_to_buy`: how many bars must be bought (`math.ceil`)\n- `leftover`: how many metres are left over, rounded to two decimals (`round`)\n- `exact`: whether the length is an exact multiple of 6 m – compare `needed / 6` and `full_bars` with `math.isclose` instead of `==`."},
   starter={"de": "import math\n\n# Ihr Code:\n", "en": "import math\n\n# your code:\n"},
   solution='import math\n\nneeded = float(input("Benötigte Länge in m: "))\nfull_bars = math.floor(needed / 6)\nbars_to_buy = math.ceil(needed / 6)\nleftover = round(bars_to_buy * 6 - needed, 2)\nexact = math.isclose(needed / 6, full_bars)\nprint(full_bars, bars_to_buy, leftover, exact)\n',
   tests="""
import math as _m
for t in ["17.4", "18", "2.5", "36.0", "40"]:
    ns, out = run(inputs=[t])
    fb, bb, lo, ex_ = need(ns, "full_bars", "bars_to_buy", "leftover", "exact")
    x = float(t)
    check(fb == _m.floor(x / 6) and bb == _m.ceil(x / 6), f"{t} m: {_m.floor(x/6)} ganze Stangen, {_m.ceil(x/6)} kaufen", f"{t} m: {_m.floor(x/6)} whole bars, buy {_m.ceil(x/6)}")
    check(approx(lo, round(_m.ceil(x / 6) * 6 - x, 2)), f"Rest = {round(_m.ceil(x/6)*6 - x, 2)} m", f"leftover = {round(_m.ceil(x/6)*6 - x, 2)} m")
    check(ex_ is _m.isclose(x / 6, _m.floor(x / 6)), f"exact = {_m.isclose(x/6, _m.floor(x/6))}", f"exact = {_m.isclose(x/6, _m.floor(x/6))}")
""",
   stdin="17.4\n", require=["import_math"], refs=["5.2e", "5.5f"])

ex(id="k5-rl", ch="5", lvl=2,
   title={"de": "Impedanz einer Spule", "en": "Impedance of a coil"},
   task={"de": "Eine reale Spule hat den Widerstand `R` (Ω) und die Induktivität `L` (H). Bei der Frequenz `f` (Hz) gilt Z = R + j·X_L mit dem Blindwiderstand X_L = ω·L und ω = 2π·f (`pi = 3.14159` ist vorgegeben). Berechnen Sie\n- `X_L`: den Blindwiderstand in Ω\n- `Z` als komplexe Zahl (`1j` verwenden)\n- `Z_abs`: den Betrag √(R² + X_L²)\n- `I`: den Strom bei der Spannung `U` als komplexe Zahl (I = U / Z)\n- `I_abs`: den Betrag des Stroms, U / |Z|\n\n`abs()` lernen wir erst in Kapitel 6 kennen.",
         "en": "A real coil has resistance `R` (Ω) and inductance `L` (H). At frequency `f` (Hz), Z = R + j·X_L with the reactance X_L = ω·L and ω = 2π·f (`pi = 3.14159` is given). Compute\n- `X_L`: the reactance in Ω\n- `Z` as a complex number (use `1j`)\n- `Z_abs`: the magnitude √(R² + X_L²)\n- `I`: the current at voltage `U` as a complex number (I = U / Z)\n- `I_abs`: the magnitude of the current, U / |Z|\n\n`abs()` only comes in chapter 6."},
   starter={"de": "pi = 3.14159\nR = 12.0     # Ohm\nL = 0.05     # H\nf = 50.0     # Hz\nU = 230.0    # V\n\n# Ihr Code:\n", "en": "pi = 3.14159\nR = 12.0     # Ohm\nL = 0.05     # H\nf = 50.0     # Hz\nU = 230.0    # V\n\n# your code:\n"},
   solution='pi = 3.14159\nR = 12.0\nL = 0.05\nf = 50.0\nU = 230.0\nomega = 2 * pi * f\nX_L = omega * L\nZ = R + 1j * X_L\nZ_abs = (R**2 + X_L**2) ** 0.5\nI = U / Z\nI_abs = U / Z_abs\nprint(Z, round(Z_abs, 2), round(I_abs, 2))\n',
   tests='''
import math as _m
for R, L, f in [(12.0, 0.05, 50.0), (100.0, 0.2, 1000.0), (5.0, 0.001, 50.0)]:
    ns, out = run(sub={"R": R, "L": L, "f": f})
    X, Z, Za, I, Ia = need(ns, "X_L", "Z", "Z_abs", "I", "I_abs")
    eZ = complex(R, 2 * 3.14159 * f * L)
    check(approx(X, eZ.imag), f"X_L ≈ {eZ.imag:.3f} Ω", f"X_L ≈ {eZ.imag:.3f} Ω")
    check(isinstance(Z, complex) and approx(Z.real, R) and approx(Z.imag, eZ.imag), f"Z = {eZ:.3f}", f"Z = {eZ:.3f}")
    check(approx(Za, abs(eZ)), f"|Z| ≈ {abs(eZ):.3f} Ω", f"|Z| ≈ {abs(eZ):.3f} Ω")
    check(isinstance(I, complex) and approx(abs(I - 230 / eZ), 0) and approx(Ia, 230 / abs(eZ)), f"I = U / Z ≈ {230/eZ:.4f} A, |I| ≈ {230/abs(eZ):.4f} A", f"I = U / Z ≈ {230/eZ:.4f} A, |I| ≈ {230/abs(eZ):.4f} A")
''',
   require=["complex"], forbid=["abs"], refs=["5.1"])

ex(id="k5-queue", ch="5", lvl=2,
   title={"de": "Prüfaufträge in der Warteschlange", "en": "Test jobs in a queue"},
   task={"de": "Die Liste `jobs` ist die Warteschlange eines Prüflabors (vorne = als Nächstes dran). Führen Sie nacheinander aus:\n1. Der Auftrag `'Härteprüfung'` wird hinten angehängt.\n2. Der vorderste Auftrag wird bearbeitet: Entfernen Sie ihn mit `pop(0)` und speichern Sie ihn in `done`.\n3. Ein Eilauftrag `'Bruchanalyse'` kommt ganz nach vorne.\n4. Speichern Sie in `n_tensile`, wie oft `'Zugversuch'` noch in der Liste steht, und in `pos`, an welcher Position der erste `'Zugversuch'` steht.",
         "en": "The list `jobs` is the queue of a testing lab (front = next). Perform in order:\n1. The job `'Härteprüfung'` is appended at the back.\n2. The front job is processed: remove it with `pop(0)` and store it in `done`.\n3. An urgent job `'Bruchanalyse'` goes to the very front.\n4. Store in `n_tensile` how often `'Zugversuch'` is still in the list, and in `pos` at which position the first `'Zugversuch'` is."},
   starter={"de": "jobs = ['Kerbschlag', 'Zugversuch', 'Rauheit', 'Zugversuch']\n\n# Ihr Code:\n", "en": "jobs = ['Kerbschlag', 'Zugversuch', 'Rauheit', 'Zugversuch']\n\n# your code:\n"},
   solution="jobs = ['Kerbschlag', 'Zugversuch', 'Rauheit', 'Zugversuch']\njobs.append('Härteprüfung')\ndone = jobs.pop(0)\njobs.insert(0, 'Bruchanalyse')\nn_tensile = jobs.count('Zugversuch')\npos = jobs.index('Zugversuch')\nprint(jobs, done, n_tensile, pos)\n",
   tests='''
for start in [['Kerbschlag', 'Zugversuch', 'Rauheit', 'Zugversuch'], ['Zugversuch', 'Rauheit', 'Zugversuch', 'Zugversuch']]:
    ns, out = run(sub={"jobs": list(start)})
    j, d, n, p = need(ns, "jobs", "done", "n_tensile", "pos")
    e = list(start); e.append('Härteprüfung'); ed = e.pop(0); e.insert(0, 'Bruchanalyse')
    check(j == e, f"Warteschlange danach: {e}", f"Queue afterwards: {e}")
    check(d == ed, f"done = {ed!r}", f"done = {ed!r}")
    check(n == e.count('Zugversuch') and p == e.index('Zugversuch'), f"n_tensile = {e.count('Zugversuch')}, pos = {e.index('Zugversuch')}", f"n_tensile = {e.count('Zugversuch')}, pos = {e.index('Zugversuch')}")
''',
   require=["list_methods"], refs=["5.3m"])

ex(id="k5-parity", ch="5", lvl=3,
   title={"de": "Paritätsbit", "en": "Parity bit"},
   task={"de": "Bei der seriellen Datenübertragung wird oft ein Paritätsbit angehängt. Lesen Sie ein Byte `n` (ganze Zahl 0–255) ein. Bestimmen Sie\n- `b`: die Binärdarstellung als String\n- `ones`: die Anzahl der Einsen darin (Tipp: `list(b)` liefert die Liste der Zeichen – und Listen haben die Methode `count`)\n- `parity_bit`: 1, wenn die Anzahl der Einsen ungerade ist, sonst 0 (ohne `if` – mit Modulo!)\n- `frame`: die Zahl, die entsteht, wenn man das Paritätsbit rechts an `n` anhängt (binär um eine Stelle nach links verschieben = mal 2)",
         "en": "Serial data transmission often appends a parity bit. Read a byte `n` (integer 0–255). Determine\n- `b`: the binary representation as a string\n- `ones`: the number of ones in it (tip: `list(b)` gives the list of characters – and lists have the method `count`)\n- `parity_bit`: 1 if the number of ones is odd, else 0 (without `if` – use modulo!)\n- `frame`: the number obtained by appending the parity bit to the right of `n` (shifting left by one binary digit = times 2)"},
   starter={"de": "# Byte einlesen\n", "en": "# read the byte\n"},
   solution='n = int(input("Byte (0-255): "))\nb = bin(n)\nones = list(b).count("1")\nparity_bit = ones % 2\nframe = n * 2 + parity_bit\nprint(b, ones, parity_bit, bin(frame))\n',
   tests='''
for n in [0, 7, 170, 255, 128]:
    ns, out = run(inputs=[str(n)])
    b, o, p, fr = need(ns, "b", "ones", "parity_bit", "frame")
    eo = bin(n).count("1")
    check(b == bin(n) and o == eo, f"{n}: {bin(n)} hat {eo} Einsen", f"{n}: {bin(n)} has {eo} ones")
    check(p == eo % 2, f"{n}: Paritätsbit {eo % 2}", f"{n}: parity bit {eo % 2}")
    check(fr == n * 2 + eo % 2, f"{n}: frame = {n*2 + eo%2} ({bin(n*2 + eo%2)})", f"{n}: frame = {n*2 + eo%2} ({bin(n*2 + eo%2)})")
''',
   stdin="170\n", require=["numsys"], forbid=["if"], refs=["5.5i", "4.2"])

ex(id="k5-det", ch="5", lvl=3,
   title={"de": "2×2-Matrix invertieren", "en": "Inverting a 2×2 matrix"},
   task={"de": "Die Matrix `M` ist als verschachtelte Liste `[[a, b], [c, d]]` gegeben. Berechnen Sie nur mit Indexzugriff\n- `det` = a·d − b·c\n- `inv`: die inverse Matrix `[[d, −b], [−c, a]] / det` als verschachtelte Liste (jedes Element durch `det` teilen)\n- `check`: das Produkt M · inv als verschachtelte Liste (sollte die Einheitsmatrix sein). Element (i, j) = M[i][0]·inv[0][j] + M[i][1]·inv[1][j].\n\nSie dürfen voraussetzen, dass `det` nicht 0 ist.",
         "en": "The matrix `M` is given as a nested list `[[a, b], [c, d]]`. Using indexing only, compute\n- `det` = a·d − b·c\n- `inv`: the inverse matrix `[[d, −b], [−c, a]] / det` as a nested list (divide each element by `det`)\n- `check`: the product M · inv as a nested list (should be the identity). Element (i, j) = M[i][0]·inv[0][j] + M[i][1]·inv[1][j].\n\nYou may assume that `det` is not 0."},
   starter={"de": "M = [[4.0, 7.0],\n     [2.0, 6.0]]\n\n# Ihr Code:\n", "en": "M = [[4.0, 7.0],\n     [2.0, 6.0]]\n\n# your code:\n"},
   solution='M = [[4.0, 7.0],\n     [2.0, 6.0]]\ndet = M[0][0] * M[1][1] - M[0][1] * M[1][0]\ninv = [[M[1][1] / det, -M[0][1] / det],\n       [-M[1][0] / det, M[0][0] / det]]\ncheck = [[M[0][0] * inv[0][0] + M[0][1] * inv[1][0], M[0][0] * inv[0][1] + M[0][1] * inv[1][1]],\n         [M[1][0] * inv[0][0] + M[1][1] * inv[1][0], M[1][0] * inv[0][1] + M[1][1] * inv[1][1]]]\nprint(det, inv, check)\n',
   tests='''
for M in [[[4.0, 7.0], [2.0, 6.0]], [[1.0, 2.0], [3.0, 4.0]], [[0.0, 1.0], [-1.0, 0.0]]]:
    ns, out = run(sub={"M": M})
    d, inv, c = need(ns, "det", "inv", "check")
    (a, b), (cc, dd) = M; ed = a * dd - b * cc
    check(approx(d, ed), f"det von {M} = {ed:g}", f"det of {M} = {ed:g}")
    ei = [[dd / ed, -b / ed], [-cc / ed, a / ed]]
    check(all(approx(inv[i][j], ei[i][j]) for i in range(2) for j in range(2)), f"Inverse = {ei}", f"Inverse = {ei}")
    check(all(approx(c[i][j], 1.0 if i == j else 0.0) for i in range(2) for j in range(2)), "M · inv ist die Einheitsmatrix", "M · inv is the identity matrix")
''',
   require=["index"], forbid=["for", "while"], refs=["5.3"])

ex(id="k5-median", ch="5", lvl=3,
   title={"de": "Median ohne Seiteneffekt", "en": "Median without side effects"},
   task={"de": "Der Median ist robuster gegen Ausreißer als der Mittelwert. Berechnen Sie den Median der Liste `values` in der Variable `median`:\n- Legen Sie eine **Kopie** an und sortieren Sie diese (das Original muss unverändert bleiben).\n- Bei n Werten ist der Median `(s[(n - 1) // 2] + s[n // 2]) / 2` – diese Formel funktioniert für gerade und ungerade n. Prüfen Sie das an einem Beispiel nach!",
         "en": "The median is more robust against outliers than the mean. Compute the median of the list `values` in the variable `median`:\n- Create a **copy** and sort it (the original must stay unchanged).\n- For n values, the median is `(s[(n - 1) // 2] + s[n // 2]) / 2` – this formula works for both even and odd n. Verify it on an example!"},
   starter={"de": "values = [4.1, 3.9, 47.0, 4.3, 4.0]\n\n# Ihr Code:\n", "en": "values = [4.1, 3.9, 47.0, 4.3, 4.0]\n\n# your code:\n"},
   solution='values = [4.1, 3.9, 47.0, 4.3, 4.0]\ns = list(values)\ns.sort()\nn = len(s)\nmedian = (s[(n - 1) // 2] + s[n // 2]) / 2\nprint(median, values)\n',
   tests='''
import statistics as _st
for v in [[4.1, 3.9, 47.0, 4.3, 4.0], [1.0, 2.0, 3.0, 10.0], [7.5], [3, 1, 2, 5, 4, 6]]:
    orig = list(v)
    ns, out = run(sub={"values": list(v)})
    m = need(ns, "median")
    check(approx(m, _st.median(v)), f"Median von {orig} = {_st.median(v)}", f"Median of {orig} = {_st.median(v)}")
    check(ns["values"] == orig, f"values bleibt unverändert", f"values stays unchanged")
''',
   forbid=["seqfuncs"], refs=["5.3m", "5.4s"])

ex(id="k5-rlc", ch="5", lvl=3,
   title={"de": "Reihenschwingkreis", "en": "Series RLC circuit"},
   task={"de": "Für einen RLC-Reihenschwingkreis mit `R` (Ω), `L` (H) und `C` (F) berechnen Sie mit `pi = 3.14159` und Wurzeln über `** 0.5`\n- `f0`: die Resonanzfrequenz f₀ = 1 / (2π·√(L·C))\n- `X`: den Blindwiderstand bei der Frequenz `f`: X = ωL − 1/(ωC) mit ω = 2πf\n- `Z`: die komplexe Impedanz Z = R + j·X\n- `Z_abs`: den Betrag √(R² + X²)\n- `inductive`: ob der Kreis bei `f` induktiv wirkt (X größer als 0)\n\nBei f = f₀ ist X = 0 und |Z| = R – probieren Sie es aus!",
         "en": "For a series RLC circuit with `R` (Ω), `L` (H) and `C` (F), compute with `pi = 3.14159` and roots via `** 0.5`\n- `f0`: the resonance frequency f₀ = 1 / (2π·√(L·C))\n- `X`: the reactance at frequency `f`: X = ωL − 1/(ωC) with ω = 2πf\n- `Z`: the complex impedance Z = R + j·X\n- `Z_abs`: the magnitude √(R² + X²)\n- `inductive`: whether the circuit behaves inductively at `f` (X greater than 0)\n\nAt f = f₀, X = 0 and |Z| = R – try it!"},
   starter={"de": "pi = 3.14159\nR = 10.0       # Ohm\nL = 0.01       # H\nC = 1e-6       # F\nf = 2000.0     # Hz\n\n# Ihr Code:\n", "en": "pi = 3.14159\nR = 10.0       # Ohm\nL = 0.01       # H\nC = 1e-6       # F\nf = 2000.0     # Hz\n\n# your code:\n"},
   solution='pi = 3.14159\nR = 10.0\nL = 0.01\nC = 1e-6\nf = 2000.0\nf0 = 1 / (2 * pi * (L * C) ** 0.5)\nomega = 2 * pi * f\nX = omega * L - 1 / (omega * C)\nZ = R + 1j * X\nZ_abs = (R**2 + X**2) ** 0.5\ninductive = X > 0\nprint(round(f0, 1), Z, round(Z_abs, 2), inductive)\n',
   tests="""
P = 3.14159
for R, L, C, f in [(10.0, 0.01, 1e-6, 2000.0), (10.0, 0.01, 1e-6, 1000.0), (50.0, 0.1, 1e-5, 500.0)]:
    ns, out = run(sub={"R": R, "L": L, "C": C, "f": f})
    f0, X, Z, Za, ind = need(ns, "f0", "X", "Z", "Z_abs", "inductive")
    ef0 = 1 / (2 * P * (L * C) ** 0.5); w = 2 * P * f; eZ = complex(R, w * L - 1 / (w * C))
    check(approx(X, eZ.imag, 1e-6), f"X bei {f:.0f} Hz ≈ {eZ.imag:.2f} Ω", f"X at {f:.0f} Hz ≈ {eZ.imag:.2f} Ω")
    check(approx(f0, ef0), f"f₀ ≈ {ef0:.2f} Hz", f"f₀ ≈ {ef0:.2f} Hz")
    check(isinstance(Z, complex) and approx(Z.imag, eZ.imag, 1e-6) and approx(Z.real, R), f"Z bei {f:.0f} Hz ≈ {eZ:.2f}", f"Z at {f:.0f} Hz ≈ {eZ:.2f}")
    check(approx(Za, abs(eZ)) and ind is (eZ.imag > 0), f"|Z| ≈ {abs(eZ):.2f} Ω, induktiv = {eZ.imag > 0}", f"|Z| ≈ {abs(eZ):.2f} Ω, inductive = {eZ.imag > 0}")
""",
   require=["complex"], refs=["5.1", "4.4"])
