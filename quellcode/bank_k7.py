from exlib import ex

# Kapitel 7: zusätzlich def, return, Standardargumente, Keyword-Argumente, *args, global, isinstance,
# sum/max/min/sorted, divmod, Typ-Annotationen. Kein Slicing, keine Dicts/Sets, keine Comprehensions, kein zip.

ex(id="k7-kelvin", ch="7", lvl=1,
   title={"de": "Umrechnungsfunktionen", "en": "Conversion functions"},
   task={"de": "Schreiben Sie zwei Funktionen, die ihr Ergebnis **zurückgeben**:\n- `celsius_to_kelvin(c)`\n- `kelvin_to_celsius(k)`\n\nRufen Sie beide einmal auf und geben Sie die Ergebnisse aus.",
         "en": "Write two functions that **return** their result:\n- `celsius_to_kelvin(c)`\n- `kelvin_to_celsius(k)`\n\nCall each once and print the results."},
   starter={"de": "def celsius_to_kelvin(c):\n    ...\n", "en": "def celsius_to_kelvin(c):\n    ...\n"},
   solution='def celsius_to_kelvin(c):\n    return c + 273.15\n\ndef kelvin_to_celsius(k):\n    return k - 273.15\n\nprint(celsius_to_kelvin(20), kelvin_to_celsius(0))\n',
   tests='''
ns, out = run()
for c in [20, -273.15, 100.5]:
    check(approx(call(ns, "celsius_to_kelvin", c), c + 273.15), f"celsius_to_kelvin({c}) = {c + 273.15:g}", f"celsius_to_kelvin({c}) = {c + 273.15:g}")
for k in [0, 300, 273.15]:
    r = call(ns, "kelvin_to_celsius", k)
    check(r is not None and approx(r, k - 273.15), f"kelvin_to_celsius({k}) = {k - 273.15:g}", f"kelvin_to_celsius({k}) = {k - 273.15:g}")
''',
   require=["def", "return"], refs=["7.3", "7.3r"])

ex(id="k7-flow", ch="7", lvl=1,
   title={"de": "Volumenstrom im Rohr", "en": "Flow rate in a pipe"},
   task={"de": "Schreiben Sie\n- `pipe_area(d)`: Querschnittsfläche eines Rohrs mit Innendurchmesser `d` (m), $A = \\pi d^2/4$ (mit der vorgegebenen Konstante `PI`)\n- `flow_rate(d, v)`: Volumenstrom $Q = A \\cdot v$ in m³/s bei der Strömungsgeschwindigkeit `v` (m/s). Nutzen Sie dafür `pipe_area`.\n- `flow_lpm(d, v)`: denselben Volumenstrom in Litern pro Minute.",
         "en": "Write\n- `pipe_area(d)`: cross-sectional area of a pipe with inner diameter `d` (m), $A = \\pi d^2/4$ (using the given constant `PI`)\n- `flow_rate(d, v)`: flow rate $Q = A \\cdot v$ in m³/s at flow velocity `v` (m/s). Use `pipe_area` for it.\n- `flow_lpm(d, v)`: the same flow rate in litres per minute."},
   starter={"de": "PI = 3.14159\n\ndef pipe_area(d):\n    ...\n", "en": "PI = 3.14159\n\ndef pipe_area(d):\n    ...\n"},
   solution='PI = 3.14159\n\ndef pipe_area(d):\n    return PI * d**2 / 4\n\ndef flow_rate(d, v):\n    return pipe_area(d) * v\n\ndef flow_lpm(d, v):\n    return flow_rate(d, v) * 1000 * 60\n\nprint(flow_lpm(0.05, 1.2))\n',
   tests='''
import math as _m
ns, out = run()
for d, v in [(0.05, 1.2), (0.1, 2.0), (0.02, 0.5)]:
    A = 3.14159 * d * d / 4
    check(approx(call(ns, "pipe_area", d), A), f"pipe_area({d}) ≈ {A:.6f} m²", f"pipe_area({d}) ≈ {A:.6f} m²")
    check(approx(call(ns, "flow_rate", d, v), A * v), f"flow_rate({d}, {v}) ≈ {A*v:.6f} m³/s", f"flow_rate({d}, {v}) ≈ {A*v:.6f} m³/s")
    check(approx(call(ns, "flow_lpm", d, v), A * v * 60000), f"flow_lpm({d}, {v}) ≈ {A*v*60000:.1f} l/min", f"flow_lpm({d}, {v}) ≈ {A*v*60000:.1f} l/min")
''',
   require=["def", "return"], refs=["7.3", "7.3r"])

ex(id="k7-inrange", ch="7", lvl=1,
   title={"de": "Grenzwertprüfung als Funktion", "en": "Limit check as a function"},
   task={"de": "Schreiben Sie `in_range(value, low, high)`, die `True` zurückgibt, wenn `low <= value <= high`, sonst `False`. Schreiben Sie außerdem `count_in_range(values, low, high)`, die mit Hilfe von `in_range` zählt, wie viele Werte einer Liste im Bereich liegen.",
         "en": "Write `in_range(value, low, high)` that returns `True` if `low <= value <= high`, otherwise `False`. Also write `count_in_range(values, low, high)` that uses `in_range` to count how many values of a list lie within the range."},
   starter={"de": "def in_range(value, low, high):\n    ...\n", "en": "def in_range(value, low, high):\n    ...\n"},
   solution='def in_range(value, low, high):\n    return low <= value <= high\n\ndef count_in_range(values, low, high):\n    count = 0\n    for v in values:\n        if in_range(v, low, high):\n            count += 1\n    return count\n\nprint(count_in_range([4.9, 5.0, 5.2, 5.6], 4.95, 5.25))\n',
   tests='''
ns, out = run()
for v, lo, hi in [(5.0, 4.95, 5.05), (4.95, 4.95, 5.05), (5.1, 4.95, 5.05), (-1, 0, 10)]:
    check(call(ns, "in_range", v, lo, hi) is (lo <= v <= hi), f"in_range({v}, {lo}, {hi}) = {lo <= v <= hi}", f"in_range({v}, {lo}, {hi}) = {lo <= v <= hi}")
for vals, lo, hi in [([4.9, 5.0, 5.2, 5.6], 4.95, 5.25), ([], 0, 1), ([1, 2, 3], 1, 3)]:
    e = len([x for x in vals if lo <= x <= hi])
    check(call(ns, "count_in_range", vals, lo, hi) == e, f"count_in_range({vals}, {lo}, {hi}) = {e}", f"count_in_range({vals}, {lo}, {hi}) = {e}")
''',
   require=["def", "return"], refs=["7.3", "7.3r"])

ex(id="k7-vdrop", ch="7", lvl=1,
   title={"de": "Spannungsfall in einer Leitung", "en": "Voltage drop in a cable"},
   task={"de": "Der Spannungsfall auf einer zweiadrigen Leitung beträgt $\\Delta U = \\dfrac{2 \\rho l I}{A}$ ($l$: einfache Länge in m, $A$: Querschnitt in mm², $I$ in A, $\\rho$ in Ω·mm²/m). Schreiben Sie `voltage_drop(current, length, area, rho=0.0178)` mit dem Standardwert für Kupfer. Rufen Sie die Funktion einmal für Kupfer und einmal mit `rho=0.0287` (Aluminium) als Keyword-Argument auf.",
         "en": "The voltage drop on a two-wire cable is $\\Delta U = \\dfrac{2 \\rho l I}{A}$ ($l$: single length in m, $A$: cross-section in mm², $I$ in A, $\\rho$ in Ω·mm²/m). Write `voltage_drop(current, length, area, rho=0.0178)` with the default value for copper. Call it once for copper and once with `rho=0.0287` (aluminium) as a keyword argument."},
   starter={"de": "def voltage_drop(current, length, area, rho=0.0178):\n    ...\n", "en": "def voltage_drop(current, length, area, rho=0.0178):\n    ...\n"},
   solution='def voltage_drop(current, length, area, rho=0.0178):\n    return 2 * rho * length * current / area\n\nprint(voltage_drop(16, 25, 2.5))\nprint(voltage_drop(16, 25, 2.5, rho=0.0287))\n',
   tests='''
ns, out = run()
for I, l, A in [(16, 25, 2.5), (10, 50, 1.5), (32, 10, 6.0)]:
    check(approx(call(ns, "voltage_drop", I, l, A), 2 * 0.0178 * l * I / A), f"Kupfer: voltage_drop({I}, {l}, {A}) ≈ {2*0.0178*l*I/A:.3f} V", f"Copper: voltage_drop({I}, {l}, {A}) ≈ {2*0.0178*l*I/A:.3f} V")
check(approx(call(ns, "voltage_drop", 16, 25, 2.5, rho=0.0287), 2 * 0.0287 * 25 * 16 / 2.5), "Aluminium mit rho=0.0287 ≈ 9.184 V", "Aluminium with rho=0.0287 ≈ 9.184 V")
''',
   require=["default_arg"], refs=["7.3p", "7.3k"])

ex(id="k7-units", ch="7", lvl=2,
   title={"de": "Längeneinheiten umrechnen", "en": "Converting length units"},
   task={"de": "Schreiben Sie `to_metres(value, unit)`, die eine Länge in Meter umrechnet. Erlaubte Einheiten: `\"mm\"`, `\"cm\"`, `\"m\"`, `\"km\"`, `\"in\"` (0.0254 m) und `\"ft\"` (0.3048 m). Bei unbekannter Einheit wird `None` zurückgegeben.\n\nSchreiben Sie dann `convert(value, unit_from, unit_to)`, die mit Hilfe von `to_metres` zwischen zwei beliebigen Einheiten umrechnet (ebenfalls `None` bei unbekannter Einheit).",
         "en": "Write `to_metres(value, unit)` that converts a length to metres. Allowed units: `\"mm\"`, `\"cm\"`, `\"m\"`, `\"km\"`, `\"in\"` (0.0254 m) and `\"ft\"` (0.3048 m). For an unknown unit, return `None`.\n\nThen write `convert(value, unit_from, unit_to)` that uses `to_metres` to convert between any two units (also `None` for an unknown unit)."},
   starter={"de": "def to_metres(value, unit):\n    ...\n", "en": "def to_metres(value, unit):\n    ...\n"},
   solution='def to_metres(value, unit):\n    if unit == "mm":\n        return value / 1000\n    elif unit == "cm":\n        return value / 100\n    elif unit == "m":\n        return value\n    elif unit == "km":\n        return value * 1000\n    elif unit == "in":\n        return value * 0.0254\n    elif unit == "ft":\n        return value * 0.3048\n    return None\n\ndef convert(value, unit_from, unit_to):\n    metres = to_metres(value, unit_from)\n    one = to_metres(1, unit_to)\n    if metres is None or one is None:\n        return None\n    return metres / one\n\nprint(convert(12, "in", "mm"))\n',
   tests='''
F = {"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0, "in": 0.0254, "ft": 0.3048}
ns, out = run()
for v, u in [(1500, "mm"), (3, "km"), (12, "in"), (6, "ft"), (2.5, "m")]:
    check(approx(call(ns, "to_metres", v, u), v * F[u]), f"to_metres({v}, {u!r}) = {v*F[u]:g}", f"to_metres({v}, {u!r}) = {v*F[u]:g}")
check(call(ns, "to_metres", 5, "yard") is None, "Unbekannte Einheit liefert None", "Unknown unit returns None")
for v, a, b in [(12, "in", "mm"), (1, "km", "ft"), (250, "cm", "m")]:
    check(approx(call(ns, "convert", v, a, b), v * F[a] / F[b]), f"convert({v}, {a!r}, {b!r}) ≈ {v*F[a]/F[b]:.4g}", f"convert({v}, {a!r}, {b!r}) ≈ {v*F[a]/F[b]:.4g}")
check(call(ns, "convert", 1, "m", "mile") is None and call(ns, "convert", 1, "mile", "m") is None, "convert mit unbekannter Einheit liefert None", "convert with an unknown unit returns None")
''',
   require=["def", "if"], refs=["7.3r", "6.1b"])

ex(id="k7-stress", ch="7", lvl=2,
   title={"de": "Spannungsnachweis", "en": "Stress check"},
   task={"de": "Schreiben Sie `stress_check(force, area, limit=235.0)` für einen Zugstab: Die Spannung $\\sigma = F/A$ ($F$ in N, $A$ in mm², $\\sigma$ in N/mm²). Die Funktion gibt **drei Werte** zurück: die Spannung, ob der Nachweis erfüllt ist ($\\sigma \\le \\mathit{limit}$) und den Ausnutzungsgrad $\\sigma/\\mathit{limit}$ in Prozent (auf eine Nachkommastelle gerundet).\n\nRufen Sie die Funktion für Baustahl S235 (Standard) und für S355 (`limit=355.0`) auf.",
         "en": "Write `stress_check(force, area, limit=235.0)` for a tension rod: the stress $\\sigma = F/A$ ($F$ in N, $A$ in mm², $\\sigma$ in N/mm²). The function returns **three values**: the stress, whether the check passes ($\\sigma \\le \\mathit{limit}$) and the utilisation $\\sigma/\\mathit{limit}$ in percent (rounded to one decimal).\n\nCall the function for structural steel S235 (default) and for S355 (`limit=355.0`)."},
   starter={"de": "def stress_check(force, area, limit=235.0):\n    ...\n", "en": "def stress_check(force, area, limit=235.0):\n    ...\n"},
   solution='def stress_check(force, area, limit=235.0):\n    sigma = force / area\n    ok = sigma <= limit\n    utilisation = round(sigma / limit * 100, 1)\n    return sigma, ok, utilisation\n\nprint(stress_check(50000, 314.0))\nprint(stress_check(90000, 314.0, limit=355.0))\n',
   tests='''
ns, out = run()
for F, A, lim in [(50000, 314.0, 235.0), (90000, 314.0, 235.0), (90000, 314.0, 355.0), (0, 10.0, 235.0), (23500, 100.0, 235.0)]:
    r = call(ns, "stress_check", F, A) if lim == 235.0 else call(ns, "stress_check", F, A, limit=lim)
    s = F / A
    ok = isinstance(r, tuple) and len(r) == 3
    check(ok and approx(r[0], s), f"F = {F} N, A = {A} mm²: σ ≈ {s:.1f} N/mm²", f"F = {F} N, A = {A} mm²: σ ≈ {s:.1f} N/mm²")
    check(ok and r[1] is (s <= lim) and approx(r[2], round(s / lim * 100, 1), 1e-9), f"Grenze {lim}: erfüllt = {s <= lim}, Ausnutzung {round(s/lim*100, 1)} %", f"limit {lim}: passes = {s <= lim}, utilisation {round(s/lim*100, 1)} %")
''',
   require=["default_arg", "return"], refs=["7.3r", "7.3p"])

ex(id="k7-topn", ch="7", lvl=2,
   title={"de": "Die größten Ausschläge", "en": "The largest amplitudes"},
   task={"de": "Schreiben Sie `top_n(values, n=3)`, die eine **neue** Liste mit den `n` größten Werten in absteigender Reihenfolge zurückgibt. Die übergebene Liste darf nicht verändert werden. Hat die Liste weniger als `n` Einträge, werden alle (absteigend) zurückgegeben.\n\nTipp: Sortieren Sie mit `sorted()` (erzeugt eine neue Liste) und kehren Sie diese mit `.reverse()` um. Slicing kommt erst in Kapitel 8 – bauen Sie die Ergebnisliste mit einer Schleife auf.",
         "en": "Write `top_n(values, n=3)` that returns a **new** list with the `n` largest values in descending order. The list passed in must not be modified. If the list has fewer than `n` entries, return all of them (descending).\n\nTip: sort with `sorted()` (creates a new list) and reverse it with `.reverse()`. Slicing only comes in chapter 8 – build the result list with a loop."},
   starter={"de": "def top_n(values, n=3):\n    ...\n", "en": "def top_n(values, n=3):\n    ...\n"},
   solution='def top_n(values, n=3):\n    ordered = sorted(values)\n    ordered.reverse()\n    result = []\n    for v in ordered:\n        if len(result) == n:\n            break\n        result.append(v)\n    return result\n\nprint(top_n([0.4, 2.7, 1.9, 3.3, 0.8]))\n',
   tests='''
ns, out = run()
for vals, n in [([0.4, 2.7, 1.9, 3.3, 0.8], 3), ([5, 1, 4], 1), ([2.0, 1.0], 5), ([3, 3, 1, 2], 2)]:
    arg = list(vals)
    r = call(ns, "top_n", arg) if n == 3 else call(ns, "top_n", arg, n)
    e = sorted(vals, reverse=True)[:n]
    check(r == e, f"top_n({vals}, {n}) = {e}", f"top_n({vals}, {n}) = {e}")
    check(arg == vals, "Die übergebene Liste bleibt unverändert", "The list passed in stays unchanged")
''',
   require=["default_arg"], forbid=["slice"], refs=["7.2s", "7.3p", "7.7"])

ex(id="k7-trapezoid", ch="7", lvl=3,
   title={"de": "Energie aus Messdaten (Trapezregel)", "en": "Energy from measured data (trapezoidal rule)"},
   task={"de": "Schreiben Sie `trapezoid(xs, ys)`, die das Integral über Messpunkte mit der Trapezregel berechnet: Summe über alle Intervalle von $(x_{i+1} - x_i) \\cdot \\dfrac{y_i + y_{i+1}}{2}$. Die Zeitpunkte müssen nicht gleichabständig sein. Bei unterschiedlich langen Listen oder weniger als zwei Punkten soll `None` zurückgegeben werden.\n\nBerechnen Sie damit die Energie in Wh aus Zeitpunkten in h und Leistungswerten in W.",
         "en": "Write `trapezoid(xs, ys)` that computes the integral over measured points using the trapezoidal rule: the sum over all intervals of $(x_{i+1} - x_i) \\cdot \\dfrac{y_i + y_{i+1}}{2}$. The time points need not be equally spaced. If the lists differ in length or have fewer than two points, return `None`.\n\nUse it to compute the energy in Wh from time points in h and power values in W."},
   starter={"de": "def trapezoid(xs, ys):\n    ...\n\nt_h = [0, 0.5, 1.0, 2.0, 3.0]\np_w = [0, 400, 650, 700, 300]\n", "en": "def trapezoid(xs, ys):\n    ...\n\nt_h = [0, 0.5, 1.0, 2.0, 3.0]\np_w = [0, 400, 650, 700, 300]\n"},
   solution='def trapezoid(xs, ys):\n    if len(xs) != len(ys) or len(xs) < 2:\n        return None\n    total = 0\n    for i in range(len(xs) - 1):\n        total += (xs[i + 1] - xs[i]) * (ys[i] + ys[i + 1]) / 2\n    return total\n\nt_h = [0, 0.5, 1.0, 2.0, 3.0]\np_w = [0, 400, 650, 700, 300]\nprint(trapezoid(t_h, p_w), "Wh")\n',
   tests='''
def ref(x, y):
    return sum((x[i+1] - x[i]) * (y[i] + y[i+1]) / 2 for i in range(len(x) - 1))
ns, out = run()
for x, y in [([0, 0.5, 1.0, 2.0, 3.0], [0, 400, 650, 700, 300]), ([0, 1], [2, 2]), ([0.0, 0.1, 0.3], [1.0, 4.0, -2.0])]:
    check(approx(call(ns, "trapezoid", x, y), ref(x, y)), f"trapezoid({x}, {y}) ≈ {ref(x, y):g}", f"trapezoid({x}, {y}) ≈ {ref(x, y):g}")
check(call(ns, "trapezoid", [0, 1, 2], [1, 2]) is None, "Unterschiedlich lange Listen liefern None", "Lists of different length return None")
check(call(ns, "trapezoid", [1], [5]) is None, "Ein einzelner Punkt liefert None", "A single point returns None")
''',
   require=["def", "for"], refs=["7.3r", "6.2b", "6.3b"])

ex(id="k7-std", ch="7", lvl=3,
   title={"de": "Mittelwert und Standardabweichung", "en": "Mean and standard deviation"},
   task={"de": "Schreiben Sie `mean_std(values)`, die Mittelwert und **Stichproben**-Standardabweichung zurückgibt (zwei Rückgabewerte):\n\n$$s = \\sqrt{\\dfrac{\\sum_i (x_i - \\bar{x})^2}{n - 1}}$$\n\nBei weniger als zwei Werten wird `None` zurückgegeben. Schreiben Sie außerdem `outliers(values, k=2.0)`, die eine Liste aller Werte zurückgibt, die mehr als `k` Standardabweichungen vom Mittelwert entfernt sind.",
         "en": "Write `mean_std(values)` that returns the mean and the **sample** standard deviation (two return values):\n\n$$s = \\sqrt{\\dfrac{\\sum_i (x_i - \\bar{x})^2}{n - 1}}$$\n\nWith fewer than two values, return `None`. Also write `outliers(values, k=2.0)` that returns a list of all values more than `k` standard deviations away from the mean."},
   starter={"de": "def mean_std(values):\n    ...\n", "en": "def mean_std(values):\n    ...\n"},
   solution='def mean_std(values):\n    n = len(values)\n    if n < 2:\n        return None\n    mean = sum(values) / n\n    squares = 0\n    for x in values:\n        squares += (x - mean) ** 2\n    std = (squares / (n - 1)) ** 0.5\n    return mean, std\n\ndef outliers(values, k=2.0):\n    stats = mean_std(values)\n    if stats is None:\n        return []\n    mean, std = stats\n    result = []\n    for x in values:\n        if abs(x - mean) > k * std:\n            result.append(x)\n    return result\n\nprint(mean_std([9.8, 10.1, 10.0, 9.9, 10.2]))\n',
   tests='''
import statistics as _st
_srt = lambda x: sorted(x) if isinstance(x, (list, tuple)) else x
ns, out = run()
for v in [[9.8, 10.1, 10.0, 9.9, 10.2], [1, 2, 3, 4], [5.0, 5.0]]:
    r = call(ns, "mean_std", v)
    check(isinstance(r, tuple) and len(r) == 2 and approx(r[0], _st.mean(v)) and approx(r[1], _st.stdev(v)), f"mean_std({v}) ≈ ({_st.mean(v):.4g}, {_st.stdev(v):.4g})", f"mean_std({v}) ≈ ({_st.mean(v):.4g}, {_st.stdev(v):.4g})")
check(call(ns, "mean_std", [3.0]) is None, "Ein einzelner Wert liefert None", "A single value returns None")
data = [10.0, 10.2, 9.9, 10.1, 9.8, 10.0, 14.0]
m, s = _st.mean(data), _st.stdev(data)
check(_srt(call(ns, "outliers", data)) == sorted(x for x in data if abs(x - m) > 2 * s), "outliers erkennt 14.0 als Ausreißer", "outliers detects 14.0 as an outlier")
check(_srt(call(ns, "outliers", data, k=0.5)) == sorted(x for x in data if abs(x - m) > 0.5 * s), "outliers mit k=0.5", "outliers with k=0.5")
''',
   require=["def", "return"], refs=["7.3r", "7.2s"])

ex(id="k7-numeric", ch="7", lvl=3,
   title={"de": "Nur Zahlen addieren", "en": "Adding numbers only"},
   task={"de": "Ein Datenlogger liefert gemischte Werte. Schreiben Sie `total(*values)`, die beliebig viele Argumente entgegennimmt und nur die Zahlen (`int` oder `float`) addiert. Alles andere wird übersprungen und gezählt. Achtung: `isinstance(True, int)` ist in Python `True` – Wahrheitswerte sollen aber **nicht** als Zahl gelten!\n\nRückgabe: zwei Werte, die Summe und die Anzahl der übersprungenen Argumente.",
         "en": "A data logger delivers mixed values. Write `total(*values)` that takes any number of arguments and adds only the numbers (`int` or `float`). Everything else is skipped and counted. Careful: `isinstance(True, int)` is `True` in Python – but booleans should **not** count as numbers!\n\nReturn two values: the sum and the number of skipped arguments."},
   starter={"de": "def total(*values):\n    ...\n", "en": "def total(*values):\n    ...\n"},
   solution='def total(*values):\n    result = 0\n    skipped = 0\n    for v in values:\n        if isinstance(v, bool) or not (isinstance(v, int) or isinstance(v, float)):\n            skipped += 1\n        else:\n            result += v\n    return result, skipped\n\nprint(total(1.5, 2, "3", None, True, 4.25))\n',
   tests='''
ns, out = run()
cases = [((1.5, 2, "3", None, True, 4.25), (7.75, 3)), ((), (0, 0)), ((10, -2.5), (7.5, 0)), ((False, "x", [1]), (0, 3))]
for args, (es, ek) in cases:
    r = call(ns, "total", *args)
    check(isinstance(r, tuple) and len(r) == 2 and approx(r[0], es) and r[1] == ek, f"total{args!r} = ({es}, {ek})", f"total{args!r} = ({es}, {ek})")
''',
   require=["varargs", "isinstance"], refs=["7.5", "7.4"])
