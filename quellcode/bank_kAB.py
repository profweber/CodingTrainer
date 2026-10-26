from exlib import ex

# Anhang A: open/with, read/write/readline, strip/split/startswith, pathlib, csv.
# Anhang B: try/except/else/finally, raise.

# ------------------------------------------------------------------ Anhang A
ex(id="kA-append", ch="A", lvl=1,
   title={"de": "Betriebsstunden anhängen", "en": "Appending operating hours"},
   task={"de": "Die Datei `data/betriebsstunden.txt` enthält bereits Einträge im Format `datum;stunden`. Hängen Sie eine neue Zeile mit `date` und `hours` an, **ohne** die vorhandenen Einträge zu löschen (richtiger Modus!). Verwenden Sie `with` und `encoding=\"utf-8\"` und denken Sie an den Zeilenumbruch.",
         "en": "The file `data/betriebsstunden.txt` already contains entries in the format `datum;stunden` (date;hours). Append a new line with `date` and `hours` **without** deleting the existing entries (right mode!). Use `with` and `encoding=\"utf-8\"` and remember the line break."},
   starter={"de": 'date = "2026-10-22"\nhours = 7.5\n\n# Ihr Code:\n', "en": 'date = "2026-10-22"\nhours = 7.5\n\n# your code:\n'},
   solution='date = "2026-10-22"\nhours = 7.5\nwith open("data/betriebsstunden.txt", "a", encoding="utf-8") as f:\n    f.write(f"{date};{hours}\\n")\n',
   tests='''
start = "datum;stunden\\n2026-10-20;8.0\\n2026-10-21;6.25\\n"
for d, h in [("2026-10-22", 7.5), ("2027-01-01", 0.0)]:
    ns, out = run(sub={"date": d, "hours": h}, files={"data/betriebsstunden.txt": start})
    c = read_file("data/betriebsstunden.txt")
    check(c.startswith(start), "Die bisherigen Einträge sind noch da", "The existing entries are still there")
    check(c[len(start):].strip() == f"{d};{h}", f"Neue Zeile '{d};{h}' wurde angehängt", f"New line '{d};{h}' was appended")
    check(c.endswith("\\n"), "Die Datei endet mit einem Zeilenumbruch", "The file ends with a line break")
''',
   require=["with", "open"], refs=["A.2"],
   files={"data/betriebsstunden.txt": "datum;stunden\n2026-10-20;8.0\n2026-10-21;6.25\n"})

ex(id="kA-readall", ch="A", lvl=1,
   title={"de": "Logdatei überblicken", "en": "Overview of a log file"},
   task={"de": "Lesen Sie die Datei `data/maschine.log` mit `read()` vollständig in die Variable `text` ein. Bestimmen Sie\n- `n_chars`: die Anzahl der Zeichen\n- `n_lines`: die Anzahl der Zeilen. Zerlegen Sie den Text dazu mit `split(\"\\n\")`. Achtung: Weil auch die letzte Zeile mit `\\n` endet, ist der letzte Eintrag der Liste ein leerer String – den dürfen Sie nicht mitzählen.\n- `has_error`: ob irgendwo `ERROR` vorkommt",
         "en": "Read the whole file `data/maschine.log` with `read()` into the variable `text`. Determine\n- `n_chars`: the number of characters\n- `n_lines`: the number of lines. Split the text with `split(\"\\n\")`. Careful: since the last line also ends with `\\n`, the last entry of the list is an empty string – don't count it.\n- `has_error`: whether `ERROR` occurs anywhere"},
   starter={"de": "# Ihr Code:\n", "en": "# your code:\n"},
   solution='with open("data/maschine.log", encoding="utf-8") as f:\n    text = f.read()\nn_chars = len(text)\nn_lines = len(text.split("\\n")) - 1\nhas_error = "ERROR" in text\nprint(n_chars, n_lines, has_error)\n',
   tests='''
for content in ["08:00 INFO Start\\n08:15 WARN Temperatur 82 °C\\n08:20 ERROR Not-Aus\\n", "INFO ok\\nINFO ok\\n", "x\\n"]:
    ns, out = run(files={"data/maschine.log": content})
    t, c, l, e = need(ns, "text", "n_chars", "n_lines", "has_error")
    check(t == content, "text enthält den kompletten Dateiinhalt", "text contains the complete file content")
    check(c == len(content) and l == content.count("\\n"), f"{len(content)} Zeichen, {content.count(chr(10))} Zeilen", f"{len(content)} characters, {content.count(chr(10))} lines")
    check(e is ("ERROR" in content), f"has_error = {'ERROR' in content}", f"has_error = {'ERROR' in content}")
''',
   require=["with", "file_methods"], refs=["A.3"],
   files={"data/maschine.log": "08:00 INFO Start\n08:15 WARN Temperatur 82 °C\n08:20 ERROR Not-Aus\n"})

ex(id="kA-pathlib", ch="A", lvl=2,
   title={"de": "Bericht mit pathlib", "en": "Report with pathlib"},
   task={"de": "Erstellen Sie mit `pathlib` einen kurzen Prüfbericht:\n- `report`: der Pfad `data/bericht.txt`, zusammengesetzt mit dem Operator `/` aus `Path(\"data\")` und dem Dateinamen\n- Schreiben Sie mit `write_text` (Encoding utf-8) zwei Zeilen: `Prüfling: {name}` und `Mittelwert: {mean} mm` (Mittelwert der Liste `values`, zwei Nachkommastellen).\n- Lesen Sie den Bericht mit `read_text` wieder in `content` ein und speichern Sie `report.suffix` in `suffix` und `report.exists()` in `exists`.",
         "en": "Use `pathlib` to create a short test report:\n- `report`: the path `data/bericht.txt`, built with the operator `/` from `Path(\"data\")` and the file name\n- Use `write_text` (encoding utf-8) to write two lines: `Prüfling: {name}` and `Mittelwert: {mean} mm` (mean of the list `values`, two decimals; keep the German labels).\n- Read the report back into `content` with `read_text`, and store `report.suffix` in `suffix` and `report.exists()` in `exists`."},
   starter={"de": 'from pathlib import Path\n\nname = "Welle W-17"\nvalues = [24.98, 25.01, 25.03, 24.99]\n\n# Ihr Code:\n', "en": 'from pathlib import Path\n\nname = "Welle W-17"\nvalues = [24.98, 25.01, 25.03, 24.99]\n\n# your code:\n'},
   solution='from pathlib import Path\n\nname = "Welle W-17"\nvalues = [24.98, 25.01, 25.03, 24.99]\nreport = Path("data") / "bericht.txt"\nmean = sum(values) / len(values)\nreport.write_text(f"Prüfling: {name}\\nMittelwert: {mean:.2f} mm\\n", encoding="utf-8")\ncontent = report.read_text(encoding="utf-8")\nsuffix = report.suffix\nexists = report.exists()\nprint(content)\n',
   tests='''
for n, v in [("Welle W-17", [24.98, 25.01, 25.03, 24.99]), ("Bolzen B2", [8.0, 8.1])]:
    ns, out = run(sub={"name": n, "values": v})
    r, c, s, e = need(ns, "report", "content", "suffix", "exists")
    check(type(r).__name__.endswith("Path") and str(r).replace("\\\\", "/") == "data/bericht.txt", "report ist ein Path-Objekt für data/bericht.txt", "report is a Path object for data/bericht.txt")
    disk = read_file("data/bericht.txt")
    m = sum(v) / len(v)
    check(f"Prüfling: {n}" in disk and f"Mittelwert: {m:.2f} mm" in disk, f"Datei enthält 'Prüfling: {n}' und 'Mittelwert: {m:.2f} mm'", f"File contains 'Prüfling: {n}' and 'Mittelwert: {m:.2f} mm'")
    check(c == disk and s == ".txt" and e is True, "content, suffix und exists stimmen", "content, suffix and exists are correct")
''',
   require=["pathlib"], refs=["A.1", "A.3"])

ex(id="kA-convert", ch="A", lvl=2,
   title={"de": "Deutsches CSV umwandeln", "en": "Converting a German CSV"},
   task={"de": "Das deutsche Excel hat die Datei `data/messung_de.csv` geschrieben: Trennzeichen `;`, Dezimalkomma. Erzeugen Sie daraus `data/messung_en.csv` mit Trennzeichen `,` und Dezimalpunkt. Die Kopfzeile wird übernommen (nur das Trennzeichen ändert sich), Leerzeilen werden übersprungen. Sammeln Sie außerdem die Messwerte (zweite Spalte) als float in der Liste `values`.",
         "en": "German Excel wrote the file `data/messung_de.csv`: separator `;`, decimal comma. Create `data/messung_en.csv` from it with separator `,` and decimal point. The header line is kept (only the separator changes), blank lines are skipped. Also collect the measurements (second column) as float in the list `values`."},
   starter={"de": "values = []\n\n# Ihr Code:\n", "en": "values = []\n\n# your code:\n"},
   solution='values = []\nwith open("data/messung_de.csv", encoding="utf-8") as src:\n    lines = src.read().split("\\n")\nwith open("data/messung_en.csv", "w", encoding="utf-8") as dst:\n    dst.write(lines[0].strip().replace(";", ",") + "\\n")\n    for line in lines[1:]:\n        line = line.strip()\n        if line == "":\n            continue\n        t, v = line.split(";")\n        v = v.replace(",", ".")\n        values.append(float(v))\n        dst.write(f"{t},{v}\\n")\nprint(values)\n',
   tests='''
for content, vals in [("zeit;wert\\n0;21,4\\n5;23,9\\n\\n10;27,5\\n", [21.4, 23.9, 27.5]), ("t_s;U_V\\n1;3,30\\n2;-0,5\\n", [3.3, -0.5])]:
    ns, out = run(files={"data/messung_de.csv": content})
    v = need(ns, "values")
    check(v == vals, f"values = {vals}", f"values = {vals}")
    try:
        lines = [l for l in read_file("data/messung_en.csv").split("\\n") if l.strip()]
    except FileNotFoundError:
        lines = []
    src = [l for l in content.split("\\n") if l.strip()]
    check(len(lines) == len(src) and lines[0] == src[0].replace(";", ","), "Kopfzeile mit Komma als Trennzeichen", "Header line with comma separator")
    check(all(float(l.split(",")[1]) == x for l, x in zip(lines[1:], vals)) and all(";" not in l for l in lines), "Datenzeilen mit ',' als Trenner und Dezimalpunkt", "Data lines with ',' separator and decimal point")
''',
   require=["with", "file_methods"], refs=["A.3", "A.4", "5.2e"],
   files={"data/messung_de.csv": "zeit;wert\n0;21,4\n5;23,9\n\n10;27,5\n"})

ex(id="kA-csvwriter", ch="A", lvl=3,
   title={"de": "Auswertung als CSV schreiben", "en": "Writing results as CSV"},
   task={"de": "Schreiben Sie mit `csv.writer` die Datei `data/auswertung.csv` (`newline=\"\"`, utf-8) mit der Kopfzeile `zeit_s, strom_A, leistung_W` und einer Zeile pro Messpunkt aus `times` und `currents`; die Leistung ist P = U · I mit `U = 230.0`, auf eine Nachkommastelle gerundet. `writer.writerow([...])` schreibt eine Zeile.\n\nLesen Sie die Datei danach mit `csv.DictReader` wieder ein und speichern Sie in `max_power` die größte Leistung (als float) und in `t_max` den zugehörigen Zeitpunkt (als int).",
         "en": "Use `csv.writer` to write the file `data/auswertung.csv` (`newline=\"\"`, utf-8) with the header `zeit_s, strom_A, leistung_W` and one row per data point from `times` and `currents`; the power is P = U · I with `U = 230.0`, rounded to one decimal. `writer.writerow([...])` writes one row.\n\nThen read the file back with `csv.DictReader` and store the largest power (as float) in `max_power` and the corresponding time (as int) in `t_max`."},
   starter={"de": "import csv\n\nU = 230.0\ntimes = [0, 10, 20, 30]\ncurrents = [2.1, 4.8, 4.3, 0.9]\n\n# Ihr Code:\n", "en": "import csv\n\nU = 230.0\ntimes = [0, 10, 20, 30]\ncurrents = [2.1, 4.8, 4.3, 0.9]\n\n# your code:\n"},
   solution='import csv\n\nU = 230.0\ntimes = [0, 10, 20, 30]\ncurrents = [2.1, 4.8, 4.3, 0.9]\nwith open("data/auswertung.csv", "w", encoding="utf-8", newline="") as f:\n    writer = csv.writer(f)\n    writer.writerow(["zeit_s", "strom_A", "leistung_W"])\n    for t, i in zip(times, currents):\n        writer.writerow([t, i, round(U * i, 1)])\n\nmax_power = None\nt_max = None\nwith open("data/auswertung.csv", encoding="utf-8", newline="") as f:\n    for row in csv.DictReader(f):\n        p = float(row["leistung_W"])\n        if max_power is None or p > max_power:\n            max_power = p\n            t_max = int(row["zeit_s"])\nprint(max_power, t_max)\n',
   tests='''
import csv as _csv, io as _io
for ti, cu in [([0, 10, 20, 30], [2.1, 4.8, 4.3, 0.9]), ([5, 6], [1.0, 0.5])]:
    ns, out = run(sub={"times": ti, "currents": cu})
    mp, tm = need(ns, "max_power", "t_max")
    rows = list(_csv.reader(_io.StringIO(read_file("data/auswertung.csv"))))
    check(rows[0] == ["zeit_s", "strom_A", "leistung_W"], "Kopfzeile stimmt", "Header row is correct")
    check(len(rows) == len(ti) + 1 and all(float(r[2]) == round(230.0 * c, 1) and int(r[0]) == t for r, t, c in zip(rows[1:], ti, cu)), "Eine Datenzeile pro Messpunkt mit richtiger Leistung", "One data row per point with the correct power")
    k = max(range(len(cu)), key=lambda j: cu[j])
    check(approx(mp, round(230.0 * cu[k], 1)) and tm == ti[k], f"max_power = {round(230.0*cu[k], 1)} W bei t = {ti[k]} s", f"max_power = {round(230.0*cu[k], 1)} W at t = {ti[k]} s")
''',
   require=["csv", "with"], refs=["A.4"])

ex(id="kA-logfilter", ch="A", lvl=3,
   title={"de": "Logdatei filtern", "en": "Filtering a log file"},
   task={"de": "Jede Zeile von `data/anlage.log` hat das Format `2026-10-22 08:00:01 WARN Temperatur hoch` (Datum, Uhrzeit, Level, Meldung).\n- `counts`: Dictionary Level → Anzahl der Zeilen\n- Schreiben Sie alle `ERROR`-Zeilen unverändert in `data/errors.txt`.\n- `first_error`: die Uhrzeit (als String) der ersten ERROR-Zeile, `None` falls es keine gibt\n\nLeerzeilen werden übersprungen. Tipp: `split(\" \", 3)` teilt höchstens dreimal, so bleibt die Meldung mit ihren Leerzeichen zusammen.",
         "en": "Each line of `data/anlage.log` has the format `2026-10-22 08:00:01 WARN Temperatur hoch` (date, time, level, message).\n- `counts`: dictionary level → number of lines\n- Write all `ERROR` lines unchanged to `data/errors.txt`.\n- `first_error`: the time (as a string) of the first ERROR line, `None` if there is none\n\nBlank lines are skipped. Tip: `split(\" \", 3)` splits at most three times, keeping the message with its spaces together."},
   starter={"de": "counts = {}\nfirst_error = None\n\n# Ihr Code:\n", "en": "counts = {}\nfirst_error = None\n\n# your code:\n"},
   solution='counts = {}\nfirst_error = None\nerrors = []\nwith open("data/anlage.log", encoding="utf-8") as f:\n    for line in f:\n        line = line.strip()\n        if line == "":\n            continue\n        date, time, level, message = line.split(" ", 3)\n        counts[level] = counts.get(level, 0) + 1\n        if level == "ERROR":\n            errors.append(line)\n            if first_error is None:\n                first_error = time\nwith open("data/errors.txt", "w", encoding="utf-8") as out:\n    for line in errors:\n        out.write(line + "\\n")\nprint(counts, first_error)\n',
   tests='''
LOG1 = "2026-10-22 08:00:01 INFO Anlage gestartet\\n2026-10-22 08:12:44 WARN Temperatur hoch\\n\\n2026-10-22 08:13:02 ERROR Pumpe 2 ausgefallen\\n2026-10-22 08:14:10 INFO Reserve aktiv\\n2026-10-22 09:01:55 ERROR Druck zu niedrig\\n"
LOG2 = "2026-10-23 10:00:00 INFO alles ok\\n"
for log in [LOG1, LOG2]:
    ns, out = run(files={"data/anlage.log": log})
    c, fe = need(ns, "counts", "first_error")
    lines = [l for l in log.split("\\n") if l.strip()]
    ec = {}
    for l in lines:
        lv = l.split(" ")[2]; ec[lv] = ec.get(lv, 0) + 1
    errs = [l for l in lines if l.split(" ")[2] == "ERROR"]
    check(c == ec, f"counts = {ec}", f"counts = {ec}")
    check(fe == (errs[0].split(" ")[1] if errs else None), f"first_error = {errs[0].split(' ')[1] if errs else None!r}", f"first_error = {errs[0].split(' ')[1] if errs else None!r}")
    try:
        written = [l for l in read_file("data/errors.txt").split("\\n") if l.strip()]
    except FileNotFoundError:
        written = None
    check(written == errs, f"errors.txt enthält genau die {len(errs)} ERROR-Zeile(n)", f"errors.txt contains exactly the {len(errs)} ERROR line(s)")
''',
   require=["with", "file_methods", "dict"], refs=["A.3", "8.3"],
   files={"data/anlage.log": "2026-10-22 08:00:01 INFO Anlage gestartet\n2026-10-22 08:12:44 WARN Temperatur hoch\n\n2026-10-22 08:13:02 ERROR Pumpe 2 ausgefallen\n2026-10-22 08:14:10 INFO Reserve aktiv\n2026-10-22 09:01:55 ERROR Druck zu niedrig\n"})

# ------------------------------------------------------------------ Anhang B
ex(id="kB-efficiency", ch="B", lvl=1,
   title={"de": "Wirkungsgrad ohne Absturz", "en": "Efficiency without crashing"},
   task={"de": "Schreiben Sie `efficiency(p_out, p_in)`, die den Wirkungsgrad p_out / p_in zurückgibt. Ist `p_in` gleich 0, soll **nicht** abgestürzt werden: Fangen Sie den `ZeroDivisionError` mit `try`/`except` ab und geben Sie `None` zurück.",
         "en": "Write `efficiency(p_out, p_in)` that returns the efficiency p_out / p_in. If `p_in` is 0, the program must **not** crash: catch the `ZeroDivisionError` with `try`/`except` and return `None`."},
   starter={"de": "def efficiency(p_out, p_in):\n    ...\n", "en": "def efficiency(p_out, p_in):\n    ...\n"},
   solution='def efficiency(p_out, p_in):\n    try:\n        return p_out / p_in\n    except ZeroDivisionError:\n        return None\n\nprint(efficiency(870, 1000), efficiency(5, 0))\n',
   tests='''
ns, out = run()
for a, b in [(870, 1000), (0, 5), (3.3, 4.4)]:
    check(approx(call(ns, "efficiency", a, b), a / b), f"efficiency({a}, {b}) = {a/b:g}", f"efficiency({a}, {b}) = {a/b:g}")
check(call(ns, "efficiency", 5, 0) is None and call(ns, "efficiency", 0, 0.0) is None, "Division durch 0 liefert None", "Division by 0 returns None")
''',
   require=["try"], forbid=["if"], refs=["B.3"])

ex(id="kB-index", ch="B", lvl=1,
   title={"de": "Messwert sicher abrufen", "en": "Fetching a reading safely"},
   task={"de": "Schreiben Sie `get_reading(values, i, default=None)`, die `values[i]` zurückgibt. Gibt es den Index nicht (`IndexError`), wird `default` zurückgegeben. Prüfen Sie den Index **nicht** vorher mit `if`, sondern fangen Sie den Fehler ab.",
         "en": "Write `get_reading(values, i, default=None)` that returns `values[i]`. If the index doesn't exist (`IndexError`), return `default`. Do **not** check the index with `if` beforehand – catch the error instead."},
   starter={"de": "def get_reading(values, i, default=None):\n    ...\n", "en": "def get_reading(values, i, default=None):\n    ...\n"},
   solution='def get_reading(values, i, default=None):\n    try:\n        return values[i]\n    except IndexError:\n        return default\n\nprint(get_reading([1.2, 3.4], 1), get_reading([1.2, 3.4], 5, 0.0))\n',
   tests='''
ns, out = run()
v = [21.4, 23.9, 27.5]
check(call(ns, "get_reading", v, 0) == 21.4 and call(ns, "get_reading", v, -1) == 27.5, "Gültige Indizes (auch negative) liefern den Wert", "Valid indices (also negative) return the value")
check(call(ns, "get_reading", v, 3) is None and call(ns, "get_reading", v, -4) is None, "Ungültige Indizes liefern None", "Invalid indices return None")
check(call(ns, "get_reading", v, 10, default=-1.0) == -1.0 and call(ns, "get_reading", [], 0, 0) == 0, "default wird zurückgegeben", "default is returned")
''',
   require=["try"], forbid=["if"], refs=["B.3", "B.2"])

ex(id="kB-material", ch="B", lvl=2,
   title={"de": "Verständliche Fehlermeldung", "en": "A meaningful error message"},
   task={"de": "Schreiben Sie `mass(material, volume_cm3, table)`, die die Masse in g aus der Dichtetabelle `table` (Werkstoff → g/cm³) berechnet.\n- Ist der Werkstoff nicht in der Tabelle, entsteht ein `KeyError`. Fangen Sie ihn ab und lösen Sie stattdessen einen `ValueError` mit der Meldung `Unbekannter Werkstoff: <name>` aus.\n- Ist das Volumen negativ, lösen Sie ebenfalls einen `ValueError` aus.",
         "en": "Write `mass(material, volume_cm3, table)` that computes the mass in g from the density table `table` (material → g/cm³).\n- If the material isn't in the table, a `KeyError` occurs. Catch it and raise a `ValueError` with the message `Unknown material: <name>` instead.\n- If the volume is negative, also raise a `ValueError`."},
   starter={"de": "DENSITY = {'Stahl': 7.85, 'Aluminium': 2.70, 'Kupfer': 8.96, 'PA6': 1.14}\n\ndef mass(material, volume_cm3, table):\n    ...\n", "en": "DENSITY = {'Stahl': 7.85, 'Aluminium': 2.70, 'Kupfer': 8.96, 'PA6': 1.14}\n\ndef mass(material, volume_cm3, table):\n    ...\n"},
   solution="DENSITY = {'Stahl': 7.85, 'Aluminium': 2.70, 'Kupfer': 8.96, 'PA6': 1.14}\n\ndef mass(material, volume_cm3, table):\n    if volume_cm3 < 0:\n        raise ValueError(f\"Volumen darf nicht negativ sein: {volume_cm3}\")\n    try:\n        rho = table[material]\n    except KeyError:\n        raise ValueError(f\"Unbekannter Werkstoff: {material}\")\n    return rho * volume_cm3\n\nprint(mass('Kupfer', 10, DENSITY))\n",
   tests='''
ns, out = run()
D = {'Stahl': 7.85, 'Aluminium': 2.70, 'Kupfer': 8.96, 'PA6': 1.14}
f = ns.get("mass")
check(approx(call(ns, "mass", "Kupfer", 10, D), 89.6) and approx(call(ns, "mass", "PA6", 2.5, D), 2.85), "mass('Kupfer', 10) = 89.6 g, mass('PA6', 2.5) = 2.85 g", "mass('Kupfer', 10) = 89.6 g, mass('PA6', 2.5) = 2.85 g")
check(raises(ValueError, lambda: f("Titan", 1, D)), "Unbekannter Werkstoff → ValueError (kein KeyError)", "Unknown material → ValueError (not KeyError)")
msg = ""
try:
    f("Titan", 1, D)
except ValueError as e:
    msg = str(e)
except Exception:
    pass
check("Titan" in msg, "Die Fehlermeldung nennt den Werkstoff", "The error message names the material")
check(raises(ValueError, lambda: f("Stahl", -5, D)), "Negatives Volumen → ValueError", "Negative volume → ValueError")
check(approx(safe(lambda: f("Stahl", 0, D)), 0), "Volumen 0 ist erlaubt (Masse 0)", "Volume 0 is allowed (mass 0)")
''',
   require=["try", "raise"], refs=["B.4", "B.3"])

ex(id="kB-parse", ch="B", lvl=2,
   title={"de": "Messwerte robust einlesen", "en": "Parsing readings robustly"},
   task={"de": "Schreiben Sie `parse_all(texts)`, die eine Liste von Strings in Zahlen umwandelt. Ein Dezimalkomma ist erlaubt. Rückgabe: zwei Werte – die Liste der erfolgreich umgewandelten Zahlen und die Liste der **Indizes** der ungültigen Einträge. Fangen Sie nur `ValueError` ab und halten Sie den `try`-Block so klein wie möglich (Tipp: `else`-Zweig).",
         "en": "Write `parse_all(texts)` that converts a list of strings into numbers. A decimal comma is allowed. Return two values – the list of successfully converted numbers and the list of the **indices** of invalid entries. Only catch `ValueError` and keep the `try` block as small as possible (tip: `else` clause)."},
   starter={"de": "def parse_all(texts):\n    ...\n", "en": "def parse_all(texts):\n    ...\n"},
   solution='def parse_all(texts):\n    numbers = []\n    invalid = []\n    for i, t in enumerate(texts):\n        try:\n            x = float(t.replace(",", "."))\n        except ValueError:\n            invalid.append(i)\n        else:\n            numbers.append(x)\n    return numbers, invalid\n\nprint(parse_all(["21,4", "abc", "23.9", "", "1e3"]))\n',
   tests='''
ns, out = run()
cases = [(["21,4", "abc", "23.9", "", "1e3"], ([21.4, 23.9, 1000.0], [1, 3])), ([], ([], [])), (["1,2,3", "-0,5"], ([-0.5], [0]))]
for t, (en, ei) in cases:
    r = call(ns, "parse_all", t)
    check(isinstance(r, tuple) and len(r) == 2 and list(r[0]) == en and list(r[1]) == ei, f"parse_all({t}) = ({en}, {ei})", f"parse_all({t}) = ({en}, {ei})")
''',
   require=["try"], refs=["B.3", "B.3e"])

ex(id="kB-thermo", ch="B", lvl=3,
   title={"de": "Thermoelement mit Plausibilitätsprüfung", "en": "Thermocouple with plausibility check"},
   task={"de": "Klasse `Thermocouple(name, t_min=-200.0, t_max=1250.0)` mit dem Attribut `history` (leere Liste).\n- `add(t)`: löst `TypeError` aus, wenn `t` keine Zahl ist (Wahrheitswerte zählen nicht als Zahl), und `ValueError`, wenn `t` außerhalb von [t_min, t_max] liegt. Sonst wird `t` an `history` angehängt.\n- `load(values)`: ruft für jeden Wert `add` auf, fängt die beiden Fehlertypen ab und gibt die Anzahl der abgelehnten Werte zurück.\n- `mean()`: Mittelwert von `history`, `None` bei leerer Historie.",
         "en": "Class `Thermocouple(name, t_min=-200.0, t_max=1250.0)` with the attribute `history` (empty list).\n- `add(t)`: raises `TypeError` if `t` is not a number (booleans don't count as numbers), and `ValueError` if `t` lies outside [t_min, t_max]. Otherwise `t` is appended to `history`.\n- `load(values)`: calls `add` for every value, catches both error types and returns the number of rejected values.\n- `mean()`: mean of `history`, `None` for an empty history."},
   starter={"de": "class Thermocouple:\n    def __init__(self, name, t_min=-200.0, t_max=1250.0):\n        ...\n", "en": "class Thermocouple:\n    def __init__(self, name, t_min=-200.0, t_max=1250.0):\n        ...\n"},
   solution='class Thermocouple:\n    def __init__(self, name, t_min=-200.0, t_max=1250.0):\n        self.name = name\n        self.t_min = t_min\n        self.t_max = t_max\n        self.history = []\n\n    def add(self, t):\n        if isinstance(t, bool) or not isinstance(t, (int, float)):\n            raise TypeError(f"Zahl erwartet, nicht {t!r}")\n        if not self.t_min <= t <= self.t_max:\n            raise ValueError(f"{t} °C liegt außerhalb von [{self.t_min}, {self.t_max}]")\n        self.history.append(t)\n\n    def load(self, values):\n        rejected = 0\n        for v in values:\n            try:\n                self.add(v)\n            except (TypeError, ValueError):\n                rejected += 1\n        return rejected\n\n    def mean(self):\n        if len(self.history) == 0:\n            return None\n        return sum(self.history) / len(self.history)\n\ntc = Thermocouple("TC1")\nprint(tc.load([20.5, "x", 1500, 22.0, True]), tc.mean())\n',
   tests='''
ns, out = run()
tc = call(ns, "Thermocouple", "TC1")
check(getattr(tc, "history", None) == [] and method(tc, "mean") is None, "Neues Objekt: leere history, mean() = None", "New object: empty history, mean() = None")
method(tc, "add", 20.5)
check(tc.history == [20.5], "add(20.5) speichert den Wert", "add(20.5) stores the value")
check(raises(ValueError, lambda: tc.add(1300)) and raises(ValueError, lambda: tc.add(-250)), "Werte außerhalb des Bereichs → ValueError", "Values out of range → ValueError")
check(raises(TypeError, lambda: tc.add("25")) and raises(TypeError, lambda: tc.add(True)), "String oder bool → TypeError", "string or bool → TypeError")
r = method(tc, "load", [22.0, "x", 1500, 23.5, None, 1250])
check(r == 3 and tc.history == [20.5, 22.0, 23.5, 1250], "load() lehnt 3 Werte ab und übernimmt die gültigen", "load() rejects 3 values and keeps the valid ones")
check(approx(method(tc, "mean"), (20.5 + 22.0 + 23.5 + 1250) / 4), "mean() stimmt", "mean() is correct")
small = call(ns, "Thermocouple", "PT", t_min=0, t_max=100)
check(method(small, "load", [-1, 50, 101]) == 2, "Eigene Grenzen t_min/t_max werden beachtet", "Custom limits t_min/t_max are respected")
''',
   require=["try", "raise", "class"], refs=["B.4", "B.3", "10.3"])

ex(id="kB-config", ch="B", lvl=3,
   title={"de": "Konfigurationsdatei laden", "en": "Loading a configuration file"},
   task={"de": "Schreiben Sie `load_config(path)`, die eine Datei mit Zeilen `schlüssel = wert` einliest und ein Dictionary zurückgibt.\n- Leerzeilen und Kommentare (`#` am Zeilenanfang) werden übersprungen; Schlüssel und Wert werden mit `strip()` bereinigt.\n- Werte, die sich in `float` umwandeln lassen, werden als Zahl gespeichert, alle anderen als String.\n- Existiert die Datei nicht, wird ein leeres Dictionary zurückgegeben.\n- Eine Zeile ohne `=` löst einen `ValueError` aus, der die Zeilennummer nennt (`Zeile 3: …`, gezählt ab 1). Tipp: `split(\"=\", 1)` teilt nur am ersten `=`.",
         "en": "Write `load_config(path)` that reads a file with lines `key = value` and returns a dictionary.\n- Blank lines and comments (`#` at the start of a line) are skipped; key and value are cleaned with `strip()`.\n- Values that can be converted to `float` are stored as numbers, all others as strings.\n- If the file doesn't exist, return an empty dictionary.\n- A line without `=` raises a `ValueError` naming the line number (`line 3: …`, counted from 1). Tip: `split(\"=\", 1)` splits at the first `=` only."},
   starter={"de": "def load_config(path):\n    ...\n", "en": "def load_config(path):\n    ...\n"},
   solution='def load_config(path):\n    config = {}\n    try:\n        with open(path, encoding="utf-8") as f:\n            text = f.read()\n    except FileNotFoundError:\n        return {}\n    for nr, line in enumerate(text.split("\\n"), start=1):\n        line = line.strip()\n        if line == "" or line.startswith("#"):\n            continue\n        if "=" not in line:\n            raise ValueError(f"Zeile {nr}: kein \'=\' gefunden")\n        key, value = line.split("=", 1)\n        key = key.strip()\n        value = value.strip()\n        try:\n            config[key] = float(value)\n        except ValueError:\n            config[key] = value\n    return config\n\nprint(load_config("data/anlage.cfg"))\n',
   tests='''
CFG = "# Anlage 3\\nname = Pumpe P-301\\n\\nmax_druck = 6.5\\ndrehzahl=1450\\nmodus = auto\\nformel = P=U*I\\n"
ns, out = run(files={"data/anlage.cfg": CFG})
f = ns.get("load_config")
if f is None:
    raise TestFailure("Es gibt keine Funktion load_config. / There is no function load_config.")
r = call(ns, "load_config", "data/anlage.cfg")
check(r == {"name": "Pumpe P-301", "max_druck": 6.5, "drehzahl": 1450.0, "modus": "auto", "formel": "P=U*I"}, "Datei wird korrekt in ein Dictionary übersetzt (Zahlen als float)", "File is correctly turned into a dictionary (numbers as float)")
check(call(ns, "load_config", "data/gibtsnicht.cfg") == {}, "Fehlende Datei → leeres Dictionary", "Missing file → empty dictionary")
with open("data/kaputt.cfg", "w", encoding="utf-8") as fh:
    fh.write("a = 1\\n# ok\\nb 2\\n")
msg = ""
try:
    f("data/kaputt.cfg")
except ValueError as e:
    msg = str(e)
except Exception as e:
    msg = "anderer Fehler: " + type(e).__name__
check(("3" in msg) and not msg.startswith("anderer"), "Zeile ohne '=' → ValueError mit Zeilennummer 3", "Line without '=' → ValueError with line number 3")
''',
   require=["try", "raise", "with"], refs=["B.4", "B.3", "A.3"],
   files={"data/anlage.cfg": "# Anlage 3\nname = Pumpe P-301\n\nmax_druck = 6.5\ndrehzahl=1450\nmodus = auto\n"})
