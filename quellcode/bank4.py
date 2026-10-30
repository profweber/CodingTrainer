from exlib import ex

# Vierter Satz (v1.1): Kapitel 9 hat ohne pandas 30 Aufgaben (je 10 pro Stufe),
# dazu kommen 10 pandas-Aufgaben. Gesamt: 250 ohne pandas, 260 mit pandas.

# ================================================================== Kapitel 9 – NumPy
ex(id="k9-cantilever", ch="9", lvl=2,
   title={"de": "Biegelinie eines Kragarms", "en": "Deflection curve of a cantilever"},
   task={"de": "Ein einseitig eingespannter Träger (Kragarm) der Länge `L` (m) trägt am freien Ende die Kraft `F` (N). Mit dem E-Modul `E` (N/m²) und dem Flächenträgheitsmoment `I` (m⁴) gilt für die Durchbiegung an der Stelle $x$\n\n$$w(x) = \\frac{F \\, x^2 \\, (3L - x)}{6 \\, E \\, I}$$\n\nBerechnen Sie **ohne Schleife**\n- `x`: `n` gleichmäßig verteilte Stellen von 0 bis einschließlich `L` (Array, `np.linspace`)\n- `w_mm`: die Durchbiegungen an diesen Stellen in mm (Array)\n- `w_end`: die Durchbiegung am freien Ende in mm (letztes Element)\n- `w_mid`: die Durchbiegung in der Mitte in mm (das mittlere Element; `n` ist ungerade)\n- `ratio`: das Verhältnis `w_mid / w_end`\n- `ok`: ob `w_end` höchstens L/300 beträgt (zulässige Durchbiegung, ebenfalls in mm)",
         "en": "A beam clamped at one end (cantilever) of length `L` (m) carries the force `F` (N) at its free end. With Young's modulus `E` (N/m²) and the second moment of area `I` (m⁴), the deflection at position $x$ is\n\n$$w(x) = \\frac{F \\, x^2 \\, (3L - x)}{6 \\, E \\, I}$$\n\nCompute **without a loop**\n- `x`: `n` evenly spaced positions from 0 up to and including `L` (array, `np.linspace`)\n- `w_mm`: the deflections at these positions in mm (array)\n- `w_end`: the deflection at the free end in mm (last element)\n- `w_mid`: the deflection in the middle in mm (the middle element; `n` is odd)\n- `ratio`: the ratio `w_mid / w_end`\n- `ok`: whether `w_end` is at most L/300 (permissible deflection, also in mm)"},
   starter={"de": "import numpy as np\n\nF = 2000.0     # N\nL = 1.5        # m\nE = 210e9      # N/m² (Stahl)\nI = 8.36e-6    # m⁴ (IPE 160)\nn = 21         # Anzahl der Stellen (ungerade)\n\n# Ihr Code:\n",
            "en": "import numpy as np\n\nF = 2000.0     # N\nL = 1.5        # m\nE = 210e9      # N/m² (steel)\nI = 8.36e-6    # m⁴ (IPE 160)\nn = 21         # number of positions (odd)\n\n# your code:\n"},
   solution='import numpy as np\n\nF = 2000.0\nL = 1.5\nE = 210e9\nI = 8.36e-6\nn = 21\nx = np.linspace(0, L, n)\nw_mm = F * x**2 * (3 * L - x) / (6 * E * I) * 1000\nw_end = w_mm[-1]\nw_mid = w_mm[n // 2]\nratio = w_mid / w_end\nok = w_end <= L * 1000 / 300\nprint(f"w_end = {w_end:.2f} mm, w_mid = {w_mid:.2f} mm, zulässig: {ok}")\n',
   tests='''
for F, L, E, I, n in [(2000.0, 1.5, 210e9, 8.36e-6, 21), (5000.0, 2.0, 70e9, 2.0e-6, 11), (800.0, 0.8, 210e9, 1.0e-7, 5), (2101.05, 1.0, 210e9, 1.0e-6, 3)]:
    ns, out = run(sub={"F": F, "L": L, "E": E, "I": I, "n": n})
    x, w, we, wm, r, ok = need(ns, "x", "w_mm", "w_end", "w_mid", "ratio", "ok")
    ex_ = [L * k / (n - 1) for k in range(n)]
    ew = [F * xx**2 * (3 * L - xx) / (6 * E * I) * 1000 for xx in ex_]
    check(type(x).__name__ == "ndarray" and len(x) == n and approx(x[0], 0) and approx(x[-1], L), f"n = {n}: x von 0 bis {L} m (n Werte)", f"n = {n}: x from 0 to {L} m (n values)")
    check(type(w).__name__ == "ndarray" and all(approx(a, b) for a, b in zip(w, ew)), f"w_mm stimmt (Ende {ew[-1]:.3f} mm)", f"w_mm is correct (end {ew[-1]:.3f} mm)")
    check(approx(we, ew[-1]) and approx(wm, ew[n // 2]), f"w_end = {ew[-1]:.3f} mm, w_mid = {ew[n // 2]:.3f} mm", f"w_end = {ew[-1]:.3f} mm, w_mid = {ew[n // 2]:.3f} mm")
    check(approx(r, 5 / 16), "ratio = 5/16 = 0.3125 (gilt für jeden Kragarm)", "ratio = 5/16 = 0.3125 (true for every cantilever)")
    check(bool(ok) is (ew[-1] <= L * 1000 / 300), f"ok = {ew[-1] <= L * 1000 / 300} (Grenze {L * 1000 / 300:.2f} mm)", f"ok = {ew[-1] <= L * 1000 / 300} (limit {L * 1000 / 300:.2f} mm)")
''',
   require=["numpy"], forbid=["for", "while", "listcomp"], refs=["9.2v", "9.2"])

ex(id="k9-dcnetwork", ch="9", lvl=3,
   title={"de": "Gleichstromnetz mit Knotenpotentialen", "en": "DC network with node voltages"},
   task={"de": "In einem Netzwerk speist die Quelle `U0` über `R1` den Knoten 1, die Quelle `Ub` über `R5` den Knoten 2. Von Knoten 1 führt `R2` nach Masse, von Knoten 2 führt `R4` nach Masse, und `R3` verbindet die beiden Knoten. Für die Knotenspannungen $U_1, U_2$ (gegen Masse) gilt das Gleichungssystem $G \\cdot U = b$ mit\n\n$$G = \\begin{pmatrix} \\frac{1}{R_1} + \\frac{1}{R_2} + \\frac{1}{R_3} & -\\frac{1}{R_3} \\\\ -\\frac{1}{R_3} & \\frac{1}{R_3} + \\frac{1}{R_4} + \\frac{1}{R_5} \\end{pmatrix}, \\qquad b = \\begin{pmatrix} U_0 / R_1 \\\\ U_b / R_5 \\end{pmatrix}$$\n\nStellen Sie `G` und `b` als Arrays auf, lösen Sie mit `np.linalg.solve` und speichern Sie\n- `U1`, `U2`: die Knotenspannungen (V)\n- `I3`: den Strom durch `R3` von Knoten 1 nach Knoten 2 (A)\n- `P_src`: die von beiden Quellen abgegebene Leistung $U_0 \\cdot \\dfrac{U_0 - U_1}{R_1} + U_b \\cdot \\dfrac{U_b - U_2}{R_5}$ (W)\n- `P_res`: die Summe der Leistungen $U^2/R$ in allen fünf Widerständen (W); die Spannung an `R1` ist $U_0 - U_1$, an `R5` ist sie $U_b - U_2$\n- `balance_ok`: ob `P_src` und `P_res` übereinstimmen (`np.isclose`)",
         "en": "In a network, source `U0` feeds node 1 via `R1`, source `Ub` feeds node 2 via `R5`. `R2` connects node 1 to ground, `R4` connects node 2 to ground, and `R3` connects the two nodes. The node voltages $U_1, U_2$ (to ground) satisfy the system $G \\cdot U = b$ with\n\n$$G = \\begin{pmatrix} \\frac{1}{R_1} + \\frac{1}{R_2} + \\frac{1}{R_3} & -\\frac{1}{R_3} \\\\ -\\frac{1}{R_3} & \\frac{1}{R_3} + \\frac{1}{R_4} + \\frac{1}{R_5} \\end{pmatrix}, \\qquad b = \\begin{pmatrix} U_0 / R_1 \\\\ U_b / R_5 \\end{pmatrix}$$\n\nSet up `G` and `b` as arrays, solve with `np.linalg.solve` and store\n- `U1`, `U2`: the node voltages (V)\n- `I3`: the current through `R3` from node 1 to node 2 (A)\n- `P_src`: the power delivered by both sources $U_0 \\cdot \\dfrac{U_0 - U_1}{R_1} + U_b \\cdot \\dfrac{U_b - U_2}{R_5}$ (W)\n- `P_res`: the sum of the powers $U^2/R$ in all five resistors (W); the voltage across `R1` is $U_0 - U_1$, across `R5` it is $U_b - U_2$\n- `balance_ok`: whether `P_src` and `P_res` agree (`np.isclose`)"},
   starter={"de": "import numpy as np\n\nU0 = 12.0   # V\nUb = 5.0    # V\nR1 = 100.0  # Ohm\nR2 = 220.0\nR3 = 150.0\nR4 = 330.0\nR5 = 47.0\n\n# Ihr Code:\n",
            "en": "import numpy as np\n\nU0 = 12.0   # V\nUb = 5.0    # V\nR1 = 100.0  # Ohm\nR2 = 220.0\nR3 = 150.0\nR4 = 330.0\nR5 = 47.0\n\n# your code:\n"},
   solution='import numpy as np\n\nU0 = 12.0\nUb = 5.0\nR1 = 100.0\nR2 = 220.0\nR3 = 150.0\nR4 = 330.0\nR5 = 47.0\nG = np.array([[1 / R1 + 1 / R2 + 1 / R3, -1 / R3],\n              [-1 / R3, 1 / R3 + 1 / R4 + 1 / R5]])\nb = np.array([U0 / R1, Ub / R5])\nU = np.linalg.solve(G, b)\nU1 = U[0]\nU2 = U[1]\nI3 = (U1 - U2) / R3\nP_src = U0 * (U0 - U1) / R1 + Ub * (Ub - U2) / R5\nP_res = (U0 - U1)**2 / R1 + U1**2 / R2 + (U1 - U2)**2 / R3 + U2**2 / R4 + (Ub - U2)**2 / R5\nbalance_ok = np.isclose(P_src, P_res)\nprint(f"U1 = {U1:.3f} V, U2 = {U2:.3f} V, I3 = {I3 * 1000:.2f} mA, P = {P_src:.4f} W, Bilanz: {balance_ok}")\n',
   tests='''
def _solve(U0, Ub, R1, R2, R3, R4, R5):
    a, b_, c, d = 1 / R1 + 1 / R2 + 1 / R3, -1 / R3, -1 / R3, 1 / R3 + 1 / R4 + 1 / R5
    r1, r2 = U0 / R1, Ub / R5
    det = a * d - b_ * c
    return (r1 * d - b_ * r2) / det, (a * r2 - c * r1) / det
for p in [(12.0, 5.0, 100.0, 220.0, 150.0, 330.0, 47.0), (24.0, 0.0, 1000.0, 1000.0, 500.0, 2000.0, 1000.0), (5.0, 9.0, 10.0, 47.0, 22.0, 100.0, 33.0)]:
    U0, Ub, R1, R2, R3, R4, R5 = p
    ns, out = run(sub=dict(zip(["U0", "Ub", "R1", "R2", "R3", "R4", "R5"], p)))
    u1, u2, i3, ps, pr, ok = need(ns, "U1", "U2", "I3", "P_src", "P_res", "balance_ok")
    e1, e2 = _solve(*p)
    eps = U0 * (U0 - e1) / R1 + Ub * (Ub - e2) / R5
    check(approx(u1, e1) and approx(u2, e2), f"U0 = {U0} V, Ub = {Ub} V: U1 = {e1:.4f} V, U2 = {e2:.4f} V", f"U0 = {U0} V, Ub = {Ub} V: U1 = {e1:.4f} V, U2 = {e2:.4f} V")
    check(approx(i3, (e1 - e2) / R3), f"I3 = {(e1 - e2) / R3 * 1000:.3f} mA (von Knoten 1 nach 2)", f"I3 = {(e1 - e2) / R3 * 1000:.3f} mA (from node 1 to 2)")
    check(approx(ps, eps) and approx(pr, eps), f"P_src = P_res = {eps:.5f} W", f"P_src = P_res = {eps:.5f} W")
    check(bool(ok) is True, "balance_ok = True", "balance_ok = True")
''',
   require=["numpy"], refs=["9.2m"])

ex(id="k9-alloy", ch="9", lvl=3,
   title={"de": "Legierung mischen", "en": "Mixing an alloy"},
   task={"de": "Aus drei vorrätigen Legierungen soll durch Einschmelzen die Menge `m_total` (kg) einer neuen Legierung mit der Zusammensetzung `target` (Massenanteile Kupfer, Zink, Zinn) entstehen. In der Liste `alloys` steht für jede vorrätige Legierung eine Liste ihrer Anteile (Kupfer, Zink, Zinn). Gesucht sind die Massen $x_1, x_2, x_3$, die man von jeder Legierung einsetzen muss: Für jedes Element muss die Summe über alle Legierungen (Anteil · Masse) gleich `m_total` · Zielanteil sein.\n- `M`: die Matrix des Gleichungssystems – Zeile = Element, Spalte = Legierung, also `np.array(alloys)` transponiert\n- `x`: die Massen als Array (`np.linalg.solve`)\n- `feasible`: ob alle Massen größer oder gleich 0 sind – nur dann lässt sich die Legierung herstellen (eingebaute Funktion `min`)\n- `cost`: die Rohstoffkosten in €, wenn `prices` die Preise der drei Legierungen in €/kg enthält (Skalarprodukt mit `np.dot`)",
         "en": "Melting down three alloys in stock is to produce the amount `m_total` (kg) of a new alloy with the composition `target` (mass fractions of copper, zinc, tin). The list `alloys` contains, for each alloy in stock, a list of its fractions (copper, zinc, tin). We need the masses $x_1, x_2, x_3$ to take from each alloy: for each element, the sum over all alloys (fraction · mass) must equal `m_total` · target fraction.\n- `M`: the matrix of the system – row = element, column = alloy, i.e. `np.array(alloys)` transposed\n- `x`: the masses as an array (`np.linalg.solve`)\n- `feasible`: whether all masses are greater than or equal to 0 – only then can the alloy be made (built-in function `min`)\n- `cost`: the raw-material cost in € if `prices` contains the prices of the three alloys in €/kg (dot product with `np.dot`)"},
   starter={"de": "import numpy as np\n\nalloys = [\n    [0.70, 0.30, 0.00],   # Messing\n    [0.60, 0.25, 0.15],   # Rotguss\n    [0.90, 0.00, 0.10],   # Bronze\n]\ntarget = [0.72, 0.20, 0.08]   # Kupfer, Zink, Zinn\nm_total = 500.0               # kg\nprices = [6.8, 8.4, 9.9]      # €/kg\n\n# Ihr Code:\n",
            "en": "import numpy as np\n\nalloys = [\n    [0.70, 0.30, 0.00],   # brass\n    [0.60, 0.25, 0.15],   # gunmetal\n    [0.90, 0.00, 0.10],   # bronze\n]\ntarget = [0.72, 0.20, 0.08]   # copper, zinc, tin\nm_total = 500.0               # kg\nprices = [6.8, 8.4, 9.9]      # €/kg\n\n# your code:\n"},
   solution='import numpy as np\n\nalloys = [\n    [0.70, 0.30, 0.00],\n    [0.60, 0.25, 0.15],\n    [0.90, 0.00, 0.10],\n]\ntarget = [0.72, 0.20, 0.08]\nm_total = 500.0\nprices = [6.8, 8.4, 9.9]\nM = np.array(alloys).T\nx = np.linalg.solve(M, m_total * np.array(target))\nfeasible = min(x) >= 0\ncost = np.dot(x, prices)\nprint(x, feasible, f"{cost:.2f} EUR")\n',
   tests='''
def _solve3(A, r):
    def det(m):
        return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
    D = det(A)
    res = []
    for j in range(3):
        Aj = [[r[i] if k == j else A[i][k] for k in range(3)] for i in range(3)]
        res.append(det(Aj) / D)
    return res
AL = [[0.70, 0.30, 0.00], [0.60, 0.25, 0.15], [0.90, 0.00, 0.10]]
AL2 = [[0.50, 0.50, 0.00], [0.80, 0.10, 0.10], [0.95, 0.00, 0.05]]
for al, tg, m, pr in [(AL, [0.72, 0.20, 0.08], 500.0, [6.8, 8.4, 9.9]), (AL, [0.65, 0.30, 0.05], 200.0, [6.0, 8.0, 10.0]), (AL2, [0.80, 0.15, 0.05], 100.0, [5.0, 7.0, 9.0])]:
    ns, out = run(sub={"alloys": al, "target": tg, "m_total": m, "prices": pr})
    M, x, fe, co = need(ns, "M", "x", "feasible", "cost")
    A = [[al[j][i] for j in range(3)] for i in range(3)]
    ex_ = _solve3(A, [m * t for t in tg])
    check(type(M).__name__ == "ndarray" and all(approx(M[i][j], A[i][j]) for i in range(3) for j in range(3)), "M: Zeile = Element, Spalte = Legierung", "M: row = element, column = alloy")
    check(type(x).__name__ == "ndarray" and len(x) == 3 and all(approx(a, b) for a, b in zip(x, ex_)), f"x = {[round(v, 2) for v in ex_]} kg", f"x = {[round(v, 2) for v in ex_]} kg")
    check(bool(fe) is (min(ex_) >= -1e-9), f"feasible = {min(ex_) >= -1e-9}", f"feasible = {min(ex_) >= -1e-9}")
    check(approx(co, sum(a * b for a, b in zip(ex_, pr))), f"cost = {sum(a * b for a, b in zip(ex_, pr)):.2f} €", f"cost = {sum(a * b for a, b in zip(ex_, pr)):.2f} €")
''',
   require=["numpy"], refs=["9.2m"])

ex(id="k9-robotarm", ch="9", lvl=3,
   title={"de": "Zweigelenk-Roboterarm", "en": "Two-joint robot arm"},
   task={"de": "Ein ebener Roboterarm besteht aus zwei Gliedern der Längen `l1` und `l2` (m). Für mehrere Stellungen sind die Gelenkwinkel in den Listen `theta1` und `theta2` (Grad) gegeben; $\\theta_2$ wird relativ zum ersten Glied gemessen. Die Position des Greifers ist\n\n$$x = l_1 \\cos\\theta_1 + l_2 \\cos(\\theta_1 + \\theta_2), \\qquad y = l_1 \\sin\\theta_1 + l_2 \\sin(\\theta_1 + \\theta_2)$$\n\nBerechnen Sie für alle Stellungen gleichzeitig, also **ohne Schleife**:\n- `t1`, `t2`: die Winkel im Bogenmaß (Arrays, `np.pi`)\n- `x`, `y`: die Greiferpositionen (Arrays, `np.cos`, `np.sin`)\n- `r`: die Abstände des Greifers vom Fußpunkt (Array, `np.sqrt`)\n- `farthest`: den Index der Stellung mit dem größten Abstand (Tipp: `list(r)`, `max` und `index`)\n- `check_ok`: ob für alle Stellungen der Kosinussatz $r^2 = l_1^2 + l_2^2 + 2\\, l_1 l_2 \\cos\\theta_2$ erfüllt ist (`np.allclose`)",
         "en": "A planar robot arm consists of two links of lengths `l1` and `l2` (m). For several poses the joint angles are given in the lists `theta1` and `theta2` (degrees); $\\theta_2$ is measured relative to the first link. The gripper position is\n\n$$x = l_1 \\cos\\theta_1 + l_2 \\cos(\\theta_1 + \\theta_2), \\qquad y = l_1 \\sin\\theta_1 + l_2 \\sin(\\theta_1 + \\theta_2)$$\n\nCompute for all poses at once, i.e. **without a loop**:\n- `t1`, `t2`: the angles in radians (arrays, `np.pi`)\n- `x`, `y`: the gripper positions (arrays, `np.cos`, `np.sin`)\n- `r`: the distances of the gripper from the base (array, `np.sqrt`)\n- `farthest`: the index of the pose with the largest distance (tip: `list(r)`, `max` and `index`)\n- `check_ok`: whether the law of cosines $r^2 = l_1^2 + l_2^2 + 2\\, l_1 l_2 \\cos\\theta_2$ holds for all poses (`np.allclose`)"},
   starter={"de": "import numpy as np\n\nl1 = 0.40   # m\nl2 = 0.30   # m\ntheta1 = [0.0, 30.0, 45.0, 90.0, 120.0]   # Grad\ntheta2 = [90.0, 45.0, 10.0, -60.0, 30.0]  # Grad\n\n# Ihr Code:\n",
            "en": "import numpy as np\n\nl1 = 0.40   # m\nl2 = 0.30   # m\ntheta1 = [0.0, 30.0, 45.0, 90.0, 120.0]   # degrees\ntheta2 = [90.0, 45.0, 10.0, -60.0, 30.0]  # degrees\n\n# your code:\n"},
   solution='import numpy as np\n\nl1 = 0.40\nl2 = 0.30\ntheta1 = [0.0, 30.0, 45.0, 90.0, 120.0]\ntheta2 = [90.0, 45.0, 10.0, -60.0, 30.0]\nt1 = np.array(theta1) * np.pi / 180\nt2 = np.array(theta2) * np.pi / 180\nx = l1 * np.cos(t1) + l2 * np.cos(t1 + t2)\ny = l1 * np.sin(t1) + l2 * np.sin(t1 + t2)\nr = np.sqrt(x**2 + y**2)\nfarthest = list(r).index(max(r))\ncheck_ok = np.allclose(r**2, l1**2 + l2**2 + 2 * l1 * l2 * np.cos(t2))\nprint(x, y)\nprint(f"Stellung {farthest} reicht am weitesten, Kosinussatz erfüllt: {check_ok}")\n',
   tests='''
import math as _m
for l1, l2, th1, th2 in [(0.40, 0.30, [0.0, 30.0, 45.0, 90.0, 120.0], [90.0, 45.0, 10.0, -60.0, 30.0]), (1.0, 0.5, [10.0, 80.0, -30.0], [170.0, 0.0, 90.0]), (0.2, 0.2, [0.0, 90.0], [120.0, -150.0])]:
    ns, out = run(sub={"l1": l1, "l2": l2, "theta1": th1, "theta2": th2})
    t1, t2, x, y, r, fa, ck = need(ns, "t1", "t2", "x", "y", "r", "farthest", "check_ok")
    a1 = [v * _m.pi / 180 for v in th1]; a2 = [v * _m.pi / 180 for v in th2]
    ex_ = [l1 * _m.cos(p) + l2 * _m.cos(p + q) for p, q in zip(a1, a2)]
    ey = [l1 * _m.sin(p) + l2 * _m.sin(p + q) for p, q in zip(a1, a2)]
    er = [_m.sqrt(a * a + b * b) for a, b in zip(ex_, ey)]
    check(type(t1).__name__ == "ndarray" and all(approx(a, b) for a, b in zip(t1, a1)) and all(approx(a, b) for a, b in zip(t2, a2)), "t1, t2 im Bogenmaß", "t1, t2 in radians")
    check(type(x).__name__ == "ndarray" and all(approx(a, b) for a, b in zip(x, ex_)) and all(approx(a, b) for a, b in zip(y, ey)), f"x = {[round(v, 3) for v in ex_]}, y = {[round(v, 3) for v in ey]}", f"x = {[round(v, 3) for v in ex_]}, y = {[round(v, 3) for v in ey]}")
    check(type(r).__name__ == "ndarray" and all(approx(a, b) for a, b in zip(r, er)), "r stimmt", "r is correct")
    check(fa == er.index(max(er)), f"farthest = {er.index(max(er))}", f"farthest = {er.index(max(er))}")
    check(bool(ck) is True, "check_ok = True", "check_ok = True")
''',
   require=["numpy"], forbid=["for", "while", "listcomp"], refs=["9.2v", "9.2"])

# ================================================================== Kapitel 9 – pandas
ex(id="k9-dfprotocol", ch="9", lvl=1,
   title={"de": "Messprotokoll als DataFrame", "en": "Test log as a DataFrame"},
   task={"de": "Bei einem Federversuch wurden Kraft und Federweg gemessen; die Werte stehen im Dictionary `data`. Erzeugen Sie daraus mit pandas das DataFrame `df` und geben Sie es mit `print(df.head())` aus. Speichern Sie außerdem\n- `n_rows`: die Anzahl der Messungen (`len`)\n- `F_mean`: die mittlere Kraft (pandas-Methode `mean`)\n- `s_std`: die Standardabweichung des Federwegs (pandas-Methode `std`)",
         "en": "In a spring test, force and spring travel were measured; the values are in the dictionary `data`. Create the DataFrame `df` from it with pandas and print it with `print(df.head())`. Also store\n- `n_rows`: the number of measurements (`len`)\n- `F_mean`: the mean force (pandas method `mean`)\n- `s_std`: the standard deviation of the spring travel (pandas method `std`)"},
   starter={"de": "import pandas as pd\n\ndata = {\n    'messung': [1, 2, 3, 4, 5],\n    'kraft_N': [10.0, 20.0, 30.0, 40.0, 50.0],\n    'weg_mm': [4.1, 8.0, 12.2, 15.9, 20.1],\n}\n\n# Ihr Code:\n",
            "en": "import pandas as pd\n\ndata = {\n    'messung': [1, 2, 3, 4, 5],\n    'kraft_N': [10.0, 20.0, 30.0, 40.0, 50.0],\n    'weg_mm': [4.1, 8.0, 12.2, 15.9, 20.1],\n}\n\n# your code:\n"},
   solution="import pandas as pd\n\ndata = {\n    'messung': [1, 2, 3, 4, 5],\n    'kraft_N': [10.0, 20.0, 30.0, 40.0, 50.0],\n    'weg_mm': [4.1, 8.0, 12.2, 15.9, 20.1],\n}\ndf = pd.DataFrame(data)\nprint(df.head())\nn_rows = len(df)\nF_mean = df['kraft_N'].mean()\ns_std = df['weg_mm'].std()\nprint(n_rows, F_mean, round(s_std, 3))\n",
   tests='''
import statistics as _st
D1 = {'messung': [1, 2, 3, 4, 5], 'kraft_N': [10.0, 20.0, 30.0, 40.0, 50.0], 'weg_mm': [4.1, 8.0, 12.2, 15.9, 20.1]}
D2 = {'messung': [1, 2, 3], 'kraft_N': [5.0, 7.5, 12.0], 'weg_mm': [1.0, 1.6, 2.3]}
for d in [D1, D2]:
    ns, out = run(sub={"data": d})
    df, n, fm, ss = need(ns, "df", "n_rows", "F_mean", "s_std")
    check(type(df).__name__ == "DataFrame" and list(df.columns) == list(d.keys()) and len(df) == len(d['kraft_N']), f"df mit {len(d['kraft_N'])} Zeilen und den Spalten aus data", f"df with {len(d['kraft_N'])} rows and the columns from data")
    check(n == len(d['kraft_N']), f"n_rows = {len(d['kraft_N'])}", f"n_rows = {len(d['kraft_N'])}")
    check(approx(fm, sum(d['kraft_N']) / len(d['kraft_N'])), f"F_mean = {sum(d['kraft_N']) / len(d['kraft_N']):.3f} N", f"F_mean = {sum(d['kraft_N']) / len(d['kraft_N']):.3f} N")
    check(approx(ss, _st.stdev(d['weg_mm'])), f"s_std = {_st.stdev(d['weg_mm']):.4f} mm (Stichproben-Standardabweichung)", f"s_std = {_st.stdev(d['weg_mm']):.4f} mm (sample standard deviation)")
    check("weg_mm" in out, "df.head() wird ausgegeben", "df.head() is printed")
''',
   require=["pandas"], refs=["9.4"])

ex(id="k9-devicecosts", ch="9", lvl=1,
   title={"de": "Stromkosten je Gerät", "en": "Electricity costs per device"},
   task={"de": "Im Dictionary `data` stehen für einige Geräte einer Werkstatt die Leistung (W) und die tägliche Betriebszeit (h). Erzeugen Sie daraus das DataFrame `df` und fügen Sie zwei Spalten hinzu:\n- `kwh_jahr`: der Jahresverbrauch in kWh (Leistung · Stunden pro Tag · 365 / 1000)\n- `kosten_EUR`: die Jahreskosten (Jahresverbrauch · Strompreis `price` in €/kWh)\n\nSpeichern Sie außerdem die Gesamtkosten aller Geräte in `total` (eingebaute Funktion `sum` auf die Spalte) und geben Sie `df` aus.",
         "en": "The dictionary `data` contains the power (W) and the daily operating time (h) of some devices in a workshop. Create the DataFrame `df` from it and add two columns:\n- `kwh_jahr`: the annual consumption in kWh (power · hours per day · 365 / 1000)\n- `kosten_EUR`: the annual cost (annual consumption · electricity price `price` in €/kWh)\n\nAlso store the total cost of all devices in `total` (built-in function `sum` on the column) and print `df`."},
   starter={"de": "import pandas as pd\n\nprice = 0.30  # €/kWh\ndata = {\n    'geraet': ['Kompressor', 'Bohrmaschine', 'Beleuchtung', 'Kühlschrank'],\n    'leistung_W': [1500.0, 800.0, 400.0, 120.0],\n    'stunden_pro_tag': [3.0, 1.5, 9.0, 24.0],\n}\n\n# Ihr Code:\n",
            "en": "import pandas as pd\n\nprice = 0.30  # €/kWh\ndata = {\n    'geraet': ['compressor', 'drill', 'lighting', 'fridge'],\n    'leistung_W': [1500.0, 800.0, 400.0, 120.0],\n    'stunden_pro_tag': [3.0, 1.5, 9.0, 24.0],\n}\n\n# your code:\n"},
   solution="import pandas as pd\n\nprice = 0.30\ndata = {\n    'geraet': ['Kompressor', 'Bohrmaschine', 'Beleuchtung', 'Kühlschrank'],\n    'leistung_W': [1500.0, 800.0, 400.0, 120.0],\n    'stunden_pro_tag': [3.0, 1.5, 9.0, 24.0],\n}\ndf = pd.DataFrame(data)\ndf['kwh_jahr'] = df['leistung_W'] * df['stunden_pro_tag'] * 365 / 1000\ndf['kosten_EUR'] = df['kwh_jahr'] * price\ntotal = sum(df['kosten_EUR'])\nprint(df)\nprint(f\"Gesamtkosten: {total:.2f} EUR\")\n",
   tests='''
D1 = {'geraet': ['A', 'B', 'C', 'D'], 'leistung_W': [1500.0, 800.0, 400.0, 120.0], 'stunden_pro_tag': [3.0, 1.5, 9.0, 24.0]}
D2 = {'geraet': ['X', 'Y'], 'leistung_W': [2000.0, 60.0], 'stunden_pro_tag': [0.5, 12.0]}
for d, pr in [(D1, 0.30), (D2, 0.25)]:
    ns, out = run(sub={"data": d, "price": pr})
    df, tot = need(ns, "df", "total")
    kwh = [p * h * 365 / 1000 for p, h in zip(d['leistung_W'], d['stunden_pro_tag'])]
    check(type(df).__name__ == "DataFrame" and "kwh_jahr" in df.columns and "kosten_EUR" in df.columns, "df hat die Spalten kwh_jahr und kosten_EUR", "df has the columns kwh_jahr and kosten_EUR")
    check(all(approx(a, b) for a, b in zip(list(df['kwh_jahr']), kwh)), f"kwh_jahr = {[round(v, 1) for v in kwh]}", f"kwh_jahr = {[round(v, 1) for v in kwh]}")
    check(all(approx(a, b * pr) for a, b in zip(list(df['kosten_EUR']), kwh)), f"kosten_EUR mit price = {pr} €/kWh", f"kosten_EUR with price = {pr} €/kWh")
    check(approx(tot, sum(kwh) * pr), f"total = {sum(kwh) * pr:.2f} €", f"total = {sum(kwh) * pr:.2f} €")
''',
   require=["pandas"], refs=["9.4"])

ex(id="k9-weather", ch="9", lvl=1,
   title={"de": "Wetterstation: CSV einlesen", "en": "Weather station: reading a CSV file"},
   task={"de": "Die Datei `data/wetter.csv` enthält die Tageswerte einer Wetterstation mit den Spalten `datum`, `temp_C`, `wind_ms` und `regen_mm`. Lesen Sie die Datei mit `pd.read_csv` in das DataFrame `df` ein, geben Sie mit `print(df.describe())` einen Überblick aus und speichern Sie\n- `n_days`: die Anzahl der Tage (`len`)\n- `temp_mean`: die mittlere Temperatur (pandas-Methode `mean`)\n- `wind_max`: die größte Windgeschwindigkeit (eingebaute Funktion `max` auf die Spalte)\n- `rain_total`: die gesamte Regenmenge (eingebaute Funktion `sum` auf die Spalte)\n\nZum Ausprobieren wird beim Ausführen eine Beispieldatei angelegt.",
         "en": "The file `data/wetter.csv` contains the daily values of a weather station with the columns `datum`, `temp_C`, `wind_ms` and `regen_mm`. Read the file with `pd.read_csv` into the DataFrame `df`, print an overview with `print(df.describe())` and store\n- `n_days`: the number of days (`len`)\n- `temp_mean`: the mean temperature (pandas method `mean`)\n- `wind_max`: the highest wind speed (built-in function `max` on the column)\n- `rain_total`: the total rainfall (built-in function `sum` on the column)\n\nFor trying it out, a sample file is created when you run your code."},
   starter={"de": "import pandas as pd\n\n# Ihr Code:\n", "en": "import pandas as pd\n\n# your code:\n"},
   solution="import pandas as pd\n\ndf = pd.read_csv('data/wetter.csv')\nprint(df.describe())\nn_days = len(df)\ntemp_mean = df['temp_C'].mean()\nwind_max = max(df['wind_ms'])\nrain_total = sum(df['regen_mm'])\nprint(n_days, round(temp_mean, 2), wind_max, rain_total)\n",
   tests='''
F1 = "datum,temp_C,wind_ms,regen_mm\\n2026-04-01,8.5,3.2,0.0\\n2026-04-02,11.2,5.8,1.4\\n2026-04-03,9.7,9.1,6.2\\n2026-04-04,13.4,2.5,0.0\\n2026-04-05,15.1,4.0,0.3\\n"
F2 = "datum,temp_C,wind_ms,regen_mm\\n2026-07-01,24.0,1.0,0.0\\n2026-07-02,27.5,12.5,18.0\\n"
for content in [F1, F2]:
    rows = [l.split(",") for l in content.strip().split("\\n")[1:]]
    t = [float(r[1]) for r in rows]; w = [float(r[2]) for r in rows]; rn = [float(r[3]) for r in rows]
    ns, out = run(files={"data/wetter.csv": content})
    df, n, tm, wm, rt = need(ns, "df", "n_days", "temp_mean", "wind_max", "rain_total")
    check(type(df).__name__ == "DataFrame" and n == len(rows), f"df eingelesen, n_days = {len(rows)}", f"df read, n_days = {len(rows)}")
    check(approx(tm, sum(t) / len(t)), f"temp_mean = {sum(t) / len(t):.3f} °C", f"temp_mean = {sum(t) / len(t):.3f} °C")
    check(approx(wm, max(w)) and approx(rt, sum(rn)), f"wind_max = {max(w)} m/s, rain_total = {sum(rn):.1f} mm", f"wind_max = {max(w)} m/s, rain_total = {sum(rn):.1f} mm")
    check("mean" in out and "std" in out, "df.describe() wird ausgegeben", "df.describe() is printed")
''',
   require=["pandas"], refs=["9.4"],
   files={"data/wetter.csv": "datum,temp_C,wind_ms,regen_mm\n2026-04-01,8.5,3.2,0.0\n2026-04-02,11.2,5.8,1.4\n2026-04-03,9.7,9.1,6.2\n2026-04-04,13.4,2.5,0.0\n2026-04-05,15.1,4.0,0.3\n"})

ex(id="k9-pumpcurve", ch="9", lvl=2,
   title={"de": "Pumpenkennlinie auswerten", "en": "Evaluating a pump curve"},
   task={"de": "Die Datei `data/pumpe.csv` enthält Messpunkte einer Kreiselpumpe mit den Spalten `durchfluss_m3h` (m³/h), `foerderhoehe_m` (m) und `p_el_kW` (aufgenommene elektrische Leistung). Lesen Sie die Datei in das DataFrame `df` ein und ergänzen Sie die Spalten\n- `p_hyd_kW`: die hydraulische Leistung $P_\\mathrm{hyd} = \\rho \\, g \\, Q \\, H$ in kW – dabei ist $Q$ der Durchfluss in m³/s (also durch 3600 teilen); `rho` und `g` sind vorgegeben\n- `eta`: den Wirkungsgrad $P_\\mathrm{hyd} / P_\\mathrm{el}$\n\nSpeichern Sie außerdem\n- `eta_mean`: den mittleren Wirkungsgrad (pandas-Methode `mean`)\n- `eta_best`: den besten Wirkungsgrad und `Q_best`: den Durchfluss in m³/h, bei dem er erreicht wird (Tipp: wandeln Sie die Spalten mit `list()` in Listen um und nutzen Sie `max` und `index`)\n\nZum Ausprobieren wird beim Ausführen eine Beispieldatei angelegt.",
         "en": "The file `data/pumpe.csv` contains measuring points of a centrifugal pump with the columns `durchfluss_m3h` (m³/h), `foerderhoehe_m` (m) and `p_el_kW` (electrical input power). Read the file into the DataFrame `df` and add the columns\n- `p_hyd_kW`: the hydraulic power $P_\\mathrm{hyd} = \\rho \\, g \\, Q \\, H$ in kW – here $Q$ is the flow rate in m³/s (so divide by 3600); `rho` and `g` are given\n- `eta`: the efficiency $P_\\mathrm{hyd} / P_\\mathrm{el}$\n\nAlso store\n- `eta_mean`: the mean efficiency (pandas method `mean`)\n- `eta_best`: the best efficiency and `Q_best`: the flow rate in m³/h at which it is reached (tip: convert the columns into lists with `list()` and use `max` and `index`)\n\nFor trying it out, a sample file is created when you run your code."},
   starter={"de": "import pandas as pd\n\nrho = 1000.0  # kg/m³\ng = 9.81      # m/s²\n\n# Ihr Code:\n", "en": "import pandas as pd\n\nrho = 1000.0  # kg/m³\ng = 9.81      # m/s²\n\n# your code:\n"},
   solution="import pandas as pd\n\nrho = 1000.0\ng = 9.81\ndf = pd.read_csv('data/pumpe.csv')\ndf['p_hyd_kW'] = rho * g * df['durchfluss_m3h'] / 3600 * df['foerderhoehe_m'] / 1000\ndf['eta'] = df['p_hyd_kW'] / df['p_el_kW']\neta_mean = df['eta'].mean()\netas = list(df['eta'])\neta_best = max(etas)\nQ_best = list(df['durchfluss_m3h'])[etas.index(eta_best)]\nprint(df)\nprint(f\"Bestpunkt: eta = {eta_best:.3f} bei Q = {Q_best} m3/h\")\n",
   tests='''
F1 = "durchfluss_m3h,foerderhoehe_m,p_el_kW\\n10,32.0,2.10\\n20,30.5,2.85\\n30,28.0,3.45\\n40,24.0,3.90\\n50,18.5,4.20\\n"
F2 = "durchfluss_m3h,foerderhoehe_m,p_el_kW\\n5,12.0,0.50\\n15,10.0,0.70\\n25,6.0,0.80\\n"
for content, rho, g in [(F1, 1000.0, 9.81), (F2, 998.0, 9.81)]:
    rows = [[float(v) for v in l.split(",")] for l in content.strip().split("\\n")[1:]]
    ph = [rho * g * q / 3600 * h / 1000 for q, h, p in rows]
    eta = [a / r[2] for a, r in zip(ph, rows)]
    ns, out = run(files={"data/pumpe.csv": content}, sub={"rho": rho, "g": g})
    df, em, eb, qb = need(ns, "df", "eta_mean", "eta_best", "Q_best")
    check(type(df).__name__ == "DataFrame" and "p_hyd_kW" in df.columns and "eta" in df.columns, "df hat die Spalten p_hyd_kW und eta", "df has the columns p_hyd_kW and eta")
    check(all(approx(a, b) for a, b in zip(list(df['p_hyd_kW']), ph)), f"p_hyd_kW = {[round(v, 3) for v in ph]}", f"p_hyd_kW = {[round(v, 3) for v in ph]}")
    check(approx(em, sum(eta) / len(eta)), f"eta_mean = {sum(eta) / len(eta):.4f}", f"eta_mean = {sum(eta) / len(eta):.4f}")
    k = eta.index(max(eta))
    check(approx(eb, eta[k]) and approx(qb, rows[k][0]), f"Bestpunkt: eta = {eta[k]:.4f} bei Q = {rows[k][0]:g} m³/h", f"best point: eta = {eta[k]:.4f} at Q = {rows[k][0]:g} m³/h")
''',
   require=["pandas"], refs=["9.4"],
   files={"data/pumpe.csv": "durchfluss_m3h,foerderhoehe_m,p_el_kW\n10,32.0,2.10\n20,30.5,2.85\n30,28.0,3.45\n40,24.0,3.90\n50,18.5,4.20\n"})

ex(id="k9-uslogger", ch="9", lvl=2,
   title={"de": "Datenlogger mit US-Einheiten", "en": "Data logger with US units"},
   task={"de": "Ein Datenlogger aus den USA speichert Temperatur in °F und Druck in psi. Die Datei `data/logger.csv` hat die Spalten `zeit_s`, `temp_F` und `druck_psi`. Lesen Sie sie in das DataFrame `df` ein und ergänzen Sie die Spalten\n- `temp_C`: die Temperatur in °C, $\\vartheta_\\mathrm{C} = (\\vartheta_\\mathrm{F} - 32) \\cdot 5/9$\n- `druck_bar`: der Druck in bar (1 psi = 0.0689476 bar)\n\nSpeichern Sie außerdem\n- `temp_mean_C`: die mittlere Temperatur in °C (pandas-Methode `mean`)\n- `druck_std_bar`: die Standardabweichung des Drucks in bar (pandas-Methode `std`)\n- `n_over`: wie viele Messpunkte einen Druck **über** `limit_bar` haben (zählen Sie mit einer Schleife über `list(df['druck_bar'])`)\n\nZum Ausprobieren wird beim Ausführen eine Beispieldatei angelegt.",
         "en": "A data logger from the USA stores temperature in °F and pressure in psi. The file `data/logger.csv` has the columns `zeit_s`, `temp_F` and `druck_psi`. Read it into the DataFrame `df` and add the columns\n- `temp_C`: the temperature in °C, $\\vartheta_\\mathrm{C} = (\\vartheta_\\mathrm{F} - 32) \\cdot 5/9$\n- `druck_bar`: the pressure in bar (1 psi = 0.0689476 bar)\n\nAlso store\n- `temp_mean_C`: the mean temperature in °C (pandas method `mean`)\n- `druck_std_bar`: the standard deviation of the pressure in bar (pandas method `std`)\n- `n_over`: how many data points have a pressure **above** `limit_bar` (count with a loop over `list(df['druck_bar'])`)\n\nFor trying it out, a sample file is created when you run your code."},
   starter={"de": "import pandas as pd\n\nlimit_bar = 6.0\n\n# Ihr Code:\n", "en": "import pandas as pd\n\nlimit_bar = 6.0\n\n# your code:\n"},
   solution="import pandas as pd\n\nlimit_bar = 6.0\ndf = pd.read_csv('data/logger.csv')\ndf['temp_C'] = (df['temp_F'] - 32) * 5 / 9\ndf['druck_bar'] = df['druck_psi'] * 0.0689476\ntemp_mean_C = df['temp_C'].mean()\ndruck_std_bar = df['druck_bar'].std()\nn_over = 0\nfor p in list(df['druck_bar']):\n    if p > limit_bar:\n        n_over += 1\nprint(df)\nprint(round(temp_mean_C, 2), round(druck_std_bar, 4), n_over)\n",
   tests='''
import statistics as _st
F1 = "zeit_s,temp_F,druck_psi\\n0,68.0,80.0\\n10,71.6,85.5\\n20,75.2,88.0\\n30,78.8,92.3\\n40,82.4,87.0\\n"
F2 = "zeit_s,temp_F,druck_psi\\n0,32.0,14.5\\n5,212.0,29.0\\n10,50.0,116.0\\n"
for content, lim in [(F1, 6.0), (F2, 2.0), (F1, 80.0 * 0.0689476)]:
    rows = [[float(v) for v in l.split(",")] for l in content.strip().split("\\n")[1:]]
    tc = [(r[1] - 32) * 5 / 9 for r in rows]; pb = [r[2] * 0.0689476 for r in rows]
    ns, out = run(files={"data/logger.csv": content}, sub={"limit_bar": lim})
    df, tm, ps, no = need(ns, "df", "temp_mean_C", "druck_std_bar", "n_over")
    check(type(df).__name__ == "DataFrame" and all(approx(a, b) for a, b in zip(list(df['temp_C']), tc)), f"temp_C = {[round(v, 2) for v in tc]}", f"temp_C = {[round(v, 2) for v in tc]}")
    check("druck_bar" in df.columns and all(approx(a, b) for a, b in zip(list(df['druck_bar']), pb)), f"druck_bar = {[round(v, 3) for v in pb]}", f"druck_bar = {[round(v, 3) for v in pb]}")
    check(approx(tm, sum(tc) / len(tc)) and approx(ps, _st.stdev(pb)), f"temp_mean_C = {sum(tc) / len(tc):.3f}, druck_std_bar = {_st.stdev(pb):.5f}", f"temp_mean_C = {sum(tc) / len(tc):.3f}, druck_std_bar = {_st.stdev(pb):.5f}")
    check(no == sum(1 for v in pb if v > lim), f"n_over = {sum(1 for v in pb if v > lim)} bei limit_bar = {lim} (echt größer)", f"n_over = {sum(1 for v in pb if v > lim)} for limit_bar = {lim} (strictly greater)")
''',
   require=["pandas"], refs=["9.4"],
   files={"data/logger.csv": "zeit_s,temp_F,druck_psi\n0,68.0,80.0\n10,71.6,85.5\n20,75.2,88.0\n30,78.8,92.3\n40,82.4,87.0\n"})

ex(id="k9-battery", ch="9", lvl=2,
   title={"de": "Entladekurve eines Akkus", "en": "Discharge curve of a battery"},
   task={"de": "Bei einem Entladeversuch wurden in gleichen Zeitabständen Spannung und Strom eines Akkus gemessen. Die Datei `data/akku.csv` hat die Spalten `zeit_min`, `spannung_V` und `strom_A`. Lesen Sie sie in das DataFrame `df` ein, fügen Sie die Spalte `p_W` mit der Leistung $P = U \\cdot I$ hinzu und speichern Sie\n- `dt_h`: den Zeitabstand zweier Messungen in Stunden (aus den ersten beiden Zeitwerten; Tipp: `list(df['zeit_min'])`)\n- `capacity_Ah`: die entnommene Ladung in Ah – jeder Messwert gilt für ein Zeitintervall `dt_h`, also Summe aller Ströme · `dt_h` (eingebaute Funktion `sum`)\n- `energy_Wh`: die entnommene Energie in Wh (ebenso aus `p_W`)\n- `u_mean`: die mittlere Spannung (pandas-Methode `mean`) und `u_min`: die niedrigste Spannung (eingebaute Funktion `min`)\n\nZum Ausprobieren wird beim Ausführen eine Beispieldatei angelegt.",
         "en": "In a discharge test, voltage and current of a battery were measured at equal time intervals. The file `data/akku.csv` has the columns `zeit_min`, `spannung_V` and `strom_A`. Read it into the DataFrame `df`, add the column `p_W` with the power $P = U \\cdot I$ and store\n- `dt_h`: the time between two measurements in hours (from the first two time values; tip: `list(df['zeit_min'])`)\n- `capacity_Ah`: the charge drawn in Ah – each measured value applies to a time interval `dt_h`, so the sum of all currents · `dt_h` (built-in function `sum`)\n- `energy_Wh`: the energy drawn in Wh (likewise from `p_W`)\n- `u_mean`: the mean voltage (pandas method `mean`) and `u_min`: the lowest voltage (built-in function `min`)\n\nFor trying it out, a sample file is created when you run your code."},
   starter={"de": "import pandas as pd\n\n# Ihr Code:\n", "en": "import pandas as pd\n\n# your code:\n"},
   solution="import pandas as pd\n\ndf = pd.read_csv('data/akku.csv')\ndf['p_W'] = df['spannung_V'] * df['strom_A']\nt = list(df['zeit_min'])\ndt_h = (t[1] - t[0]) / 60\ncapacity_Ah = sum(df['strom_A']) * dt_h\nenergy_Wh = sum(df['p_W']) * dt_h\nu_mean = df['spannung_V'].mean()\nu_min = min(df['spannung_V'])\nprint(df)\nprint(f\"{capacity_Ah:.2f} Ah, {energy_Wh:.1f} Wh, U zwischen {u_min} und Mittel {u_mean:.2f} V\")\n",
   tests='''
F1 = "zeit_min,spannung_V,strom_A\\n0,12.6,2.0\\n15,12.4,2.0\\n30,12.2,2.0\\n45,12.0,2.1\\n60,11.7,2.1\\n75,11.3,2.2\\n"
F2 = "zeit_min,spannung_V,strom_A\\n0,4.15,1.5\\n6,3.90,1.4\\n12,3.70,1.3\\n"
for content in [F1, F2]:
    rows = [[float(v) for v in l.split(",")] for l in content.strip().split("\\n")[1:]]
    dt = (rows[1][0] - rows[0][0]) / 60
    cap = sum(r[2] for r in rows) * dt; en = sum(r[1] * r[2] for r in rows) * dt
    us = [r[1] for r in rows]
    ns, out = run(files={"data/akku.csv": content})
    df, d, c, e, um, un = need(ns, "df", "dt_h", "capacity_Ah", "energy_Wh", "u_mean", "u_min")
    check(type(df).__name__ == "DataFrame" and "p_W" in df.columns and all(approx(a, r[1] * r[2]) for a, r in zip(list(df['p_W']), rows)), "df hat die Spalte p_W = U · I", "df has the column p_W = U · I")
    check(approx(d, dt), f"dt_h = {dt:.4f} h", f"dt_h = {dt:.4f} h")
    check(approx(c, cap) and approx(e, en), f"capacity_Ah = {cap:.4f} Ah, energy_Wh = {en:.3f} Wh", f"capacity_Ah = {cap:.4f} Ah, energy_Wh = {en:.3f} Wh")
    check(approx(um, sum(us) / len(us)) and approx(un, min(us)), f"u_mean = {sum(us) / len(us):.3f} V, u_min = {min(us)} V", f"u_mean = {sum(us) / len(us):.3f} V, u_min = {min(us)} V")
''',
   require=["pandas"], refs=["9.4"],
   files={"data/akku.csv": "zeit_min,spannung_V,strom_A\n0,12.6,2.0\n15,12.4,2.0\n30,12.2,2.0\n45,12.0,2.1\n60,11.7,2.1\n75,11.3,2.2\n"})
