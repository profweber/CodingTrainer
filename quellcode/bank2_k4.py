from exlib import ex

# Kapitel 4, zweiter Satz: nur print, f-Strings, Rechnen, Zuweisungen, input (als Text), Vergleiche,
# and/or/not, in, len, round. Kein int()/float()/str() (Kapitel 5), kein if (Kapitel 6).

# ------------------------------------------------------------------ Stufe 1
ex(id="k4-speed", ch="4", lvl=1,
   title={"de": "Durchschnittsgeschwindigkeit", "en": "Average speed"},
   task={"de": "Ein Lieferwagen legt die Strecke `s_km` (in km) in `t_min` Minuten zurück. Berechnen Sie die Durchschnittsgeschwindigkeit in km/h (`v_kmh`) und in m/s (`v_ms`). Geben Sie beide Werte mit einer Nachkommastelle aus, z.B. `v = 64.0 km/h = 17.8 m/s`.\n\nTipp: Rechnen Sie die Minuten zuerst in Stunden um.",
         "en": "A delivery van covers the distance `s_km` (in km) in `t_min` minutes. Compute the average speed in km/h (`v_kmh`) and in m/s (`v_ms`). Print both values with one decimal, e.g. `v = 64.0 km/h = 17.8 m/s`.\n\nTip: convert the minutes to hours first."},
   starter={"de": "s_km = 48.0   # Strecke in km\nt_min = 45    # Fahrzeit in Minuten\n\n# Ihr Code:\n", "en": "s_km = 48.0   # distance in km\nt_min = 45    # travel time in minutes\n\n# your code:\n"},
   solution='s_km = 48.0\nt_min = 45\nv_kmh = s_km / (t_min / 60)\nv_ms = v_kmh / 3.6\nprint(f"v = {v_kmh:.1f} km/h = {v_ms:.1f} m/s")\n',
   tests='''
for s, t in [(48.0, 45), (12.5, 10), (300.0, 150)]:
    ns, out = run(sub={"s_km": s, "t_min": t})
    vk, vm = need(ns, "v_kmh", "v_ms")
    ek = s / (t / 60)
    check(approx(vk, ek), f"{s} km in {t} min: {ek:.2f} km/h", f"{s} km in {t} min: {ek:.2f} km/h")
    check(approx(vm, ek / 3.6), f"= {ek/3.6:.3f} m/s", f"= {ek/3.6:.3f} m/s")
    check(f"{ek:.1f}" in out and f"{ek/3.6:.1f}" in out, "Ausgabe mit einer Nachkommastelle", "Output with one decimal")
''',
   refs=["4.2", "4.3"])

ex(id="k4-density", ch="4", lvl=1,
   title={"de": "Werkstoff bestimmen", "en": "Identifying a material"},
   task={"de": "Ein quaderförmiges Probestück hat die Kantenlängen `a`, `b`, `c` (in mm) und die Masse `m_g` (in g). Berechnen Sie das Volumen `V_cm3` in cm³ und die Dichte `rho` in g/cm³. Speichern Sie in `is_aluminium`, ob die Dichte zwischen 2.6 und 2.8 g/cm³ liegt (Comparison Chain). Ausgabe z.B. `Dichte: 2.70 g/cm³, Aluminium: True`.",
         "en": "A cuboid specimen has the edge lengths `a`, `b`, `c` (in mm) and the mass `m_g` (in g). Compute the volume `V_cm3` in cm³ and the density `rho` in g/cm³. Store in `is_aluminium` whether the density lies between 2.6 and 2.8 g/cm³ (comparison chain). Output e.g. `Density: 2.70 g/cm³, aluminium: True`."},
   starter={"de": "a = 50.0   # mm\nb = 20.0   # mm\nc = 10.0   # mm\nm_g = 27.0 # g\n\n# Ihr Code:\n", "en": "a = 50.0   # mm\nb = 20.0   # mm\nc = 10.0   # mm\nm_g = 27.0 # g\n\n# your code:\n"},
   solution='a = 50.0\nb = 20.0\nc = 10.0\nm_g = 27.0\nV_cm3 = a * b * c / 1000\nrho = m_g / V_cm3\nis_aluminium = 2.6 <= rho <= 2.8\nprint(f"Dichte: {rho:.2f} g/cm³, Aluminium: {is_aluminium}")\n',
   tests='''
for a, b, c, m in [(50.0, 20.0, 10.0, 27.0), (40.0, 40.0, 10.0, 125.6), (100.0, 10.0, 10.0, 26.5), (50.0, 20.0, 10.0, 29.0)]:
    ns, out = run(sub={"a": a, "b": b, "c": c, "m_g": m})
    V, r, al = need(ns, "V_cm3", "rho", "is_aluminium")
    eV = a * b * c / 1000; er = m / eV
    check(approx(V, eV), f"{a}×{b}×{c} mm = {eV:g} cm³", f"{a}×{b}×{c} mm = {eV:g} cm³")
    check(approx(r, er), f"Dichte = {er:.3f} g/cm³", f"density = {er:.3f} g/cm³")
    check(al is (2.6 <= er <= 2.8), f"is_aluminium = {2.6 <= er <= 2.8}", f"is_aluminium = {2.6 <= er <= 2.8}")
''',
   refs=["4.2", "4.4"])

ex(id="k4-label", ch="4", lvl=1,
   title={"de": "Typenschild drucken", "en": "Printing a nameplate"},
   task={"de": "Lesen Sie mit `input()` die Gerätebezeichnung (`device`) und den Standort (`location`) ein. Setzen Sie daraus mit einem f-String den Text `label` zusammen, z.B. `Gerät: Pumpe P-301 | Standort: Halle 2`, und geben Sie ihn aus. Speichern Sie in `n_chars` die Anzahl der Zeichen von `label` – der Etikettendrucker schafft höchstens 40 Zeichen; speichern Sie in `fits`, ob das Etikett passt.\n\nEingaben für „Ausführen“ tragen Sie im Feld *Eingaben für input()* ein, eine pro Zeile.",
         "en": "Use `input()` to read the device name (`device`) and the location (`location`). Build the text `label` from them with an f-string, e.g. `Device: Pump P-301 | Location: Hall 2`, and print it. Store the number of characters of `label` in `n_chars` – the label printer can handle at most 40 characters; store in `fits` whether the label fits.\n\nInputs for “Run” go into the field *Input for input()*, one per line."},
   starter={"de": "# Bezeichnung und Standort einlesen\n", "en": "# read name and location\n"},
   solution='device = input("Gerät: ")\nlocation = input("Standort: ")\nlabel = f"Gerät: {device} | Standort: {location}"\nprint(label)\nn_chars = len(label)\nfits = n_chars <= 40\n',
   tests='''
for d, l in [("Pumpe P-301", "Halle 2"), ("Kompressor K1", "Technikraum Untergeschoss Nord"), ("X", "Y")]:
    ns, out = run(inputs=[d, l])
    dev, loc, lab, n, f = need(ns, "device", "location", "label", "n_chars", "fits")
    check(dev == d and loc == l, "device und location enthalten die Eingaben", "device and location hold the inputs")
    check(isinstance(lab, str) and d in lab and l in lab and lab.index(d) < lab.index(l), f"label enthält {d!r} und danach {l!r}", f"label contains {d!r} followed by {l!r}")
    check(n == len(lab) and f is (len(lab) <= 40), f"n_chars = {len(lab)}, fits = {len(lab) <= 40}", f"n_chars = {len(lab)}, fits = {len(lab) <= 40}")
    check(lab in out, "label wird ausgegeben", "label is printed")
ns, out = run(inputs=["X", "Y"])
base = len(ns["label"]) - 1 if isinstance(ns.get("label"), str) else 99
for k in [40 - base, 41 - base]:
    if k < 1:
        continue
    ns, out = run(inputs=["X" * k, "Y"])
    lab, f = ns.get("label"), ns.get("fits")
    if isinstance(lab, str) and len(lab) in (40, 41):
        check(f is (len(lab) <= 40), f"Etikett mit genau {len(lab)} Zeichen: fits = {len(lab) <= 40}", f"label with exactly {len(lab)} characters: fits = {len(lab) <= 40}")
''',
   stdin="Pumpe P-301\nHalle 2\n", require=["input", "fstring"], refs=["4.3e", "4.3", "4.5"])

ex(id="k4-lineloss", ch="4", lvl=1,
   title={"de": "Leitungsverluste", "en": "Line losses"},
   task={"de": "Über eine Zuleitung mit dem Widerstand `R_line` (Ω) fließt der Strom `I` (A) zu einem Verbraucher mit der Leistung `P_load` (W). Berechnen Sie die Verlustleistung in der Leitung `P_loss = I² · R` und ihren Anteil an der Verbraucherleistung in Prozent (`loss_percent`). Geben Sie beides mit zwei Nachkommastellen aus.\n\nAchtung: Potenz mit `**`, nicht mit `^`!",
         "en": "The current `I` (A) flows through a supply line with resistance `R_line` (Ω) to a load with power `P_load` (W). Compute the power loss in the line `P_loss = I² · R` and its share of the load power in percent (`loss_percent`). Print both with two decimals.\n\nCareful: power with `**`, not with `^`!"},
   starter={"de": "R_line = 0.35   # Ohm\nI = 16.0        # A\nP_load = 3500.0 # W\n\n# Ihr Code:\n", "en": "R_line = 0.35   # Ohm\nI = 16.0        # A\nP_load = 3500.0 # W\n\n# your code:\n"},
   solution='R_line = 0.35\nI = 16.0\nP_load = 3500.0\nP_loss = I**2 * R_line\nloss_percent = P_loss / P_load * 100\nprint(f"Verlust: {P_loss:.2f} W ({loss_percent:.2f} %)")\n',
   tests='''
for R, I, P in [(0.35, 16.0, 3500.0), (0.1, 10.0, 2000.0), (1.2, 2.5, 500.0)]:
    ns, out = run(sub={"R_line": R, "I": I, "P_load": P})
    pl, lp = need(ns, "P_loss", "loss_percent")
    e = I * I * R
    check(approx(pl, e), f"I = {I} A, R = {R} Ω: P_loss = {e:.2f} W", f"I = {I} A, R = {R} Ω: P_loss = {e:.2f} W")
    check(approx(lp, e / P * 100), f"Anteil = {e/P*100:.2f} %", f"share = {e/P*100:.2f} %")
    check(f"{e:.2f}" in out and f"{e/P*100:.2f}" in out, "Ausgabe mit zwei Nachkommastellen", "Output with two decimals")
''',
   refs=["4.2", "4.3"])

ex(id="k4-wavelength", ch="4", lvl=1,
   title={"de": "Wellenlänge und Exponentialschreibweise", "en": "Wavelength and scientific notation"},
   task={"de": "Eine Funkwelle hat die Frequenz `f` (Hz). Mit der Lichtgeschwindigkeit `c = 3e8` m/s gilt für die Wellenlänge λ = c / f. Berechnen Sie `wavelength` (m) und die Periodendauer `T = 1 / f` (s). Geben Sie beide Werte in Exponentialschreibweise mit zwei Nachkommastellen aus (Formatangabe `.2e`), z.B. `λ = 3.46e-01 m, T = 1.15e-09 s`.",
         "en": "A radio wave has the frequency `f` (Hz). With the speed of light `c = 3e8` m/s, the wavelength is λ = c / f. Compute `wavelength` (m) and the period `T = 1 / f` (s). Print both values in scientific notation with two decimals (format spec `.2e`), e.g. `λ = 3.46e-01 m, T = 1.15e-09 s`."},
   starter={"de": "c = 3e8      # m/s\nf = 868e6    # Hz (LoRa-Funk)\n\n# Ihr Code:\n", "en": "c = 3e8      # m/s\nf = 868e6    # Hz (LoRa radio)\n\n# your code:\n"},
   solution='c = 3e8\nf = 868e6\nwavelength = c / f\nT = 1 / f\nprint(f"λ = {wavelength:.2e} m, T = {T:.2e} s")\n',
   tests='''
for f in [868e6, 50.0, 2.4e9]:
    ns, out = run(sub={"f": f})
    w, T = need(ns, "wavelength", "T")
    check(approx(w, 3e8 / f) and approx(T, 1 / f), f"f = {f:g} Hz: λ = {3e8/f:.3e} m, T = {1/f:.3e} s", f"f = {f:g} Hz: λ = {3e8/f:.3e} m, T = {1/f:.3e} s")
    check(f"{3e8/f:.2e}" in out and f"{1/f:.2e}" in out, "Ausgabe im Format .2e", "Output in .2e format")
''',
   refs=["4.2", "4.3"])

# ------------------------------------------------------------------ Stufe 2
ex(id="k4-stock", ch="4", lvl=2,
   title={"de": "Lagerbuchungen", "en": "Stock bookings"},
   task={"de": "Der Bestand `stock` eines Lagerartikels wird im Laufe eines Tages verändert. Verwenden Sie **nur erweiterte Zuweisungen** (`+=`, `-=`, `*=`) auf `stock`:\n1. Wareneingang `incoming` Stück\n2. Entnahme `outgoing` Stück\n3. Bei der Inventur werden `damaged_percent` Prozent des Bestands als beschädigt ausgebucht (Bestand mit dem passenden Faktor multiplizieren).\n\nSpeichern Sie außerdem in `reorder`, ob der Bestand danach unter dem Meldebestand `min_stock` liegt, und geben Sie Bestand (eine Nachkommastelle) und `reorder` aus.",
         "en": "The quantity `stock` of a stock item changes during a day. Use **only augmented assignments** (`+=`, `-=`, `*=`) on `stock`:\n1. Goods receipt of `incoming` pieces\n2. Withdrawal of `outgoing` pieces\n3. At the stock-take, `damaged_percent` percent of the stock are written off as damaged (multiply the stock by the matching factor).\n\nAlso store in `reorder` whether the stock is then below the reorder level `min_stock`, and print the stock (one decimal) and `reorder`."},
   starter={"de": "stock = 120\nincoming = 40\noutgoing = 95\ndamaged_percent = 5\nmin_stock = 60\n\n# Ihr Code:\n", "en": "stock = 120\nincoming = 40\noutgoing = 95\ndamaged_percent = 5\nmin_stock = 60\n\n# your code:\n"},
   solution='stock = 120\nincoming = 40\noutgoing = 95\ndamaged_percent = 5\nmin_stock = 60\nstock += incoming\nstock -= outgoing\nstock *= 1 - damaged_percent / 100\nreorder = stock < min_stock\nprint(f"Bestand: {stock:.1f} Stück, nachbestellen: {reorder}")\n',
   tests='''
for st, i, o, d, mn in [(120, 40, 95, 5, 60), (500, 0, 100, 0, 100), (30, 10, 0, 50, 25)]:
    ns, out = run(sub={"stock": st, "incoming": i, "outgoing": o, "damaged_percent": d, "min_stock": mn})
    s, r = need(ns, "stock", "reorder")
    e = (st + i - o) * (1 - d / 100)
    check(approx(s, e), f"Start {st}, +{i}, −{o}, −{d} %: Bestand {e:g}", f"start {st}, +{i}, −{o}, −{d} %: stock {e:g}")
    check(r is (e < mn), f"reorder = {e < mn} (Meldebestand {mn})", f"reorder = {e < mn} (reorder level {mn})")
check("+=" in SOURCE and "-=" in SOURCE and "*=" in SOURCE, "Mit +=, -= und *= gelöst", "Solved with +=, -= and *=")
''',
   require=["augassign"], refs=["4.3", "4.4"])

ex(id="k4-holes", ch="4", lvl=2,
   title={"de": "Lochreihe in einem Flachstahl", "en": "Row of holes in a flat bar"},
   task={"de": "In einen Flachstahl der Länge `L` (mm) soll eine Lochreihe gebohrt werden. Zu beiden Enden muss der Randabstand `e` eingehalten werden, die Löcher haben den Abstand `p` (Teilung). Berechnen Sie mit Ganzzahl-Division und Modulo\n- `usable`: die nutzbare Länge L − 2·e\n- `n_holes`: die Anzahl der Löcher (das erste Loch sitzt genau am Randabstand, dann alle `p` mm eins – also `usable // p + 1`)\n- `rest`: wie viel nutzbare Länge hinter dem letzten Loch übrig bleibt (`%`)\n\nAusgabe z.B. `9 Löcher, Rest 0 mm`.",
         "en": "A row of holes is to be drilled into a flat bar of length `L` (mm). The edge distance `e` must be kept at both ends; the holes are `p` apart (pitch). Using integer division and modulo, compute\n- `usable`: the usable length L − 2·e\n- `n_holes`: the number of holes (the first hole sits exactly at the edge distance, then one every `p` mm – i.e. `usable // p + 1`)\n- `rest`: how much usable length remains after the last hole (`%`)\n\nOutput e.g. `9 holes, rest 0 mm`."},
   starter={"de": "L = 1000   # mm\ne = 40     # mm Randabstand\np = 115    # mm Teilung\n\n# Ihr Code:\n", "en": "L = 1000   # mm\ne = 40     # mm edge distance\np = 115    # mm pitch\n\n# your code:\n"},
   solution='L = 1000\ne = 40\np = 115\nusable = L - 2 * e\nn_holes = usable // p + 1\nrest = usable % p\nprint(f"{n_holes} Löcher, Rest {rest} mm")\n',
   tests='''
for L, e, p in [(1000, 40, 115), (600, 30, 60), (250, 25, 300), (2400, 50, 100)]:
    ns, out = run(sub={"L": L, "e": e, "p": p})
    u, n, r = need(ns, "usable", "n_holes", "rest")
    eu = L - 2 * e
    check(u == eu, f"L = {L}, e = {e}: nutzbar {eu} mm", f"L = {L}, e = {e}: usable {eu} mm")
    check(n == eu // p + 1 and r == eu % p, f"Teilung {p}: {eu // p + 1} Löcher, Rest {eu % p} mm", f"pitch {p}: {eu // p + 1} holes, rest {eu % p} mm")
    check(f"{eu // p + 1}" in out and f"{eu % p}" in out, "Ausgabe enthält Anzahl und Rest", "Output contains count and rest")
''',
   refs=["4.2", "4.3"])

ex(id="k4-grid", ch="4", lvl=2,
   title={"de": "Netzqualität prüfen", "en": "Checking power quality"},
   task={"de": "Ein Netzanalysator misst Spannung `U` (V), Frequenz `f` (Hz) und Oberschwingungsgehalt `thd` (%). Nach der Norm gelten (vereinfacht) folgende Grenzen:\n- Spannung zwischen 207 und 253 V (Grenzen eingeschlossen)\n- Frequenz zwischen 49.8 und 50.2 Hz (Grenzen eingeschlossen)\n- THD kleiner als 8 %\n\nSpeichern Sie die drei Teilergebnisse in `u_ok`, `f_ok`, `thd_ok` (Comparison Chains, wo es passt), das Gesamtergebnis in `grid_ok` und in `alarm` das Gegenteil davon (mit `not`).",
         "en": "A power analyser measures voltage `U` (V), frequency `f` (Hz) and harmonic content `thd` (%). According to the standard (simplified), these limits apply:\n- voltage between 207 and 253 V (limits included)\n- frequency between 49.8 and 50.2 Hz (limits included)\n- THD less than 8 %\n\nStore the three partial results in `u_ok`, `f_ok`, `thd_ok` (comparison chains where they fit), the overall result in `grid_ok` and its opposite (using `not`) in `alarm`."},
   starter={"de": "U = 231.4   # V\nf = 50.03   # Hz\nthd = 3.2   # %\n\n# Ihr Code:\n", "en": "U = 231.4   # V\nf = 50.03   # Hz\nthd = 3.2   # %\n\n# your code:\n"},
   solution='U = 231.4\nf = 50.03\nthd = 3.2\nu_ok = 207 <= U <= 253\nf_ok = 49.8 <= f <= 50.2\nthd_ok = thd < 8\ngrid_ok = u_ok and f_ok and thd_ok\nalarm = not grid_ok\nprint("Netz ok:", grid_ok, "Alarm:", alarm)\n',
   tests='''
cases = [(231.4, 50.03, 3.2), (207.0, 49.8, 7.99), (253.0, 50.2, 2.0), (206.9, 50.0, 1.0), (240.0, 50.21, 2.0), (230.0, 50.0, 8.0), (253.1, 50.0, 2.0), (260.0, 48.0, 12.0)]
for U, f, t in cases:
    ns, out = run(sub={"U": U, "f": f, "thd": t})
    a, b, c, g, al = need(ns, "u_ok", "f_ok", "thd_ok", "grid_ok", "alarm")
    ea, eb, ec = 207 <= U <= 253, 49.8 <= f <= 50.2, t < 8
    check((a, b, c) == (ea, eb, ec), f"U = {U}, f = {f}, THD = {t}: Teilergebnisse {ea}, {eb}, {ec}", f"U = {U}, f = {f}, THD = {t}: partial results {ea}, {eb}, {ec}")
    check(g is (ea and eb and ec) and al is (not (ea and eb and ec)), f"grid_ok = {ea and eb and ec}, alarm = {not (ea and eb and ec)}", f"grid_ok = {ea and eb and ec}, alarm = {not (ea and eb and ec)}")
''',
   require=["boolop"], refs=["4.4"])

ex(id="k4-cutting", ch="4", lvl=2,
   title={"de": "Stangen zuschneiden", "en": "Cutting bars to length"},
   task={"de": "Eine Stange der Länge `L` (mm) wird mit einer Säge in `n` gleich lange Stücke geteilt. Jeder Schnitt kostet die Sägeblattbreite `kerf` (mm), bei n Stücken gibt es n − 1 Schnitte. Berechnen Sie\n- `piece`: die Länge eines Stücks, auf 0.1 mm gerundet (`round(…, 1)`)\n- `loss`: den gesamten Verschnitt durch die Schnitte in mm\n- `loss_percent`: den Verschnitt in Prozent der Stangenlänge, auf zwei Nachkommastellen gerundet\n\nAusgabe z.B. `8 Stücke zu 747.4 mm, Verschnitt 0.35 %`.",
         "en": "A bar of length `L` (mm) is sawn into `n` pieces of equal length. Every cut costs the blade width `kerf` (mm); n pieces need n − 1 cuts. Compute\n- `piece`: the length of one piece, rounded to 0.1 mm (`round(…, 1)`)\n- `loss`: the total material lost by the cuts in mm\n- `loss_percent`: the loss in percent of the bar length, rounded to two decimals\n\nOutput e.g. `8 pieces of 747.4 mm, loss 0.35 %`."},
   starter={"de": "L = 6000.0   # mm\nn = 8\nkerf = 3.0   # mm\n\n# Ihr Code:\n", "en": "L = 6000.0   # mm\nn = 8\nkerf = 3.0   # mm\n\n# your code:\n"},
   solution='L = 6000.0\nn = 8\nkerf = 3.0\nloss = (n - 1) * kerf\npiece = round((L - loss) / n, 1)\nloss_percent = round(loss / L * 100, 2)\nprint(f"{n} Stücke zu {piece} mm, Verschnitt {loss_percent} %")\n',
   tests='''
for L, n, k in [(6000.0, 8, 3.0), (1000.0, 4, 2.5), (3000.0, 1, 3.0), (2500.0, 7, 4.2)]:
    ns, out = run(sub={"L": L, "n": n, "kerf": k})
    p, lo, lp = need(ns, "piece", "loss", "loss_percent")
    el = (n - 1) * k
    check(approx(lo, el), f"{n} Stücke, Schnittbreite {k} mm: Verschnitt {el:g} mm", f"{n} pieces, kerf {k} mm: loss {el:g} mm")
    check(approx(p, round((L - el) / n, 1)), f"Stücklänge {round((L - el) / n, 1)} mm", f"piece length {round((L - el) / n, 1)} mm")
    check(approx(lp, round(el / L * 100, 2)), f"Verschnitt {round(el / L * 100, 2)} %", f"loss {round(el / L * 100, 2)} %")
''',
   require=["round"], refs=["4.2", "4.4"])

ex(id="k4-password", ch="4", lvl=2,
   title={"de": "Passwort für die Steuerung", "en": "Password for the controller"},
   task={"de": "Eine Maschinensteuerung verlangt beim Ändern des Passworts:\n- mindestens 10 Zeichen\n- das Passwort darf den Benutzernamen nicht enthalten\n- es darf nicht das Standardpasswort `\"admin1234\"` enthalten\n- es muss mindestens eines der Sonderzeichen `!`, `#` oder `?` enthalten\n\nLesen Sie zuerst den Benutzernamen `user`, dann das Passwort `pw` mit `input()` ein. Speichern Sie die vier Teilprüfungen in `long_enough`, `no_user`, `no_default`, `has_special` und das Gesamtergebnis in `accepted`. Geben Sie `accepted` aus.",
         "en": "A machine controller requires when changing the password:\n- at least 10 characters\n- the password must not contain the user name\n- it must not contain the default password `\"admin1234\"`\n- it must contain at least one of the special characters `!`, `#` or `?`\n\nFirst read the user name `user`, then the password `pw` with `input()`. Store the four partial checks in `long_enough`, `no_user`, `no_default`, `has_special` and the overall result in `accepted`. Print `accepted`."},
   starter={"de": "# Benutzername und Passwort einlesen\n", "en": "# read user name and password\n"},
   solution='user = input("Benutzer: ")\npw = input("Passwort: ")\nlong_enough = len(pw) >= 10\nno_user = user not in pw\nno_default = "admin1234" not in pw\nhas_special = "!" in pw or "#" in pw or "?" in pw\naccepted = long_enough and no_user and no_default and has_special\nprint("Passwort akzeptiert:", accepted)\n',
   tests='''
cases = [("weber", "Fraese#2026x", True), ("weber", "kurz#1", False), ("weber", "weber#2026abc", False),
         ("weber", "xadmin1234!y", False), ("weber", "OhneSonderzeichen", False), ("op", "Linie?Drei!!", True), ("op", "Abcdefgh#1", True), ("op", "Abcdefg#1", False)]
for u, p, e in cases:
    ns, out = run(inputs=[u, p])
    a = need(ns, "accepted")
    check(a is e, f"Benutzer {u!r}, Passwort {p!r}: accepted = {e}", f"user {u!r}, password {p!r}: accepted = {e}")
ns, out = run(inputs=["weber", "weber#2026abc"])
check(ns.get("long_enough") is True and ns.get("no_user") is False and ns.get("has_special") is True, "Teilprüfungen für 'weber#2026abc' stimmen", "Partial checks for 'weber#2026abc' are correct")
''',
   stdin="weber\nFraese#2026x\n", require=["in", "boolop"], refs=["4.4", "4.3e"])

# ------------------------------------------------------------------ Stufe 3
ex(id="k4-cantilever", ch="4", lvl=3,
   title={"de": "Durchbiegung eines Kragträgers", "en": "Deflection of a cantilever"},
   task={"de": "Ein Kragträger mit Rechteckquerschnitt (Breite `b`, Höhe `h` in mm) und der Länge `L` (mm) wird am freien Ende mit der Kraft `F` (N) belastet. Mit dem E-Modul `E` (N/mm²) gilt:\n- Flächenträgheitsmoment I = b·h³ / 12 (mm⁴)\n- Durchbiegung am Ende f = F·L³ / (3·E·I) (mm)\n\nBerechnen Sie `I` und `f`. Die zulässige Durchbiegung ist `f_max = L / 250`. Speichern Sie in `ok`, ob f höchstens f_max ist, und in `utilisation` die Ausnutzung f / f_max in Prozent (eine Nachkommastelle, `round`). Ausgabe z.B. `f = 2.41 mm (zulässig 4.80 mm), Ausnutzung 50.2 %`.",
         "en": "A cantilever with rectangular cross-section (width `b`, height `h` in mm) and length `L` (mm) carries the force `F` (N) at its free end. With Young's modulus `E` (N/mm²):\n- second moment of area I = b·h³ / 12 (mm⁴)\n- deflection at the end f = F·L³ / (3·E·I) (mm)\n\nCompute `I` and `f`. The permissible deflection is `f_max = L / 250`. Store in `ok` whether f is at most f_max, and in `utilisation` the utilisation f / f_max in percent (one decimal, `round`). Output e.g. `f = 2.41 mm (permissible 4.80 mm), utilisation 50.2 %`."},
   starter={"de": "b = 40.0       # mm\nh = 80.0       # mm\nL = 1200.0     # mm\nF = 1500.0     # N\nE = 210000.0   # N/mm² (Stahl)\n\n# Ihr Code:\n", "en": "b = 40.0       # mm\nh = 80.0       # mm\nL = 1200.0     # mm\nF = 1500.0     # N\nE = 210000.0   # N/mm² (steel)\n\n# your code:\n"},
   solution='b = 40.0\nh = 80.0\nL = 1200.0\nF = 1500.0\nE = 210000.0\nI = b * h**3 / 12\nf = F * L**3 / (3 * E * I)\nf_max = L / 250\nok = f <= f_max\nutilisation = round(f / f_max * 100, 1)\nprint(f"f = {f:.2f} mm (zulässig {f_max:.2f} mm), Ausnutzung {utilisation} %")\n',
   tests='''
for b, h, L, F, E in [(40.0, 80.0, 1200.0, 1500.0, 210000.0), (30.0, 30.0, 500.0, 200.0, 70000.0), (60.0, 120.0, 3000.0, 4000.0, 210000.0)]:
    ns, out = run(sub={"b": b, "h": h, "L": L, "F": F, "E": E})
    I, f, ok, u = need(ns, "I", "f", "ok", "utilisation")
    eI = b * h**3 / 12; ef = F * L**3 / (3 * E * eI); fm = L / 250
    check(approx(I, eI), f"b = {b}, h = {h}: I = {eI:.4g} mm⁴", f"b = {b}, h = {h}: I = {eI:.4g} mm⁴")
    check(approx(f, ef), f"Durchbiegung f = {ef:.3f} mm", f"deflection f = {ef:.3f} mm")
    check(ok is (ef <= fm) and approx(u, round(ef / fm * 100, 1)), f"ok = {ef <= fm}, Ausnutzung {round(ef / fm * 100, 1)} %", f"ok = {ef <= fm}, utilisation {round(ef / fm * 100, 1)} %")
''',
   refs=["4.2", "4.4"])

ex(id="k4-payback", ch="4", lvl=3,
   title={"de": "Lohnt sich die LED-Umrüstung?", "en": "Is the LED retrofit worth it?"},
   task={"de": "Eine Halle wird auf LED umgerüstet. Die Investition kostet `invest` €, die Stromkosten sinken im ersten Jahr um `saving` €. Weil der Strompreis jedes Jahr um `p` Prozent steigt, wächst die Ersparnis entsprechend: Im Jahr k beträgt sie saving·q^(k−1) mit q = 1 + p/100.\n\nDie Summe der Ersparnisse über n Jahre ist eine geometrische Reihe: S = saving · (qⁿ − 1) / (q − 1).\n\nBerechnen Sie `q`, die Ersparnis im letzten Jahr `last_year`, die Gesamtersparnis `total` nach `n` Jahren und speichern Sie in `pays_off`, ob sich die Investition in dieser Zeit amortisiert (total ≥ invest). Geben Sie Gesamtersparnis und `pays_off` aus (Ersparnis auf ganze Euro gerundet).\n\nSie dürfen voraussetzen, dass p größer als 0 ist.",
         "en": "A hall is retrofitted with LEDs. The investment costs `invest` €; the electricity costs drop by `saving` € in the first year. Because the electricity price rises by `p` percent every year, the saving grows accordingly: in year k it is saving·q^(k−1) with q = 1 + p/100.\n\nThe sum of the savings over n years is a geometric series: S = saving · (qⁿ − 1) / (q − 1).\n\nCompute `q`, the saving in the last year `last_year`, the total saving `total` after `n` years, and store in `pays_off` whether the investment pays for itself in that time (total ≥ invest). Print the total saving and `pays_off` (saving rounded to whole euros).\n\nYou may assume that p is greater than 0."},
   starter={"de": "invest = 18000.0  # €\nsaving = 2400.0   # € im ersten Jahr\np = 4.0           # % Preissteigerung pro Jahr\nn = 6             # Jahre\n\n# Ihr Code:\n", "en": "invest = 18000.0  # €\nsaving = 2400.0   # € in the first year\np = 4.0           # % price increase per year\nn = 6             # years\n\n# your code:\n"},
   solution='invest = 18000.0\nsaving = 2400.0\np = 4.0\nn = 6\nq = 1 + p / 100\nlast_year = saving * q**(n - 1)\ntotal = saving * (q**n - 1) / (q - 1)\npays_off = total >= invest\nprint(f"Ersparnis nach {n} Jahren: {round(total)} €, amortisiert: {pays_off}")\n',
   tests='''
for inv, s, p, n in [(18000.0, 2400.0, 4.0, 6), (18000.0, 2400.0, 4.0, 7), (5000.0, 1000.0, 10.0, 4), (100.0, 50.0, 2.5, 1), (1000.0, 1000.0, 5.0, 1)]:
    ns, out = run(sub={"invest": inv, "saving": s, "p": p, "n": n})
    q, ly, t, po = need(ns, "q", "last_year", "total", "pays_off")
    eq = 1 + p / 100; et = s * (eq**n - 1) / (eq - 1)
    check(approx(q, eq) and approx(ly, s * eq**(n - 1)), f"p = {p} %: q = {eq}, letztes Jahr {s * eq**(n-1):.2f} €", f"p = {p} %: q = {eq}, last year {s * eq**(n-1):.2f} €")
    check(approx(t, et), f"Gesamtersparnis nach {n} Jahren: {et:.2f} €", f"total saving after {n} years: {et:.2f} €")
    check(po is (et >= inv), f"pays_off = {et >= inv} (Investition {inv:g} €)", f"pays_off = {et >= inv} (investment {inv:g} €)")
    check(str(round(et)) in out, f"Ausgabe zeigt {round(et)} €", f"Output shows {round(et)} €")
''',
   refs=["4.2", "4.4"])

ex(id="k4-gas", ch="4", lvl=3,
   title={"de": "Druckbehälter in der Sonne", "en": "Pressure vessel in the sun"},
   task={"de": "Ein geschlossener Druckluftbehälter (Volumen konstant) wurde bei `T1_C` °C auf den Überdruck `p1_gauge` bar gefüllt. In der Sonne erwärmt er sich auf `T2_C` °C. Für ein ideales Gas bei konstantem Volumen gilt p₂ / p₁ = T₂ / T₁ – aber nur mit **absoluten** Drücken und Temperaturen!\n- Absolutdruck = Überdruck + 1.013 bar, absolute Temperatur T = ϑ + 273.15 K\n\nBerechnen Sie `p1_abs`, `T1_K`, `T2_K`, den neuen Absolutdruck `p2_abs` und den neuen Überdruck `p2_gauge`. Speichern Sie in `valve_opens`, ob das Sicherheitsventil anspricht (Überdruck **größer** als `p_valve`). Ausgabe: neuer Überdruck mit zwei Nachkommastellen und `valve_opens`.",
         "en": "A closed compressed-air vessel (constant volume) was filled at `T1_C` °C to the gauge pressure `p1_gauge` bar. In the sun it heats up to `T2_C` °C. For an ideal gas at constant volume, p₂ / p₁ = T₂ / T₁ – but only with **absolute** pressures and temperatures!\n- absolute pressure = gauge pressure + 1.013 bar, absolute temperature T = ϑ + 273.15 K\n\nCompute `p1_abs`, `T1_K`, `T2_K`, the new absolute pressure `p2_abs` and the new gauge pressure `p2_gauge`. Store in `valve_opens` whether the safety valve responds (gauge pressure **greater** than `p_valve`). Output: new gauge pressure with two decimals and `valve_opens`."},
   starter={"de": "p1_gauge = 10.0  # bar Überdruck\nT1_C = 15.0      # °C\nT2_C = 60.0      # °C\np_valve = 11.5   # bar Ansprechdruck\n\n# Ihr Code:\n", "en": "p1_gauge = 10.0  # bar gauge\nT1_C = 15.0      # °C\nT2_C = 60.0      # °C\np_valve = 11.5   # bar set pressure\n\n# your code:\n"},
   solution='p1_gauge = 10.0\nT1_C = 15.0\nT2_C = 60.0\np_valve = 11.5\np1_abs = p1_gauge + 1.013\nT1_K = T1_C + 273.15\nT2_K = T2_C + 273.15\np2_abs = p1_abs * T2_K / T1_K\np2_gauge = p2_abs - 1.013\nvalve_opens = p2_gauge > p_valve\nprint(f"Neuer Überdruck: {p2_gauge:.2f} bar, Ventil öffnet: {valve_opens}")\n',
   tests='''
for p1, t1, t2, pv in [(10.0, 15.0, 60.0, 11.5), (10.0, 15.0, 40.0, 11.5), (6.0, -10.0, 25.0, 8.0), (2.0, 20.0, 20.0, 2.0)]:
    ns, out = run(sub={"p1_gauge": p1, "T1_C": t1, "T2_C": t2, "p_valve": pv})
    pa, T1, T2, p2a, p2g, vo = need(ns, "p1_abs", "T1_K", "T2_K", "p2_abs", "p2_gauge", "valve_opens")
    ep2 = (p1 + 1.013) * (t2 + 273.15) / (t1 + 273.15)
    check(approx(pa, p1 + 1.013) and approx(T1, t1 + 273.15) and approx(T2, t2 + 273.15), "Absolutdruck und absolute Temperaturen stimmen", "Absolute pressure and absolute temperatures are correct")
    check(approx(p2a, ep2) and approx(p2g, ep2 - 1.013), f"{p1} bar bei {t1} °C → {ep2 - 1.013:.3f} bar Überdruck bei {t2} °C", f"{p1} bar at {t1} °C → {ep2 - 1.013:.3f} bar gauge at {t2} °C")
    check(vo is (ep2 - 1.013 > pv), f"valve_opens = {ep2 - 1.013 > pv}", f"valve_opens = {ep2 - 1.013 > pv}")
''',
   refs=["4.2", "4.4"])

ex(id="k4-throw", ch="4", lvl=3,
   title={"de": "Waagerechter Wurf vom Förderband", "en": "Horizontal throw from a conveyor"},
   task={"de": "Am Ende eines Förderbands (Höhe `h` in m über dem Behälterboden) fallen Teile mit der Bandgeschwindigkeit `v0` (m/s) waagerecht ab (Luftwiderstand vernachlässigt, g = 9.81 m/s²).\n- Fallzeit t = √(2h / g)\n- Wurfweite x = v0 · t\n- Aufprallgeschwindigkeit v = √(v0² + (g·t)²)\n\nWurzeln berechnen Sie mit `** 0.5`. Speichern Sie die Ergebnisse in `t`, `x`, `v`. Der Behälter beginnt bei `x_start` und endet bei `x_end` (m, gemessen ab der Bandkante): Speichern Sie in `hits_bin`, ob die Teile im Behälter landen (Grenzen eingeschlossen). Ausgabe mit drei Nachkommastellen.",
         "en": "At the end of a conveyor belt (height `h` in m above the bottom of a bin), parts leave horizontally with the belt speed `v0` (m/s) (air resistance neglected, g = 9.81 m/s²).\n- fall time t = √(2h / g)\n- throw distance x = v0 · t\n- impact speed v = √(v0² + (g·t)²)\n\nCompute roots with `** 0.5`. Store the results in `t`, `x`, `v`. The bin starts at `x_start` and ends at `x_end` (m, measured from the belt edge): store in `hits_bin` whether the parts land in the bin (limits included). Output with three decimals."},
   starter={"de": "h = 0.8        # m\nv0 = 1.2       # m/s\nx_start = 0.3  # m\nx_end = 0.7    # m\n\n# Ihr Code:\n", "en": "h = 0.8        # m\nv0 = 1.2       # m/s\nx_start = 0.3  # m\nx_end = 0.7    # m\n\n# your code:\n"},
   solution='h = 0.8\nv0 = 1.2\nx_start = 0.3\nx_end = 0.7\nt = (2 * h / 9.81) ** 0.5\nx = v0 * t\nv = (v0**2 + (9.81 * t)**2) ** 0.5\nhits_bin = x_start <= x <= x_end\nprint(f"t = {t:.3f} s, x = {x:.3f} m, v = {v:.3f} m/s, im Behälter: {hits_bin}")\n',
   tests='''
for h, v0 in [(0.8, 1.2), (0.8, 2.5), (1.5, 0.4), (0.2, 1.0)]:
    ns, out = run(sub={"h": h, "v0": v0})
    t, x, v, hb = need(ns, "t", "x", "v", "hits_bin")
    et = (2 * h / 9.81) ** 0.5; ex_ = v0 * et; ev = (v0**2 + (9.81 * et)**2) ** 0.5
    check(approx(t, et) and approx(x, ex_), f"h = {h} m, v0 = {v0} m/s: t = {et:.3f} s, x = {ex_:.3f} m", f"h = {h} m, v0 = {v0} m/s: t = {et:.3f} s, x = {ex_:.3f} m")
    check(approx(v, ev), f"Aufprallgeschwindigkeit {ev:.3f} m/s", f"impact speed {ev:.3f} m/s")
    check(hb is (0.3 <= ex_ <= 0.7), f"hits_bin = {0.3 <= ex_ <= 0.7}", f"hits_bin = {0.3 <= ex_ <= 0.7}")
''',
   refs=["4.2", "4.4"])

ex(id="k4-fit", ch="4", lvl=3,
   title={"de": "Passung: Spiel oder Übermaß?", "en": "Fit: clearance or interference?"},
   task={"de": "Eine Bohrung hat das Mindestmaß `hole_min` und das Höchstmaß `hole_max`, die Welle `shaft_min` und `shaft_max` (alle in mm). Berechnen Sie\n- `clearance_max` = Höchstmaß Bohrung − Mindestmaß Welle (Höchstspiel)\n- `clearance_min` = Mindestmaß Bohrung − Höchstmaß Welle (Mindestspiel; negativ bedeutet Übermaß)\n\nDie Passung ist eine\n- **Spielpassung** (`clearance_fit`), wenn das Mindestspiel größer als 0 ist,\n- **Übermaßpassung** (`interference_fit`), wenn das Höchstspiel kleiner als 0 ist,\n- sonst eine **Übergangspassung** (`transition_fit`) – ohne `if`, mit `not` und `and`.\n\nRunden Sie die beiden Spiele auf drei Nachkommastellen (`round`), damit keine Rundungsfehler stören, und geben Sie alles aus.",
         "en": "A bore has the minimum size `hole_min` and the maximum size `hole_max`, the shaft `shaft_min` and `shaft_max` (all in mm). Compute\n- `clearance_max` = bore maximum − shaft minimum (maximum clearance)\n- `clearance_min` = bore minimum − shaft maximum (minimum clearance; negative means interference)\n\nThe fit is a\n- **clearance fit** (`clearance_fit`) if the minimum clearance is greater than 0,\n- **interference fit** (`interference_fit`) if the maximum clearance is less than 0,\n- otherwise a **transition fit** (`transition_fit`) – without `if`, using `not` and `and`.\n\nRound both clearances to three decimals (`round`) so that rounding errors don't interfere, and print everything."},
   starter={"de": "hole_min = 25.000\nhole_max = 25.021\nshaft_min = 24.959\nshaft_max = 24.980\n\n# Ihr Code:\n", "en": "hole_min = 25.000\nhole_max = 25.021\nshaft_min = 24.959\nshaft_max = 24.980\n\n# your code:\n"},
   solution='hole_min = 25.000\nhole_max = 25.021\nshaft_min = 24.959\nshaft_max = 24.980\nclearance_max = round(hole_max - shaft_min, 3)\nclearance_min = round(hole_min - shaft_max, 3)\nclearance_fit = clearance_min > 0\ninterference_fit = clearance_max < 0\ntransition_fit = not clearance_fit and not interference_fit\nprint(clearance_max, clearance_min, clearance_fit, interference_fit, transition_fit)\n',
   tests='''
cases = [(25.000, 25.021, 24.959, 24.980), (25.000, 25.021, 25.035, 25.048), (25.000, 25.021, 24.991, 25.015), (40.0, 40.025, 39.95, 39.975), (25.000, 25.021, 25.021, 25.040), (25.000, 25.021, 24.980, 25.000)]
for a, b, c, d in cases:
    ns, out = run(sub={"hole_min": a, "hole_max": b, "shaft_min": c, "shaft_max": d})
    cmax, cmin, cf, inf, tf = need(ns, "clearance_max", "clearance_min", "clearance_fit", "interference_fit", "transition_fit")
    e1, e2 = round(b - c, 3), round(a - d, 3)
    check(approx(cmax, e1) and approx(cmin, e2), f"Bohrung {a}…{b}, Welle {c}…{d}: Höchstspiel {e1}, Mindestspiel {e2}", f"bore {a}…{b}, shaft {c}…{d}: max clearance {e1}, min clearance {e2}")
    exp = (e2 > 0, e1 < 0, not e2 > 0 and not e1 < 0)
    check((cf, inf, tf) == exp, f"Spiel/Übermaß/Übergang = {exp}", f"clearance/interference/transition = {exp}")
''',
   require=["boolop", "round"], refs=["4.4", "4.2"])
