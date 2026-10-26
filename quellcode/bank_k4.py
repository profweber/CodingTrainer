from exlib import ex

# Kapitel 4: nur print, f-Strings, Rechnen, Zuweisungen, Vergleiche, and/or/not, in, len, round.
# Kein int()/float()/str() (Kapitel 5), kein if (Kapitel 6).

ex(id="k4-energy", ch="4", lvl=1,
   title={"de": "Stromkosten", "en": "Electricity costs"},
   task={"de": "Ein Gerät mit der Leistung `P` (in W) läuft `hours` Stunden am Tag. Berechnen Sie den Energiebedarf pro Tag in kWh (`energy_kwh`) und die Kosten pro Jahr (365 Tage) in Euro (`cost_year`) beim Preis `price` (€/kWh). Ausgabe z.B. `0.96 kWh pro Tag, 112.13 € pro Jahr`.",
         "en": "A device with power `P` (in W) runs `hours` hours a day. Compute the energy per day in kWh (`energy_kwh`) and the cost per year (365 days) in euros (`cost_year`) at the price `price` (€/kWh). Output e.g. `0.96 kWh per day, 112.13 € per year`."},
   starter={"de": "P = 40        # W\nhours = 24    # h pro Tag\nprice = 0.32  # € pro kWh\n\n# Ihr Code:\n", "en": "P = 40        # W\nhours = 24    # h per day\nprice = 0.32  # € per kWh\n\n# your code:\n"},
   solution='P = 40\nhours = 24\nprice = 0.32\nenergy_kwh = P * hours / 1000\ncost_year = energy_kwh * 365 * price\nprint(f"{energy_kwh:.2f} kWh pro Tag, {cost_year:.2f} € pro Jahr")\n',
   tests='''
for P, h, pr in [(40, 24, 0.32), (2000, 0.5, 0.40), (7, 10, 0.30)]:
    ns, out = run(sub={"P": P, "hours": h, "price": pr})
    e, c = need(ns, "energy_kwh", "cost_year")
    ee = P * h / 1000; ec = ee * 365 * pr
    check(approx(e, ee), f"{P} W, {h} h: {ee:.3f} kWh pro Tag", f"{P} W, {h} h: {ee:.3f} kWh per day")
    check(approx(c, ec), f"Jahreskosten {ec:.2f} €", f"yearly cost {ec:.2f} €")
    check(f"{ec:.2f}" in out, f"Ausgabe zeigt {ec:.2f} €", f"Output shows {ec:.2f} €")
''',
   refs=["4.2", "4.3"])

ex(id="k4-pressure", ch="4", lvl=1,
   title={"de": "Druck umrechnen", "en": "Converting pressure"},
   task={"de": "Ein Reifendruck ist in bar gegeben (`p_bar`). Rechnen Sie ihn in Pascal (`p_pa`, 1 bar = 10⁵ Pa) und in psi (`p_psi`, 1 psi = 6894.76 Pa) um. Geben Sie Pascal in Exponentialschreibweise mit zwei Nachkommastellen aus (z.B. `2.40e+05 Pa`) und psi mit einer Nachkommastelle.",
         "en": "A tyre pressure is given in bar (`p_bar`). Convert it to pascal (`p_pa`, 1 bar = 10⁵ Pa) and to psi (`p_psi`, 1 psi = 6894.76 Pa). Print pascal in scientific notation with two decimals (e.g. `2.40e+05 Pa`) and psi with one decimal."},
   starter={"de": "p_bar = 2.4\n\n# Ihr Code:\n", "en": "p_bar = 2.4\n\n# your code:\n"},
   solution='p_bar = 2.4\np_pa = p_bar * 1e5\np_psi = p_pa / 6894.76\nprint(f"{p_pa:.2e} Pa = {p_psi:.1f} psi")\n',
   tests='''
for p in [2.4, 0.5, 200.0]:
    ns, out = run(sub={"p_bar": p})
    pa, psi = need(ns, "p_pa", "p_psi")
    check(approx(pa, p * 1e5) and approx(psi, p * 1e5 / 6894.76), f"{p} bar = {p*1e5:.0f} Pa = {p*1e5/6894.76:.2f} psi", f"{p} bar = {p*1e5:.0f} Pa = {p*1e5/6894.76:.2f} psi")
    check(f"{p*1e5:.2e}" in out, f"Pascal in Exponentialschreibweise: {p*1e5:.2e}", f"Pascal in scientific notation: {p*1e5:.2e}")
    check(f"{p*1e5/6894.76:.1f}" in out, f"psi mit einer Nachkommastelle: {p*1e5/6894.76:.1f}", f"psi with one decimal: {p*1e5/6894.76:.1f}")
''',
   refs=["4.2", "4.3"])

ex(id="k4-cylinder", ch="4", lvl=1,
   title={"de": "Masse eines Stahlzylinders", "en": "Mass of a steel cylinder"},
   task={"de": "Ein Zylinder aus Stahl hat den Durchmesser `d` und die Höhe `h` (beide in mm). Berechnen Sie das Volumen `V_cm3` in cm³ (V = π·r²·h, verwenden Sie `pi = 3.14159`) und die Masse `m_kg` in kg bei der Dichte `rho = 7.85` g/cm³. Achtung bei den Einheiten: 1 cm³ = 1000 mm³.",
         "en": "A steel cylinder has diameter `d` and height `h` (both in mm). Compute the volume `V_cm3` in cm³ (V = π·r²·h, use `pi = 3.14159`) and the mass `m_kg` in kg for the density `rho = 7.85` g/cm³. Watch the units: 1 cm³ = 1000 mm³."},
   starter={"de": "pi = 3.14159\nd = 40.0    # mm\nh = 100.0   # mm\nrho = 7.85  # g/cm³\n\n# Ihr Code:\n", "en": "pi = 3.14159\nd = 40.0    # mm\nh = 100.0   # mm\nrho = 7.85  # g/cm³\n\n# your code:\n"},
   solution='pi = 3.14159\nd = 40.0\nh = 100.0\nrho = 7.85\nr = d / 2\nV_cm3 = pi * r**2 * h / 1000\nm_kg = V_cm3 * rho / 1000\nprint(f"V = {V_cm3:.1f} cm³, m = {m_kg:.3f} kg")\n',
   tests='''
for d, h in [(40.0, 100.0), (10.0, 10.0), (120.0, 35.0)]:
    ns, out = run(sub={"d": d, "h": h})
    V, m = need(ns, "V_cm3", "m_kg")
    eV = 3.14159 * (d / 2) ** 2 * h / 1000
    check(approx(V, eV, 1e-5), f"d = {d} mm, h = {h} mm: V ≈ {eV:.2f} cm³", f"d = {d} mm, h = {h} mm: V ≈ {eV:.2f} cm³")
    check(approx(m, eV * 7.85 / 1000, 1e-5), f"Masse ≈ {eV*7.85/1000:.4f} kg", f"mass ≈ {eV*7.85/1000:.4f} kg")
''',
   refs=["4.2", "4.3"])

ex(id="k4-current-loop", ch="4", lvl=2,
   title={"de": "4–20-mA-Signal", "en": "4–20 mA signal"},
   task={"de": "Ein Drucksensor liefert ein 4–20-mA-Signal: 4 mA entsprechen 0 bar, 20 mA entsprechen `p_max` bar. Für den Strom `i_mA` berechnen Sie:\n- `valid`: ob der Strom im Bereich 4 bis 20 mA liegt (Grenzen eingeschlossen, Comparison Chain)\n- `wire_break`: ob der Strom unter 3.8 mA liegt (Hinweis auf Drahtbruch)\n- `pressure`: den Druck in bar (lineare Umrechnung)\n\nGeben Sie den Druck mit zwei Nachkommastellen aus.",
         "en": "A pressure sensor delivers a 4–20 mA signal: 4 mA corresponds to 0 bar, 20 mA to `p_max` bar. For the current `i_mA` compute:\n- `valid`: whether the current lies within 4 to 20 mA (limits included, comparison chain)\n- `wire_break`: whether the current is below 3.8 mA (indicates a broken wire)\n- `pressure`: the pressure in bar (linear conversion)\n\nPrint the pressure with two decimals."},
   starter={"de": "p_max = 10.0  # bar bei 20 mA\ni_mA = 12.0\n\n# Ihr Code:\n", "en": "p_max = 10.0  # bar at 20 mA\ni_mA = 12.0\n\n# your code:\n"},
   solution='p_max = 10.0\ni_mA = 12.0\nvalid = 4 <= i_mA <= 20\nwire_break = i_mA < 3.8\npressure = (i_mA - 4) / 16 * p_max\nprint(f"Druck: {pressure:.2f} bar, gültig: {valid}, Drahtbruch: {wire_break}")\n',
   tests='''
for i, pm in [(12.0, 10.0), (4.0, 10.0), (20.0, 250.0), (3.5, 10.0), (21.0, 16.0), (3.9, 10.0), (3.8, 10.0)]:
    ns, out = run(sub={"i_mA": i, "p_max": pm})
    v, w, p = need(ns, "valid", "wire_break", "pressure")
    check(v is (4 <= i <= 20), f"{i} mA: valid = {4 <= i <= 20}", f"{i} mA: valid = {4 <= i <= 20}")
    check(w is (i < 3.8), f"{i} mA: wire_break = {i < 3.8}", f"{i} mA: wire_break = {i < 3.8}")
    check(approx(p, (i - 4) / 16 * pm), f"{i} mA bei p_max = {pm} bar: {(i-4)/16*pm:.2f} bar", f"{i} mA with p_max = {pm} bar: {(i-4)/16*pm:.2f} bar")
''',
   refs=["4.4", "4.2"])

ex(id="k4-resistors", ch="4", lvl=2,
   title={"de": "Reihen- und Parallelschaltung", "en": "Series and parallel circuits"},
   task={"de": "Zwei Widerstände `R1` und `R2` (Ω) sind gegeben. Berechnen Sie den Gesamtwiderstand der Reihenschaltung `R_series` und der Parallelschaltung `R_parallel` = R1·R2 / (R1 + R2). Speichern Sie in `smaller_than_both`, ob `R_parallel` kleiner als beide Einzelwiderstände ist. Geben Sie beide Widerstände auf eine Nachkommastelle aus.",
         "en": "Two resistors `R1` and `R2` (Ω) are given. Compute the total resistance of the series circuit `R_series` and of the parallel circuit `R_parallel` = R1·R2 / (R1 + R2). Store in `smaller_than_both` whether `R_parallel` is smaller than both individual resistors. Print both resistances with one decimal."},
   starter={"de": "R1 = 220.0\nR2 = 330.0\n\n# Ihr Code:\n", "en": "R1 = 220.0\nR2 = 330.0\n\n# your code:\n"},
   solution='R1 = 220.0\nR2 = 330.0\nR_series = R1 + R2\nR_parallel = R1 * R2 / (R1 + R2)\nsmaller_than_both = R_parallel < R1 and R_parallel < R2\nprint(f"Reihe: {R_series:.1f} Ohm, parallel: {R_parallel:.1f} Ohm")\n',
   tests='''
for a, b in [(220.0, 330.0), (100.0, 100.0), (4.7, 1000.0)]:
    ns, out = run(sub={"R1": a, "R2": b})
    s, p, sm = need(ns, "R_series", "R_parallel", "smaller_than_both")
    ep = a * b / (a + b)
    check(approx(s, a + b), f"Reihe {a} + {b} = {a+b} Ω", f"Series {a} + {b} = {a+b} Ω")
    check(approx(p, ep), f"Parallel ≈ {ep:.2f} Ω", f"Parallel ≈ {ep:.2f} Ω")
    check(sm is True, "smaller_than_both ist True", "smaller_than_both is True")
    check(f"{ep:.1f}" in out, f"Ausgabe zeigt {ep:.1f}", f"Output shows {ep:.1f}")
''',
   refs=["4.2", "4.4"])

ex(id="k4-serial", ch="4", lvl=2,
   title={"de": "Seriennummer prüfen", "en": "Checking a serial number"},
   task={"de": "Eine Seriennummer `serial` ist gültig, wenn sie genau 12 Zeichen lang ist, `\"TR\"` enthält und das Jahr `year` (als Text gegeben) enthält, aber **nicht** das Wort `\"TEST\"`. Speichern Sie die Teilergebnisse in `length_ok`, `has_prefix`, `has_year`, `is_test` und das Gesamtergebnis in `valid`. Geben Sie `valid` aus.",
         "en": "A serial number `serial` is valid if it is exactly 12 characters long, contains `\"TR\"` and the year `year` (given as text), but does **not** contain the word `\"TEST\"`. Store the partial results in `length_ok`, `has_prefix`, `has_year`, `is_test` and the overall result in `valid`. Print `valid`."},
   starter={"de": 'serial = "TR-2026-0457"\nyear = "2026"\n\n# Ihr Code:\n', "en": 'serial = "TR-2026-0457"\nyear = "2026"\n\n# your code:\n'},
   solution='serial = "TR-2026-0457"\nyear = "2026"\nlength_ok = len(serial) == 12\nhas_prefix = "TR" in serial\nhas_year = year in serial\nis_test = "TEST" in serial\nvalid = length_ok and has_prefix and has_year and not is_test\nprint("Gültig:", valid)\n',
   tests='''
cases = [("TR-2026-0457", "2026", True), ("TR-2025-0457", "2026", False), ("TR-2026-457", "2026", False), ("XX-2026-0457", "2026", False), ("TR-TEST-2026", "2026", False)]
for s, y, e in cases:
    ns, out = run(sub={"serial": s, "year": y})
    v = need(ns, "valid")
    check(v is e, f"{s!r} (Jahr {y}): valid = {e}", f"{s!r} (year {y}): valid = {e}")
ns, out = run(sub={"serial": "TR-TEST-2026"})
check(ns.get("is_test") is True and ns.get("length_ok") is True, "Teilergebnisse für 'TR-TEST-2026' stimmen", "Partial results for 'TR-TEST-2026' are correct")
''',
   refs=["4.4", "4.5"])

ex(id="k4-heating", ch="4", lvl=3,
   title={"de": "Heizdauer eines Wasserkochers", "en": "Heating time of a kettle"},
   task={"de": "Ein Wasserkocher mit der Leistung `P` (W) und dem Wirkungsgrad `eta` erwärmt `m` kg Wasser von `T_start` auf `T_end` (°C). Die benötigte Wärme ist Q = m · c · ΔT mit c = 4190 J/(kg·K). Berechnen Sie die Heizdauer in Sekunden, gerundet auf ganze Sekunden (`t_s`, mit `round`), und zerlegen Sie sie in `minutes` und `seconds`. Ausgabe: `Heizdauer: 4 min 57 s`.",
         "en": "A kettle with power `P` (W) and efficiency `eta` heats `m` kg of water from `T_start` to `T_end` (°C). The heat required is Q = m · c · ΔT with c = 4190 J/(kg·K). Compute the heating time in seconds, rounded to whole seconds (`t_s`, using `round`), and split it into `minutes` and `seconds`. Output: `Heating time: 4 min 57 s`."},
   starter={"de": "P = 2000.0     # W\neta = 0.9\nm = 1.5        # kg\nT_start = 15.0 # °C\nT_end = 100.0  # °C\n\n# Ihr Code:\n", "en": "P = 2000.0     # W\neta = 0.9\nm = 1.5        # kg\nT_start = 15.0 # °C\nT_end = 100.0  # °C\n\n# your code:\n"},
   solution='P = 2000.0\neta = 0.9\nm = 1.5\nT_start = 15.0\nT_end = 100.0\nQ = m * 4190 * (T_end - T_start)\nt_s = round(Q / (P * eta))\nminutes = t_s // 60\nseconds = t_s % 60\nprint(f"Heizdauer: {minutes} min {seconds} s")\n',
   tests='''
for P, eta, m, a, b in [(2000.0, 0.9, 1.5, 15.0, 100.0), (3000.0, 0.95, 0.5, 20.0, 80.0), (1200.0, 0.8, 1.0, 10.0, 100.0), (800.0, 0.8, 3.0, 10.0, 100.0)]:
    ns, out = run(sub={"P": P, "eta": eta, "m": m, "T_start": a, "T_end": b})
    t, mi, se = need(ns, "t_s", "minutes", "seconds")
    et = round(m * 4190 * (b - a) / (P * eta))
    check(t == et, f"{P} W, {m} kg, {a}→{b} °C: t = {et} s", f"{P} W, {m} kg, {a}→{b} °C: t = {et} s")
    check((mi, se) == (et // 60, et % 60), f"= {et//60} min {et%60} s", f"= {et//60} min {et%60} s")
    check(f"{et//60} min {et%60} s" in out, "Ausgabe im Format 'x min y s'", "Output in the format 'x min y s'")
''',
   refs=["4.2", "4.3"])

ex(id="k4-gearbox", ch="4", lvl=3,
   title={"de": "Zweistufiges Getriebe", "en": "Two-stage gearbox"},
   task={"de": "Ein zweistufiges Zahnradgetriebe hat die Zähnezahlen `z1`→`z2` (Stufe 1) und `z3`→`z4` (Stufe 2). Die Gesamtübersetzung ist i = (z2/z1)·(z4/z3). Berechnen Sie `i`, die Abtriebsdrehzahl `n_out = n_in / i` und das Abtriebsmoment `M_out = M_in · i · eta²` (jede Stufe hat den Wirkungsgrad `eta`). Ausgabe: `i = 9.00, n_out = 161.1 1/min, M_out = 169.4 Nm`.",
         "en": "A two-stage gearbox has the tooth counts `z1`→`z2` (stage 1) and `z3`→`z4` (stage 2). The overall ratio is i = (z2/z1)·(z4/z3). Compute `i`, the output speed `n_out = n_in / i` and the output torque `M_out = M_in · i · eta²` (each stage has efficiency `eta`). Output: `i = 9.00, n_out = 161.1 1/min, M_out = 169.4 Nm`."},
   starter={"de": "n_in = 1450.0  # 1/min\nM_in = 20.0    # Nm\nz1 = 17\nz2 = 51\nz3 = 19\nz4 = 57\neta = 0.97\n\n# Ihr Code:\n", "en": "n_in = 1450.0  # 1/min\nM_in = 20.0    # Nm\nz1 = 17\nz2 = 51\nz3 = 19\nz4 = 57\neta = 0.97\n\n# your code:\n"},
   solution='n_in = 1450.0\nM_in = 20.0\nz1 = 17\nz2 = 51\nz3 = 19\nz4 = 57\neta = 0.97\ni = (z2 / z1) * (z4 / z3)\nn_out = n_in / i\nM_out = M_in * i * eta**2\nprint(f"i = {i:.2f}, n_out = {n_out:.1f} 1/min, M_out = {M_out:.1f} Nm")\n',
   tests='''
for nin, Min, eta in [(1450.0, 20.0, 0.97), (3000.0, 5.0, 0.9), (960.0, 100.0, 0.98)]:
    ns, out = run(sub={"n_in": nin, "M_in": Min, "eta": eta})
    i, n, M = need(ns, "i", "n_out", "M_out")
    check(approx(i, 9.0), "Übersetzung i = 9", "Ratio i = 9")
    check(approx(n, nin / 9) and approx(M, Min * 9 * eta ** 2), f"n_in = {nin}: n_out ≈ {nin/9:.1f}, M_out ≈ {Min*9*eta**2:.1f}", f"n_in = {nin}: n_out ≈ {nin/9:.1f}, M_out ≈ {Min*9*eta**2:.1f}")
    check(f"{M*1:.1f}" in out and f"{nin/9:.1f}" in out, "Ausgabe mit einer Nachkommastelle", "Output with one decimal")
ns, out = run(sub={"z1": 20, "z2": 40, "z3": 10, "z4": 50})
check(approx(ns.get("i"), 10.0), "Mit anderen Zähnezahlen (20/40, 10/50) ergibt sich i = 10", "With other tooth counts (20/40, 10/50), i = 10")
''',
   refs=["4.2", "4.3"])

ex(id="k4-triangle", ch="4", lvl=3,
   title={"de": "Dreiecksblech", "en": "Triangular sheet"},
   task={"de": "Aus einem Blech soll ein Dreieck mit den Seiten `a ≤ b ≤ c` (mm, aufsteigend gegeben) geschnitten werden.\n- `valid`: Ein Dreieck existiert nur, wenn a + b > c.\n- `area`: Fläche nach Heron: s = (a+b+c)/2, A = √(s·(s−a)·(s−b)·(s−c)), Wurzel mit `** 0.5`\n- `right_angle`: ob das Dreieck rechtwinklig ist (a² + b² = c²). Gleitkommazahlen nie mit `==` vergleichen: prüfen Sie mit einer Comparison Chain, ob die Differenz zwischen −1e-9 und 1e-9 liegt.",
         "en": "A triangle with sides `a ≤ b ≤ c` (mm, given in ascending order) is to be cut from a sheet.\n- `valid`: a triangle only exists if a + b > c.\n- `area`: area by Heron: s = (a+b+c)/2, A = √(s·(s−a)·(s−b)·(s−c)), root with `** 0.5`\n- `right_angle`: whether the triangle is right-angled (a² + b² = c²). Never compare floats with `==`: use a comparison chain to check whether the difference lies between −1e-9 and 1e-9."},
   starter={"de": "a = 30.0\nb = 40.0\nc = 50.0\n\n# Ihr Code:\n", "en": "a = 30.0\nb = 40.0\nc = 50.0\n\n# your code:\n"},
   solution='a = 30.0\nb = 40.0\nc = 50.0\nvalid = a + b > c\ns = (a + b + c) / 2\narea = (s * (s - a) * (s - b) * (s - c)) ** 0.5\nright_angle = -1e-9 < a**2 + b**2 - c**2 < 1e-9\nprint(valid, area, right_angle)\n',
   tests='''
for a, b, c in [(30.0, 40.0, 50.0), (5.0, 5.0, 8.0), (0.3, 0.4, 0.5), (7.0, 7.0, 7.0), (3.0, 4.0, 5.01)]:
    ns, out = run(sub={"a": a, "b": b, "c": c})
    v, A, r = need(ns, "valid", "area", "right_angle")
    s = (a + b + c) / 2; eA = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    check(v is True and approx(A, eA), f"{a}, {b}, {c}: Fläche ≈ {eA:.3f} mm²", f"{a}, {b}, {c}: area ≈ {eA:.3f} mm²")
    check(r is (abs(a*a + b*b - c*c) < 1e-9), f"{a}, {b}, {c}: right_angle = {abs(a*a+b*b-c*c) < 1e-9}", f"{a}, {b}, {c}: right_angle = {abs(a*a+b*b-c*c) < 1e-9}")
for a, b, c in [(2.0, 3.0, 6.0), (2.0, 3.0, 5.0)]:
    ns, out = run(sub={"a": a, "b": b, "c": c})
    check(ns.get("valid") is False, f"{a:g}, {b:g}, {c:g} ist kein Dreieck (valid = False)", f"{a:g}, {b:g}, {c:g} is no triangle (valid = False)")
''',
   refs=["4.2", "4.4"])
