from exlib import ex

# Kapitel 9: zusätzlich import-Varianten, NumPy (Arrays, Vektorisierung, Broadcasting, Slicing, linalg), pandas.
# Matplotlib wird nicht geprüft (keine Grafikausgabe im Trainer).

ex(id="k9-pendulum", ch="9", lvl=1,
   title={"de": "Fadenpendel mit from … import", "en": "Pendulum with from … import"},
   task={"de": "Importieren Sie aus `math` gezielt `sqrt` und `pi` (`from … import …`). Berechnen Sie für ein Fadenpendel der Länge `l` (m) die Schwingungsdauer $T = 2\\pi\\sqrt{l/g}$ mit $g = 9.81\\,\\mathrm{m/s^2}$ (`T`) und die Frequenz `f = 1/T`. Geben Sie beides mit drei Nachkommastellen aus.",
         "en": "Import `sqrt` and `pi` specifically from `math` (`from … import …`). For a pendulum of length `l` (m), compute the period $T = 2\\pi\\sqrt{l/g}$ with $g = 9.81\\,\\mathrm{m/s^2}$ (`T`) and the frequency `f = 1/T`. Print both with three decimals."},
   starter={"de": "l = 0.75  # m\n\n# Ihr Code:\n", "en": "l = 0.75  # m\n\n# your code:\n"},
   solution='from math import sqrt, pi\n\nl = 0.75\nT = 2 * pi * sqrt(l / 9.81)\nf = 1 / T\nprint(f"T = {T:.3f} s, f = {f:.3f} Hz")\n',
   tests='''
import math as _m
for l in [0.75, 1.0, 2.5]:
    ns, out = run(sub={"l": l})
    T, f = need(ns, "T", "f")
    eT = 2 * _m.pi * _m.sqrt(l / 9.81)
    check(approx(T, eT) and approx(f, 1 / eT), f"l = {l} m: T ≈ {eT:.3f} s, f ≈ {1/eT:.3f} Hz", f"l = {l} m: T ≈ {eT:.3f} s, f ≈ {1/eT:.3f} Hz")
    check(f"{eT:.3f}" in out, "Ausgabe mit drei Nachkommastellen", "Output with three decimals")
''',
   require=["import"], refs=["9.1"])

ex(id="k9-arrays", ch="9", lvl=1,
   title={"de": "Arrays erzeugen", "en": "Creating arrays"},
   task={"de": "Importieren Sie NumPy als `np` und erzeugen Sie\n- `t`: 9 gleichabständige Zeitpunkte von 0 bis 2 s (Endpunkt eingeschlossen)\n- `angles`: die Winkel 0, 15, 30, …, 345 Grad mit `np.arange`\n- `grid`: eine 3×4-Matrix aus Nullen\n- `n_cells`: die Anzahl der Elemente von `grid` (Attribut!)\n- `rad`: die Winkel aus `angles` im Bogenmaß (vektorisiert, ohne Schleife)",
         "en": "Import NumPy as `np` and create\n- `t`: 9 equally spaced time points from 0 to 2 s (end point included)\n- `angles`: the angles 0, 15, 30, …, 345 degrees using `np.arange`\n- `grid`: a 3×4 matrix of zeros\n- `n_cells`: the number of elements of `grid` (attribute!)\n- `rad`: the angles from `angles` in radians (vectorised, no loop)"},
   starter={"de": "import numpy as np\n\n# Ihr Code:\n", "en": "import numpy as np\n\n# your code:\n"},
   solution='import numpy as np\n\nt = np.linspace(0, 2, 9)\nangles = np.arange(0, 360, 15)\ngrid = np.zeros((3, 4))\nn_cells = grid.size\nrad = angles * np.pi / 180\nprint(t, angles, grid.shape, n_cells, rad[:3])\n',
   tests='''
import math as _m
ns, out = run()
t, a, g, n, r = need(ns, "t", "angles", "grid", "n_cells", "rad")
check(len(t) == 9 and approx(t[0], 0) and approx(t[-1], 2) and approx(t[1], 0.25), "t = [0, 0.25, …, 2]", "t = [0, 0.25, …, 2]")
check(len(a) == 24 and a[0] == 0 and a[-1] == 345, "angles = [0, 15, …, 345]", "angles = [0, 15, …, 345]")
check(getattr(g, "shape", None) == (3, 4) and float(abs(g).max()) == 0.0, "grid ist eine 3×4-Nullmatrix", "grid is a 3×4 zero matrix")
check(n == 12, "n_cells = 12", "n_cells = 12")
check(type(r).__name__ == "ndarray" and len(r) == 24 and approx(r[6], _m.pi / 2), "rad im Bogenmaß (90° = π/2)", "rad in radians (90° = π/2)")
check(all(w in SOURCE for w in ("linspace", "arange", "zeros", ".size")), "Erzeugt mit np.linspace, np.arange, np.zeros und dem Attribut .size", "Created with np.linspace, np.arange, np.zeros and the attribute .size")
''',
   require=["numpy"], forbid=["for", "while", "listcomp"], refs=["9.2", "9.2v"])

ex(id="k9-power-vec", ch="9", lvl=1,
   title={"de": "Wellenleistung vektorisiert", "en": "Shaft power, vectorised"},
   task={"de": "Für mehrere Betriebspunkte eines Motors sind die Drehzahlen `rpm` (1/min) und die Drehmomente `torque` (Nm) als Listen gegeben. Wandeln Sie beide in NumPy-Arrays um und berechnen Sie **ohne Schleife**\n- `omega`: die Winkelgeschwindigkeit $\\omega = 2\\pi n/60$ in rad/s\n- `power_kw`: die mechanische Leistung $P = M \\omega$ in kW",
         "en": "For several operating points of a motor, the speeds `rpm` (1/min) and torques `torque` (Nm) are given as lists. Convert both to NumPy arrays and compute **without a loop**\n- `omega`: the angular velocity $\\omega = 2\\pi n/60$ in rad/s\n- `power_kw`: the mechanical power $P = M \\omega$ in kW"},
   starter={"de": "rpm = [750, 1450, 2900, 3600]\ntorque = [48.0, 36.2, 18.1, 12.5]\n\n# Ihr Code:\n", "en": "rpm = [750, 1450, 2900, 3600]\ntorque = [48.0, 36.2, 18.1, 12.5]\n\n# your code:\n"},
   solution='import numpy as np\n\nrpm = [750, 1450, 2900, 3600]\ntorque = [48.0, 36.2, 18.1, 12.5]\nn = np.array(rpm)\nM = np.array(torque)\nomega = 2 * np.pi * n / 60\npower_kw = M * omega / 1000\nprint(omega, power_kw)\n',
   tests='''
import math as _m
for r, t in [([750, 1450, 2900, 3600], [48.0, 36.2, 18.1, 12.5]), ([1000], [10.0])]:
    ns, out = run(sub={"rpm": r, "torque": t})
    o, p = need(ns, "omega", "power_kw")
    eo = [2 * _m.pi * x / 60 for x in r]
    check(type(o).__name__ == "ndarray" and len(o) == len(r) and all(approx(a, b) for a, b in zip(o, eo)), "omega stimmt (als Array)", "omega is correct (as an array)")
    ep = [m * w / 1000 for m, w in zip(t, eo)]
    check(type(p).__name__ == "ndarray" and all(approx(a, b) for a, b in zip(p, ep)), f"power_kw ≈ {[round(x, 2) for x in ep]}", f"power_kw ≈ {[round(x, 2) for x in ep]}")
''',
   require=["numpy"], forbid=["for", "while", "listcomp"], refs=["9.2v"])

ex(id="k9-calibrate", ch="9", lvl=2,
   title={"de": "Kalibrieren mit Broadcasting", "en": "Calibrating with broadcasting"},
   task={"de": "Die Matrix `raw` enthält Messungen: Jede Zeile ist ein Zeitpunkt, jede Spalte ein Sensor. Jeder Sensor hat einen Nullpunktfehler (`offset`) und einen Verstärkungsfaktor (`gain`), beide als Vektor mit einem Wert pro Sensor.\n- Berechnen Sie mit Broadcasting `calibrated = (raw - offset) * gain` – ohne Schleife.\n- `sensor2`: alle kalibrierten Werte von Sensor 2 (dritte Spalte) per Slicing\n- `last_row`: die kalibrierten Werte des letzten Zeitpunkts",
         "en": "The matrix `raw` contains measurements: each row is a point in time, each column a sensor. Every sensor has a zero-point error (`offset`) and a gain factor (`gain`), both as vectors with one value per sensor.\n- Use broadcasting to compute `calibrated = (raw - offset) * gain` – without a loop.\n- `sensor2`: all calibrated values of sensor 2 (third column) via slicing\n- `last_row`: the calibrated values of the last point in time"},
   starter={"de": "import numpy as np\n\nraw = np.array([[1.02, 2.10, 0.48],\n                [1.05, 2.16, 0.51],\n                [1.11, 2.25, 0.55]])\noffset = np.array([0.02, 0.10, -0.02])\ngain = np.array([10.0, 5.0, 20.0])\n\n# Ihr Code:\n",
            "en": "import numpy as np\n\nraw = np.array([[1.02, 2.10, 0.48],\n                [1.05, 2.16, 0.51],\n                [1.11, 2.25, 0.55]])\noffset = np.array([0.02, 0.10, -0.02])\ngain = np.array([10.0, 5.0, 20.0])\n\n# your code:\n"},
   solution='import numpy as np\n\nraw = np.array([[1.02, 2.10, 0.48],\n                [1.05, 2.16, 0.51],\n                [1.11, 2.25, 0.55]])\noffset = np.array([0.02, 0.10, -0.02])\ngain = np.array([10.0, 5.0, 20.0])\ncalibrated = (raw - offset) * gain\nsensor2 = calibrated[:, 2]\nlast_row = calibrated[-1, :]\nprint(calibrated)\n',
   tests='''
ns, out = run()
c, s2, lr = need(ns, "calibrated", "sensor2", "last_row")
raw = [[1.02, 2.10, 0.48], [1.05, 2.16, 0.51], [1.11, 2.25, 0.55]]; off = [0.02, 0.10, -0.02]; g = [10.0, 5.0, 20.0]
e = [[(raw[i][j] - off[j]) * g[j] for j in range(3)] for i in range(3)]
check(getattr(c, "shape", None) == (3, 3) and all(approx(c[i, j], e[i][j]) for i in range(3) for j in range(3)), "calibrated stimmt für alle 9 Werte", "calibrated is correct for all 9 values")
check(len(s2) == 3 and all(approx(s2[i], e[i][2]) for i in range(3)), f"sensor2 = {[round(e[i][2], 2) for i in range(3)]}", f"sensor2 = {[round(e[i][2], 2) for i in range(3)]}")
check(len(lr) == 3 and all(approx(lr[j], e[2][j]) for j in range(3)), f"last_row = {[round(x, 2) for x in e[2]]}", f"last_row = {[round(x, 2) for x in e[2]]}")
''',
   require=["numpy", "slice"], forbid=["for", "while", "listcomp"], refs=["9.2b", "9.2"])

ex(id="k9-view", ch="9", lvl=2,
   title={"de": "View oder Kopie?", "en": "View or copy?"},
   task={"de": "Gegeben ist die Matrix `data` (Zeilen = Messreihen).\n1. `block`: die letzten beiden Zeilen und die ersten beiden Spalten (Slicing).\n2. `baseline`: eine **echte Kopie** der ersten Zeile. Setzen Sie anschließend `baseline[0] = 0` – `data` darf sich dadurch nicht ändern.\n3. `col`: die mittlere Spalte als **View**. Verdoppeln Sie über `col` den Wert in der ersten Zeile (`col[0] = col[0] * 2`) – diese Änderung soll in `data` sichtbar sein.",
         "en": "The matrix `data` is given (rows = measurement series).\n1. `block`: the last two rows and the first two columns (slicing).\n2. `baseline`: a **real copy** of the first row. Then set `baseline[0] = 0` – `data` must not change.\n3. `col`: the middle column as a **view**. Double the value in the first row through `col` (`col[0] = col[0] * 2`) – this change should be visible in `data`."},
   starter={"de": "import numpy as np\n\ndata = np.array([[10, 20, 30],\n                 [40, 50, 60],\n                 [70, 80, 90]])\n\n# Ihr Code:\n",
            "en": "import numpy as np\n\ndata = np.array([[10, 20, 30],\n                 [40, 50, 60],\n                 [70, 80, 90]])\n\n# your code:\n"},
   solution='import numpy as np\n\ndata = np.array([[10, 20, 30],\n                 [40, 50, 60],\n                 [70, 80, 90]])\nblock = data[1:, :2]\nbaseline = data[0, :].copy()\nbaseline[0] = 0\ncol = data[:, 1]\ncol[0] = col[0] * 2\nprint(data)\n',
   tests='''
ns, out = run()
d, b, bl, c = need(ns, "data", "block", "baseline", "col")
check(d.tolist() == [[10, 40, 30], [40, 50, 60], [70, 80, 90]], "data: nur der Wert 20 wurde (über col) auf 40 verdoppelt", "data: only the value 20 was doubled to 40 (through col)")
check(getattr(b, "shape", None) == (2, 2) and b.tolist() == [[40, 50], [70, 80]], "block = [[40, 50], [70, 80]]", "block = [[40, 50], [70, 80]]")
check(bl.tolist() == [0, 20, 30], "baseline = [0, 20, 30] (Kopie)", "baseline = [0, 20, 30] (copy)")
check(".copy()" in SOURCE and "col[0]" in SOURCE and "data[" in SOURCE, "Mit Slicing, .copy() und Änderung über die View col gelöst", "Solved with slicing, .copy() and a change through the view col")
class _Code:
    def __init__(self, c): self.c = c
    def __repr__(self): return self.c
ns, out = run(sub={"data": _Code("np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])")})
check(ns["data"].tolist() == [[1, 4, 3], [4, 5, 6], [7, 8, 9]] and ns["block"].tolist() == [[4, 5], [7, 8]] and ns["baseline"].tolist() == [0, 2, 3], "Funktioniert auch mit einer anderen Matrix (keine fest eingetippten Werte)", "Works with another matrix too (no hard-coded values)")
''',
   require=["numpy", "slice"], refs=["9.2", "8.7"])

ex(id="k9-tensile", ch="9", lvl=3,
   title={"de": "Zugversuch mit pandas", "en": "Tensile test with pandas"},
   task={"de": "Ein Zugversuch an einer Rundprobe (Ausgangsdurchmesser `d0` in mm, Messlänge `L0` in mm) liefert Kraft und Verlängerung. Erzeugen Sie aus `data` ein DataFrame `df` und ergänzen Sie die Spalten\n- `sigma_MPa`: Spannung $F/A_0$ in N/mm² mit $A_0 = \\pi d_0^2/4$ (`np.pi`)\n- `eps`: Dehnung $\\Delta L / L_0$\n\nSpeichern Sie die Zugfestigkeit `Rm` (größte Spannung, mit der eingebauten Funktion `max()`) und den Elastizitätsmodul `E` in N/mm² als Mittelwert von $\\sigma/\\varepsilon$ über die ersten drei Messpunkte (`df.head(3)`).",
         "en": "A tensile test on a round specimen (initial diameter `d0` in mm, gauge length `L0` in mm) delivers force and elongation. Create a DataFrame `df` from `data` and add the columns\n- `sigma_MPa`: stress $F/A_0$ in N/mm² with $A_0 = \\pi d_0^2/4$ (`np.pi`)\n- `eps`: strain $\\Delta L / L_0$\n\nStore the tensile strength `Rm` (largest stress, using the built-in function `max()`) and Young's modulus `E` in N/mm² as the mean of $\\sigma/\\varepsilon$ over the first three data points (`df.head(3)`)."},
   starter={"de": "import numpy as np\nimport pandas as pd\n\nd0 = 10.0  # mm\nL0 = 50.0  # mm\ndata = {\n    'F_N': [3927, 7854, 11781, 25000, 31000, 29500],\n    'dL_mm': [0.0119, 0.0238, 0.0357, 1.2, 4.5, 8.0],\n}\n\n# Ihr Code:\n",
            "en": "import numpy as np\nimport pandas as pd\n\nd0 = 10.0  # mm\nL0 = 50.0  # mm\ndata = {\n    'F_N': [3927, 7854, 11781, 25000, 31000, 29500],\n    'dL_mm': [0.0119, 0.0238, 0.0357, 1.2, 4.5, 8.0],\n}\n\n# your code:\n"},
   solution="import numpy as np\nimport pandas as pd\n\nd0 = 10.0\nL0 = 50.0\ndata = {\n    'F_N': [3927, 7854, 11781, 25000, 31000, 29500],\n    'dL_mm': [0.0119, 0.0238, 0.0357, 1.2, 4.5, 8.0],\n}\ndf = pd.DataFrame(data)\nA0 = np.pi * d0**2 / 4\ndf['sigma_MPa'] = df['F_N'] / A0\ndf['eps'] = df['dL_mm'] / L0\nRm = max(df['sigma_MPa'])\nfirst = df.head(3)\nE = (first['sigma_MPa'] / first['eps']).mean()\nprint(df)\nprint(f\"Rm = {Rm:.0f} MPa, E = {E:.0f} MPa\")\n",
   tests='''
import math as _m
F = [3927, 7854, 11781, 25000, 31000, 29500]; dL = [0.0119, 0.0238, 0.0357, 1.2, 4.5, 8.0]
for d0, L0 in [(10.0, 50.0), (8.0, 40.0)]:
    ns, out = run(sub={"d0": d0, "L0": L0})
    df, Rm, E = need(ns, "df", "Rm", "E")
    A0 = _m.pi * d0 * d0 / 4
    sig = [f / A0 for f in F]; eps = [x / L0 for x in dL]
    eE = sum(sig[k] / eps[k] for k in range(3)) / 3
    check(type(df).__name__ == "DataFrame" and "sigma_MPa" in df.columns and "eps" in df.columns, "df hat die Spalten sigma_MPa und eps", "df has the columns sigma_MPa and eps")
    check(all(approx(df["sigma_MPa"].iloc[k], sig[k]) and approx(df["eps"].iloc[k], eps[k]) for k in range(6)), f"d0 = {d0} mm, L0 = {L0} mm: Spannungen und Dehnungen stimmen", f"d0 = {d0} mm, L0 = {L0} mm: stresses and strains are correct")
    check(approx(Rm, max(sig)) and approx(E, eE), f"Rm ≈ {max(sig):.1f} MPa, E ≈ {eE:.0f} MPa", f"Rm ≈ {max(sig):.1f} MPa, E ≈ {eE:.0f} MPa")
''',
   require=["pandas"], refs=["9.4"])

ex(id="k9-beam", ch="9", lvl=3,
   title={"de": "Auflagerkräfte eines Balkens", "en": "Support reactions of a beam"},
   task={"de": "Ein Balken der Länge `L` (m) liegt auf einem Festlager A (bei $x = 0$) und einem Loslager B (bei $x = L$). Er trägt die Einzellasten `F1` bei `a1` und `F2` bei `a2` (kN, m). Aus den Gleichgewichtsbedingungen folgt\n\n$$\\begin{aligned} A + B &= F_1 + F_2 \\\\ L \\cdot B &= F_1 a_1 + F_2 a_2 \\quad \\text{(Momente um A)} \\end{aligned}$$\n\nStellen Sie das System als Matrix `K` und Vektor `rhs` auf, lösen Sie es mit `np.linalg.solve` nach `reactions = [A, B]` und speichern Sie in `ok`, ob `K @ reactions` mit `rhs` übereinstimmt (`np.allclose`).",
         "en": "A beam of length `L` (m) rests on a fixed support A (at $x = 0$) and a roller support B (at $x = L$). It carries the point loads `F1` at `a1` and `F2` at `a2` (kN, m). The equilibrium conditions give\n\n$$\\begin{aligned} A + B &= F_1 + F_2 \\\\ L \\cdot B &= F_1 a_1 + F_2 a_2 \\quad \\text{(moments about A)} \\end{aligned}$$\n\nSet up the system as matrix `K` and vector `rhs`, solve it with `np.linalg.solve` for `reactions = [A, B]` and store in `ok` whether `K @ reactions` matches `rhs` (`np.allclose`)."},
   starter={"de": "import numpy as np\n\nL = 6.0\nF1 = 12.0\na1 = 1.5\nF2 = 8.0\na2 = 4.0\n\n# Ihr Code:\n", "en": "import numpy as np\n\nL = 6.0\nF1 = 12.0\na1 = 1.5\nF2 = 8.0\na2 = 4.0\n\n# your code:\n"},
   solution='import numpy as np\n\nL = 6.0\nF1 = 12.0\na1 = 1.5\nF2 = 8.0\na2 = 4.0\nK = np.array([[1.0, 1.0],\n              [0.0, L]])\nrhs = np.array([F1 + F2, F1 * a1 + F2 * a2])\nreactions = np.linalg.solve(K, rhs)\nok = np.allclose(K @ reactions, rhs)\nprint(f"A = {reactions[0]:.2f} kN, B = {reactions[1]:.2f} kN, Probe: {ok}")\n',
   tests='''
for L, F1, a1, F2, a2 in [(6.0, 12.0, 1.5, 8.0, 4.0), (10.0, 5.0, 5.0, 0.0, 2.0), (4.0, 3.0, 0.0, 7.0, 4.0)]:
    ns, out = run(sub={"L": L, "F1": F1, "a1": a1, "F2": F2, "a2": a2})
    r, ok = need(ns, "reactions", "ok")
    eB = (F1 * a1 + F2 * a2) / L; eA = F1 + F2 - eB
    check(len(r) == 2 and approx(r[0], eA) and approx(r[1], eB), f"L = {L}: A = {eA:.3f} kN, B = {eB:.3f} kN", f"L = {L}: A = {eA:.3f} kN, B = {eB:.3f} kN")
    check(bool(ok) is True, "Probe ok = True", "Check ok = True")
''',
   require=["numpy", "matmul"], refs=["9.2m"])

ex(id="k9-triangle3d", ch="9", lvl=3,
   title={"de": "Dreieck im Raum", "en": "Triangle in space"},
   task={"de": "Drei Eckpunkte einer Dreiecksfläche (z.B. aus einem CAD-Netz) sind als Listen `P1`, `P2`, `P3` gegeben. Berechnen Sie mit NumPy\n- `normal`: das Kreuzprodukt $(P_2 - P_1) \\times (P_3 - P_1)$\n- `area`: die Dreiecksfläche = halbe Länge des Normalenvektors (Länge = $\\sqrt{n \\cdot n}$ mit `np.dot`)\n- `unit_normal`: den Normalenvektor mit Länge 1\n- `right_angle`: ob der Innenwinkel bei P1 ein rechter Winkel ist. Das ist der Fall, wenn das Skalarprodukt $u \\cdot v$ ($u = P_2 - P_1$, $v = P_3 - P_1$) null ist – bei Gleitkommazahlen: `np.isclose(…, 0)`.",
         "en": "Three vertices of a triangular face (e.g. from a CAD mesh) are given as lists `P1`, `P2`, `P3`. Use NumPy to compute\n- `normal`: the cross product $(P_2 - P_1) \\times (P_3 - P_1)$\n- `area`: the triangle area = half the length of the normal vector (length = $\\sqrt{n \\cdot n}$ with `np.dot`)\n- `unit_normal`: the normal vector with length 1\n- `right_angle`: whether the interior angle at P1 is a right angle. That is the case if the dot product $u \\cdot v$ ($u = P_2 - P_1$, $v = P_3 - P_1$) is zero – for floats: `np.isclose(…, 0)`."},
   starter={"de": "import numpy as np\n\nP1 = [0.0, 0.0, 0.0]\nP2 = [4.0, 0.0, 0.0]\nP3 = [0.0, 3.0, 0.0]\n\n# Ihr Code:\n", "en": "import numpy as np\n\nP1 = [0.0, 0.0, 0.0]\nP2 = [4.0, 0.0, 0.0]\nP3 = [0.0, 3.0, 0.0]\n\n# your code:\n"},
   solution='import numpy as np\n\nP1 = [0.0, 0.0, 0.0]\nP2 = [4.0, 0.0, 0.0]\nP3 = [0.0, 3.0, 0.0]\np1 = np.array(P1)\nu = np.array(P2) - p1\nv = np.array(P3) - p1\nnormal = np.cross(u, v)\nlength = np.sqrt(np.dot(normal, normal))\narea = length / 2\nunit_normal = normal / length\nright_angle = bool(np.isclose(np.dot(u, v), 0))\nprint(area, unit_normal, right_angle)\n',
   tests='''
import math as _m
def sub(a, b): return [x - y for x, y in zip(a, b)]
def cross(a, b): return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
def dot(a, b): return sum(x * y for x, y in zip(a, b))
for P1, P2, P3 in [([0.0, 0.0, 0.0], [4.0, 0.0, 0.0], [0.0, 3.0, 0.0]), ([1.0, 2.0, 3.0], [2.0, 4.0, 1.0], [0.0, 3.0, 5.0]), ([0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 2.0])]:
    ns, out = run(sub={"P1": P1, "P2": P2, "P3": P3})
    n, A, un, ra = need(ns, "normal", "area", "unit_normal", "right_angle")
    u, v = sub(P2, P1), sub(P3, P1); en = cross(u, v); L = _m.sqrt(dot(en, en))
    check(len(n) == 3 and all(approx(n[k], en[k]) for k in range(3)), f"normal = {en}", f"normal = {en}")
    check(approx(A, L / 2) and all(approx(un[k], en[k] / L) for k in range(3)), f"Fläche ≈ {L/2:.4f}, Einheitsnormale stimmt", f"area ≈ {L/2:.4f}, unit normal is correct")
    er = abs(dot(u, v)) < 1e-8
    check(bool(ra) is er, f"right_angle = {er}", f"right_angle = {er}")
''',
   require=["numpy"], refs=["9.2m", "9.2v"])

ex(id="k9-fit", ch="9", lvl=3,
   title={"de": "Ausgleichsgerade für einen Temperatursensor", "en": "Best-fit line for a temperature sensor"},
   task={"de": "Ein Platin-Messwiderstand wurde bei mehreren Temperaturen `T` (°C) vermessen, die Widerstände stehen in `R` (Ω). Bestimmen Sie die Ausgleichsgerade $R = m T + c$ nach der Methode der kleinsten Quadrate:\n- Bauen Sie die Matrix `A` mit einer Spalte `T` und einer Spalte Einsen: `np.array([T, np.ones(len(T))]).T`\n- Lösen Sie die Normalgleichungen $(A^\\mathsf{T} A)\\,p = A^\\mathsf{T} R$ mit `np.linalg.solve` und `@`; speichern Sie `slope` = m und `intercept` = c.\n- `alpha`: den Temperaturkoeffizienten m / c (Einheit 1/K)\n- `max_dev`: die größte Abweichung $|R - (m T + c)|$ eines Messpunkts von der Gerade (vektorisiert, mit `abs` und `max`)",
         "en": "A platinum resistance thermometer was measured at several temperatures `T` (°C); the resistances are in `R` (Ω). Determine the best-fit line $R = m T + c$ using least squares:\n- Build the matrix `A` with a column `T` and a column of ones: `np.array([T, np.ones(len(T))]).T`\n- Solve the normal equations $(A^\\mathsf{T} A)\\,p = A^\\mathsf{T} R$ with `np.linalg.solve` and `@`; store `slope` = m and `intercept` = c.\n- `alpha`: the temperature coefficient m / c (unit 1/K)\n- `max_dev`: the largest deviation $|R - (m T + c)|$ of a data point from the line (vectorised, using `abs` and `max`)"},
   starter={"de": "import numpy as np\n\nT = [0.0, 20.0, 40.0, 60.0, 80.0, 100.0]\nR = [100.0, 107.8, 115.5, 123.3, 131.0, 138.6]\n\n# Ihr Code:\n", "en": "import numpy as np\n\nT = [0.0, 20.0, 40.0, 60.0, 80.0, 100.0]\nR = [100.0, 107.8, 115.5, 123.3, 131.0, 138.6]\n\n# your code:\n"},
   solution='import numpy as np\n\nT = [0.0, 20.0, 40.0, 60.0, 80.0, 100.0]\nR = [100.0, 107.8, 115.5, 123.3, 131.0, 138.6]\nt = np.array(T)\nr = np.array(R)\nA = np.array([t, np.ones(len(t))]).T\np = np.linalg.solve(A.T @ A, A.T @ r)\nslope = p[0]\nintercept = p[1]\nalpha = slope / intercept\nmax_dev = max(abs(r - (slope * t + intercept)))\nprint(f"R = {slope:.4f} * T + {intercept:.3f}, alpha = {alpha:.5f} 1/K, max. Abweichung {max_dev:.3f} Ohm")\n',
   tests='''
def fit(x, y):
    n = len(x); sx = sum(x); sy = sum(y); sxx = sum(a * a for a in x); sxy = sum(a * b for a, b in zip(x, y))
    m = (n * sxy - sx * sy) / (n * sxx - sx * sx); c = (sy - m * sx) / n
    return m, c, max(abs(b - (m * a + c)) for a, b in zip(x, y))
for T, R in [([0.0, 20.0, 40.0, 60.0, 80.0, 100.0], [100.0, 107.8, 115.5, 123.3, 131.0, 138.6]), ([1.0, 2.0, 3.0], [2.0, 4.1, 5.9]), ([-10.0, 0.0, 10.0, 25.0], [96.1, 100.0, 103.9, 109.7])]:
    ns, out = run(sub={"T": T, "R": R})
    s, c, a, d = need(ns, "slope", "intercept", "alpha", "max_dev")
    em, ec, ed = fit(T, R)
    check(approx(s, em, 1e-6) and approx(c, ec, 1e-6), f"Gerade R = {em:.4f}·T + {ec:.3f}", f"line R = {em:.4f}·T + {ec:.3f}")
    check(approx(a, em / ec, 1e-6), f"alpha ≈ {em/ec:.5f} 1/K", f"alpha ≈ {em/ec:.5f} 1/K")
    check(approx(d, ed, 1e-6), f"größte Abweichung ≈ {ed:.4f} Ω", f"largest deviation ≈ {ed:.4f} Ω")
check("solve" in SOURCE and "@" in SOURCE, "Mit np.linalg.solve und @ gelöst", "Solved with np.linalg.solve and @")
''',
   require=["numpy", "matmul"], refs=["9.2m", "9.2v"])
