from exlib import ex

# Kapitel 9, zweiter Satz: import-Varianten (math, Aliase), NumPy (Arrays, Vektorisierung, Broadcasting,
# Slicing, Views, linalg), pandas (DataFrame, read_csv, Spalten, mean/std).
# Aus dem Skript: math.sqrt/cos/sin/pi/factorial; np.array/zeros/ones/arange/linspace/dot/cross/sqrt/exp/sin/
# linalg.solve/eigvals, .T, .shape/.ndim/.size, .copy(); pd.DataFrame/read_csv, head/describe/mean/std.

# ------------------------------------------------------------------ Stufe 1
ex(id="k9-combinations", ch="9", lvl=1,
   title={"de": "Stichproben ziehen (Alias für math)", "en": "Drawing samples (alias for math)"},
   task={"de": "Aus einer Charge von `n` Bauteilen werden `k` Stück zur Prüfung entnommen. Die Anzahl der möglichen Stichproben ist der Binomialkoeffizient n! / (k! · (n − k)!).\n\nImportieren Sie das Modul `math` mit dem Alias `m` (`import math as m`) und berechnen Sie mit `m.factorial`\n- `samples`: die Anzahl der möglichen Stichproben (ganze Zahl – verwenden Sie `//`)\n- `p_specific`: die Wahrscheinlichkeit, genau eine bestimmte Stichprobe zu ziehen (1 / samples)\n\nGeben Sie `samples` aus und `p_specific` in Exponentialschreibweise mit zwei Nachkommastellen.",
         "en": "From a batch of `n` parts, `k` pieces are taken for inspection. The number of possible samples is the binomial coefficient n! / (k! · (n − k)!).\n\nImport the module `math` with the alias `m` (`import math as m`) and use `m.factorial` to compute\n- `samples`: the number of possible samples (integer – use `//`)\n- `p_specific`: the probability of drawing exactly one particular sample (1 / samples)\n\nPrint `samples`, and `p_specific` in scientific notation with two decimals."},
   starter={"de": "n = 50   # Bauteile in der Charge\nk = 5    # Stichprobengröße\n\n# Ihr Code:\n", "en": "n = 50   # parts in the batch\nk = 5    # sample size\n\n# your code:\n"},
   solution='import math as m\n\nn = 50\nk = 5\nsamples = m.factorial(n) // (m.factorial(k) * m.factorial(n - k))\np_specific = 1 / samples\nprint(samples, f"{p_specific:.2e}")\n',
   tests='''
import math as _m
for n, k in [(50, 5), (10, 3), (20, 20), (7, 0)]:
    ns, out = run(sub={"n": n, "k": k})
    s, p = need(ns, "samples", "p_specific")
    e = _m.comb(n, k)
    check(s == e and isinstance(s, int), f"n = {n}, k = {k}: {e} Stichproben (ganze Zahl)", f"n = {n}, k = {k}: {e} samples (integer)")
    check(approx(p, 1 / e) and str(e) in out, f"p_specific = {1/e:.3e}", f"p_specific = {1/e:.3e}")
check("as m" in SOURCE and "m.factorial" in SOURCE, "math mit Alias m importiert und m.factorial verwendet", "math imported with alias m and m.factorial used")
''',
   require=["import"], refs=["9.1"])

ex(id="k9-forces", ch="9", lvl=1,
   title={"de": "Kräfte addieren mit NumPy", "en": "Adding forces with NumPy"},
   task={"de": "An einem Knotenblech greifen drei Kräfte an, gegeben als Listen `[Fx, Fy, Fz]` in N. Wandeln Sie sie in NumPy-Arrays um und berechnen Sie **ohne Schleife**\n- `R`: die resultierende Kraft (Summe der drei Vektoren)\n- `magnitude`: deren Betrag √(R·R) mit `np.dot` und `np.sqrt`\n- `direction`: den Einheitsvektor in Richtung von R\n\nGeben Sie den Betrag mit einer Nachkommastelle aus.",
         "en": "Three forces act on a gusset plate, given as lists `[Fx, Fy, Fz]` in N. Convert them into NumPy arrays and compute **without a loop**\n- `R`: the resulting force (sum of the three vectors)\n- `magnitude`: its magnitude √(R·R) with `np.dot` and `np.sqrt`\n- `direction`: the unit vector in the direction of R\n\nPrint the magnitude with one decimal."},
   starter={"de": "import numpy as np\n\nF1 = [300.0, 0.0, -50.0]\nF2 = [-100.0, 400.0, 0.0]\nF3 = [0.0, -150.0, 120.0]\n\n# Ihr Code:\n", "en": "import numpy as np\n\nF1 = [300.0, 0.0, -50.0]\nF2 = [-100.0, 400.0, 0.0]\nF3 = [0.0, -150.0, 120.0]\n\n# your code:\n"},
   solution='import numpy as np\n\nF1 = [300.0, 0.0, -50.0]\nF2 = [-100.0, 400.0, 0.0]\nF3 = [0.0, -150.0, 120.0]\nR = np.array(F1) + np.array(F2) + np.array(F3)\nmagnitude = np.sqrt(np.dot(R, R))\ndirection = R / magnitude\nprint(R, f"{magnitude:.1f} N", direction)\n',
   tests='''
for a, b, c in [([300.0, 0.0, -50.0], [-100.0, 400.0, 0.0], [0.0, -150.0, 120.0]), ([1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]), ([5.0, 5.0, 5.0], [0.0, 0.0, 0.0], [-2.0, 1.0, 3.0])]:
    ns, out = run(sub={"F1": a, "F2": b, "F3": c})
    R, m, d = need(ns, "R", "magnitude", "direction")
    eR = [x + y + z for x, y, z in zip(a, b, c)]; em = sum(v * v for v in eR) ** 0.5
    check(type(R).__name__ == "ndarray" and all(approx(R[i], eR[i]) for i in range(3)), f"R = {eR}", f"R = {eR}")
    check(approx(m, em) and all(approx(d[i], eR[i] / em) for i in range(3)), f"|R| = {em:.2f} N, Einheitsvektor stimmt", f"|R| = {em:.2f} N, unit vector is correct")
''',
   require=["numpy"], forbid=["for", "while", "listcomp"], refs=["9.2", "9.2m"])

ex(id="k9-curve", ch="9", lvl=1,
   title={"de": "Funktionswerte vektorisiert", "en": "Function values, vectorised"},
   task={"de": "Wird an einen RLC-Reihenschwingkreis im aperiodischen Grenzfall eine Gleichspannung U gelegt, so gilt für den Strom i(t) = I₀ · t · e^(−t/τ) mit I₀ = U / L. Erzeugen Sie mit `np.linspace` das Array `t` mit `n` gleichabständigen Zeitpunkten von 0 bis `t_end` (in ms) und berechnen Sie **ohne Schleife** das Array `i` der Stromwerte (mit `np.exp`).\n\nSpeichern Sie außerdem `i_peak`, den größten Wert in `i` (eingebaute Funktion `max`), und `t_peak`, den Zeitpunkt, an dem er auftritt (Tipp: `list(i).index(i_peak)` liefert den Index).",
         "en": "When a DC voltage U is applied to a series RLC circuit in the critically damped case, the current is i(t) = I₀ · t · e^(−t/τ) with I₀ = U / L. Use `np.linspace` to create the array `t` with `n` equally spaced points in time from 0 to `t_end` (in ms) and compute **without a loop** the array `i` of the current values (using `np.exp`).\n\nAlso store `i_peak`, the largest value in `i` (built-in function `max`), and `t_peak`, the time at which it occurs (tip: `list(i).index(i_peak)` gives the index)."},
   starter={"de": "import numpy as np\n\nI0 = 2.0      # A/ms\ntau = 1.5     # ms\nt_end = 10.0  # ms\nn = 101\n\n# Ihr Code:\n", "en": "import numpy as np\n\nI0 = 2.0      # A/ms\ntau = 1.5     # ms\nt_end = 10.0  # ms\nn = 101\n\n# your code:\n"},
   solution='import numpy as np\n\nI0 = 2.0\ntau = 1.5\nt_end = 10.0\nn = 101\nt = np.linspace(0, t_end, n)\ni = I0 * t * np.exp(-t / tau)\ni_peak = max(i)\nt_peak = t[list(i).index(i_peak)]\nprint(f"Maximum {i_peak:.3f} A bei t = {t_peak:.2f} ms")\n',
   tests='''
import math as _m
for I0, tau, te, n in [(2.0, 1.5, 10.0, 101), (1.0, 4.0, 20.0, 41), (0.5, 0.5, 3.0, 7)]:
    ns, out = run(sub={"I0": I0, "tau": tau, "t_end": te, "n": n})
    t, i, ip, tp = need(ns, "t", "i", "i_peak", "t_peak")
    et = [te * k / (n - 1) for k in range(n)]; ei = [I0 * x * _m.exp(-x / tau) for x in et]
    check(type(t).__name__ == "ndarray" and len(t) == n and approx(t[-1], te), f"t: {n} Punkte von 0 bis {te}", f"t: {n} points from 0 to {te}")
    check(type(i).__name__ == "ndarray" and all(approx(a, b) for a, b in zip(i, ei)), "i(t) stimmt für alle Zeitpunkte", "i(t) is correct for all points in time")
    k = ei.index(max(ei))
    check(approx(ip, ei[k]) and approx(tp, et[k]), f"i_peak = {ei[k]:.4f} A bei t = {et[k]:.2f} ms", f"i_peak = {ei[k]:.4f} A at t = {et[k]:.2f} ms")
''',
   require=["numpy"], forbid=["for", "while"], refs=["9.2v", "9.2"])

ex(id="k9-shapes", ch="9", lvl=1,
   title={"de": "Arrays untersuchen", "en": "Inspecting arrays"},
   task={"de": "Die Messwerte von vier Dehnungsmessstreifen (Spalten) zu drei Laststufen (Zeilen) stehen in der verschachtelten Liste `data`. Wandeln Sie sie in das NumPy-Array `A` um und bestimmen Sie\n- `dims`, `shape`, `n_values`: Anzahl der Dimensionen, Form und Anzahl der Elemente (Attribute!)\n- `value`: den Wert in Laststufe 2 (Zeile, Index 1) an Streifen 3 (Spalte, Index 2) – Indizes durch Komma getrennt\n- `stage3`: alle Werte der letzten Laststufe (Slicing)\n- `gauge1`: alle Werte von Streifen 1 (erste Spalte)\n- `AT_shape`: die Form der transponierten Matrix",
         "en": "The readings of four strain gauges (columns) at three load stages (rows) are in the nested list `data`. Convert it into the NumPy array `A` and determine\n- `dims`, `shape`, `n_values`: number of dimensions, shape and number of elements (attributes!)\n- `value`: the value at load stage 2 (row, index 1) on gauge 3 (column, index 2) – indices separated by a comma\n- `stage3`: all values of the last load stage (slicing)\n- `gauge1`: all values of gauge 1 (first column)\n- `AT_shape`: the shape of the transposed matrix"},
   starter={"de": "import numpy as np\n\ndata = [[102, 98, 110, 95],\n        [205, 199, 221, 190],\n        [311, 297, 330, 288]]  # µm/m\n\n# Ihr Code:\n", "en": "import numpy as np\n\ndata = [[102, 98, 110, 95],\n        [205, 199, 221, 190],\n        [311, 297, 330, 288]]  # µm/m\n\n# your code:\n"},
   solution='import numpy as np\n\ndata = [[102, 98, 110, 95],\n        [205, 199, 221, 190],\n        [311, 297, 330, 288]]\nA = np.array(data)\ndims = A.ndim\nshape = A.shape\nn_values = A.size\nvalue = A[1, 2]\nstage3 = A[-1, :]\ngauge1 = A[:, 0]\nAT_shape = A.T.shape\nprint(dims, shape, n_values, value, stage3, gauge1, AT_shape)\n',
   tests='''
for d in [[[102, 98, 110, 95], [205, 199, 221, 190], [311, 297, 330, 288]], [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]]:
    ns, out = run(sub={"data": d})
    A, di, sh, nv, v, s3, g1, ats = need(ns, "A", "dims", "shape", "n_values", "value", "stage3", "gauge1", "AT_shape")
    r, c = len(d), len(d[0])
    check(type(A).__name__ == "ndarray" and di == 2 and tuple(sh) == (r, c) and nv == r * c, f"ndim = 2, shape = ({r}, {c}), size = {r * c}", f"ndim = 2, shape = ({r}, {c}), size = {r * c}")
    check(v == d[1][2] and list(s3) == d[-1] and list(g1) == [row[0] for row in d], f"value = {d[1][2]}, stage3 = {d[-1]}, gauge1 = {[row[0] for row in d]}", f"value = {d[1][2]}, stage3 = {d[-1]}, gauge1 = {[row[0] for row in d]}")
    check(tuple(ats) == (c, r), f"Transponierte hat die Form ({c}, {r})", f"Transpose has the shape ({c}, {r})")
check(".ndim" in SOURCE and ".shape" in SOURCE and ".size" in SOURCE, "Mit den Attributen ndim, shape und size bestimmt", "Determined with the attributes ndim, shape and size")
''',
   require=["numpy", "slice"], refs=["9.2"])

# ------------------------------------------------------------------ Stufe 2
ex(id="k9-rotation", ch="9", lvl=2,
   title={"de": "Bohrbild drehen", "en": "Rotating a hole pattern"},
   task={"de": "Die Bohrungen eines Bauteils stehen in der Matrix `P`: erste Zeile x-Koordinaten, zweite Zeile y-Koordinaten (mm), eine Spalte pro Bohrung. Das Bauteil wird um den Winkel `angle_deg` (gegen den Uhrzeigersinn) um den Ursprung gedreht. Die Drehmatrix ist\n\n  R = [[cos φ, −sin φ], [sin φ, cos φ]]\n\n- Rechnen Sie den Winkel ins Bogenmaß um (`np.pi`) und legen Sie `R` mit `np.cos` und `np.sin` als Array an.\n- `P_rot`: die gedrehten Koordinaten aller Bohrungen in **einer** Matrixmultiplikation (`@`).\n- `dist_before`, `dist_after`: die Abstände aller Bohrungen vom Ursprung vor und nach der Drehung als Arrays (vektorisiert: `np.sqrt(x**2 + y**2)` mit den Zeilen der Matrix) – sie müssen gleich bleiben!",
         "en": "The holes of a part are in the matrix `P`: first row x coordinates, second row y coordinates (mm), one column per hole. The part is rotated by the angle `angle_deg` (counter-clockwise) about the origin. The rotation matrix is\n\n  R = [[cos φ, −sin φ], [sin φ, cos φ]]\n\n- Convert the angle to radians (`np.pi`) and create `R` with `np.cos` and `np.sin` as an array.\n- `P_rot`: the rotated coordinates of all holes in **one** matrix multiplication (`@`).\n- `dist_before`, `dist_after`: the distances of all holes from the origin before and after the rotation as arrays (vectorised: `np.sqrt(x**2 + y**2)` with the rows of the matrix) – they must stay the same!"},
   starter={"de": "import numpy as np\n\nP = np.array([[40.0, 0.0, -25.0, 10.0],\n              [0.0, 30.0, 25.0, -15.0]])\nangle_deg = 90.0\n\n# Ihr Code:\n", "en": "import numpy as np\n\nP = np.array([[40.0, 0.0, -25.0, 10.0],\n              [0.0, 30.0, 25.0, -15.0]])\nangle_deg = 90.0\n\n# your code:\n"},
   solution='import numpy as np\n\nP = np.array([[40.0, 0.0, -25.0, 10.0],\n              [0.0, 30.0, 25.0, -15.0]])\nangle_deg = 90.0\nphi = angle_deg * np.pi / 180\nR = np.array([[np.cos(phi), -np.sin(phi)],\n              [np.sin(phi), np.cos(phi)]])\nP_rot = R @ P\ndist_before = np.sqrt(P[0, :]**2 + P[1, :]**2)\ndist_after = np.sqrt(P_rot[0, :]**2 + P_rot[1, :]**2)\nprint(P_rot)\nprint(dist_before, dist_after)\n',
   tests='''
import math as _m
for a in [90.0, 30.0, -45.0, 180.0]:
    ns, out = run(sub={"angle_deg": a})
    R, Pr, db, da = need(ns, "R", "P_rot", "dist_before", "dist_after")
    phi = a * _m.pi / 180; c, s = _m.cos(phi), _m.sin(phi)
    P = [[40.0, 0.0, -25.0, 10.0], [0.0, 30.0, 25.0, -15.0]]
    check(getattr(R, "shape", None) == (2, 2) and approx(R[0, 0], c, 1e-9) and approx(R[0, 1] + s, 0, 1e-9), f"Drehmatrix für {a}°", f"rotation matrix for {a}°")
    ok = getattr(Pr, "shape", None) == (2, 4) and all(approx(Pr[0, k], c * P[0][k] - s * P[1][k], 1e-9) and approx(Pr[1, k], s * P[0][k] + c * P[1][k], 1e-9) for k in range(4))
    check(ok, f"Gedrehte Koordinaten für {a}° stimmen", f"Rotated coordinates for {a}° are correct")
    check(len(db) == 4 and all(approx(db[k], (P[0][k]**2 + P[1][k]**2) ** 0.5) and approx(da[k], db[k]) for k in range(4)), "Abstände vorher und nachher gleich", "Distances before and after are equal")
check("@" in SOURCE, "Mit dem Operator @ multipliziert", "Multiplied with the operator @")
''',
   require=["numpy", "matmul", "slice"], forbid=["for", "while"], refs=["9.2m", "9.2v", "9.2"])

ex(id="k9-threephase", ch="9", lvl=2,
   title={"de": "Leistungsbilanz eines Verteilers", "en": "Power balance of a distribution board"},
   task={"de": "In einem Unterverteiler wurden für jeden Abgang Spannung `U` (V), Strom `I` (A) und Leistungsfaktor `cos_phi` gemessen (je eine Liste, gleiche Reihenfolge). Wandeln Sie die Listen in Arrays um und berechnen Sie **ohne Schleife**\n- `P`: die Wirkleistungen P = U · I · cos φ der Abgänge (W)\n- `S`: die Scheinleistungen S = U · I (VA)\n- `P_total`, `S_total`: die Summen (eingebaute Funktion `sum`)\n- `pf_total`: den Gesamt-Leistungsfaktor P_total / S_total\n- `share`: den Anteil jedes Abgangs an P_total in Prozent (Array)",
         "en": "In a sub-distribution board, voltage `U` (V), current `I` (A) and power factor `cos_phi` were measured for every outgoing circuit (one list each, same order). Convert the lists into arrays and compute **without a loop**\n- `P`: the active powers P = U · I · cos φ of the circuits (W)\n- `S`: the apparent powers S = U · I (VA)\n- `P_total`, `S_total`: the sums (built-in function `sum`)\n- `pf_total`: the overall power factor P_total / S_total\n- `share`: the share of each circuit in P_total in percent (array)"},
   starter={"de": "import numpy as np\n\nU = [230.0, 229.5, 231.2, 230.4]\nI = [8.2, 15.6, 2.4, 11.0]\ncos_phi = [0.95, 0.82, 1.0, 0.88]\n\n# Ihr Code:\n", "en": "import numpy as np\n\nU = [230.0, 229.5, 231.2, 230.4]\nI = [8.2, 15.6, 2.4, 11.0]\ncos_phi = [0.95, 0.82, 1.0, 0.88]\n\n# your code:\n"},
   solution='import numpy as np\n\nU = [230.0, 229.5, 231.2, 230.4]\nI = [8.2, 15.6, 2.4, 11.0]\ncos_phi = [0.95, 0.82, 1.0, 0.88]\nu = np.array(U)\ni = np.array(I)\npf = np.array(cos_phi)\nS = u * i\nP = S * pf\nP_total = sum(P)\nS_total = sum(S)\npf_total = P_total / S_total\nshare = P / P_total * 100\nprint(P, round(P_total, 1), round(pf_total, 3), share)\n',
   tests='''
for U, I, c in [([230.0, 229.5, 231.2, 230.4], [8.2, 15.6, 2.4, 11.0], [0.95, 0.82, 1.0, 0.88]), ([400.0], [10.0], [0.5]), ([100.0, 100.0], [1.0, 3.0], [1.0, 1.0])]:
    ns, out = run(sub={"U": U, "I": I, "cos_phi": c})
    P, S, pt, st, pf, sh = need(ns, "P", "S", "P_total", "S_total", "pf_total", "share")
    eP = [u * i * k for u, i, k in zip(U, I, c)]; eS = [u * i for u, i in zip(U, I)]
    check(type(P).__name__ == "ndarray" and all(approx(a, b) for a, b in zip(P, eP)) and all(approx(a, b) for a, b in zip(S, eS)), f"P = {[round(x, 1) for x in eP]}", f"P = {[round(x, 1) for x in eP]}")
    check(approx(pt, sum(eP)) and approx(st, sum(eS)) and approx(pf, sum(eP) / sum(eS)), f"P_total = {sum(eP):.1f} W, Leistungsfaktor {sum(eP) / sum(eS):.3f}", f"P_total = {sum(eP):.1f} W, power factor {sum(eP) / sum(eS):.3f}")
    check(all(approx(a, b / sum(eP) * 100) for a, b in zip(sh, eP)), "Anteile in Prozent stimmen", "Shares in percent are correct")
''',
   require=["numpy", "seqfuncs"], forbid=["for", "while", "listcomp"], refs=["9.2v", "7.2s"])

ex(id="k9-powermap", ch="9", lvl=2,
   title={"de": "Leistungskennfeld mit Broadcasting", "en": "Power map with broadcasting"},
   task={"de": "Für einen Antrieb soll ein Kennfeld der mechanischen Leistung P = M · 2π · n / 60 (W) für alle Kombinationen aus Drehmomenten `torques` (Nm) und Drehzahlen `speeds` (1/min) berechnet werden – **ohne Schleife**:\n- Machen Sie aus den Drehmomenten einen **Spaltenvektor**: `np.array([torques]).T` hat die Form (Anzahl, 1).\n- Multiplizieren Sie ihn mit dem Drehzahl-Array: Durch Broadcasting entsteht die Matrix `P_map` mit einer Zeile pro Drehmoment und einer Spalte pro Drehzahl.\n- `P_kW`: das Kennfeld in kW, `max_kW`: der größte Wert im Kennfeld. Tipp: Alle Werte sind positiv, der größte steht also in der Zeile des größten Drehmoments. Bestimmen Sie diese Zeile mit `torques.index(max(torques))` und wenden Sie `max` auf die Zeile `P_kW[zeile, :]` an.\n- `shape`: die Form von `P_map`",
         "en": "For a drive, a map of the mechanical power P = M · 2π · n / 60 (W) is to be computed for all combinations of torques `torques` (Nm) and speeds `speeds` (1/min) – **without a loop**:\n- Turn the torques into a **column vector**: `np.array([torques]).T` has the shape (count, 1).\n- Multiply it by the speed array: broadcasting gives the matrix `P_map` with one row per torque and one column per speed.\n- `P_kW`: the map in kW, `max_kW`: the largest value in the map. Tip: all values are positive, so the largest one is in the row of the largest torque. Find that row with `torques.index(max(torques))` and apply `max` to the row `P_kW[row, :]`.\n- `shape`: the shape of `P_map`"},
   starter={"de": "import numpy as np\n\ntorques = [10.0, 20.0, 30.0]          # Nm\nspeeds = [500, 1000, 1500, 2000, 3000] # 1/min\n\n# Ihr Code:\n", "en": "import numpy as np\n\ntorques = [10.0, 20.0, 30.0]          # Nm\nspeeds = [500, 1000, 1500, 2000, 3000] # 1/min\n\n# your code:\n"},
   solution='import numpy as np\n\ntorques = [10.0, 20.0, 30.0]\nspeeds = [500, 1000, 1500, 2000, 3000]\nM = np.array([torques]).T\nn = np.array(speeds)\nP_map = M * 2 * np.pi * n / 60\nP_kW = P_map / 1000\nrow = torques.index(max(torques))\nmax_kW = max(P_kW[row, :])\nshape = P_map.shape\nprint(shape)\nprint(P_kW)\nprint(max_kW)\n',
   tests='''
import math as _m
for t, s in [([10.0, 20.0, 30.0], [500, 1000, 1500, 2000, 3000]), ([5.0], [1450]), ([1.0, 2.0], [60, 120, 180])]:
    ns, out = run(sub={"torques": t, "speeds": s})
    P, Pk, mk, sh = need(ns, "P_map", "P_kW", "max_kW", "shape")
    check(tuple(sh) == (len(t), len(s)) and getattr(P, "shape", None) == (len(t), len(s)), f"P_map hat die Form ({len(t)}, {len(s)})", f"P_map has the shape ({len(t)}, {len(s)})")
    ok = all(approx(P[i, j], t[i] * 2 * _m.pi * s[j] / 60) and approx(Pk[i, j], t[i] * 2 * _m.pi * s[j] / 60000) for i in range(len(t)) for j in range(len(s)))
    check(ok, "Alle Kennfeldwerte stimmen (W und kW)", "All map values are correct (W and kW)")
    check(approx(mk, max(t) * 2 * _m.pi * max(s) / 60000), f"max_kW = {max(t) * 2 * _m.pi * max(s) / 60000:.2f}", f"max_kW = {max(t) * 2 * _m.pi * max(s) / 60000:.2f}")
''',
   require=["numpy"], forbid=["for", "while", "listcomp"], refs=["9.2b", "9.2"])

ex(id="k9-readcsv", ch="9", lvl=2,
   title={"de": "Prüfstandslauf mit read_csv", "en": "Test-bench run with read_csv"},
   task={"de": "Die Datei `data/lauf.csv` enthält einen Prüfstandslauf mit den Spalten `zeit_s`, `drehzahl_rpm`, `drehmoment_Nm` und `temperatur_C`. Lesen Sie sie mit pandas in das DataFrame `df` ein und\n- speichern Sie die Anzahl der Messzeilen in `n_rows` (`len`)\n- fügen Sie die Spalte `p_mech_W` mit der mechanischen Leistung P = M · 2π · n / 60 hinzu (`np.pi`)\n- speichern Sie die mittlere Leistung in `p_mean` und die Standardabweichung der Temperatur in `t_std` (pandas-Methoden `mean` und `std`)\n- speichern Sie in `t_rise` den Temperaturanstieg vom ersten bis zum letzten Messpunkt (Tipp: `list(df['temperatur_C'])` liefert eine Liste)\n\nZum Ausprobieren wird beim Ausführen eine Beispieldatei angelegt.",
         "en": "The file `data/lauf.csv` contains a test-bench run with the columns `zeit_s`, `drehzahl_rpm`, `drehmoment_Nm` and `temperatur_C`. Read it with pandas into the DataFrame `df` and\n- store the number of data rows in `n_rows` (`len`)\n- add the column `p_mech_W` with the mechanical power P = M · 2π · n / 60 (`np.pi`)\n- store the mean power in `p_mean` and the standard deviation of the temperature in `t_std` (pandas methods `mean` and `std`)\n- store in `t_rise` the temperature rise from the first to the last data point (tip: `list(df['temperatur_C'])` gives a list)\n\nFor trying it out, a sample file is created when you run your code."},
   starter={"de": "import numpy as np\nimport pandas as pd\n\n# Ihr Code:\n", "en": "import numpy as np\nimport pandas as pd\n\n# your code:\n"},
   solution="import numpy as np\nimport pandas as pd\n\ndf = pd.read_csv('data/lauf.csv')\nn_rows = len(df)\ndf['p_mech_W'] = df['drehmoment_Nm'] * 2 * np.pi * df['drehzahl_rpm'] / 60\np_mean = df['p_mech_W'].mean()\nt_std = df['temperatur_C'].std()\ntemps = list(df['temperatur_C'])\nt_rise = temps[-1] - temps[0]\nprint(df.head())\nprint(n_rows, round(p_mean, 1), round(t_std, 2), t_rise)\n",
   tests='''
import math as _m, statistics as _st
F1 = "zeit_s,drehzahl_rpm,drehmoment_Nm,temperatur_C\\n0,1467,33.8,24.6\\n2,1461,35.4,25.3\\n4,1460,32.2,25.7\\n6,1454,37.1,25.9\\n8,1456,36.0,26.4\\n"
F2 = "zeit_s,drehzahl_rpm,drehmoment_Nm,temperatur_C\\n0,3000,10.0,20.0\\n1,2990,12.0,21.5\\n"
for content in [F1, F2]:
    rows = [l.split(",") for l in content.strip().split("\\n")[1:]]
    p = [float(r[2]) * 2 * _m.pi * float(r[1]) / 60 for r in rows]; t = [float(r[3]) for r in rows]
    ns, out = run(files={"data/lauf.csv": content})
    df, n, pm, ts, tr = need(ns, "df", "n_rows", "p_mean", "t_std", "t_rise")
    check(type(df).__name__ == "DataFrame" and "p_mech_W" in df.columns and n == len(rows), f"df mit {len(rows)} Zeilen und Spalte p_mech_W", f"df with {len(rows)} rows and column p_mech_W")
    check(approx(pm, sum(p) / len(p)), f"p_mean = {sum(p) / len(p):.1f} W", f"p_mean = {sum(p) / len(p):.1f} W")
    check(approx(ts, _st.stdev(t)) and approx(tr, t[-1] - t[0]), f"t_std = {_st.stdev(t):.3f} °C, t_rise = {t[-1] - t[0]:.1f} K", f"t_std = {_st.stdev(t):.3f} °C, t_rise = {t[-1] - t[0]:.1f} K")
''',
   require=["pandas"], refs=["9.4"],
   files={"data/lauf.csv": "zeit_s,drehzahl_rpm,drehmoment_Nm,temperatur_C\n0,1467,33.8,24.6\n2,1461,35.4,25.3\n4,1460,32.2,25.7\n6,1454,37.1,25.9\n8,1456,36.0,26.4\n"})

# ------------------------------------------------------------------ Stufe 3
ex(id="k9-eigen", ch="9", lvl=3,
   title={"de": "Eigenfrequenzen eines Zweimassenschwingers", "en": "Natural frequencies of a two-mass oscillator"},
   task={"de": "Zwei gleiche Massen m (kg) sind über Federn verbunden: Feder `k1` (N/m) zwischen Boden und Masse 1, Feder `k2` zwischen Masse 1 und Masse 2. Die Steifigkeitsmatrix ist\n\n  K = [[k1 + k2, −k2], [−k2, k2]]\n\nDie Eigenwerte λ der Matrix K / m sind die Quadrate der Eigenkreisfrequenzen: ω = √λ, und f = ω / (2π).\n- Legen Sie `K` als Array an und berechnen Sie mit `np.linalg.eigvals` die Eigenwerte `lam` von K / m. Je nach NumPy-Version erscheinen sie als komplexe Zahlen mit Imaginärteil 0 – mit `abs(lam)` erhalten Sie reelle Werte (die Eigenwerte sind hier positiv).\n- `freqs`: die beiden Eigenfrequenzen in Hz, **aufsteigend sortiert** (Liste; `sorted` funktioniert auch mit Arrays)\n- `ratio`: das Verhältnis der höheren zur niedrigeren Eigenfrequenz\n- `resonance`: ob die Anregungsfrequenz `f_exc` näher als 10 % an einer der beiden Eigenfrequenzen liegt (|f_exc − f| < 0.1 · f)",
         "en": "Two equal masses m (kg) are connected by springs: spring `k1` (N/m) between the ground and mass 1, spring `k2` between mass 1 and mass 2. The stiffness matrix is\n\n  K = [[k1 + k2, −k2], [−k2, k2]]\n\nThe eigenvalues λ of the matrix K / m are the squares of the natural angular frequencies: ω = √λ, and f = ω / (2π).\n- Create `K` as an array and use `np.linalg.eigvals` to compute the eigenvalues `lam` of K / m. Depending on the NumPy version they appear as complex numbers with imaginary part 0 – `abs(lam)` gives real values (the eigenvalues are positive here).\n- `freqs`: the two natural frequencies in Hz, **sorted in ascending order** (list; `sorted` also works with arrays)\n- `ratio`: the ratio of the higher to the lower natural frequency\n- `resonance`: whether the excitation frequency `f_exc` is closer than 10 % to one of the two natural frequencies (|f_exc − f| < 0.1 · f)"},
   starter={"de": "import numpy as np\n\nm = 2.0        # kg\nk1 = 8000.0    # N/m\nk2 = 4000.0    # N/m\nf_exc = 12.0   # Hz\n\n# Ihr Code:\n", "en": "import numpy as np\n\nm = 2.0        # kg\nk1 = 8000.0    # N/m\nk2 = 4000.0    # N/m\nf_exc = 12.0   # Hz\n\n# your code:\n"},
   solution='import numpy as np\n\nm = 2.0\nk1 = 8000.0\nk2 = 4000.0\nf_exc = 12.0\nK = np.array([[k1 + k2, -k2],\n              [-k2, k2]])\nlam = np.linalg.eigvals(K / m)\nfreqs = sorted(np.sqrt(abs(lam)) / (2 * np.pi))\nratio = freqs[1] / freqs[0]\nresonance = abs(f_exc - freqs[0]) < 0.1 * freqs[0] or abs(f_exc - freqs[1]) < 0.1 * freqs[1]\nprint(f"f1 = {freqs[0]:.2f} Hz, f2 = {freqs[1]:.2f} Hz, Resonanzgefahr: {resonance}")\n',
   tests='''
import math as _m
def ref(m, k1, k2):
    a, b, d = (k1 + k2) / m, -k2 / m, k2 / m
    tr, det = a + d, a * d - b * b
    disc = (tr * tr / 4 - det) ** 0.5
    return sorted([_m.sqrt(tr / 2 - disc) / (2 * _m.pi), _m.sqrt(tr / 2 + disc) / (2 * _m.pi)])
for m, k1, k2, fe in [(2.0, 8000.0, 4000.0, 12.0), (2.0, 8000.0, 4000.0, 25.0), (1.0, 1000.0, 1000.0, 3.1), (5.0, 2e5, 5e4, 40.0), (2.0, 8000.0, 4000.0, 6.5), (2.0, 8000.0, 4000.0, 5.2)]:
    ns, out = run(sub={"m": m, "k1": k1, "k2": k2, "f_exc": fe})
    lam, fr, r, res = need(ns, "lam", "freqs", "ratio", "resonance")
    ef = ref(m, k1, k2)
    check(len(fr) == 2 and approx(fr[0], ef[0]) and approx(fr[1], ef[1]), f"m = {m}, k1 = {k1:g}, k2 = {k2:g}: f = {ef[0]:.3f} Hz, {ef[1]:.3f} Hz", f"m = {m}, k1 = {k1:g}, k2 = {k2:g}: f = {ef[0]:.3f} Hz, {ef[1]:.3f} Hz")
    eres = abs(fe - ef[0]) < 0.1 * ef[0] or abs(fe - ef[1]) < 0.1 * ef[1]
    check(approx(r, ef[1] / ef[0]) and bool(res) is eres, f"ratio = {ef[1] / ef[0]:.3f}, resonance bei {fe} Hz = {eres}", f"ratio = {ef[1] / ef[0]:.3f}, resonance at {fe} Hz = {eres}")
check("eigvals" in SOURCE, "Eigenwerte mit np.linalg.eigvals berechnet", "Eigenvalues computed with np.linalg.eigvals")
''',
   require=["numpy"], refs=["9.2m"])

ex(id="k9-truss", ch="9", lvl=3,
   title={"de": "Stabkräfte in einem Zweibock", "en": "Bar forces in a two-bar frame"},
   task={"de": "Zwei Stäbe sind in einem Knoten gelenkig verbunden und an Wänden gelagert. Am Knoten hängt eine Last `F` (N, nach unten). Stab 1 zeigt vom Knoten unter dem Winkel `alpha1` (Grad, gegen die Horizontale) nach links oben, Stab 2 unter `alpha2` nach rechts oben. Mit den Stabkräften S₁, S₂ (Zug positiv) lauten die Gleichgewichtsbedingungen am Knoten\n\n  −S₁·cos α₁ + S₂·cos α₂ = 0   (horizontal)\n  S₁·sin α₁ + S₂·sin α₂ = F    (vertikal)\n\nStellen Sie das System als Matrix `A` und rechte Seite `b` auf (Winkel ins Bogenmaß umrechnen, `np.cos`, `np.sin`), lösen Sie mit `np.linalg.solve` nach `S` und speichern Sie\n- `S1`, `S2`: die beiden Stabkräfte\n- `critical`: den Index (0 oder 1) des höher belasteten Stabs\n- `ok`: ob alle Stabkräfte die zulässige Kraft `S_max` nicht überschreiten",
         "en": "Two bars are pin-jointed at a node and supported at walls. A load `F` (N, downwards) hangs from the node. Bar 1 points from the node at the angle `alpha1` (degrees, against the horizontal) to the upper left, bar 2 at `alpha2` to the upper right. With the bar forces S₁, S₂ (tension positive), the equilibrium conditions at the node are\n\n  −S₁·cos α₁ + S₂·cos α₂ = 0   (horizontal)\n  S₁·sin α₁ + S₂·sin α₂ = F    (vertical)\n\nSet up the system as matrix `A` and right-hand side `b` (convert the angles to radians, `np.cos`, `np.sin`), solve with `np.linalg.solve` for `S` and store\n- `S1`, `S2`: the two bar forces\n- `critical`: the index (0 or 1) of the more heavily loaded bar\n- `ok`: whether no bar force exceeds the permissible force `S_max`"},
   starter={"de": "import numpy as np\n\nF = 5000.0      # N\nalpha1 = 30.0   # Grad\nalpha2 = 60.0   # Grad\nS_max = 4500.0  # N\n\n# Ihr Code:\n", "en": "import numpy as np\n\nF = 5000.0      # N\nalpha1 = 30.0   # degrees\nalpha2 = 60.0   # degrees\nS_max = 4500.0  # N\n\n# your code:\n"},
   solution='import numpy as np\n\nF = 5000.0\nalpha1 = 30.0\nalpha2 = 60.0\nS_max = 4500.0\na1 = alpha1 * np.pi / 180\na2 = alpha2 * np.pi / 180\nA = np.array([[-np.cos(a1), np.cos(a2)],\n              [np.sin(a1), np.sin(a2)]])\nb = np.array([0.0, F])\nS = np.linalg.solve(A, b)\nS1 = S[0]\nS2 = S[1]\ncritical = 0 if abs(S1) >= abs(S2) else 1\nok = abs(S1) <= S_max and abs(S2) <= S_max\nprint(f"S1 = {S1:.1f} N, S2 = {S2:.1f} N, zulässig: {ok}")\n',
   tests='''
import math as _m
def ref(F, a1, a2):
    a1, a2 = _m.radians(a1), _m.radians(a2)
    det = -_m.cos(a1) * _m.sin(a2) - _m.cos(a2) * _m.sin(a1)
    s1 = (0 * _m.sin(a2) - _m.cos(a2) * F) / det
    s2 = (-_m.cos(a1) * F - _m.sin(a1) * 0) / det
    return s1, s2
for F, a1, a2, sm in [(5000.0, 30.0, 60.0, 4500.0), (5000.0, 45.0, 45.0, 4000.0), (1200.0, 10.0, 80.0, 2000.0), (800.0, 60.0, 20.0, 1000.0), (5000.0, 30.0, 60.0, 4000.0)]:
    ns, out = run(sub={"F": F, "alpha1": a1, "alpha2": a2, "S_max": sm})
    A, b, s1, s2, cr, ok = need(ns, "A", "b", "S1", "S2", "critical", "ok")
    e1, e2 = ref(F, a1, a2)
    check(getattr(A, "shape", None) == (2, 2) and len(b) == 2, "A ist 2×2, b hat 2 Einträge", "A is 2×2, b has 2 entries")
    check(approx(s1, e1) and approx(s2, e2), f"F = {F:g} N, α₁ = {a1}°, α₂ = {a2}°: S₁ = {e1:.1f} N, S₂ = {e2:.1f} N", f"F = {F:g} N, α₁ = {a1}°, α₂ = {a2}°: S₁ = {e1:.1f} N, S₂ = {e2:.1f} N")
    check(cr == (0 if abs(e1) >= abs(e2) else 1) and bool(ok) is (abs(e1) <= sm and abs(e2) <= sm), f"critical = {0 if abs(e1) >= abs(e2) else 1}, ok = {abs(e1) <= sm and abs(e2) <= sm}", f"critical = {0 if abs(e1) >= abs(e2) else 1}, ok = {abs(e1) <= sm and abs(e2) <= sm}")
''',
   require=["numpy"], refs=["9.2m", "9.2v"])

ex(id="k9-energy", ch="9", lvl=3,
   title={"de": "Energiemonitoring mit pandas", "en": "Energy monitoring with pandas"},
   task={"de": "Für ein Bürogebäude liegen tägliche Werte vor: Wochentag, Heizenergie (kWh) und Außentemperatur (°C) im Dictionary `data`. Erzeugen Sie das DataFrame `df` und ergänzen Sie die Spalten\n- `kosten_EUR`: Heizenergie · Preis `price` (€/kWh)\n- `gradtage`: die Heizgradtage 20 − Außentemperatur\n- `kwh_pro_gt`: der spezifische Verbrauch Heizenergie / Heizgradtage\n\nSpeichern Sie außerdem\n- `cost_total`: die Gesamtkosten (eingebaute Funktion `sum` auf die Spalte)\n- `spec_mean` und `spec_std`: Mittelwert und Standardabweichung von `kwh_pro_gt` (pandas)\n- `worst_day`: den Wochentag mit dem höchsten spezifischen Verbrauch (Tipp: wandeln Sie die Spalten mit `list()` in Listen um und nutzen Sie `max` und `index`)",
         "en": "Daily values are available for an office building: weekday, heating energy (kWh) and outdoor temperature (°C) in the dictionary `data`. Create the DataFrame `df` and add the columns\n- `kosten_EUR`: heating energy · price `price` (€/kWh)\n- `gradtage`: the heating degree days 20 − outdoor temperature\n- `kwh_pro_gt`: the specific consumption heating energy / heating degree days\n\nAlso store\n- `cost_total`: the total costs (built-in function `sum` on the column)\n- `spec_mean` and `spec_std`: mean and standard deviation of `kwh_pro_gt` (pandas)\n- `worst_day`: the weekday with the highest specific consumption (tip: convert the columns into lists with `list()` and use `max` and `index`)"},
   starter={"de": "import pandas as pd\n\nprice = 0.11  # €/kWh\ndata = {\n    'tag': ['Mo', 'Di', 'Mi', 'Do', 'Fr'],\n    'kwh': [412.0, 455.0, 380.0, 520.0, 398.0],\n    'temp_C': [4.2, 2.1, 6.0, -1.5, 5.1],\n}\n\n# Ihr Code:\n", "en": "import pandas as pd\n\nprice = 0.11  # €/kWh\ndata = {\n    'tag': ['Mo', 'Di', 'Mi', 'Do', 'Fr'],\n    'kwh': [412.0, 455.0, 380.0, 520.0, 398.0],\n    'temp_C': [4.2, 2.1, 6.0, -1.5, 5.1],\n}\n\n# your code:\n"},
   solution="import pandas as pd\n\nprice = 0.11\ndata = {\n    'tag': ['Mo', 'Di', 'Mi', 'Do', 'Fr'],\n    'kwh': [412.0, 455.0, 380.0, 520.0, 398.0],\n    'temp_C': [4.2, 2.1, 6.0, -1.5, 5.1],\n}\ndf = pd.DataFrame(data)\ndf['kosten_EUR'] = df['kwh'] * price\ndf['gradtage'] = 20 - df['temp_C']\ndf['kwh_pro_gt'] = df['kwh'] / df['gradtage']\ncost_total = sum(df['kosten_EUR'])\nspec_mean = df['kwh_pro_gt'].mean()\nspec_std = df['kwh_pro_gt'].std()\nspec = list(df['kwh_pro_gt'])\nworst_day = list(df['tag'])[spec.index(max(spec))]\nprint(df)\nprint(round(cost_total, 2), round(spec_mean, 2), round(spec_std, 2), worst_day)\n",
   tests='''
import statistics as _st
D1 = {'tag': ['Mo', 'Di', 'Mi', 'Do', 'Fr'], 'kwh': [412.0, 455.0, 380.0, 520.0, 398.0], 'temp_C': [4.2, 2.1, 6.0, -1.5, 5.1]}
D2 = {'tag': ['Sa', 'So'], 'kwh': [100.0, 300.0], 'temp_C': [10.0, 15.0]}
for d, pr in [(D1, 0.11), (D2, 0.2)]:
    ns, out = run(sub={"data": d, "price": pr})
    df, ct, sm, ss, wd = need(ns, "df", "cost_total", "spec_mean", "spec_std", "worst_day")
    spec = [k / (20 - t) for k, t in zip(d['kwh'], d['temp_C'])]
    check(type(df).__name__ == "DataFrame" and all(c in df.columns for c in ("kosten_EUR", "gradtage", "kwh_pro_gt")), "df hat die drei neuen Spalten", "df has the three new columns")
    check(approx(ct, sum(d['kwh']) * pr), f"cost_total = {sum(d['kwh']) * pr:.2f} €", f"cost_total = {sum(d['kwh']) * pr:.2f} €")
    check(approx(sm, sum(spec) / len(spec)) and approx(ss, _st.stdev(spec)), f"spez. Verbrauch: Mittel {sum(spec) / len(spec):.3f}, Std. {_st.stdev(spec):.3f}", f"specific consumption: mean {sum(spec) / len(spec):.3f}, std {_st.stdev(spec):.3f}")
    check(wd == d['tag'][spec.index(max(spec))], f"worst_day = {d['tag'][spec.index(max(spec))]!r}", f"worst_day = {d['tag'][spec.index(max(spec))]!r}")
''',
   require=["pandas"], refs=["9.4"])

ex(id="k9-parabola", ch="9", lvl=3,
   title={"de": "Parabel durch drei Messpunkte", "en": "Parabola through three data points"},
   task={"de": "Der Wirkungsgrad einer Pumpe wurde bei drei Volumenströmen gemessen: `Q` (m³/h) und `eta` (%). Legen Sie eine Parabel η(Q) = a·Q² + b·Q + c exakt durch die drei Punkte:\n- Bauen Sie die 3×3-Matrix `A` mit den Zeilen [Qᵢ², Qᵢ, 1] (z.B. mit einer List Comprehension) und lösen Sie A · [a, b, c] = η mit `np.linalg.solve` → `coeffs`.\n- `Q_best`: der Volumenstrom mit dem besten Wirkungsgrad (Scheitel der Parabel: −b / (2a))\n- `eta_best`: der Wirkungsgrad dort\n- `eta_at`: die Wirkungsgrade an den Stellen `Q_test` als Array (vektorisiert)\n- `is_max`: ob der Scheitel wirklich ein Maximum ist (a < 0)",
         "en": "The efficiency of a pump was measured at three flow rates: `Q` (m³/h) and `eta` (%). Fit a parabola η(Q) = a·Q² + b·Q + c exactly through the three points:\n- Build the 3×3 matrix `A` with the rows [Qᵢ², Qᵢ, 1] (e.g. with a list comprehension) and solve A · [a, b, c] = η with `np.linalg.solve` → `coeffs`.\n- `Q_best`: the flow rate with the best efficiency (vertex of the parabola: −b / (2a))\n- `eta_best`: the efficiency there\n- `eta_at`: the efficiencies at the points `Q_test` as an array (vectorised)\n- `is_max`: whether the vertex really is a maximum (a < 0)"},
   starter={"de": "import numpy as np\n\nQ = [20.0, 40.0, 60.0]      # m³/h\neta = [58.0, 74.0, 66.0]    # %\nQ_test = [30.0, 45.0, 50.0]\n\n# Ihr Code:\n", "en": "import numpy as np\n\nQ = [20.0, 40.0, 60.0]      # m³/h\neta = [58.0, 74.0, 66.0]    # %\nQ_test = [30.0, 45.0, 50.0]\n\n# your code:\n"},
   solution='import numpy as np\n\nQ = [20.0, 40.0, 60.0]\neta = [58.0, 74.0, 66.0]\nQ_test = [30.0, 45.0, 50.0]\nA = np.array([[q**2, q, 1.0] for q in Q])\ncoeffs = np.linalg.solve(A, np.array(eta))\na = coeffs[0]\nb = coeffs[1]\nc = coeffs[2]\nQ_best = -b / (2 * a)\neta_best = a * Q_best**2 + b * Q_best + c\nqt = np.array(Q_test)\neta_at = a * qt**2 + b * qt + c\nis_max = a < 0\nprint(coeffs, round(Q_best, 1), round(eta_best, 1), eta_at, is_max)\n',
   tests='''
def ref(Q, E):
    (x0, x1, x2), (y0, y1, y2) = Q, E
    d0 = (x0 - x1) * (x0 - x2); d1 = (x1 - x0) * (x1 - x2); d2 = (x2 - x0) * (x2 - x1)
    a = y0 / d0 + y1 / d1 + y2 / d2
    b = -y0 * (x1 + x2) / d0 - y1 * (x0 + x2) / d1 - y2 * (x0 + x1) / d2
    c = y0 * x1 * x2 / d0 + y1 * x0 * x2 / d1 + y2 * x0 * x1 / d2
    return a, b, c
for Q, E, T in [([20.0, 40.0, 60.0], [58.0, 74.0, 66.0], [30.0, 45.0, 50.0]), ([1.0, 2.0, 3.0], [1.0, 4.0, 9.0], [0.0, 4.0]), ([10.0, 30.0, 70.0], [40.0, 70.0, 62.0], [50.0])]:
    ns, out = run(sub={"Q": Q, "eta": E, "Q_test": T})
    co, qb, eb, ea, im = need(ns, "coeffs", "Q_best", "eta_best", "eta_at", "is_max")
    a, b, c = ref(Q, E)
    check(len(co) == 3 and approx(co[0], a, 1e-6) and approx(co[1], b, 1e-6) and approx(co[2], c, 1e-6), f"a = {a:.5f}, b = {b:.4f}, c = {c:.3f}", f"a = {a:.5f}, b = {b:.4f}, c = {c:.3f}")
    eq = -b / (2 * a)
    check(approx(qb, eq, 1e-6) and approx(eb, a * eq**2 + b * eq + c, 1e-6), f"Scheitel bei Q = {eq:.2f}, η = {a * eq**2 + b * eq + c:.2f}", f"vertex at Q = {eq:.2f}, η = {a * eq**2 + b * eq + c:.2f}")
    check(len(ea) == len(T) and all(approx(ea[k], a * T[k]**2 + b * T[k] + c, 1e-6) for k in range(len(T))) and bool(im) is (a < 0), f"eta_at stimmt, is_max = {a < 0}", f"eta_at is correct, is_max = {a < 0}")
''',
   require=["numpy", "listcomp"], refs=["9.2m", "9.2v", "8.8"])

ex(id="k9-heatrod", ch="9", lvl=3,
   title={"de": "Wärmeleitung in einem Stab simulieren", "en": "Simulating heat conduction in a rod"},
   task={"de": "Ein Stab ist in Abschnitte unterteilt; das Array `T` enthält die Temperaturen der Abschnitte (°C). Die Enden werden konstant auf ihren Anfangswerten gehalten. In jedem Zeitschritt ändert sich jeder **innere** Abschnitt nach dem expliziten Verfahren\n\n  T_neu[i] = T[i] + r · (T[i−1] − 2·T[i] + T[i+1])\n\nmit der Konstante `r` (für Stabilität ≤ 0.5). Führen Sie `steps` Zeitschritte aus. Berechnen Sie die inneren Werte in jedem Schritt **ohne innere Schleife** mit Slicing: `T[2:]` sind die rechten, `T[:-2]` die linken Nachbarn von `T[1:-1]`. Arbeiten Sie mit einer Kopie (`.copy()`), damit Sie nicht schon veränderte Werte verwenden.\n\nSpeichern Sie das Ergebnis wieder in `T`, außerdem `T_mid` (Temperatur des mittleren Abschnitts, Index `len(T) // 2`) und `heat_flow_ok`: ob die Temperaturen von links nach rechts streng monoton fallen (prüfen Sie es mit einer Schleife oder Comprehension über benachbarte Werte).",
         "en": "A rod is divided into sections; the array `T` contains the temperatures of the sections (°C). The ends are held constant at their initial values. In every time step, each **inner** section changes according to the explicit scheme\n\n  T_new[i] = T[i] + r · (T[i−1] − 2·T[i] + T[i+1])\n\nwith the constant `r` (≤ 0.5 for stability). Perform `steps` time steps. Compute the inner values in every step **without an inner loop** using slicing: `T[2:]` are the right neighbours, `T[:-2]` the left neighbours of `T[1:-1]`. Work with a copy (`.copy()`) so that you don't use values that have already changed.\n\nStore the result in `T` again, as well as `T_mid` (temperature of the middle section, index `len(T) // 2`) and `heat_flow_ok`: whether the temperatures fall strictly monotonically from left to right (check it with a loop or comprehension over neighbouring values)."},
   starter={"de": "import numpy as np\n\nT = np.array([100.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0])\nr = 0.4\nsteps = 50\n\n# Ihr Code:\n", "en": "import numpy as np\n\nT = np.array([100.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0])\nr = 0.4\nsteps = 50\n\n# your code:\n"},
   solution='import numpy as np\n\nT = np.array([100.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0])\nr = 0.4\nsteps = 50\nfor k in range(steps):\n    T_new = T.copy()\n    T_new[1:-1] = T[1:-1] + r * (T[:-2] - 2 * T[1:-1] + T[2:])\n    T = T_new\nT_mid = T[len(T) // 2]\nheat_flow_ok = True\nfor i in range(len(T) - 1):\n    if not T[i] > T[i + 1]:\n        heat_flow_ok = False\nprint(T, T_mid, heat_flow_ok)\n',
   tests='''
def ref(T, r, steps):
    T = list(T)
    for _ in range(steps):
        N = list(T)
        for i in range(1, len(T) - 1):
            N[i] = T[i] + r * (T[i - 1] - 2 * T[i] + T[i + 1])
        T = N
    return T
for T0, r, st in [([100.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0], 0.4, 50), ([0.0, 50.0, 50.0, 0.0], 0.25, 10), ([80.0, 20.0, 20.0, 20.0, 40.0], 0.5, 3), ([100.0, 80.0, 60.0, 70.0], 0.3, 0)]:
    ns, out = run(sub={"T": Code(f"np.array({T0})"), "r": r, "steps": st})
    T, tm, hf = need(ns, "T", "T_mid", "heat_flow_ok")
    e = ref(T0, r, st)
    check(type(T).__name__ == "ndarray" and len(T) == len(e) and all(approx(a, b, 1e-9) for a, b in zip(T, e)), f"Nach {st} Schritten (r = {r}): T = {[round(x, 2) for x in e]}", f"After {st} steps (r = {r}): T = {[round(x, 2) for x in e]}")
    check(approx(tm, e[len(e) // 2]) and bool(hf) is all(e[i] > e[i + 1] for i in range(len(e) - 1)), f"T_mid = {e[len(e) // 2]:.3f}, heat_flow_ok = {all(e[i] > e[i + 1] for i in range(len(e) - 1))}", f"T_mid = {e[len(e) // 2]:.3f}, heat_flow_ok = {all(e[i] > e[i + 1] for i in range(len(e) - 1))}")
check("[1:-1]" in SOURCE.replace(" ", "") and ".copy()" in SOURCE, "Mit Slicing und .copy() gelöst", "Solved with slicing and .copy()")
''',
   require=["numpy", "slice"], refs=["9.2", "9.2v", "8.1x"])
