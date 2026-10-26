from exlib import ex

# Dritter Satz (v1.0): 14 Aufgaben, damit Kapitel 4–10 je 30 und die Anhänge je 20 Aufgaben haben.

# ================================================================== Kapitel 9
ex(id="k9-expansion", ch="9", lvl=1,
   title={"de": "Wärmeausdehnung einer Schiene", "en": "Thermal expansion of a rail"},
   task={"de": "Eine Stahlschiene der Länge `L0` (m) wird bei unterschiedlichen Temperaturen betrieben. Gegenüber 20 °C ändert sich ihre Länge um\n\n$$\\Delta L = \\alpha \\cdot L_0 \\cdot (T - 20\\,{}^{\\circ}\\mathrm{C})$$\n\nmit dem Ausdehnungskoeffizienten `alpha` (1/K). Wandeln Sie die Liste `temps` (°C) in ein NumPy-Array um und berechnen Sie **ohne Schleife**\n- `dL_mm`: die Längenänderungen in mm (Array, gleiche Reihenfolge wie `temps`)\n- `L_m`: die Schienenlängen in m (Array)\n- `gap_mm`: die nötige Breite der Dehnfuge in mm, also größte minus kleinste Längenänderung (eingebaute Funktionen `max` und `min`)\n\nGeben Sie `gap_mm` mit einer Nachkommastelle aus.",
         "en": "A steel rail of length `L0` (m) is operated at different temperatures. Compared with 20 °C its length changes by\n\n$$\\Delta L = \\alpha \\cdot L_0 \\cdot (T - 20\\,{}^{\\circ}\\mathrm{C})$$\n\nwith the expansion coefficient `alpha` (1/K). Convert the list `temps` (°C) into a NumPy array and compute **without a loop**\n- `dL_mm`: the length changes in mm (array, same order as `temps`)\n- `L_m`: the rail lengths in m (array)\n- `gap_mm`: the required width of the expansion joint in mm, i.e. largest minus smallest length change (built-in functions `max` and `min`)\n\nPrint `gap_mm` with one decimal."},
   starter={"de": "import numpy as np\n\nL0 = 60.0        # m\nalpha = 1.2e-5   # 1/K (Stahl)\ntemps = [-20.0, 0.0, 20.0, 45.0, 60.0]   # °C\n\n# Ihr Code:\n",
            "en": "import numpy as np\n\nL0 = 60.0        # m\nalpha = 1.2e-5   # 1/K (steel)\ntemps = [-20.0, 0.0, 20.0, 45.0, 60.0]   # °C\n\n# your code:\n"},
   solution='import numpy as np\n\nL0 = 60.0\nalpha = 1.2e-5\ntemps = [-20.0, 0.0, 20.0, 45.0, 60.0]\nT = np.array(temps)\ndL_mm = alpha * L0 * (T - 20) * 1000\nL_m = L0 + dL_mm / 1000\ngap_mm = max(dL_mm) - min(dL_mm)\nprint(f"Dehnfuge: {gap_mm:.1f} mm")\n',
   tests='''
for L0, a, ts in [(60.0, 1.2e-5, [-20.0, 0.0, 20.0, 45.0, 60.0]), (25.0, 2.3e-5, [20.0, 80.0]), (100.0, 1.2e-5, [5.0, -30.0, 35.0])]:
    ns, out = run(sub={"L0": L0, "alpha": a, "temps": ts})
    d, L, g = need(ns, "dL_mm", "L_m", "gap_mm")
    ed = [a * L0 * (t - 20) * 1000 for t in ts]
    check(type(d).__name__ == "ndarray" and len(d) == len(ts) and all(approx(x, y) for x, y in zip(d, ed)), f"L0 = {L0} m: dL_mm = {[round(x, 2) for x in ed]}", f"L0 = {L0} m: dL_mm = {[round(x, 2) for x in ed]}")
    check(type(L).__name__ == "ndarray" and all(approx(x, L0 + y / 1000) for x, y in zip(L, ed)), "L_m = L0 + ΔL stimmt", "L_m = L0 + ΔL is correct")
    check(approx(g, max(ed) - min(ed)) and f"{max(ed) - min(ed):.1f}" in out, f"gap_mm = {max(ed) - min(ed):.1f} mm (und ausgegeben)", f"gap_mm = {max(ed) - min(ed):.1f} mm (and printed)")
''',
   require=["numpy"], forbid=["for", "while", "listcomp"], refs=["9.2v", "9.2"])

ex(id="k9-loadzeros", ch="9", lvl=1,
   title={"de": "Lastprofil mit np.zeros und Slicing", "en": "Load profile with np.zeros and slicing"},
   task={"de": "Für einen Tag soll das stündliche Lastprofil eines Betriebs erstellt werden (Index = Stunde 0 bis 23). Arbeiten Sie **ohne Schleife**:\n- `hours`: die Stunden 0, 1, …, 23 als Array (`np.arange`)\n- `load`: zuerst mit `np.zeros` ein Array mit 24 Nullen. Addieren Sie dann für alle Stunden die Grundlast `base` (kW) und mit Slicing für die Stunden `start` bis **ausschließlich** `end` zusätzlich die Schichtlast `shift_load` (kW).\n- `energy`: die Tagesenergie in kWh (jede Stunde: Leistung · 1 h; eingebaute Funktion `sum`)\n- `night`: die Energie in der Nacht, d.h. in den Stunden 22, 23 und 0 bis 5 (zwei Slices)",
         "en": "The hourly load profile of a plant is to be created for one day (index = hour 0 to 23). Work **without a loop**:\n- `hours`: the hours 0, 1, …, 23 as an array (`np.arange`)\n- `load`: first an array of 24 zeros with `np.zeros`. Then add the base load `base` (kW) for all hours and, using slicing, the shift load `shift_load` (kW) in addition for the hours `start` up to but **excluding** `end`.\n- `energy`: the day's energy in kWh (each hour: power · 1 h; built-in function `sum`)\n- `night`: the energy during the night, i.e. in the hours 22, 23 and 0 to 5 (two slices)"},
   starter={"de": "import numpy as np\n\nbase = 12.0        # kW\nshift_load = 30.0  # kW\nstart = 6          # Schichtbeginn (Uhr)\nend = 22           # Schichtende (Uhr)\n\n# Ihr Code:\n",
            "en": "import numpy as np\n\nbase = 12.0        # kW\nshift_load = 30.0  # kW\nstart = 6          # start of shift (o'clock)\nend = 22           # end of shift (o'clock)\n\n# your code:\n"},
   solution='import numpy as np\n\nbase = 12.0\nshift_load = 30.0\nstart = 6\nend = 22\nhours = np.arange(0, 24)\nload = np.zeros(24)\nload = load + base\nload[start:end] = load[start:end] + shift_load\nenergy = sum(load)\nnight = sum(load[22:]) + sum(load[:6])\nprint(load)\nprint(f"{energy:.1f} kWh, davon nachts {night:.1f} kWh")\n',
   tests='''
for b, s, st, en in [(12.0, 30.0, 6, 22), (5.0, 8.0, 8, 16), (0.0, 10.0, 0, 24), (3.5, 2.0, 20, 24)]:
    ns, out = run(sub={"base": b, "shift_load": s, "start": st, "end": en})
    h, L, E, N = need(ns, "hours", "load", "energy", "night")
    eL = [b + (s if st <= k < en else 0) for k in range(24)]
    check(type(h).__name__ == "ndarray" and list(h) == list(range(24)), "hours = 0 … 23", "hours = 0 … 23")
    check(type(L).__name__ == "ndarray" and len(L) == 24 and all(approx(x, y) for x, y in zip(L, eL)), f"Schicht {st}–{en} Uhr: load stimmt in allen Stunden", f"shift {st}–{en}: load is correct for every hour")
    eN = sum(eL[22:]) + sum(eL[:6])
    check(approx(E, sum(eL)) and approx(N, eN), f"energy = {sum(eL):g} kWh, night = {eN:g} kWh", f"energy = {sum(eL):g} kWh, night = {eN:g} kWh")
''',
   require=["numpy", "slice"], forbid=["for", "while", "listcomp"], refs=["9.2", "8.1x"])

ex(id="k9-rmsvec", ch="9", lvl=2,
   title={"de": "Effektivwert aus Abtastwerten", "en": "RMS value from samples"},
   task={"de": "Eine Wechselspannung $u(t) = \\hat{u} \\cdot \\sin(2\\pi f t)$ wird während einer Periode `n`-mal gleichmäßig abgetastet. Berechnen Sie **ohne Schleife**\n- `t`: die Abtastzeitpunkte $t_k = \\dfrac{k}{n \\cdot f}$ für $k = 0, 1, \\dots, n-1$ (Array, mit `np.arange`)\n- `u`: die Abtastwerte (Array, mit `np.sin` und `np.pi`)\n- `u_rms`: den Effektivwert $U_\\mathrm{eff} = \\sqrt{\\dfrac{1}{n} \\sum_k u_k^2}$ (eingebaute Funktion `sum`, `np.sqrt`)\n- `ratio`: das Verhältnis $\\hat{u} / U_\\mathrm{eff}$\n- `sine_ok`: ob `ratio` weniger als `1e-6` von $\\sqrt{2}$ abweicht (für eine reine Sinusspannung gilt $\\hat{u} = \\sqrt{2} \\cdot U_\\mathrm{eff}$)",
         "en": "An AC voltage $u(t) = \\hat{u} \\cdot \\sin(2\\pi f t)$ is sampled `n` times at equal intervals during one period. Compute **without a loop**\n- `t`: the sampling times $t_k = \\dfrac{k}{n \\cdot f}$ for $k = 0, 1, \\dots, n-1$ (array, using `np.arange`)\n- `u`: the samples (array, using `np.sin` and `np.pi`)\n- `u_rms`: the RMS value $U_\\mathrm{rms} = \\sqrt{\\dfrac{1}{n} \\sum_k u_k^2}$ (built-in function `sum`, `np.sqrt`)\n- `ratio`: the ratio $\\hat{u} / U_\\mathrm{rms}$\n- `sine_ok`: whether `ratio` differs from $\\sqrt{2}$ by less than `1e-6` (for a pure sine voltage $\\hat{u} = \\sqrt{2} \\cdot U_\\mathrm{rms}$)"},
   starter={"de": "import numpy as np\n\nu_hat = 325.0   # Scheitelwert in V\nf = 50.0        # Hz\nn = 40          # Abtastwerte pro Periode\n\n# Ihr Code:\n",
            "en": "import numpy as np\n\nu_hat = 325.0   # peak value in V\nf = 50.0        # Hz\nn = 40          # samples per period\n\n# your code:\n"},
   solution='import numpy as np\n\nu_hat = 325.0\nf = 50.0\nn = 40\nt = np.arange(0, n) / (n * f)\nu = u_hat * np.sin(2 * np.pi * f * t)\nu_rms = np.sqrt(sum(u**2) / n)\nratio = u_hat / u_rms\nsine_ok = abs(ratio - np.sqrt(2)) < 1e-6\nprint(f"U_eff = {u_rms:.1f} V, Verhältnis {ratio:.4f}, Sinus: {sine_ok}")\n',
   tests='''
import math as _m
for uh, f, n in [(325.0, 50.0, 40), (10.0, 1000.0, 8), (565.7, 60.0, 3)]:
    ns, out = run(sub={"u_hat": uh, "f": f, "n": n})
    t, u, ur, r, ok = need(ns, "t", "u", "u_rms", "ratio", "sine_ok")
    et = [k / (n * f) for k in range(n)]
    eu = [uh * _m.sin(2 * _m.pi * f * x) for x in et]
    check(type(t).__name__ == "ndarray" and len(t) == n and all(approx(a, b, 1e-9) for a, b in zip(t, et)), f"n = {n}, f = {f:g} Hz: {n} Zeitpunkte ab 0 im Abstand {1 / (n * f):.3g} s", f"n = {n}, f = {f:g} Hz: {n} times from 0 with spacing {1 / (n * f):.3g} s")
    check(type(u).__name__ == "ndarray" and all(abs(a - b) < 1e-6 * uh for a, b in zip(u, eu)), "Abtastwerte u stimmen", "samples u are correct")
    eur = _m.sqrt(sum(x * x for x in eu) / n)
    check(approx(ur, eur) and approx(r, uh / eur), f"U_eff = {eur:.3f} V, ratio = {uh / eur:.6f}", f"U_rms = {eur:.3f} V, ratio = {uh / eur:.6f}")
    check(bool(ok) is (abs(uh / eur - _m.sqrt(2)) < 1e-6), f"sine_ok = {abs(uh / eur - _m.sqrt(2)) < 1e-6}", f"sine_ok = {abs(uh / eur - _m.sqrt(2)) < 1e-6}")
ns, out = run(sub={"n": 2})
check(ns.get("sine_ok") is False or bool(ns.get("sine_ok")) is False, "Mit nur 2 Abtastwerten ist sine_ok = False (beide Werte sind 0)", "With only 2 samples sine_ok = False (both samples are 0)")
''',
   require=["numpy"], forbid=["for", "while", "listcomp"], refs=["9.2v", "9.2"])

ex(id="k9-moments", ch="9", lvl=2,
   title={"de": "Momente mit dem Kreuzprodukt", "en": "Moments with the cross product"},
   task={"de": "An einem Bauteil greifen mehrere Kräfte an. `r_list` enthält die Ortsvektoren der Angriffspunkte (m), `F_list` die Kraftvektoren (N), jeweils eine Zeile `[x, y, z]` pro Kraft. Das Moment einer Kraft bezüglich des Ursprungs ist $\\vec{M} = \\vec{r} \\times \\vec{F}$.\n\nWandeln Sie beide Listen in 2D-Arrays `R` und `F` um und berechnen Sie **ohne Schleife**\n- `M`: die Momente aller Kräfte als Array mit einer Zeile pro Kraft – `np.cross(R, F)` bildet für zwei gleich große n×3-Arrays das Kreuzprodukt Zeile für Zeile\n- `M_total`: das Gesamtmoment (Vektor); die eingebaute Funktion `sum` addiert die Zeilen eines 2D-Arrays\n- `M_abs`: den Betrag des Gesamtmoments (`np.dot`, `np.sqrt`)\n- `balanced`: ob das Bauteil momentenfrei ist (`M_abs` kleiner als `1e-9`)",
         "en": "Several forces act on a component. `r_list` contains the position vectors of the points of application (m), `F_list` the force vectors (N), one row `[x, y, z]` per force. The moment of a force about the origin is $\\vec{M} = \\vec{r} \\times \\vec{F}$.\n\nConvert both lists into 2D arrays `R` and `F` and compute **without a loop**\n- `M`: the moments of all forces as an array with one row per force – `np.cross(R, F)` forms the cross product row by row for two n×3 arrays of the same size\n- `M_total`: the total moment (vector); the built-in function `sum` adds up the rows of a 2D array\n- `M_abs`: the magnitude of the total moment (`np.dot`, `np.sqrt`)\n- `balanced`: whether the component is free of moments (`M_abs` smaller than `1e-9`)"},
   starter={"de": "import numpy as np\n\nr_list = [[0.5, 0.0, 0.0], [0.0, 0.3, 0.0], [0.2, 0.2, 0.1]]       # m\nF_list = [[0.0, 100.0, 0.0], [50.0, 0.0, 20.0], [0.0, 0.0, -40.0]]  # N\n\n# Ihr Code:\n",
            "en": "import numpy as np\n\nr_list = [[0.5, 0.0, 0.0], [0.0, 0.3, 0.0], [0.2, 0.2, 0.1]]       # m\nF_list = [[0.0, 100.0, 0.0], [50.0, 0.0, 20.0], [0.0, 0.0, -40.0]]  # N\n\n# your code:\n"},
   solution='import numpy as np\n\nr_list = [[0.5, 0.0, 0.0], [0.0, 0.3, 0.0], [0.2, 0.2, 0.1]]\nF_list = [[0.0, 100.0, 0.0], [50.0, 0.0, 20.0], [0.0, 0.0, -40.0]]\nR = np.array(r_list)\nF = np.array(F_list)\nM = np.cross(R, F)\nM_total = sum(M)\nM_abs = np.sqrt(np.dot(M_total, M_total))\nbalanced = M_abs < 1e-9\nprint(M)\nprint(M_total, f"{M_abs:.2f} Nm", balanced)\n',
   tests='''
def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
cases = [([[0.5, 0.0, 0.0], [0.0, 0.3, 0.0], [0.2, 0.2, 0.1]], [[0.0, 100.0, 0.0], [50.0, 0.0, 20.0], [0.0, 0.0, -40.0]]),
         ([[1.0, 0.0, 0.0], [-1.0, 0.0, 0.0]], [[0.0, 10.0, 0.0], [0.0, 10.0, 0.0]]),
         ([[1.0, 0.0, 0.0], [-2.0, 0.0, 0.0]], [[0.0, 10.0, 0.0], [0.0, 5.0, 0.0]]),
         ([[0.01, 0.0, 0.0]], [[0.0, 10.0, 0.0]])]
for rl, fl in cases:
    ns, out = run(sub={"r_list": rl, "F_list": fl})
    R, F, M, Mt, Ma, b = need(ns, "R", "F", "M", "M_total", "M_abs", "balanced")
    eM = [cross(r, f) for r, f in zip(rl, fl)]
    eMt = [sum(m[i] for m in eM) for i in range(3)]
    eMa = sum(x * x for x in eMt) ** 0.5
    check(getattr(R, "shape", None) == (len(rl), 3) and getattr(F, "shape", None) == (len(fl), 3), f"R und F sind {len(rl)}×3-Arrays", f"R and F are {len(rl)}×3 arrays")
    check(getattr(M, "shape", None) == (len(rl), 3) and all(approx(M[i][j], eM[i][j]) for i in range(len(rl)) for j in range(3)), f"M = {eM}", f"M = {eM}")
    check(len(Mt) == 3 and all(approx(Mt[j], eMt[j]) for j in range(3)) and approx(Ma, eMa), f"M_total = {[round(x, 3) for x in eMt]}, |M| = {eMa:.3f} Nm", f"M_total = {[round(x, 3) for x in eMt]}, |M| = {eMa:.3f} Nm")
    check(bool(b) is (eMa < 1e-9), f"balanced = {eMa < 1e-9}", f"balanced = {eMa < 1e-9}")
check("cross(" in SOURCE, "Momente mit np.cross berechnet", "Moments computed with np.cross")
''',
   require=["numpy"], forbid=["for", "while", "listcomp"], refs=["9.2m", "9.2v"])

# ================================================================== Kapitel 10
ex(id="k10-spring", ch="10", lvl=1,
   title={"de": "Klasse Schraubenfeder", "en": "Class Spring"},
   task={"de": "Schreiben Sie die Klasse `Spring(k, l0)` für eine Schraubenfeder mit der Federrate `k` (N/mm) und der ungespannten Länge `l0` (mm). Der Konstruktor speichert beide Werte als Attribute gleichen Namens.\n- `force(length)`: die Federkraft $F = k \\cdot (l - l_0)$ in N bei der Länge `length` (negativ bei Druck)\n- `energy(length)`: die gespeicherte Energie $E = \\tfrac{1}{2} \\cdot k \\cdot (l - l_0)^2$ in N·mm\n- `length_for(force)`: die Länge, bei der die Feder die Kraft `force` liefert: $l = l_0 + F/k$\n\nAlle drei Methoden geben ihr Ergebnis zurück.",
         "en": "Write the class `Spring(k, l0)` for a coil spring with the spring rate `k` (N/mm) and the unloaded length `l0` (mm). The constructor stores both values as attributes of the same name.\n- `force(length)`: the spring force $F = k \\cdot (l - l_0)$ in N at the length `length` (negative under compression)\n- `energy(length)`: the stored energy $E = \\tfrac{1}{2} \\cdot k \\cdot (l - l_0)^2$ in N·mm\n- `length_for(force)`: the length at which the spring delivers the force `force`: $l = l_0 + F/k$\n\nAll three methods return their result."},
   starter={"de": "class Spring:\n    def __init__(self, k, l0):\n        pass   # Ihr Code\n\n\ns = Spring(2.5, 80.0)\n", "en": "class Spring:\n    def __init__(self, k, l0):\n        pass   # your code\n\n\ns = Spring(2.5, 80.0)\n"},
   solution='class Spring:\n    def __init__(self, k, l0):\n        self.k = k\n        self.l0 = l0\n\n    def force(self, length):\n        return self.k * (length - self.l0)\n\n    def energy(self, length):\n        return 0.5 * self.k * (length - self.l0) ** 2\n\n    def length_for(self, force):\n        return self.l0 + force / self.k\n\n\ns = Spring(2.5, 80.0)\nprint(s.force(100.0), s.energy(100.0), s.length_for(25.0))\n',
   tests='''
ns, out = run()
for k, l0 in [(2.5, 80.0), (10.0, 35.0)]:
    s = call(ns, "Spring", k, l0)
    check(getattr(s, "k", None) == k and getattr(s, "l0", None) == l0, f"Spring({k}, {l0}): Attribute k und l0", f"Spring({k}, {l0}): attributes k and l0")
    for L in [l0 + 20.0, l0 - 5.0, l0]:
        check(approx(method(s, "force", L), k * (L - l0)) and approx(method(s, "energy", L), 0.5 * k * (L - l0) ** 2), f"Länge {L} mm: F = {k * (L - l0):g} N, E = {0.5 * k * (L - l0) ** 2:g} N·mm", f"length {L} mm: F = {k * (L - l0):g} N, E = {0.5 * k * (L - l0) ** 2:g} N·mm")
    check(approx(method(s, "length_for", 25.0), l0 + 25.0 / k) and approx(method(s, "length_for", -10.0), l0 - 10.0 / k), f"length_for(25) = {l0 + 25 / k:g} mm", f"length_for(25) = {l0 + 25 / k:g} mm")
''',
   require=["class"], refs=["10.3", "10.2"])

ex(id="k10-pipe", ch="10", lvl=1,
   title={"de": "Klasse Rohrleitung", "en": "Class Pipe"},
   task={"de": "Schreiben Sie die Klasse `Pipe(d_mm, length_m)` für einen Rohrabschnitt mit dem Innendurchmesser `d_mm` (mm) und der Länge `length_m` (m). Der Konstruktor speichert beide Werte als Attribute gleichen Namens.\n- `area()`: die Querschnittsfläche $A = \\pi d^2 / 4$ in m² (Durchmesser vorher in m umrechnen, `math.pi`)\n- `volume_l()`: das Innenvolumen in Litern\n- `velocity(flow_lps)`: die mittlere Strömungsgeschwindigkeit $v = Q / A$ in m/s für den Volumenstrom `flow_lps` in l/s\n- `fill_time(flow_lps)`: wie viele Sekunden es dauert, das leere Rohr mit diesem Volumenstrom zu füllen\n\nAlle Methoden geben ihr Ergebnis zurück.",
         "en": "Write the class `Pipe(d_mm, length_m)` for a pipe section with the inner diameter `d_mm` (mm) and the length `length_m` (m). The constructor stores both values as attributes of the same name.\n- `area()`: the cross-sectional area $A = \\pi d^2 / 4$ in m² (convert the diameter to m first, `math.pi`)\n- `volume_l()`: the inner volume in litres\n- `velocity(flow_lps)`: the mean flow velocity $v = Q / A$ in m/s for the flow rate `flow_lps` in l/s\n- `fill_time(flow_lps)`: how many seconds it takes to fill the empty pipe at this flow rate\n\nAll methods return their result."},
   starter={"de": "import math\n\n\nclass Pipe:\n    def __init__(self, d_mm, length_m):\n        pass   # Ihr Code\n\n\np = Pipe(50.0, 12.0)\n", "en": "import math\n\n\nclass Pipe:\n    def __init__(self, d_mm, length_m):\n        pass   # your code\n\n\np = Pipe(50.0, 12.0)\n"},
   solution='import math\n\n\nclass Pipe:\n    def __init__(self, d_mm, length_m):\n        self.d_mm = d_mm\n        self.length_m = length_m\n\n    def area(self):\n        d = self.d_mm / 1000\n        return math.pi * d**2 / 4\n\n    def volume_l(self):\n        return self.area() * self.length_m * 1000\n\n    def velocity(self, flow_lps):\n        return flow_lps / 1000 / self.area()\n\n    def fill_time(self, flow_lps):\n        return self.volume_l() / flow_lps\n\n\np = Pipe(50.0, 12.0)\nprint(round(p.volume_l(), 2), "l", round(p.velocity(2.0), 2), "m/s", round(p.fill_time(2.0), 1), "s")\n',
   tests='''
import math as _m
ns, out = run()
for d, L, q in [(50.0, 12.0, 2.0), (100.0, 3.5, 10.0), (20.0, 1.0, 0.25)]:
    p = call(ns, "Pipe", d, L)
    A = _m.pi * (d / 1000) ** 2 / 4
    check(getattr(p, "d_mm", None) == d and getattr(p, "length_m", None) == L, f"Pipe({d}, {L}): Attribute d_mm und length_m", f"Pipe({d}, {L}): attributes d_mm and length_m")
    check(approx(method(p, "area"), A) and approx(method(p, "volume_l"), A * L * 1000), f"DN {d:g}, {L} m: A = {A:.6f} m², V = {A * L * 1000:.3f} l", f"DN {d:g}, {L} m: A = {A:.6f} m², V = {A * L * 1000:.3f} l")
    check(approx(method(p, "velocity", q), q / 1000 / A) and approx(method(p, "fill_time", q), A * L * 1000 / q), f"Q = {q} l/s: v = {q / 1000 / A:.3f} m/s, Füllzeit {A * L * 1000 / q:.2f} s", f"Q = {q} l/s: v = {q / 1000 / A:.3f} m/s, fill time {A * L * 1000 / q:.2f} s")
''',
   require=["class"], refs=["10.3", "10.2"])

ex(id="k10-length", ch="10", lvl=2,
   title={"de": "Längenangaben mit Einheiten", "en": "Lengths with units"},
   task={"de": "Auf Zeichnungen stehen Maße in unterschiedlichen Einheiten. Schreiben Sie die Klasse `Length(value, unit)` mit den Attributen `value` und `unit`; erlaubt sind die Einheiten `\"mm\"`, `\"cm\"`, `\"m\"` und `\"km\"` (speichern Sie die Umrechnungsfaktoren nach mm in einem Dictionary).\n- `to_mm()`: der Wert in mm\n- `to(unit)`: ein **neues** `Length`-Objekt mit derselben Länge in der Einheit `unit`\n- `__add__`: Summe zweier Längen, das Ergebnis in der Einheit des **linken** Operanden\n- `__eq__`: gleich lang (Abweichung in mm kleiner als `1e-9`), z.B. `Length(1, \"m\") == Length(100, \"cm\")`\n- `__lt__`: kürzer als – damit funktioniert auch `sorted()` mit einer Liste von Längen\n- `__str__`: Wert im Format `:g` und Einheit, z.B. `1.5 m` oder `250 mm`",
         "en": "Drawings show dimensions in different units. Write the class `Length(value, unit)` with the attributes `value` and `unit`; the units `\"mm\"`, `\"cm\"`, `\"m\"` and `\"km\"` are allowed (store the conversion factors to mm in a dictionary).\n- `to_mm()`: the value in mm\n- `to(unit)`: a **new** `Length` object with the same length in the unit `unit`\n- `__add__`: sum of two lengths, the result in the unit of the **left** operand\n- `__eq__`: equally long (difference in mm smaller than `1e-9`), e.g. `Length(1, \"m\") == Length(100, \"cm\")`\n- `__lt__`: shorter than – then `sorted()` also works with a list of lengths\n- `__str__`: value in the format `:g` and unit, e.g. `1.5 m` or `250 mm`"},
   starter={"de": "class Length:\n    FACTOR = {\"mm\": 1, \"cm\": 10, \"m\": 1000, \"km\": 1000000}\n\n    def __init__(self, value, unit):\n        pass   # Ihr Code\n", "en": "class Length:\n    FACTOR = {\"mm\": 1, \"cm\": 10, \"m\": 1000, \"km\": 1000000}\n\n    def __init__(self, value, unit):\n        pass   # your code\n"},
   solution='class Length:\n    FACTOR = {"mm": 1, "cm": 10, "m": 1000, "km": 1000000}\n\n    def __init__(self, value, unit):\n        self.value = value\n        self.unit = unit\n\n    def to_mm(self):\n        return self.value * self.FACTOR[self.unit]\n\n    def to(self, unit):\n        return Length(self.to_mm() / self.FACTOR[unit], unit)\n\n    def __add__(self, other):\n        return Length(self.value + other.to_mm() / self.FACTOR[self.unit], self.unit)\n\n    def __eq__(self, other):\n        return abs(self.to_mm() - other.to_mm()) < 1e-9\n\n    def __lt__(self, other):\n        return self.to_mm() < other.to_mm()\n\n    def __str__(self):\n        return f"{self.value:g} {self.unit}"\n\n\nparts = [Length(1.2, "m"), Length(450, "mm"), Length(30, "cm")]\nprint(parts[0] + parts[1], parts[1].to("cm"), [str(p) for p in sorted(parts)])\n',
   tests='''
ns, out = run()
L = ns.get("Length")
a = call(ns, "Length", 1.2, "m"); b = call(ns, "Length", 450, "mm"); c = call(ns, "Length", 30, "cm")
check(getattr(a, "value", None) == 1.2 and getattr(a, "unit", None) == "m", "Attribute value und unit", "Attributes value and unit")
check(approx(method(a, "to_mm"), 1200) and approx(method(c, "to_mm"), 300) and approx(method(call(ns, "Length", 0.5, "km"), "to_mm"), 500000), "to_mm(): 1.2 m = 1200 mm, 30 cm = 300 mm, 0.5 km = 500000 mm", "to_mm(): 1.2 m = 1200 mm, 30 cm = 300 mm, 0.5 km = 500000 mm")
t = method(b, "to", "cm")
check(isinstance(t, L) and t is not b and t.unit == "cm" and approx(t.value, 45) and b.unit == "mm", "450 mm .to('cm') ist ein neues Objekt 45 cm", "450 mm .to('cm') is a new object 45 cm")
s = safe(lambda: a + b); s2 = safe(lambda: b + a)
check(isinstance(s, L) and s.unit == "m" and approx(s.value, 1.65) and isinstance(s2, L) and s2.unit == "mm" and approx(s2.value, 1650), "1.2 m + 450 mm = 1.65 m, 450 mm + 1.2 m = 1650 mm", "1.2 m + 450 mm = 1.65 m, 450 mm + 1.2 m = 1650 mm")
check(safe(lambda: call(ns, "Length", 1, "m") == call(ns, "Length", 100, "cm")) is True and safe(lambda: a == b) is False and safe(lambda: call(ns, "Length", 1000.5, "mm") == call(ns, "Length", 1, "m")) is False, "1 m == 100 cm, aber 1.2 m != 450 mm", "1 m == 100 cm, but 1.2 m != 450 mm")
check(safe(lambda: c < b) is True and safe(lambda: a < c) is False and [str(x) for x in safe(lambda: sorted([a, b, c])) or []] == ["30 cm", "450 mm", "1.2 m"], "__lt__ und sorted(): 30 cm < 450 mm < 1.2 m", "__lt__ and sorted(): 30 cm < 450 mm < 1.2 m")
check(safe(lambda: str(call(ns, "Length", 1.5, "m"))) == "1.5 m" and safe(lambda: str(call(ns, "Length", 250.0, "mm"))) == "250 mm", "str: '1.5 m', '250 mm'", "str: '1.5 m', '250 mm'")
''',
   require=["class", "magic", "dict"], refs=["10.7", "8.3"])

ex(id="k10-rangelogger", ch="10", lvl=2,
   title={"de": "Datenlogger mit Plausibilitätsfilter", "en": "Data logger with plausibility filter"},
   task={"de": "Basisklasse `DataLogger(name)` mit den Attributen `name`, `times` und `values` (beide anfangs leere Listen) und den Methoden\n- `record(t, value)`: hängt die Zeit an `times` und den Messwert an `values` an und gibt `True` zurück\n- `count()`: Anzahl der gespeicherten Messwerte\n- `last()`: das Tupel `(t, value)` des zuletzt gespeicherten Messwerts oder `None`, wenn noch nichts gespeichert ist\n\nAbgeleitete Klasse `RangeLogger(name, low, high)` (Konstruktor mit `super().__init__(…)`) mit dem zusätzlichen Attribut `rejected` (Start 0). Sie **überschreibt** `record`: Liegt der Wert im Bereich `low` bis `high` (Grenzen eingeschlossen), wird er mit `super().record(…)` gespeichert und `True` zurückgegeben; sonst wird `rejected` um 1 erhöht und `False` zurückgegeben.\n\n`count()` und `last()` stehen **nur** in der Basisklasse.",
         "en": "Base class `DataLogger(name)` with the attributes `name`, `times` and `values` (both initially empty lists) and the methods\n- `record(t, value)`: appends the time to `times` and the reading to `values` and returns `True`\n- `count()`: number of stored readings\n- `last()`: the tuple `(t, value)` of the most recently stored reading, or `None` if nothing has been stored yet\n\nDerived class `RangeLogger(name, low, high)` (constructor with `super().__init__(…)`) with the additional attribute `rejected` (initially 0). It **overrides** `record`: if the value lies within `low` to `high` (limits included), it is stored with `super().record(…)` and `True` is returned; otherwise `rejected` is increased by 1 and `False` is returned.\n\n`count()` and `last()` are **only** in the base class."},
   starter={"de": "class DataLogger:\n    def __init__(self, name):\n        pass   # Ihr Code\n", "en": "class DataLogger:\n    def __init__(self, name):\n        pass   # your code\n"},
   solution='class DataLogger:\n    def __init__(self, name):\n        self.name = name\n        self.times = []\n        self.values = []\n\n    def record(self, t, value):\n        self.times.append(t)\n        self.values.append(value)\n        return True\n\n    def count(self):\n        return len(self.values)\n\n    def last(self):\n        if len(self.values) == 0:\n            return None\n        return (self.times[-1], self.values[-1])\n\n\nclass RangeLogger(DataLogger):\n    def __init__(self, name, low, high):\n        super().__init__(name)\n        self.low = low\n        self.high = high\n        self.rejected = 0\n\n    def record(self, t, value):\n        if self.low <= value <= self.high:\n            return super().record(t, value)\n        self.rejected += 1\n        return False\n\n\nlog = RangeLogger("T_Kühlwasser", 0, 120)\nfor t, v in [(0, 21.5), (10, 999.0), (20, 23.0), (30, -40.0)]:\n    log.record(t, v)\nprint(log.count(), log.last(), log.rejected)\n',
   tests='''
ns, out = run()
D, R = ns.get("DataLogger"), ns.get("RangeLogger")
d = call(ns, "DataLogger", "p1")
check(getattr(d, "name", None) == "p1" and getattr(d, "times", None) == [] and getattr(d, "values", None) == [] and method(d, "count") == 0 and method(d, "last") is None, "Neuer DataLogger: leere Listen, count 0, last None", "New DataLogger: empty lists, count 0, last None")
check(method(d, "record", 0, 1.5) is True and method(d, "record", 5, 99.0) is True and method(d, "count") == 2 and method(d, "last") == (5, 99.0) and d.times == [0, 5], "DataLogger speichert alles; last() = (5, 99.0)", "DataLogger stores everything; last() = (5, 99.0)")
r = call(ns, "RangeLogger", "T", 0, 120)
check(isinstance(r, D) and getattr(r, "name", None) == "T" and getattr(r, "rejected", None) == 0 and getattr(r, "values", None) == [], "RangeLogger erbt von DataLogger, rejected = 0", "RangeLogger inherits from DataLogger, rejected = 0")
res = [method(r, "record", t, v) for t, v in [(0, 21.5), (10, 999.0), (20, 120), (30, -40.0), (40, 0)]]
check(res == [True, False, True, False, True], "record: 21.5 ✓, 999 ✗, 120 ✓ (Grenze), −40 ✗, 0 ✓ (Grenze)", "record: 21.5 ✓, 999 ✗, 120 ✓ (limit), −40 ✗, 0 ✓ (limit)")
check(r.values == [21.5, 120, 0] and r.times == [0, 20, 40] and r.rejected == 2 and method(r, "count") == 3 and method(r, "last") == (40, 0), "Gespeichert: 21.5, 120, 0; rejected = 2; last() = (40, 0)", "Stored: 21.5, 120, 0; rejected = 2; last() = (40, 0)")
check(R is not None and "count" not in vars(R) and "last" not in vars(R) and "record" in vars(R), "record überschrieben, count/last nur in der Basisklasse", "record overridden, count/last only in the base class")
''',
   require=["class", "super"], refs=["10.5", "10.3"])

ex(id="k10-assembly", ch="10", lvl=3,
   title={"de": "Baugruppen und Einzelteile", "en": "Assemblies and parts"},
   task={"de": "Eine Stückliste ist hierarchisch: Eine Baugruppe enthält Einzelteile **und** weitere Baugruppen, jeweils mit einer Stückzahl. Schreiben Sie zwei Klassen mit denselben drei Methoden:\n\n`Part(name, mass_kg)` – ein Einzelteil:\n- `total_mass()`: seine Masse\n- `count(name)`: 1, wenn es so heißt, sonst 0\n- `parts_list()`: das Dictionary `{name: 1}`\n\n`Assembly(name)` – eine Baugruppe mit dem Attribut `children` (anfangs leere Liste):\n- `add(component, qty=1)`: hängt das Tupel `(component, qty)` an `children` an; `component` ist ein `Part` oder eine `Assembly`\n- `total_mass()`: Summe aus Stückzahl · Masse aller Bestandteile\n- `count(name)`: wie viele Einzelteile dieses Namens insgesamt enthalten sind (auch in Unterbaugruppen, mit Stückzahlen multipliziert)\n- `parts_list()`: Dictionary Name → Gesamtzahl für **alle** enthaltenen Einzelteile\n\nTipp: Jede Methode von `Assembly` ruft einfach dieselbe Methode ihrer Bestandteile auf – egal, ob das ein `Part` oder eine `Assembly` ist.",
         "en": "A bill of materials is hierarchical: an assembly contains parts **and** further assemblies, each with a quantity. Write two classes with the same three methods:\n\n`Part(name, mass_kg)` – a single part:\n- `total_mass()`: its mass\n- `count(name)`: 1 if that is its name, otherwise 0\n- `parts_list()`: the dictionary `{name: 1}`\n\n`Assembly(name)` – an assembly with the attribute `children` (initially an empty list):\n- `add(component, qty=1)`: appends the tuple `(component, qty)` to `children`; `component` is a `Part` or an `Assembly`\n- `total_mass()`: sum of quantity · mass of all components\n- `count(name)`: how many parts of this name are contained in total (also in sub-assemblies, multiplied by the quantities)\n- `parts_list()`: dictionary name → total number for **all** contained parts\n\nTip: each method of `Assembly` simply calls the same method of its components – no matter whether that is a `Part` or an `Assembly`."},
   starter={"de": "class Part:\n    def __init__(self, name, mass_kg):\n        self.name = name\n        self.mass_kg = mass_kg\n\n\nclass Assembly:\n    def __init__(self, name):\n        self.name = name\n        self.children = []\n", "en": "class Part:\n    def __init__(self, name, mass_kg):\n        self.name = name\n        self.mass_kg = mass_kg\n\n\nclass Assembly:\n    def __init__(self, name):\n        self.name = name\n        self.children = []\n"},
   solution='class Part:\n    def __init__(self, name, mass_kg):\n        self.name = name\n        self.mass_kg = mass_kg\n\n    def total_mass(self):\n        return self.mass_kg\n\n    def count(self, name):\n        return 1 if self.name == name else 0\n\n    def parts_list(self):\n        return {self.name: 1}\n\n\nclass Assembly:\n    def __init__(self, name):\n        self.name = name\n        self.children = []\n\n    def add(self, component, qty=1):\n        self.children.append((component, qty))\n\n    def total_mass(self):\n        total = 0\n        for component, qty in self.children:\n            total += qty * component.total_mass()\n        return total\n\n    def count(self, name):\n        n = 0\n        for component, qty in self.children:\n            n += qty * component.count(name)\n        return n\n\n    def parts_list(self):\n        result = {}\n        for component, qty in self.children:\n            for part, n in component.parts_list().items():\n                result[part] = result.get(part, 0) + qty * n\n        return result\n\n\nscrew = Part("Schraube M6", 0.004)\nbearing = Part("Lager 6204", 0.11)\nhub = Assembly("Nabe")\nhub.add(bearing, 2)\nhub.add(screw, 6)\nwheel = Assembly("Laufrad")\nwheel.add(hub)\nwheel.add(Part("Felge", 1.8))\nwheel.add(screw, 12)\nprint(round(wheel.total_mass(), 3), wheel.count("Schraube M6"), wheel.parts_list())\n',
   tests='''
ns, out = run()
P = lambda n, m: call(ns, "Part", n, m)
s = P("Schraube", 0.004); b = P("Lager", 0.11); f = P("Felge", 1.8)
check(approx(method(s, "total_mass"), 0.004) and method(s, "count", "Schraube") == 1 and method(s, "count", "Lager") == 0 and method(s, "parts_list") == {"Schraube": 1}, "Part: total_mass, count, parts_list", "Part: total_mass, count, parts_list")
hub = call(ns, "Assembly", "Nabe")
method(hub, "add", b, 2); method(hub, "add", s, 6)
check(len(hub.children) == 2 and hub.children[0] == (b, 2), "add() hängt (Bauteil, Stückzahl) an children an", "add() appends (component, quantity) to children")
check(approx(method(hub, "total_mass"), 2 * 0.11 + 6 * 0.004) and method(hub, "count", "Schraube") == 6, "Nabe: 2 Lager + 6 Schrauben = 0.244 kg", "hub: 2 bearings + 6 screws = 0.244 kg")
wheel = call(ns, "Assembly", "Laufrad")
method(wheel, "add", hub); method(wheel, "add", f); method(wheel, "add", s, 12)
em = 0.244 + 1.8 + 12 * 0.004
check(approx(method(wheel, "total_mass"), em) and method(wheel, "count", "Schraube") == 18 and method(wheel, "count", "Lager") == 2, f"Laufrad: {em:.3f} kg, 18 Schrauben (auch in der Nabe), 2 Lager", f"wheel: {em:.3f} kg, 18 screws (also inside the hub), 2 bearings")
cart = call(ns, "Assembly", "Wagen")
method(cart, "add", wheel, 4); method(cart, "add", P("Rahmen", 12.0))
check(approx(method(cart, "total_mass"), 4 * em + 12.0) and method(cart, "parts_list") == {"Lager": 8, "Schraube": 72, "Felge": 4, "Rahmen": 1}, "Drei Ebenen: Wagen mit 4 Laufrädern – parts_list = {Lager: 8, Schraube: 72, Felge: 4, Rahmen: 1}", "Three levels: cart with 4 wheels – parts_list = {Lager: 8, Schraube: 72, Felge: 4, Rahmen: 1}")
check(method(call(ns, "Assembly", "leer"), "total_mass") == 0 and method(call(ns, "Assembly", "leer"), "parts_list") == {}, "Leere Baugruppe: Masse 0, parts_list {}", "Empty assembly: mass 0, parts_list {}")
''',
   require=["class", "dict_methods"], refs=["10.3", "8.3"])

ex(id="k10-signal", ch="10", lvl=3,
   title={"de": "Messsignal als Objekt", "en": "Measurement signal as an object"},
   task={"de": "Schreiben Sie die Klasse `Signal(values, dt)` für ein abgetastetes Messsignal: `values` ist die Liste der Messwerte, `dt` der zeitliche Abstand in s. Speichern Sie eine **Kopie** der Liste im Attribut `values` und `dt` im gleichnamigen Attribut.\n- `__len__`: Anzahl der Messwerte\n- `__add__`: Summe zweier Signale Wert für Wert → neues `Signal`; haben die Signale unterschiedliche Länge oder unterschiedliches `dt`, wird `None` zurückgegeben\n- `__mul__`: Multiplikation mit einer Zahl (`int` oder `float`, prüfen mit `isinstance`) → neues `Signal`; bei anderen Typen `None`\n- `integral()`: das Integral nach der Trapezregel: $\\Delta t \\cdot \\left(\\sum_k v_k - \\dfrac{v_0 + v_{n-1}}{2}\\right)$ (0 bei weniger als zwei Werten)\n- `derivative()`: neues `Signal` aus den Differenzenquotienten $(v_{k+1} - v_k) / \\Delta t$ (ein Wert weniger, gleiches `dt`)\n- `__str__`: genau im Format `Signal: <Anzahl> × <dt> s`, z.B. `Signal: 5 × 0.1 s`\n\nAlle Operationen lassen die beteiligten Signale unverändert.",
         "en": "Write the class `Signal(values, dt)` for a sampled measurement signal: `values` is the list of readings, `dt` the time step in s. Store a **copy** of the list in the attribute `values` and `dt` in the attribute of the same name.\n- `__len__`: number of readings\n- `__add__`: sum of two signals value by value → new `Signal`; if the signals differ in length or in `dt`, `None` is returned\n- `__mul__`: multiplication by a number (`int` or `float`, check with `isinstance`) → new `Signal`; `None` for other types\n- `integral()`: the integral by the trapezoidal rule: $\\Delta t \\cdot \\left(\\sum_k v_k - \\dfrac{v_0 + v_{n-1}}{2}\\right)$ (0 for fewer than two values)\n- `derivative()`: new `Signal` of the difference quotients $(v_{k+1} - v_k) / \\Delta t$ (one value fewer, same `dt`)\n- `__str__`: exactly in the format `Signal: <count> × <dt> s`, e.g. `Signal: 5 × 0.1 s`\n\nNo operation changes the signals involved."},
   starter={"de": "class Signal:\n    def __init__(self, values, dt):\n        pass   # Ihr Code\n", "en": "class Signal:\n    def __init__(self, values, dt):\n        pass   # your code\n"},
   solution='class Signal:\n    def __init__(self, values, dt):\n        self.values = list(values)\n        self.dt = dt\n\n    def __len__(self):\n        return len(self.values)\n\n    def __add__(self, other):\n        if len(self) != len(other) or self.dt != other.dt:\n            return None\n        return Signal([a + b for a, b in zip(self.values, other.values)], self.dt)\n\n    def __mul__(self, factor):\n        if not isinstance(factor, (int, float)):\n            return None\n        return Signal([v * factor for v in self.values], self.dt)\n\n    def integral(self):\n        if len(self.values) < 2:\n            return 0\n        return self.dt * (sum(self.values) - (self.values[0] + self.values[-1]) / 2)\n\n    def derivative(self):\n        v = self.values\n        return Signal([(v[k + 1] - v[k]) / self.dt for k in range(len(v) - 1)], self.dt)\n\n    def __str__(self):\n        return f"Signal: {len(self)} × {self.dt} s"\n\n\ns = Signal([0.0, 2.0, 4.0, 4.0, 2.0], 0.1)\nprint(s, s.integral(), s.derivative().values, (s * 2).values)\n',
   tests='''
ns, out = run()
S = ns.get("Signal")
data = [0.0, 2.0, 4.0, 4.0, 2.0]
s = call(ns, "Signal", data, 0.1)
check(getattr(s, "values", None) == data and getattr(s, "dt", None) == 0.1 and s.values is not data, "values ist eine Kopie der übergebenen Liste, dt gespeichert", "values is a copy of the list passed in, dt stored")
check(safe(lambda: len(s)) == 5 and safe(lambda: str(s)) == "Signal: 5 × 0.1 s", "len(s) = 5, str(s) = 'Signal: 5 × 0.1 s'", "len(s) = 5, str(s) = 'Signal: 5 × 0.1 s'")
t = call(ns, "Signal", [1.0, 1.0, 1.0, 1.0, 1.0], 0.1)
u = safe(lambda: s + t)
check(isinstance(u, S) and u.values == [1.0, 3.0, 5.0, 5.0, 3.0] and u.dt == 0.1 and s.values == data, "s + t addiert Wert für Wert, s bleibt unverändert", "s + t adds value by value, s stays unchanged")
check(safe(lambda: s + call(ns, "Signal", [1.0, 2.0], 0.1)) is None and safe(lambda: s + call(ns, "Signal", [1.0] * 5, 0.2)) is None, "Andere Länge oder anderes dt → None", "Different length or dt → None")
m = safe(lambda: s * 2); m2 = safe(lambda: s * 0.5)
check(isinstance(m, S) and m.values == [0.0, 4.0, 8.0, 8.0, 4.0] and isinstance(m2, S) and m2.values == [0.0, 1.0, 2.0, 2.0, 1.0] and safe(lambda: s * "x") is None, "s * 2, s * 0.5 → neue Signale; s * 'x' → None", "s * 2, s * 0.5 → new signals; s * 'x' → None")
check(approx(method(s, "integral"), 0.1 * (12.0 - 1.0)) and approx(method(call(ns, "Signal", [3.0, 3.0], 2.0), "integral"), 6.0) and method(call(ns, "Signal", [5.0], 1.0), "integral") == 0, "integral(): 1.1 (Trapezregel), [3, 3] mit dt 2 → 6, ein Wert → 0", "integral(): 1.1 (trapezoidal rule), [3, 3] with dt 2 → 6, one value → 0")
d = method(s, "derivative")
check(isinstance(d, S) and len(d.values) == 4 and all(approx(a, b) for a, b in zip(d.values, [20.0, 20.0, 0.0, -20.0])) and d.dt == 0.1 and s.values == data, "derivative() = [20, 20, 0, −20], dt bleibt 0.1", "derivative() = [20, 20, 0, −20], dt stays 0.1")
''',
   require=["class", "magic", "isinstance"], refs=["10.7", "7.4"])

# ================================================================== Anhang A
ex(id="kA-maxline", ch="A", lvl=1,
   title={"de": "Höchsten Druck in einer Datei finden", "en": "Finding the highest pressure in a file"},
   task={"de": "Die Datei `data/druck.txt` enthält in der ersten Zeile eine Überschrift und danach einen Druck in bar pro Zeile (Dezimalpunkt). Öffnen Sie sie mit `with`, überspringen Sie die Überschrift mit `readline()` und lesen Sie die übrigen Zeilen mit einer `for`-Schleife ein. Bestimmen Sie\n- `values`: die Liste der Drücke als `float`, in der Reihenfolge der Datei\n- `max_value`: den höchsten Druck\n- `max_line`: in welcher Zeile der Datei er steht (gezählt ab 1, die Überschrift ist Zeile 1; kommt der Höchstwert mehrfach vor, zählt das erste Vorkommen)\n\nSchreiben Sie anschließend in die Datei `data/max.txt` genau eine Zeile im Format `Maximum: 7.8 bar in Zeile 4` und geben Sie diese Zeile auch aus.",
         "en": "The file `data/druck.txt` contains a heading in its first line, followed by one pressure in bar per line (decimal point). Open it with `with`, skip the heading with `readline()` and read the remaining lines with a `for` loop. Determine\n- `values`: the list of pressures as `float`, in the order of the file\n- `max_value`: the highest pressure\n- `max_line`: in which line of the file it is (counted from 1, the heading is line 1; if the maximum occurs several times, the first occurrence counts)\n\nThen write exactly one line in the format `Maximum: 7.8 bar in Zeile 4` to the file `data/max.txt` (keep the German wording) and print this line as well."},
   starter={"de": "# Die Beispieldatei data/druck.txt wird beim Ausführen angelegt.\n\n# Ihr Code:\n", "en": "# The sample file data/druck.txt is created when you run your code.\n\n# your code:\n"},
   files={"data/druck.txt": "Druck in bar\n6.2\n6.9\n7.8\n7.1\n7.8\n6.5\n"},
   solution='with open("data/druck.txt", encoding="utf-8") as f:\n    f.readline()\n    values = []\n    for line in f:\n        values.append(float(line.strip()))\n\nmax_value = max(values)\nmax_line = values.index(max_value) + 2\ntext = f"Maximum: {max_value} bar in Zeile {max_line}"\nwith open("data/max.txt", "w", encoding="utf-8") as f:\n    f.write(text + "\\n")\nprint(text)\n',
   tests='''
for content in ["Druck in bar\\n6.2\\n6.9\\n7.8\\n7.1\\n7.8\\n6.5\\n", "p_bar\\n12.5\\n3.0\\n", "Druck\\n1.0\\n2.0\\n3.5\\n"]:
    vals = [float(x) for x in content.strip().split("\\n")[1:]]
    ns, out = run(files={"data/druck.txt": content})
    v, mv, ml = need(ns, "values", "max_value", "max_line")
    ev, eml = max(vals), vals.index(max(vals)) + 2
    check(v == vals, f"values = {vals}", f"values = {vals}")
    check(approx(mv, ev) and ml == eml, f"max_value = {ev}, max_line = {eml}", f"max_value = {ev}, max_line = {eml}")
    try:
        lines = [l for l in read_file("data/max.txt").split("\\n") if l.strip()]
    except FileNotFoundError:
        lines = []
    check(len(lines) == 1 and has_num(lines[0], ev) and has_num(lines[0], eml) and lines[0].strip() in out, f"data/max.txt: eine Zeile mit {ev} bar und Zeile {eml} (auch ausgegeben)", f"data/max.txt: one line with {ev} bar and line {eml} (also printed)")
''',
   require=["with", "file_methods"], refs=["A.3", "A.2"])

ex(id="kA-splitdays", ch="A", lvl=2,
   title={"de": "Messdatei nach Tagen aufteilen", "en": "Splitting a measurement file by day"},
   task={"de": "Die Datei `data/messung.csv` enthält eine Kopfzeile `datum;zeit;temperatur` und danach Messzeilen wie `2026-10-05;08:00;21.4` – die Tage können durcheinander stehen. Teilen Sie sie in eine Datei pro Tag auf:\n- Lesen Sie die Datei ein (Kopfzeile überspringen, Leerzeilen ignorieren) und sammeln Sie die Zeilen in einem Dictionary Datum → Liste der Zeilen `zeit;temperatur`.\n- Schreiben Sie für jedes Datum die Datei `data/tag_<datum>.txt` (z.B. `data/tag_2026-10-05.txt`) mit einer Zeile `zeit;temperatur` pro Messung, in der Reihenfolge der Ausgangsdatei.\n- `counts`: Dictionary Datum → Anzahl der Messungen\n- `days`: die sortierte Liste aller Daten\n\nTipp: `line.strip().split(\";\", 1)` trennt das Datum vom Rest der Zeile.",
         "en": "The file `data/messung.csv` contains a header `datum;zeit;temperatur` (date;time;temperature) followed by measurement lines such as `2026-10-05;08:00;21.4` – the days may be mixed up. Split it into one file per day:\n- Read the file (skip the header, ignore blank lines) and collect the lines in a dictionary date → list of the lines `zeit;temperatur`.\n- For every date, write the file `data/tag_<datum>.txt` (e.g. `data/tag_2026-10-05.txt`) with one line `zeit;temperatur` per measurement, in the order of the source file.\n- `counts`: dictionary date → number of measurements\n- `days`: the sorted list of all dates\n\nTip: `line.strip().split(\";\", 1)` separates the date from the rest of the line."},
   starter={"de": "# Die Beispieldatei data/messung.csv wird beim Ausführen angelegt.\n\n# Ihr Code:\n", "en": "# The sample file data/messung.csv is created when you run your code.\n\n# your code:\n"},
   files={"data/messung.csv": "datum;zeit;temperatur\n2026-10-05;08:00;21.4\n2026-10-06;08:00;19.8\n2026-10-05;12:00;23.1\n\n2026-10-07;08:00;18.2\n2026-10-06;12:00;22.0\n2026-10-05;16:00;22.5\n"},
   solution='by_day = {}\nwith open("data/messung.csv", encoding="utf-8") as f:\n    f.readline()\n    for line in f:\n        line = line.strip()\n        if line == "":\n            continue\n        day, rest = line.split(";", 1)\n        if day not in by_day:\n            by_day[day] = []\n        by_day[day].append(rest)\n\nfor day, rows in by_day.items():\n    with open(f"data/tag_{day}.txt", "w", encoding="utf-8") as f:\n        for row in rows:\n            f.write(row + "\\n")\n\ncounts = {day: len(rows) for day, rows in by_day.items()}\ndays = sorted(by_day)\nprint(days, counts)\n',
   tests='''
F1 = "datum;zeit;temperatur\\n2026-10-05;08:00;21.4\\n2026-10-06;08:00;19.8\\n2026-10-05;12:00;23.1\\n\\n2026-10-07;08:00;18.2\\n2026-10-06;12:00;22.0\\n2026-10-05;16:00;22.5\\n"
F2 = "datum;zeit;temperatur\\n2027-01-02;10:00;-3.5\\n2027-01-01;10:00;-1.0\\n"
for content in [F1, F2]:
    rows = [l.split(";", 1) for l in content.strip().split("\\n")[1:] if l.strip()]
    exp = {}
    for d, r in rows:
        exp.setdefault(d, []).append(r)
    ns, out = run(files={"data/messung.csv": content})
    c, ds = need(ns, "counts", "days")
    check(c == {d: len(r) for d, r in exp.items()}, f"counts = {({d: len(r) for d, r in exp.items()})}", f"counts = {({d: len(r) for d, r in exp.items()})}")
    check(ds == sorted(exp), f"days = {sorted(exp)}", f"days = {sorted(exp)}")
    ok = True
    for d, r in exp.items():
        try:
            got = [l.strip() for l in read_file(f"data/tag_{d}.txt").split("\\n") if l.strip()]
        except FileNotFoundError:
            got = None
        ok = ok and got == r
    check(ok, "Für jeden Tag gibt es data/tag_<datum>.txt mit den Zeilen zeit;temperatur in der Reihenfolge der Ausgangsdatei", "For every day there is data/tag_<date>.txt with the lines zeit;temperatur in the order of the source file")
''',
   require=["with", "dict"], refs=["A.3", "A.2", "8.3"])

# ================================================================== Anhang B
ex(id="kB-device", ch="B", lvl=2,
   title={"de": "Messgerät mit Wiederholversuchen abfragen", "en": "Querying an instrument with retries"},
   task={"de": "Ein Messgerät antwortet über eine gestörte Schnittstelle nicht immer brauchbar. Simuliert wird es durch die Liste `replies` mit den Antworten als Text in zeitlicher Reihenfolge, z.B. `[\"ERR\", \"\", \"23.7\"]`. Schreiben Sie `query(replies, attempts=3)`:\n- Holen Sie die jeweils nächste Antwort mit `replies.pop(0)` und wandeln Sie sie mit `float()` um. Gelingt das, wird der Wert sofort zurückgegeben (übrige Antworten bleiben in der Liste).\n- Ist eine Antwort unbrauchbar (`ValueError`), wird es mit der nächsten Antwort erneut versucht – insgesamt höchstens `attempts`-mal.\n- Sind alle Versuche verbraucht oder ist die Liste vorher leer (`IndexError` bei `pop`), lösen Sie einen `ValueError` mit der Meldung `Keine gültige Antwort nach <n> Versuchen` aus; `<n>` ist die Anzahl der tatsächlich gelesenen Antworten.\n\nFangen Sie die beiden Fehlertypen gezielt ab.",
         "en": "An instrument does not always give a usable answer over a noisy interface. It is simulated by the list `replies` with the answers as text in chronological order, e.g. `[\"ERR\", \"\", \"23.7\"]`. Write `query(replies, attempts=3)`:\n- Fetch the next answer with `replies.pop(0)` and convert it with `float()`. If that works, return the value immediately (the remaining answers stay in the list).\n- If an answer is unusable (`ValueError`), try again with the next answer – at most `attempts` times in total.\n- If all attempts are used up or the list runs empty first (`IndexError` on `pop`), raise a `ValueError` with the message `Keine gültige Antwort nach <n> Versuchen` (no valid answer after n attempts); `<n>` is the number of answers actually read.\n\nCatch the two error types specifically."},
   starter={"de": "def query(replies, attempts=3):\n    pass   # Ihr Code\n\n\nprint(query([\"ERR\", \"\", \"23.7\"]))\n", "en": "def query(replies, attempts=3):\n    pass   # your code\n\n\nprint(query([\"ERR\", \"\", \"23.7\"]))\n"},
   solution='def query(replies, attempts=3):\n    tries = 0\n    while tries < attempts:\n        try:\n            reply = replies.pop(0)\n        except IndexError:\n            break\n        tries += 1\n        try:\n            return float(reply)\n        except ValueError:\n            pass\n    raise ValueError(f"Keine gültige Antwort nach {tries} Versuchen")\n\n\nprint(query(["ERR", "", "23.7"]))\n',
   tests='''
ns, out = run()
f = ns.get("query")
if f is None:
    raise TestFailure("Es gibt keine Funktion query. / There is no function query.")
r = ["21.5", "ERR"]
check(approx(call(ns, "query", r), 21.5) and r == ["ERR"], "Erste Antwort gültig → 21.5, die übrige Antwort bleibt in der Liste", "First answer valid → 21.5, the remaining answer stays in the list")
r = ["ERR", "", "23.7", "24.0"]
check(approx(call(ns, "query", r), 23.7) and r == ["24.0"], "Zwei Störungen, dann 23.7 (dritter Versuch)", "Two faults, then 23.7 (third attempt)")
def msg(replies, **kw):
    try:
        f(replies, **kw)
    except ValueError as e:
        return str(e)
    except Exception as e:
        return "anderer Fehler " + type(e).__name__
    return None
r = ["x", "y", "z", "5.0"]
m = msg(r)
check(m is not None and not m.startswith("anderer") and "3" in m and r == ["5.0"], "Drei unbrauchbare Antworten → ValueError mit 3 Versuchen, die vierte Antwort wird nicht gelesen", "Three unusable answers → ValueError with 3 attempts, the fourth answer is not read")
m = msg(["ERR"])
check(m is not None and not m.startswith("anderer") and "1" in m, "Liste nach einer Antwort leer → ValueError (1 Versuch), kein IndexError", "List empty after one answer → ValueError (1 attempt), no IndexError")
m = msg([])
check(m is not None and not m.startswith("anderer") and "0" in m, "Leere Liste → ValueError (0 Versuche)", "Empty list → ValueError (0 attempts)")
r = ["a", "b", "c", "d", "7"]
check(approx(call(ns, "query", r, attempts=5), 7.0) and r == [], "attempts=5: fünfter Versuch gültig", "attempts=5: fifth attempt valid")
check(msg(["a", "b"], attempts=1) is not None and "1" in msg(["a", "b"], attempts=1), "attempts=1: nach einer Störung ValueError", "attempts=1: ValueError after one fault")
''',
   require=["try", "raise", "def"], refs=["B.3", "B.4"])

ex(id="kB-calc", ch="B", lvl=3,
   title={"de": "Taschenrechner mit Fehlermeldungen", "en": "Calculator with error messages"},
   task={"de": "Ein Prüfstand protokolliert Rechenschritte als Text der Form `<Zahl> <Operator> <Zahl>`, z.B. `\"12,5 * 4\"` (Dezimalkomma erlaubt, Operatoren `+`, `-`, `*`, `/`).\n\n1. Schreiben Sie `calculate(a, op, b)` für zwei Zahlen. Bei einem unbekannten Operator lösen Sie einen `ValueError` aus; eine Division durch 0 führt ohnehin zu einem `ZeroDivisionError` – den lassen Sie durch.\n2. Schreiben Sie `evaluate(expr)`, die **zwei Werte** zurückgibt: `(ergebnis, None)` bei Erfolg, sonst `(None, meldung)` mit genau einer dieser Meldungen:\n   - `\"Format\"`: der Text besteht nicht aus genau drei durch Leerzeichen getrennten Teilen (`split()`)\n   - `\"Zahl ungültig\"`: eine der Zahlen lässt sich nicht umwandeln (`ValueError` beim Umwandeln)\n   - `\"Operator unbekannt\"`: `calculate` meldet einen `ValueError`\n   - `\"Division durch 0\"`: `calculate` meldet einen `ZeroDivisionError`\n\n   Verwenden Sie dafür zwei getrennte `try`-Blöcke: einen für das Umwandeln der Zahlen, einen für den Aufruf von `calculate`.\n3. Schreiben Sie `evaluate_all(lines)`, die **zwei Werte** zurückgibt: die Liste der Ergebnisse aller erfolgreichen Zeilen (in der Reihenfolge der Zeilen) und ein Dictionary Meldung → Anzahl (nur Meldungen, die vorkommen).",
         "en": "A test bench logs calculation steps as text of the form `<number> <operator> <number>`, e.g. `\"12,5 * 4\"` (decimal comma allowed, operators `+`, `-`, `*`, `/`).\n\n1. Write `calculate(a, op, b)` for two numbers. For an unknown operator raise a `ValueError`; a division by 0 leads to a `ZeroDivisionError` anyway – let it through.\n2. Write `evaluate(expr)` that returns **two values**: `(result, None)` on success, otherwise `(None, message)` with exactly one of these messages (keep the German texts):\n   - `\"Format\"`: the text does not consist of exactly three parts separated by spaces (`split()`)\n   - `\"Zahl ungültig\"` (invalid number): one of the numbers cannot be converted (`ValueError` when converting)\n   - `\"Operator unbekannt\"` (unknown operator): `calculate` reports a `ValueError`\n   - `\"Division durch 0\"` (division by 0): `calculate` reports a `ZeroDivisionError`\n\n   Use two separate `try` blocks for this: one for converting the numbers, one for calling `calculate`.\n3. Write `evaluate_all(lines)` that returns **two values**: the list of the results of all successful lines (in the order of the lines) and a dictionary message → count (only messages that occur)."},
   starter={"de": "def calculate(a, op, b):\n    pass   # Ihr Code\n\n\ndef evaluate(expr):\n    pass   # Ihr Code\n", "en": "def calculate(a, op, b):\n    pass   # your code\n\n\ndef evaluate(expr):\n    pass   # your code\n"},
   solution='def calculate(a, op, b):\n    if op == "+":\n        return a + b\n    elif op == "-":\n        return a - b\n    elif op == "*":\n        return a * b\n    elif op == "/":\n        return a / b\n    raise ValueError(f"Unbekannter Operator: {op}")\n\n\ndef evaluate(expr):\n    parts = expr.split()\n    if len(parts) != 3:\n        return None, "Format"\n    try:\n        a = float(parts[0].replace(",", "."))\n        b = float(parts[2].replace(",", "."))\n    except ValueError:\n        return None, "Zahl ungültig"\n    try:\n        return calculate(a, parts[1], b), None\n    except ValueError:\n        return None, "Operator unbekannt"\n    except ZeroDivisionError:\n        return None, "Division durch 0"\n\n\ndef evaluate_all(lines):\n    results = []\n    errors = {}\n    for line in lines:\n        value, message = evaluate(line)\n        if message is None:\n            results.append(value)\n        else:\n            errors[message] = errors.get(message, 0) + 1\n    return results, errors\n\n\nprint(evaluate("12,5 * 4"), evaluate("3 / 0"), evaluate("2 ^ 3"))\nprint(evaluate_all(["1 + 2", "x * 3", "4 / 0", "5", "6 - 1,5"]))\n',
   tests='''
ns, out = run()
c = ns.get("calculate")
check(approx(call(ns, "calculate", 6.0, "+", 1.5), 7.5) and approx(call(ns, "calculate", 6.0, "/", 1.5), 4.0) and approx(call(ns, "calculate", 6.0, "-", 1.5), 4.5) and approx(call(ns, "calculate", 6.0, "*", 1.5), 9.0), "calculate rechnet + - * /", "calculate computes + - * /")
check(c is not None and raises(ValueError, lambda: c(1.0, "^", 2.0)) and raises(ZeroDivisionError, lambda: c(1.0, "/", 0.0)), "calculate: unbekannter Operator → ValueError, Division durch 0 → ZeroDivisionError", "calculate: unknown operator → ValueError, division by 0 → ZeroDivisionError")
cases = [("12,5 * 4", (50.0, None)), ("3 / 0", (None, "Division durch 0")), ("2 ^ 3", (None, "Operator unbekannt")), ("x * 3", (None, "Zahl ungültig")), ("4,5,1 + 1", (None, "Zahl ungültig")), ("5", (None, "Format")), ("1 + 2 + 3", (None, "Format")), ("-2 - -3", (1.0, None)), ("", (None, "Format"))]
for expr, e in cases:
    r = call(ns, "evaluate", expr)
    ok = isinstance(r, tuple) and len(r) == 2 and r[1] == e[1] and (approx(r[0], e[0]) if e[0] is not None else r[0] is None)
    check(ok, f"evaluate({expr!r}) = {e}", f"evaluate({expr!r}) = {e}")
r = call(ns, "evaluate_all", ["1 + 2", "x * 3", "4 / 0", "5", "6 - 1,5", "8 / 0"])
check(isinstance(r, tuple) and len(r) == 2 and [round(x, 9) for x in r[0]] == [3.0, 4.5] and r[1] == {"Zahl ungültig": 1, "Division durch 0": 2, "Format": 1}, "evaluate_all: Ergebnisse [3.0, 4.5], Meldungen {Zahl ungültig: 1, Division durch 0: 2, Format: 1}", "evaluate_all: results [3.0, 4.5], messages {Zahl ungültig: 1, Division durch 0: 2, Format: 1}")
check(tuple(call(ns, "evaluate_all", [])) == ([], {}), "evaluate_all([]) = ([], {})", "evaluate_all([]) = ([], {})")
''',
   require=["try", "raise", "def"], refs=["B.3", "B.4", "8.3"])
