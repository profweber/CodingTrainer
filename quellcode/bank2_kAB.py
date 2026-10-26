from exlib import ex

# Anhang A und B, zweiter Satz.
# A: open/with, read/write/readline, Zeilen iterieren, strip/split/startswith, pathlib, csv (DictReader, writer).
# B: try/except (mehrere Typen, as e), else/finally, raise.

# ------------------------------------------------------------------ Anhang A, Stufe 1
ex(id="kA-comments", ch="A", lvl=1,
   title={"de": "Kommentarzeilen zählen", "en": "Counting comment lines"},
   task={"de": "Ein Datenlogger schreibt in `data/logger.txt` Kommentarzeilen (beginnen mit `#`), Leerzeilen und Messzeilen. Lesen Sie die Datei mit `with` und einer `for`-Schleife zeilenweise ein und zählen Sie\n- `n_comments`: Kommentarzeilen\n- `n_empty`: Leerzeilen (nach `strip()` leer)\n- `n_data`: alle übrigen Zeilen\n\nSammeln Sie außerdem die Kommentarzeilen ohne das führende `#` und ohne Leerzeichen am Rand in der Liste `comments` (Tipp: Slicing ab Index 1, dann `strip()`).",
         "en": "A data logger writes comment lines (starting with `#`), blank lines and data lines to `data/logger.txt`. Read the file line by line with `with` and a `for` loop and count\n- `n_comments`: comment lines\n- `n_empty`: blank lines (empty after `strip()`)\n- `n_data`: all other lines\n\nAlso collect the comment lines without the leading `#` and without spaces at the edges in the list `comments` (tip: slicing from index 1, then `strip()`)."},
   starter={"de": "n_comments = 0\nn_empty = 0\nn_data = 0\ncomments = []\n\n# Ihr Code:\n", "en": "n_comments = 0\nn_empty = 0\nn_data = 0\ncomments = []\n\n# your code:\n"},
   solution='n_comments = 0\nn_empty = 0\nn_data = 0\ncomments = []\nwith open("data/logger.txt", encoding="utf-8") as f:\n    for line in f:\n        line = line.strip()\n        if line == "":\n            n_empty += 1\n        elif line.startswith("#"):\n            n_comments += 1\n            comments.append(line[1:].strip())\n        else:\n            n_data += 1\nprint(n_comments, n_empty, n_data, comments)\n',
   tests='''
F1 = "# Logger L-07\\n# Intervall 10 s\\n\\n12.4\\n12.6\\n\\n#Ende\\n12.9\\n"
F2 = "1\\n2\\n3\\n"
for content in [F1, F2]:
    lines = [l.strip() for l in content.split("\\n")[:-1]]
    ec = [l[1:].strip() for l in lines if l.startswith("#")]
    ns, out = run(files={"data/logger.txt": content})
    a, b, c, cm = need(ns, "n_comments", "n_empty", "n_data", "comments")
    check(a == len(ec) and b == lines.count("") and c == len(lines) - len(ec) - lines.count(""), f"{len(ec)} Kommentare, {lines.count('')} Leerzeilen, {len(lines) - len(ec) - lines.count('')} Messzeilen", f"{len(ec)} comments, {lines.count('')} blank lines, {len(lines) - len(ec) - lines.count('')} data lines")
    check(cm == ec, f"comments = {ec}", f"comments = {ec}")
''',
   require=["with", "file_methods"], refs=["A.3"],
   files={"data/logger.txt": "# Logger L-07\n# Intervall 10 s\n\n12.4\n12.6\n\n#Ende\n12.9\n"})

ex(id="kA-header", ch="A", lvl=1,
   title={"de": "Kopfzeile einer CSV-Datei", "en": "Header line of a CSV file"},
   task={"de": "Bevor eine große Messdatei verarbeitet wird, soll nur ihre Kopfzeile geprüft werden. Öffnen Sie `data/messung.csv` und lesen Sie mit `readline()` **nur die erste Zeile**. Bestimmen Sie\n- `header`: die erste Zeile ohne Zeilenumbruch (`strip()`)\n- `columns`: die Liste der Spaltennamen in der Reihenfolge der Datei (`split(\",\")`)\n- `n_columns`: die Anzahl der Spalten\n- `has_time`: ob es eine Spalte `zeit_s` gibt\n- `second_line`: die zweite Zeile (ein weiteres `readline()`, ebenfalls mit `strip()`)",
         "en": "Before a large measurement file is processed, only its header line is to be checked. Open `data/messung.csv` and read **only the first line** with `readline()`. Determine\n- `header`: the first line without the line break (`strip()`)\n- `columns`: the list of column names in the order of the file (`split(\",\")`)\n- `n_columns`: the number of columns\n- `has_time`: whether there is a column `zeit_s`\n- `second_line`: the second line (another `readline()`, also with `strip()`)"},
   starter={"de": "# Ihr Code:\n", "en": "# your code:\n"},
   solution='with open("data/messung.csv", encoding="utf-8") as f:\n    header = f.readline().strip()\n    second_line = f.readline().strip()\ncolumns = header.split(",")\nn_columns = len(columns)\nhas_time = "zeit_s" in columns\nprint(columns, n_columns, has_time, second_line)\n',
   tests='''
for content in ["zeit_s,drehzahl_rpm,drehmoment_Nm\\n0,1467,33.8\\n2,1461,35.4\\n", "t,U,I,P\\n1,2,3,4\\n", "zeit_s\\n5\\n"]:
    lines = content.split("\\n")
    ns, out = run(files={"data/messung.csv": content})
    h, c, n, ht, sl = need(ns, "header", "columns", "n_columns", "has_time", "second_line")
    check(h == lines[0] and c == lines[0].split(","), f"header = {lines[0]!r}", f"header = {lines[0]!r}")
    check(n == len(lines[0].split(",")) and ht is ("zeit_s" in lines[0].split(",")), f"n_columns = {len(lines[0].split(','))}, has_time = {'zeit_s' in lines[0].split(',')}", f"n_columns = {len(lines[0].split(','))}, has_time = {'zeit_s' in lines[0].split(',')}")
    check(sl == lines[1], f"second_line = {lines[1]!r}", f"second_line = {lines[1]!r}")
check("readline" in SOURCE, "Mit readline() gelesen", "Read with readline()")
''',
   require=["with", "file_methods"], refs=["A.4", "A.3"],
   files={"data/messung.csv": "zeit_s,drehzahl_rpm,drehmoment_Nm\n0,1467,33.8\n2,1461,35.4\n"})

ex(id="kA-units", ch="A", lvl=1,
   title={"de": "Temperaturtabelle mit Einheiten schreiben", "en": "Writing a temperature table with units"},
   task={"de": "Schreiben Sie die Temperaturen eines Ofens in die Datei `data/ofen.txt`. Verwenden Sie `with` und unbedingt `encoding=\"utf-8\"` (wegen des Zeichens `°`).\n- Erste Zeile: `Ofen 2 – Aufheizkurve`\n- Danach eine Zeile pro Messwert in der Reihenfolge der Messung im Format `t = 5 min: 312.5 °C` (Temperatur mit einer Nachkommastelle)\n- Letzte Zeile: `Maximum: 650.0 °C`\n\nDie Zeiten stehen in `times_min`, die Temperaturen in `temps_C`. Denken Sie daran: `write()` fügt keinen Zeilenumbruch hinzu.",
         "en": "Write the temperatures of a furnace to the file `data/ofen.txt`. Use `with` and definitely `encoding=\"utf-8\"` (because of the character `°`).\n- First line: `Ofen 2 – Aufheizkurve`\n- Then one line per reading in the order of the measurement, in the format `t = 5 min: 312.5 °C` (temperature with one decimal)\n- Last line: `Maximum: 650.0 °C`\n\nThe times are in `times_min`, the temperatures in `temps_C`. Remember: `write()` doesn't add a line break."},
   starter={"de": "times_min = [0, 5, 10, 15]\ntemps_C = [22.0, 312.5, 548.25, 650.0]\n\n# Ihr Code:\n", "en": "times_min = [0, 5, 10, 15]\ntemps_C = [22.0, 312.5, 548.25, 650.0]\n\n# your code:\n"},
   solution='times_min = [0, 5, 10, 15]\ntemps_C = [22.0, 312.5, 548.25, 650.0]\nwith open("data/ofen.txt", "w", encoding="utf-8") as f:\n    f.write("Ofen 2 – Aufheizkurve\\n")\n    for t, temp in zip(times_min, temps_C):\n        f.write(f"t = {t} min: {temp:.1f} °C\\n")\n    f.write(f"Maximum: {max(temps_C):.1f} °C\\n")\n',
   tests='''
for ti, te in [([0, 5, 10, 15], [22.0, 312.5, 548.25, 650.0]), ([1, 2], [100.04, 99.95])]:
    ns, out = run(sub={"times_min": ti, "temps_C": te})
    try:
        lines = [l for l in read_file("data/ofen.txt").split("\\n") if l.strip()]
    except FileNotFoundError:
        raise TestFailure("Die Datei data/ofen.txt wurde nicht angelegt. / The file data/ofen.txt was not created.")
    check(lines[0].strip() == "Ofen 2 – Aufheizkurve", "Kopfzeile stimmt", "Header line is correct")
    check([l.strip() for l in lines[1:-1]] == [f"t = {t} min: {x:.1f} °C" for t, x in zip(ti, te)], f"Eine Zeile pro Messwert für {ti}", f"One line per reading for {ti}")
    check(lines[-1].strip() == f"Maximum: {max(te):.1f} °C", f"Letzte Zeile 'Maximum: {max(te):.1f} °C'", f"Last line 'Maximum: {max(te):.1f} °C'")
''',
   require=["with", "open"], refs=["A.2"])

# ------------------------------------------------------------------ Anhang A, Stufe 2
ex(id="kA-filter", ch="A", lvl=2,
   title={"de": "Ausschuss aus dem Prüfprotokoll filtern", "en": "Filtering rejects from the test log"},
   task={"de": "Die Datei `data/pruefung.csv` enthält die Spalten `teil`, `mass_mm`, `status` (`OK` oder `NIO`). Lesen Sie sie mit `csv.DictReader` und schreiben Sie alle `NIO`-Zeilen mit `csv.writer` in die neue Datei `data/nio.csv` – mit derselben Kopfzeile `teil,mass_mm,status`. Speichern Sie außerdem\n- `n_total`: Anzahl aller Datensätze\n- `nio_parts`: Liste der Teilenummern aller NIO-Teile\n- `nio_rate`: den NIO-Anteil in Prozent (eine Nachkommastelle)\n\nCSV-Dateien öffnen Sie immer mit `newline=\"\"`.",
         "en": "The file `data/pruefung.csv` contains the columns `teil` (part), `mass_mm` (dimension), `status` (`OK` or `NIO` = not OK). Read it with `csv.DictReader` and write all `NIO` rows with `csv.writer` into the new file `data/nio.csv` – with the same header `teil,mass_mm,status`. Also store\n- `n_total`: number of all records\n- `nio_parts`: list of the part numbers of all NIO parts\n- `nio_rate`: the NIO share in percent (one decimal)\n\nAlways open CSV files with `newline=\"\"`."},
   starter={"de": "import csv\n\nn_total = 0\nnio_parts = []\n\n# Ihr Code:\n", "en": "import csv\n\nn_total = 0\nnio_parts = []\n\n# your code:\n"},
   solution='import csv\n\nn_total = 0\nnio_parts = []\nrows = []\nwith open("data/pruefung.csv", encoding="utf-8", newline="") as f:\n    for row in csv.DictReader(f):\n        n_total += 1\n        if row["status"] == "NIO":\n            nio_parts.append(row["teil"])\n            rows.append([row["teil"], row["mass_mm"], row["status"]])\nwith open("data/nio.csv", "w", encoding="utf-8", newline="") as f:\n    writer = csv.writer(f)\n    writer.writerow(["teil", "mass_mm", "status"])\n    for r in rows:\n        writer.writerow(r)\nnio_rate = round(len(nio_parts) / n_total * 100, 1)\nprint(n_total, nio_parts, nio_rate)\n',
   tests='''
import csv as _csv, io as _io
F1 = "teil,mass_mm,status\\nW-001,25.01,OK\\nW-002,25.09,NIO\\nW-003,24.99,OK\\nW-004,24.90,NIO\\nW-005,25.00,OK\\n"
F2 = "teil,mass_mm,status\\nA,1.0,OK\\n"
for content in [F1, F2]:
    rows = [l.split(",") for l in content.strip().split("\\n")[1:]]
    nio = [r for r in rows if r[2] == "NIO"]
    ns, out = run(files={"data/pruefung.csv": content})
    n, p, rate = need(ns, "n_total", "nio_parts", "nio_rate")
    check(n == len(rows) and isinstance(p, list) and sorted(p) == sorted(r[0] for r in nio), f"n_total = {len(rows)}, nio_parts = {[r[0] for r in nio]}", f"n_total = {len(rows)}, nio_parts = {[r[0] for r in nio]}")
    check(approx(rate, round(len(nio) / len(rows) * 100, 1)), f"nio_rate = {round(len(nio) / len(rows) * 100, 1)} %", f"nio_rate = {round(len(nio) / len(rows) * 100, 1)} %")
    try:
        written = list(_csv.reader(_io.StringIO(read_file("data/nio.csv"))))
    except FileNotFoundError:
        written = []
    check(written[:1] == [["teil", "mass_mm", "status"]] and sorted(written[1:]) == sorted(nio), f"nio.csv enthält Kopfzeile und {len(nio)} NIO-Zeile(n)", f"nio.csv contains the header and {len(nio)} NIO row(s)")
''',
   require=["csv", "with"], refs=["A.4"],
   files={"data/pruefung.csv": "teil,mass_mm,status\nW-001,25.01,OK\nW-002,25.09,NIO\nW-003,24.99,OK\nW-004,24.90,NIO\nW-005,25.00,OK\n"})

ex(id="kA-mergefiles", ch="A", lvl=2,
   title={"de": "Zwei Logdateien zusammenführen", "en": "Merging two log files"},
   task={"de": "Zwei Steuerungen schreiben je eine Logdatei: `data/sps1.log` und `data/sps2.log`. Jede Zeile beginnt mit einer Uhrzeit im Format `HH:MM:SS`, gefolgt von einem Leerzeichen und der Meldung; die Zeilen jeder Datei sind zeitlich sortiert.\n- Lesen Sie beide Dateien ein (Leerzeilen überspringen) und versehen Sie jede Meldung mit ihrer Quelle: `08:00:05 [SPS1] Start`.\n- `merged`: alle Zeilen beider Dateien zeitlich sortiert (Strings dieses Formats lassen sich mit `sorted()` richtig nach der Uhrzeit sortieren – warum?)\n- Schreiben Sie `merged` zeilenweise in `data/gesamt.log`.\n- `n_lines`: Anzahl der Zeilen in der Gesamtdatei\n\nTipp: `line.split(\" \", 1)` trennt die Uhrzeit von der Meldung.",
         "en": "Two controllers each write a log file: `data/sps1.log` and `data/sps2.log`. Every line starts with a time in the format `HH:MM:SS`, followed by a space and the message; the lines of each file are sorted by time.\n- Read both files (skip blank lines) and tag every message with its source: `08:00:05 [SPS1] Start`.\n- `merged`: all lines of both files sorted by time (strings in this format sort correctly by time with `sorted()` – why?)\n- Write `merged` line by line to `data/gesamt.log`.\n- `n_lines`: number of lines in the combined file\n\nTip: `line.split(\" \", 1)` separates the time from the message."},
   starter={"de": "merged = []\n\n# Ihr Code:\n", "en": "merged = []\n\n# your code:\n"},
   solution='merged = []\nlines = []\nfor name, tag in [("data/sps1.log", "SPS1"), ("data/sps2.log", "SPS2")]:\n    with open(name, encoding="utf-8") as f:\n        for line in f:\n            line = line.strip()\n            if line == "":\n                continue\n            time, message = line.split(" ", 1)\n            lines.append(f"{time} [{tag}] {message}")\nmerged = sorted(lines)\nwith open("data/gesamt.log", "w", encoding="utf-8") as f:\n    for line in merged:\n        f.write(line + "\\n")\nn_lines = len(merged)\nprint(merged, n_lines)\n',
   tests='''
A1 = "08:00:05 Start\\n08:12:40 Druck ok\\n\\n09:30:00 Stopp\\n"
B1 = "07:59:58 Netz ein\\n08:12:41 Ventil auf\\n"
for a, b in [(A1, B1), ("10:00:00 x y z\\n", "")]:
    exp = sorted([f"{l.split(' ', 1)[0]} [SPS1] {l.split(' ', 1)[1]}" for l in a.split("\\n") if l.strip()] + [f"{l.split(' ', 1)[0]} [SPS2] {l.split(' ', 1)[1]}" for l in b.split("\\n") if l.strip()])
    ns, out = run(files={"data/sps1.log": a, "data/sps2.log": b})
    m, n = need(ns, "merged", "n_lines")
    check(m == exp and n == len(exp), f"merged = {exp}", f"merged = {exp}")
    try:
        written = [l for l in read_file("data/gesamt.log").split("\\n") if l.strip()]
    except FileNotFoundError:
        written = None
    check(written == exp, "gesamt.log enthält alle Zeilen in zeitlicher Reihenfolge", "gesamt.log contains all lines in chronological order")
''',
   require=["with", "file_methods"], refs=["A.3", "A.2", "8.1s"],
   files={"data/sps1.log": "08:00:05 Start\n08:12:40 Druck ok\n\n09:30:00 Stopp\n", "data/sps2.log": "07:59:58 Netz ein\n08:12:41 Ventil auf\n"})

ex(id="kA-report", ch="A", lvl=2,
   title={"de": "Auswertebericht schreiben", "en": "Writing an evaluation report"},
   task={"de": "Die Datei `data/drehmoment.txt` enthält eine Kopfzeile und danach pro Zeile ein gemessenes Anzugsdrehmoment in Nm (Dezimalpunkt). Lesen Sie die Werte als `float` in die Liste `values` ein. Schreiben Sie dann mit `pathlib` (`Path(\"data\") / \"bericht.txt\"` und `write_text`) einen Bericht mit genau diesen vier Zeilen:\n\n  Anzahl: 6\n  Mittelwert: 24.95 Nm\n  Minimum: 24.10 Nm\n  Maximum: 25.80 Nm\n\n(Werte mit zwei Nachkommastellen). Speichern Sie den Pfad des Berichts in `report` und den Mittelwert in `mean`.",
         "en": "The file `data/drehmoment.txt` contains a header line followed by one measured tightening torque in Nm per line (decimal point). Read the values as `float` into the list `values`. Then use `pathlib` (`Path(\"data\") / \"bericht.txt\"` and `write_text`) to write a report with exactly these four lines:\n\n  Anzahl: 6\n  Mittelwert: 24.95 Nm\n  Minimum: 24.10 Nm\n  Maximum: 25.80 Nm\n\n(values with two decimals; keep the German labels). Store the path of the report in `report` and the mean in `mean`."},
   starter={"de": "from pathlib import Path\n\nvalues = []\n\n# Ihr Code:\n", "en": "from pathlib import Path\n\nvalues = []\n\n# your code:\n"},
   solution='from pathlib import Path\n\nvalues = []\nwith open("data/drehmoment.txt", encoding="utf-8") as f:\n    f.readline()\n    for line in f:\n        line = line.strip()\n        if line != "":\n            values.append(float(line))\nmean = sum(values) / len(values)\nreport = Path("data") / "bericht.txt"\ntext = f"Anzahl: {len(values)}\\nMittelwert: {mean:.2f} Nm\\nMinimum: {min(values):.2f} Nm\\nMaximum: {max(values):.2f} Nm\\n"\nreport.write_text(text, encoding="utf-8")\nprint(text)\n',
   tests='''
for content in ["Anzugsdrehmoment [Nm]\\n24.9\\n25.8\\n24.1\\n25.0\\n24.6\\n25.3\\n", "M\\n10.0\\n12.5\\n\\n"]:
    vals = [float(l) for l in content.split("\\n")[1:] if l.strip()]
    ns, out = run(files={"data/drehmoment.txt": content})
    v, m, r = need(ns, "values", "mean", "report")
    check(v == vals and approx(m, sum(vals) / len(vals)), f"values = {vals}, Mittelwert {sum(vals) / len(vals):.3f}", f"values = {vals}, mean {sum(vals) / len(vals):.3f}")
    exp = [f"Anzahl: {len(vals)}", f"Mittelwert: {sum(vals) / len(vals):.2f} Nm", f"Minimum: {min(vals):.2f} Nm", f"Maximum: {max(vals):.2f} Nm"]
    try:
        lines = [l.strip() for l in read_file("data/bericht.txt").split("\\n") if l.strip()]
    except FileNotFoundError:
        lines = []
    check(lines == exp, f"bericht.txt = {exp}", f"bericht.txt = {exp}")
    check(type(r).__name__.endswith("Path"), "report ist ein Path-Objekt", "report is a Path object")
''',
   require=["with", "pathlib"], refs=["A.1", "A.3"],
   files={"data/drehmoment.txt": "Anzugsdrehmoment [Nm]\n24.9\n25.8\n24.1\n25.0\n24.6\n25.3\n"})

# ------------------------------------------------------------------ Anhang A, Stufe 3
ex(id="kA-shifts", ch="A", lvl=3,
   title={"de": "Schichtbericht aus Produktionsdaten", "en": "Shift report from production data"},
   task={"de": "Die Datei `data/produktion.csv` enthält pro Zeile einen Produktionsauftrag mit den Spalten `maschine`, `schicht`, `gut`, `ausschuss`. Lesen Sie sie mit `csv.DictReader` ein und berechnen Sie\n- `totals`: Dictionary Maschine → Liste `[gut, ausschuss]` (aufsummiert über alle Aufträge)\n- `scrap_rate`: Dictionary Maschine → Ausschussquote in Prozent (Ausschuss / (gut + Ausschuss) · 100, auf zwei Stellen gerundet)\n- `worst`: die Maschine mit der höchsten Ausschussquote\n\nSchreiben Sie anschließend mit `csv.writer` die Datei `data/schichtbericht.csv` mit der Kopfzeile `maschine,gut,ausschuss,quote_prozent` und einer Zeile pro Maschine, **alphabetisch sortiert** nach Maschine.",
         "en": "The file `data/produktion.csv` contains one production order per line with the columns `maschine` (machine), `schicht` (shift), `gut` (good), `ausschuss` (scrap). Read it with `csv.DictReader` and compute\n- `totals`: dictionary machine → list `[good, scrap]` (summed over all orders)\n- `scrap_rate`: dictionary machine → scrap rate in percent (scrap / (good + scrap) · 100, rounded to two decimals)\n- `worst`: the machine with the highest scrap rate\n\nThen use `csv.writer` to write the file `data/schichtbericht.csv` with the header `maschine,gut,ausschuss,quote_prozent` and one row per machine, **sorted alphabetically** by machine."},
   starter={"de": "import csv\n\ntotals = {}\n\n# Ihr Code:\n", "en": "import csv\n\ntotals = {}\n\n# your code:\n"},
   solution='import csv\n\ntotals = {}\nwith open("data/produktion.csv", encoding="utf-8", newline="") as f:\n    for row in csv.DictReader(f):\n        m = row["maschine"]\n        if m not in totals:\n            totals[m] = [0, 0]\n        totals[m][0] += int(row["gut"])\n        totals[m][1] += int(row["ausschuss"])\nscrap_rate = {m: round(s / (g + s) * 100, 2) for m, (g, s) in totals.items()}\nworst = None\nfor m in sorted(scrap_rate):\n    if worst is None or scrap_rate[m] > scrap_rate[worst]:\n        worst = m\nwith open("data/schichtbericht.csv", "w", encoding="utf-8", newline="") as f:\n    writer = csv.writer(f)\n    writer.writerow(["maschine", "gut", "ausschuss", "quote_prozent"])\n    for m in sorted(totals):\n        writer.writerow([m, totals[m][0], totals[m][1], scrap_rate[m]])\nprint(totals, scrap_rate, worst)\n',
   tests='''
import csv as _csv, io as _io
F1 = "maschine,schicht,gut,ausschuss\\nSpritzguss 2,Früh,480,12\\nSpritzguss 1,Früh,510,4\\nSpritzguss 2,Spät,455,20\\nSpritzguss 1,Spät,498,9\\nStanze,Früh,1200,6\\n"
F2 = "maschine,schicht,gut,ausschuss\\nB,1,9,1\\nA,1,1,1\\n"
for content in [F1, F2]:
    rows = list(_csv.DictReader(_io.StringIO(content)))
    et = {}
    for r in rows:
        et.setdefault(r["maschine"], [0, 0]); et[r["maschine"]][0] += int(r["gut"]); et[r["maschine"]][1] += int(r["ausschuss"])
    er = {m: round(s / (g + s) * 100, 2) for m, (g, s) in et.items()}
    ns, out = run(files={"data/produktion.csv": content})
    t, sr, w = need(ns, "totals", "scrap_rate", "worst")
    check(t == et, f"totals = {et}", f"totals = {et}")
    check(isinstance(sr, dict) and set(sr) == set(er) and all(approx(sr[k], er[k]) for k in er) and w == max(sorted(er), key=lambda k: er[k]), f"scrap_rate = {er}, worst = {max(sorted(er), key=lambda k: er[k])!r}", f"scrap_rate = {er}, worst = {max(sorted(er), key=lambda k: er[k])!r}")
    try:
        written = list(_csv.reader(_io.StringIO(read_file("data/schichtbericht.csv"))))
    except FileNotFoundError:
        written = []
    exp = [["maschine", "gut", "ausschuss", "quote_prozent"]] + [[m, str(et[m][0]), str(et[m][1]), str(er[m])] for m in sorted(et)]
    check(written == exp, "schichtbericht.csv: Kopfzeile und eine Zeile pro Maschine, alphabetisch", "schichtbericht.csv: header and one row per machine, alphabetical")
''',
   require=["csv", "with", "dict"], refs=["A.4", "8.3"],
   files={"data/produktion.csv": "maschine,schicht,gut,ausschuss\nSpritzguss 2,Früh,480,12\nSpritzguss 1,Früh,510,4\nSpritzguss 2,Spät,455,20\nSpritzguss 1,Spät,498,9\nStanze,Früh,1200,6\n"})

ex(id="kA-blocks", ch="A", lvl=3,
   title={"de": "Messdatei mit mehreren Blöcken", "en": "Measurement file with several blocks"},
   task={"de": "Ein Messgerät schreibt die Werte mehrerer Kanäle in **eine** Datei `data/kanaele.txt`. Jeder Block beginnt mit einer Zeile `[Kanal-Name]`, danach folgen die Messwerte des Kanals, eine Zahl pro Zeile. Leerzeilen und Zeilen, die mit `#` beginnen, werden ignoriert.\n- `channels`: Dictionary Kanalname (ohne Klammern) → Liste der Messwerte als `float` (in der Reihenfolge der Datei)\n- `means`: Dictionary Kanalname → Mittelwert (auf drei Stellen gerundet); Kanäle ohne Werte bekommen `None`\n- Schreiben Sie eine Zusammenfassung nach `data/zusammenfassung.txt`: pro Kanal eine Zeile `Kanalname;Anzahl;Mittelwert` in der Reihenfolge der Datei (bei fehlendem Mittelwert steht dort `-`).\n\nTipp: Merken Sie sich in einer Variable, zu welchem Kanal die aktuelle Zeile gehört.",
         "en": "A measuring device writes the values of several channels into **one** file `data/kanaele.txt`. Each block starts with a line `[channel name]`, followed by the readings of that channel, one number per line. Blank lines and lines starting with `#` are ignored.\n- `channels`: dictionary channel name (without brackets) → list of readings as `float` (in the order of the file)\n- `means`: dictionary channel name → mean (rounded to three decimals); channels without values get `None`\n- Write a summary to `data/zusammenfassung.txt`: one line per channel `channelname;count;mean` in the order of the file (if the mean is missing, write `-`).\n\nTip: keep a variable that remembers which channel the current line belongs to."},
   starter={"de": "channels = {}\n\n# Ihr Code:\n", "en": "channels = {}\n\n# your code:\n"},
   solution='channels = {}\ncurrent = None\nwith open("data/kanaele.txt", encoding="utf-8") as f:\n    for line in f:\n        line = line.strip()\n        if line == "" or line.startswith("#"):\n            continue\n        if line.startswith("["):\n            current = line[1:-1]\n            channels[current] = []\n        else:\n            channels[current].append(float(line))\nmeans = {name: round(sum(v) / len(v), 3) if len(v) > 0 else None for name, v in channels.items()}\nwith open("data/zusammenfassung.txt", "w", encoding="utf-8") as f:\n    for name, v in channels.items():\n        m = "-" if means[name] is None else means[name]\n        f.write(f"{name};{len(v)};{m}\\n")\nprint(channels, means)\n',
   tests='''
F1 = "# Messung 12\\n[U_L1]\\n230.1\\n229.8\\n\\n230.4\\n[I_L1]\\n# in A\\n4.21\\n4.35\\n[Reserve]\\n"
F2 = "[A]\\n1\\n[B]\\n2\\n3\\n"
for content in [F1, F2]:
    ec, cur = {}, None
    for l in content.split("\\n"):
        l = l.strip()
        if not l or l.startswith("#"): continue
        if l.startswith("["): cur = l[1:-1]; ec[cur] = []
        else: ec[cur].append(float(l))
    em = {k: (round(sum(v) / len(v), 3) if v else None) for k, v in ec.items()}
    ns, out = run(files={"data/kanaele.txt": content})
    c, m = need(ns, "channels", "means")
    check(c == ec, f"channels = {ec}", f"channels = {ec}")
    check(isinstance(m, dict) and set(m) == set(em) and all((m[k] is None) if em[k] is None else approx(m[k], em[k]) for k in em), f"means = {em}", f"means = {em}")
    exp = [f"{k};{len(v)};{'-' if em[k] is None else em[k]}" for k, v in ec.items()]
    try:
        written = [l.strip() for l in read_file("data/zusammenfassung.txt").split("\\n") if l.strip()]
    except FileNotFoundError:
        written = None
    check(written == exp, f"zusammenfassung.txt = {exp}", f"zusammenfassung.txt = {exp}")
''',
   require=["with", "file_methods", "dict"], refs=["A.3", "A.2", "8.3"],
   files={"data/kanaele.txt": "# Messung 12\n[U_L1]\n230.1\n229.8\n\n230.4\n[I_L1]\n# in A\n4.21\n4.35\n[Reserve]\n"})

ex(id="kA-rotate", ch="A", lvl=3,
   title={"de": "Logdatei begrenzen", "en": "Limiting a log file"},
   task={"de": "Auf einem Gerät mit wenig Speicher darf die Logdatei `data/geraet.log` höchstens `max_lines` Zeilen haben. Schreiben Sie das Programm, das neue Meldungen anhängt und die Datei danach kürzt:\n1. Hängen Sie alle Meldungen aus `new_messages` an die Datei an (Modus `\"a\"`, eine Meldung pro Zeile). Existiert die Datei noch nicht, wird sie dabei angelegt.\n2. Lesen Sie die Datei danach komplett ein (`read()` und `split(\"\\n\")`, Leerzeilen weglassen).\n3. Hat sie mehr als `max_lines` Zeilen, werden die **ältesten** Zeilen verworfen: Schreiben Sie nur die letzten `max_lines` Zeilen zurück (Modus `\"w\"`, Slicing).\n\nSpeichern Sie in `kept` die Liste der Zeilen, die danach in der Datei stehen (in der Reihenfolge der Datei), und in `dropped` die Anzahl der verworfenen Zeilen.",
         "en": "On a device with little memory, the log file `data/geraet.log` may have at most `max_lines` lines. Write the program that appends new messages and then shortens the file:\n1. Append all messages from `new_messages` to the file (mode `\"a\"`, one message per line). If the file doesn't exist yet, it is created in the process.\n2. Then read the whole file (`read()` and `split(\"\\n\")`, leave out blank lines).\n3. If it has more than `max_lines` lines, the **oldest** lines are discarded: write back only the last `max_lines` lines (mode `\"w\"`, slicing).\n\nStore in `kept` the list of lines that are in the file afterwards (in the order of the file), and in `dropped` the number of discarded lines."},
   starter={"de": "new_messages = ['10:05 Tür offen', '10:06 Tür zu', '10:30 Akku 20 %']\nmax_lines = 5\n\n# Ihr Code:\n", "en": "new_messages = ['10:05 Tür offen', '10:06 Tür zu', '10:30 Akku 20 %']\nmax_lines = 5\n\n# your code:\n"},
   solution='new_messages = [\'10:05 Tür offen\', \'10:06 Tür zu\', \'10:30 Akku 20 %\']\nmax_lines = 5\nwith open("data/geraet.log", "a", encoding="utf-8") as f:\n    for msg in new_messages:\n        f.write(msg + "\\n")\nwith open("data/geraet.log", encoding="utf-8") as f:\n    lines = [l for l in f.read().split("\\n") if l.strip() != ""]\ndropped = 0\nkept = lines\nif len(lines) > max_lines:\n    kept = lines[-max_lines:]\n    dropped = len(lines) - max_lines\n    with open("data/geraet.log", "w", encoding="utf-8") as f:\n        for line in kept:\n            f.write(line + "\\n")\nprint(kept, dropped)\n',
   tests='''
OLD = "09:00 Start\\n09:10 Messung ok\\n09:45 Wartung\\n"
for old, new, mx in [(OLD, ['10:05 Tür offen', '10:06 Tür zu', '10:30 Akku 20 %'], 5), (OLD, ['x'], 10), (None, ['a', 'b', 'c'], 2)]:
    files = {"data/geraet.log": old} if old is not None else {}
    ns, out = run(sub={"new_messages": new, "max_lines": mx}, files=files)
    k, d = need(ns, "kept", "dropped")
    allines = ([l for l in old.split("\\n") if l.strip()] if old else []) + new
    ek = allines[-mx:] if len(allines) > mx else allines
    check(k == ek and d == len(allines) - len(ek), f"kept = {ek}, dropped = {len(allines) - len(ek)}", f"kept = {ek}, dropped = {len(allines) - len(ek)}")
    written = [l for l in read_file("data/geraet.log").split("\\n") if l.strip()]
    check(written == ek, f"Datei enthält die {len(ek)} neuesten Zeilen", f"File contains the {len(ek)} newest lines")
''',
   require=["with", "slice"], refs=["A.2", "A.3", "8.1x"])

# ------------------------------------------------------------------ Anhang B, Stufe 1
ex(id="kB-fileorfallback", ch="B", lvl=1,
   title={"de": "Konfiguration mit Standardwert", "en": "Configuration with a default"},
   task={"de": "Eine Messsoftware liest beim Start die Abtastrate (Hz) aus der Datei, deren Pfad übergeben wird; die Datei enthält nur eine Zahl. Schreiben Sie `read_rate(path, default=100.0)`:\n- Existiert die Datei nicht (`FileNotFoundError`), wird `default` zurückgegeben.\n- Enthält sie keine gültige Zahl (`ValueError`), wird ebenfalls `default` zurückgegeben.\n- Sonst wird die Zahl als `float` zurückgegeben (Leerzeichen und Zeilenumbruch mit `strip()` entfernen).\n\nFangen Sie die beiden Fehlertypen gezielt ab – kein `except` ohne Fehlertyp!",
         "en": "At start-up, a measurement software reads the sampling rate (Hz) from the file whose path is passed in; the file contains only a number. Write `read_rate(path, default=100.0)`:\n- If the file doesn't exist (`FileNotFoundError`), `default` is returned.\n- If it doesn't contain a valid number (`ValueError`), `default` is returned as well.\n- Otherwise the number is returned as a `float` (remove spaces and the line break with `strip()`).\n\nCatch the two error types specifically – no `except` without an error type!"},
   starter={"de": "def read_rate(path, default=100.0):\n    ...\n", "en": "def read_rate(path, default=100.0):\n    ...\n"},
   solution='def read_rate(path, default=100.0):\n    try:\n        with open(path, encoding="utf-8") as f:\n            return float(f.read().strip())\n    except FileNotFoundError:\n        return default\n    except ValueError:\n        return default\n\nprint(read_rate("data/rate.txt"), read_rate("data/gibtsnicht.txt"))\n',
   tests='''
import ast as _ast
ns, out = run(files={"data/rate.txt": "250\\n", "data/kaputt.txt": "zweihundert\\n", "data/leer.txt": ""})
check(approx(call(ns, "read_rate", "data/rate.txt"), 250.0), "Gültige Datei → 250.0", "Valid file → 250.0")
check(call(ns, "read_rate", "data/gibtsnicht.txt") == 100.0 and call(ns, "read_rate", "data/gibtsnicht.txt", 50.0) == 50.0, "Fehlende Datei → Standardwert", "Missing file → default")
check(call(ns, "read_rate", "data/kaputt.txt") == 100.0 and call(ns, "read_rate", "data/leer.txt", default=1.0) == 1.0, "Ungültiger Inhalt → Standardwert", "Invalid content → default")
bare = any(isinstance(n, _ast.ExceptHandler) and n.type is None for n in _ast.walk(_ast.parse(SOURCE)))
check(not bare, "Kein except ohne Fehlertyp", "No except without an error type")
''',
   require=["try", "with"], refs=["B.3", "B.5", "A.3"])

ex(id="kB-classify", ch="B", lvl=1,
   title={"de": "Spannung einordnen mit raise", "en": "Classifying a voltage with raise"},
   task={"de": "Schreiben Sie `voltage_class(u)` für eine Spannung in Volt:\n- unter 50 V: `\"Kleinspannung\"`\n- 50 V bis 1000 V (einschließlich): `\"Niederspannung\"`\n- über 1000 V: `\"Hochspannung\"`\n\nLösen Sie einen `TypeError` aus, wenn `u` keine Zahl (`int` oder `float`) ist, und einen `ValueError`, wenn `u` negativ ist. Geben Sie beiden Fehlern eine Meldung, die den übergebenen Wert nennt.",
         "en": "Write `voltage_class(u)` for a voltage in volts:\n- below 50 V: `\"Kleinspannung\"` (extra-low voltage)\n- 50 V to 1000 V (inclusive): `\"Niederspannung\"` (low voltage)\n- above 1000 V: `\"Hochspannung\"` (high voltage)\n\nRaise a `TypeError` if `u` is not a number (`int` or `float`) and a `ValueError` if `u` is negative. Give both errors a message that names the value passed in. Keep the German return texts."},
   starter={"de": "def voltage_class(u):\n    ...\n", "en": "def voltage_class(u):\n    ...\n"},
   solution='def voltage_class(u):\n    if not isinstance(u, (int, float)):\n        raise TypeError(f"Zahl erwartet, nicht {u!r}")\n    if u < 0:\n        raise ValueError(f"Spannung darf nicht negativ sein: {u}")\n    if u < 50:\n        return "Kleinspannung"\n    elif u <= 1000:\n        return "Niederspannung"\n    return "Hochspannung"\n\nprint(voltage_class(24), voltage_class(400), voltage_class(20000))\n',
   tests='''
ns, out = run()
f = ns.get("voltage_class")
for u, e in [(24, "Kleinspannung"), (49.9, "Kleinspannung"), (50, "Niederspannung"), (1000, "Niederspannung"), (1000.1, "Hochspannung"), (0, "Kleinspannung")]:
    check(call(ns, "voltage_class", u) == e, f"voltage_class({u}) = {e!r}", f"voltage_class({u}) = {e!r}")
check(raises(ValueError, lambda: f(-5)), "Negative Spannung → ValueError", "Negative voltage → ValueError")
check(raises(TypeError, lambda: f("230")) and raises(TypeError, lambda: f(None)), "Text oder None → TypeError", "Text or None → TypeError")
msg = ""
try:
    f(-7.5)
except ValueError as e:
    msg = str(e)
except Exception:
    pass
check("-7.5" in msg, "Die Fehlermeldung nennt den Wert", "The error message names the value")
''',
   require=["raise", "isinstance"], refs=["B.4", "7.4"])

ex(id="kB-convert", ch="B", lvl=1,
   title={"de": "Mehrere Fehlertypen unterscheiden", "en": "Telling error types apart"},
   task={"de": "Aus einer Schnittstelle kommen Messwerte in unterschiedlicher Form: als Zahl, als Text oder gelegentlich als `None` bzw. Liste (Übertragungsfehler). Schreiben Sie `convert(x)`, die **zwei Werte** zurückgibt:\n- bei Erfolg: `(float(x), \"ok\")`\n- bei einem `ValueError` (z.B. Text `\"abc\"`): `(None, \"ungültiger Wert\")`\n- bei einem `TypeError` (z.B. `None` oder eine Liste): `(None, \"falscher Typ\")`\n\nVerwenden Sie zwei getrennte `except`-Blöcke. Schreiben Sie außerdem `convert_all(items)`, die eine Liste aller erfolgreich umgewandelten Werte und die Anzahl der Fehler zurückgibt.",
         "en": "Readings come from an interface in different forms: as a number, as text or occasionally as `None` or a list (transmission errors). Write `convert(x)` that returns **two values**:\n- on success: `(float(x), \"ok\")`\n- on a `ValueError` (e.g. text `\"abc\"`): `(None, \"ungültiger Wert\")` (invalid value)\n- on a `TypeError` (e.g. `None` or a list): `(None, \"falscher Typ\")` (wrong type)\n\nUse two separate `except` blocks and keep the German status texts. Also write `convert_all(items)` that returns a list of all successfully converted values and the number of errors."},
   starter={"de": "def convert(x):\n    ...\n", "en": "def convert(x):\n    ...\n"},
   solution='def convert(x):\n    try:\n        return float(x), "ok"\n    except ValueError:\n        return None, "ungültiger Wert"\n    except TypeError:\n        return None, "falscher Typ"\n\ndef convert_all(items):\n    values = []\n    errors = 0\n    for item in items:\n        value, status = convert(item)\n        if status == "ok":\n            values.append(value)\n        else:\n            errors += 1\n    return values, errors\n\nprint(convert("21.5"), convert("abc"), convert(None))\nprint(convert_all([1, "2.5", None, "x", [3]]))\n',
   tests='''
ns, out = run()
for x, e in [("21.5", (21.5, "ok")), (3, (3.0, "ok")), ("abc", (None, "ungültiger Wert")), (None, (None, "falscher Typ")), ([1], (None, "falscher Typ")), ("", (None, "ungültiger Wert"))]:
    r = call(ns, "convert", x)
    check(isinstance(r, tuple) and tuple(r) == e, f"convert({x!r}) = {e}", f"convert({x!r}) = {e}")
r = call(ns, "convert_all", [1, "2.5", None, "x", [3]])
check(isinstance(r, tuple) and sorted(r[0]) == [1.0, 2.5] and r[1] == 3, "convert_all([1, '2.5', None, 'x', [3]]) = ([1.0, 2.5], 3)", "convert_all([1, '2.5', None, 'x', [3]]) = ([1.0, 2.5], 3)")
check(tuple(call(ns, "convert_all", [])) == ([], 0), "convert_all([]) = ([], 0)", "convert_all([]) = ([], 0)")
''',
   require=["try"], refs=["B.3", "B.2"])

# ------------------------------------------------------------------ Anhang B, Stufe 2
ex(id="kB-finally", ch="B", lvl=2,
   title={"de": "Messgerät immer abschalten", "en": "Always switching off the instrument"},
   task={"de": "Ein Messgerät muss nach jeder Messreihe abgeschaltet werden – auch wenn dabei ein Fehler auftritt. Simuliert wird das Gerät durch die Liste `log`, in die Ereignisse geschrieben werden.\n\nSchreiben Sie `measure(log, raw_values, gain)`:\n- Hängen Sie zuerst `\"an\"` an `log`.\n- Rechnen Sie dann alle Rohwerte um (`raw / gain`) und sammeln Sie die Ergebnisse.\n- Im `finally`-Zweig wird **immer** `\"aus\"` an `log` gehängt.\n- Die Funktion gibt die Liste der Ergebnisse in der Reihenfolge der Rohwerte zurück. Tritt ein Fehler auf (z.B. `ZeroDivisionError` bei `gain = 0`), wird er **nicht** abgefangen, sondern an den Aufrufer weitergegeben – nur das Abschalten muss trotzdem passieren.",
         "en": "An instrument must be switched off after every measurement series – even if an error occurs. The instrument is simulated by the list `log`, into which events are written.\n\nWrite `measure(log, raw_values, gain)`:\n- First append `\"an\"` (on) to `log`.\n- Then convert all raw values (`raw / gain`) and collect the results.\n- In the `finally` clause, `\"aus\"` (off) is **always** appended to `log`.\n- The function returns the list of results in the order of the raw values. If an error occurs (e.g. `ZeroDivisionError` for `gain = 0`), it is **not** caught but passed on to the caller – only the switching off must happen anyway."},
   starter={"de": "def measure(log, raw_values, gain):\n    ...\n", "en": "def measure(log, raw_values, gain):\n    ...\n"},
   solution='def measure(log, raw_values, gain):\n    log.append("an")\n    try:\n        results = []\n        for raw in raw_values:\n            results.append(raw / gain)\n        return results\n    finally:\n        log.append("aus")\n\nlog = []\nprint(measure(log, [100, 250], 50), log)\n',
   tests='''
ns, out = run()
log = []
r = call(ns, "measure", log, [100, 250, 0], 50)
check(r == [2.0, 5.0, 0.0] and log == ["an", "aus"], "measure(log, [100, 250, 0], 50) = [2.0, 5.0, 0.0], log = ['an', 'aus']", "measure(log, [100, 250, 0], 50) = [2.0, 5.0, 0.0], log = ['an', 'aus']")
f = ns["measure"]
log2 = []
check(raises(ZeroDivisionError, lambda: f(log2, [1, 2], 0)), "gain = 0: ZeroDivisionError wird weitergegeben", "gain = 0: ZeroDivisionError is passed on")
check(log2 == ["an", "aus"], "Auch bei einem Fehler wird abgeschaltet: log = ['an', 'aus']", "Switched off even on an error: log = ['an', 'aus']")
log3 = []
check(raises(TypeError, lambda: f(log3, [1, "x"], 2)) and log3 == ["an", "aus"], "Auch bei TypeError wird abgeschaltet", "Also switched off on a TypeError")
check("finally" in SOURCE, "Mit finally gelöst", "Solved with finally")
''',
   require=["try", "def"], refs=["B.3e", "B.3"])

ex(id="kB-linenumbers", ch="B", lvl=2,
   title={"de": "Fehlermeldung mit Zeilennummer", "en": "Error message with line number"},
   task={"de": "Eine Liste von Textzeilen (`lines`) soll in Zahlen umgewandelt werden (Dezimalkomma erlaubt). Wenn eine Zeile ungültig ist, soll **nicht** einfach Pythons Originalmeldung erscheinen, sondern eine verständliche: Schreiben Sie `parse_lines(lines)`, die die Liste der Zahlen in der Reihenfolge der Zeilen zurückgibt. Tritt bei einer Zeile ein `ValueError` auf, fangen Sie ihn ab und lösen Sie einen neuen `ValueError` mit der Meldung `Zeile 3: 'abc' ist keine Zahl` aus (Zeilen gezählt ab 1, der Originaltext in Anführungszeichen – `{text!r}` im f-String erzeugt sie automatisch).\n\nLeere Zeilen (nach `strip()`) werden übersprungen, zählen aber bei der Nummerierung mit.",
         "en": "A list of text lines (`lines`) is to be converted into numbers (decimal comma allowed). If a line is invalid, Python's original message should **not** simply appear, but an understandable one: write `parse_lines(lines)` that returns the list of numbers in the order of the lines. If a `ValueError` occurs for a line, catch it and raise a new `ValueError` with the message `Zeile 3: 'abc' ist keine Zahl` (line 3: 'abc' is not a number; lines counted from 1, the original text in quotes – `{text!r}` in the f-string adds them automatically).\n\nEmpty lines (after `strip()`) are skipped but still count for the numbering."},
   starter={"de": "def parse_lines(lines):\n    ...\n", "en": "def parse_lines(lines):\n    ...\n"},
   solution='def parse_lines(lines):\n    numbers = []\n    for nr, line in enumerate(lines, start=1):\n        text = line.strip()\n        if text == "":\n            continue\n        try:\n            numbers.append(float(text.replace(",", ".")))\n        except ValueError:\n            raise ValueError(f"Zeile {nr}: {text!r} ist keine Zahl")\n    return numbers\n\nprint(parse_lines(["21,4", "", "23.9"]))\n',
   tests='''
ns, out = run()
f = ns.get("parse_lines")
check(call(ns, "parse_lines", ["21,4", "", "23.9", " 1e2 "]) == [21.4, 23.9, 100.0] and call(ns, "parse_lines", []) == [], "Gültige Zeilen werden umgewandelt, leere übersprungen", "Valid lines are converted, empty ones skipped")
for lines, nr, bad in [(["1", "2", "abc"], 3, "abc"), (["", "x1"], 2, "x1"), (["5,5,5"], 1, "5,5,5")]:
    msg = ""
    try:
        f(lines)
    except ValueError as e:
        msg = str(e)
    except Exception as e:
        msg = "anderer Fehler " + type(e).__name__
    check((f"zeile {nr}" in msg.lower() or f"line {nr}" in msg.lower()) and repr(bad) in msg, f"{lines}: Meldung nennt Zeile {nr} und {bad!r}", f"{lines}: message names line {nr} and {bad!r}")
''',
   require=["try", "raise"], refs=["B.4", "B.3", "B.2"])

ex(id="kB-validate", ch="B", lvl=2,
   title={"de": "Bauteildaten prüfen", "en": "Validating part data"},
   task={"de": "Aus einem ERP-System kommen Bauteildaten als Dictionaries mit den Schlüsseln `\"nr\"`, `\"length\"` und `\"mass\"`. Schreiben Sie `validate(part)`:\n- Fehlt ein Schlüssel, entsteht beim Zugriff ein `KeyError` – lassen Sie ihn einfach durch (nicht abfangen).\n- Ist `length` oder `mass` keine Zahl (`int`/`float`), lösen Sie einen `TypeError` aus.\n- Ist `length` oder `mass` nicht positiv, lösen Sie einen `ValueError` aus.\n- Sonst wird `True` zurückgegeben.\n\nSchreiben Sie dann `check_batch(parts)`, die für eine Liste von Bauteilen ein Dictionary mit den Zählern `\"ok\"`, `\"KeyError\"`, `\"TypeError\"` und `\"ValueError\"` zurückgibt (alle vier Schlüssel immer vorhanden). Tipp: `type(e).__name__` liefert den Namen des Fehlertyps.",
         "en": "Part data come from an ERP system as dictionaries with the keys `\"nr\"`, `\"length\"` and `\"mass\"`. Write `validate(part)`:\n- If a key is missing, accessing it raises a `KeyError` – simply let it through (don't catch it).\n- If `length` or `mass` is not a number (`int`/`float`), raise a `TypeError`.\n- If `length` or `mass` is not positive, raise a `ValueError`.\n- Otherwise return `True`.\n\nThen write `check_batch(parts)` that returns, for a list of parts, a dictionary with the counters `\"ok\"`, `\"KeyError\"`, `\"TypeError\"` and `\"ValueError\"` (all four keys always present). Tip: `type(e).__name__` gives the name of the error type."},
   starter={"de": "def validate(part):\n    ...\n", "en": "def validate(part):\n    ...\n"},
   solution='def validate(part):\n    length = part["length"]\n    mass = part["mass"]\n    nr = part["nr"]\n    for x in (length, mass):\n        if not isinstance(x, (int, float)):\n            raise TypeError(f"{nr}: Zahl erwartet, nicht {x!r}")\n        if x <= 0:\n            raise ValueError(f"{nr}: Wert muss positiv sein, nicht {x}")\n    return True\n\ndef check_batch(parts):\n    counts = {"ok": 0, "KeyError": 0, "TypeError": 0, "ValueError": 0}\n    for part in parts:\n        try:\n            validate(part)\n        except (KeyError, TypeError, ValueError) as e:\n            counts[type(e).__name__] += 1\n        else:\n            counts["ok"] += 1\n    return counts\n\nprint(check_batch([{"nr": "A1", "length": 120, "mass": 0.4}, {"nr": "A2", "length": "120", "mass": 1}]))\n',
   tests='''
ns, out = run()
f = ns.get("validate")
check(call(ns, "validate", {"nr": "A1", "length": 120, "mass": 0.4}) is True, "Gültiges Bauteil → True", "Valid part → True")
check(raises(KeyError, lambda: f({"nr": "A2", "length": 10})), "Fehlender Schlüssel → KeyError", "Missing key → KeyError")
check(raises(TypeError, lambda: f({"nr": "A3", "length": "10", "mass": 1})) and raises(TypeError, lambda: f({"nr": "A3", "length": 10, "mass": None})), "Text/None → TypeError", "Text/None → TypeError")
check(raises(ValueError, lambda: f({"nr": "A4", "length": 0, "mass": 1})) and raises(ValueError, lambda: f({"nr": "A4", "length": 5, "mass": -2.0})), "Nicht positiv → ValueError", "Not positive → ValueError")
batch = [{"nr": "1", "length": 1, "mass": 1}, {"nr": "2", "length": 2}, {"nr": "3", "length": "x", "mass": 1}, {"nr": "4", "length": -1, "mass": 1}, {"nr": "5", "length": 3.5, "mass": 2}, {"mass": 1, "length": 1}]
check(call(ns, "check_batch", batch) == {"ok": 2, "KeyError": 2, "TypeError": 1, "ValueError": 1}, "check_batch zählt 2 ok, 2 KeyError, 1 TypeError, 1 ValueError", "check_batch counts 2 ok, 2 KeyError, 1 TypeError, 1 ValueError")
check(call(ns, "check_batch", []) == {"ok": 0, "KeyError": 0, "TypeError": 0, "ValueError": 0}, "Leere Liste → alle Zähler 0", "Empty list → all counters 0")
''',
   require=["try", "raise"], refs=["B.4", "B.3", "8.3"])

# ------------------------------------------------------------------ Anhang B, Stufe 3
ex(id="kB-import", ch="B", lvl=3,
   title={"de": "Robuster Import mit Fehlerprotokoll", "en": "Robust import with an error log"},
   task={"de": "Die Datei `data/import.csv` hat eine Kopfzeile und danach Zeilen der Form `zeit_s;druck_bar`. In der Praxis enthält sie Fehler: fehlende Trennzeichen, Text statt Zahl, Dezimalkommas (diese sind erlaubt!). Schreiben Sie `import_file(path)`:\n- Gibt **zwei Werte** zurück: die Liste der gültigen Datensätze als Tupel `(zeit, druck)` (beide `float`) und die Liste der Fehler als Tupel `(zeilennummer, meldung)` – Zeilen gezählt ab 1 inklusive Kopfzeile.\n- Pro Zeile: `split(\";\")` und Indexzugriff auf beide Teile; fangen Sie `ValueError` **und** `IndexError` gemeinsam ab (`except (…, …) as e`) und speichern Sie `str(e)` als Meldung.\n- Leerzeilen werden übersprungen.\n- Existiert die Datei nicht, wird `([], [(0, \"Datei fehlt\")])` zurückgegeben.\n- Schreiben Sie die Fehler zusätzlich in die Datei `data/import_fehler.txt` (eine Zeile pro Fehler: `Zeile 4: …`) – aber nur, wenn es Fehler gibt.",
         "en": "The file `data/import.csv` has a header line followed by lines of the form `zeit_s;druck_bar` (time;pressure). In practice it contains errors: missing separators, text instead of numbers, decimal commas (these are allowed!). Write `import_file(path)`:\n- Returns **two values**: the list of valid records as tuples `(time, pressure)` (both `float`) and the list of errors as tuples `(line_number, message)` – lines counted from 1 including the header.\n- Per line: `split(\";\")` and indexing of both parts; catch `ValueError` **and** `IndexError` together (`except (…, …) as e`) and store `str(e)` as the message.\n- Blank lines are skipped.\n- If the file doesn't exist, `([], [(0, \"Datei fehlt\")])` is returned.\n- Additionally write the errors to the file `data/import_fehler.txt` (one line per error: `Zeile 4: …`) – but only if there are errors."},
   starter={"de": "def import_file(path):\n    ...\n", "en": "def import_file(path):\n    ...\n"},
   solution='def import_file(path):\n    records = []\n    errors = []\n    try:\n        with open(path, encoding="utf-8") as f:\n            lines = f.read().split("\\n")\n    except FileNotFoundError:\n        return [], [(0, "Datei fehlt")]\n    for nr, line in enumerate(lines, start=1):\n        if nr == 1 or line.strip() == "":\n            continue\n        try:\n            parts = line.strip().split(";")\n            t = float(parts[0].replace(",", "."))\n            p = float(parts[1].replace(",", "."))\n        except (ValueError, IndexError) as e:\n            errors.append((nr, str(e)))\n        else:\n            records.append((t, p))\n    if len(errors) > 0:\n        with open("data/import_fehler.txt", "w", encoding="utf-8") as f:\n            for nr, msg in errors:\n                f.write(f"Zeile {nr}: {msg}\\n")\n    return records, errors\n\nprint(import_file("data/import.csv"))\n',
   tests='''
F1 = "zeit_s;druck_bar\\n0;1,02\\n10;1.35\\n20 1.6\\n30;abc\\n\\n40;2,10\\n"
F2 = "zeit_s;druck_bar\\n1;2\\n"
ns, out = run(files={"data/import.csv": F1, "data/ok.csv": F2})
r = call(ns, "import_file", "data/import.csv")
check(isinstance(r, tuple) and len(r) == 2 and sorted(r[0]) == [(0.0, 1.02), (10.0, 1.35), (40.0, 2.1)], "Gültige Datensätze: (0, 1.02), (10, 1.35), (40, 2.1)", "Valid records: (0, 1.02), (10, 1.35), (40, 2.1)")
errs = list(r[1]) if isinstance(r, tuple) and len(r) == 2 else []
check(sorted(e[0] for e in errs) == [4, 5] and all(isinstance(e[1], str) and e[1] for e in errs), "Fehler in Zeile 4 (Trennzeichen fehlt) und 5 (Text) mit Meldung", "Errors in line 4 (separator missing) and 5 (text) with message")
try:
    lines = [l for l in read_file("data/import_fehler.txt").split("\\n") if l.strip()]
except FileNotFoundError:
    lines = []
check(len(lines) == 2 and any(l.lower().startswith(("zeile 4:", "line 4:")) for l in lines) and any(l.lower().startswith(("zeile 5:", "line 5:")) for l in lines), "import_fehler.txt enthält zwei Fehlerzeilen", "import_fehler.txt contains two error lines")
ns, out = run(files={"data/ok.csv": F2})
r2 = call(ns, "import_file", "data/ok.csv")
import os as _os
check(tuple(r2) == ([(1.0, 2.0)], []) and not _os.path.exists("data/import_fehler.txt"), "Fehlerfreie Datei: keine Fehlerdatei", "Error-free file: no error file")
check(tuple(call(ns, "import_file", "data/fehlt.csv")) == ([], [(0, "Datei fehlt")]), "Fehlende Datei → ([], [(0, 'Datei fehlt')])", "Missing file → ([], [(0, 'Datei fehlt')])")
ns, out = run(files={"data/eins.csv": "zeit_s;druck_bar\\n1;2\\n2;x\\n"})
r3 = call(ns, "import_file", "data/eins.csv")
try:
    lines = [l for l in read_file("data/import_fehler.txt").split("\\n") if l.strip()]
except FileNotFoundError:
    lines = []
check(len(lines) == 1 and lines[0].lower().startswith(("zeile 3:", "line 3:")), "Auch ein einzelner Fehler wird in import_fehler.txt geschrieben", "A single error is also written to import_fehler.txt")
''',
   require=["try", "with"], refs=["B.3", "B.3e", "A.3"],
   files={"data/import.csv": "zeit_s;druck_bar\n0;1,02\n10;1.35\n20 1.6\n30;abc\n\n40;2,10\n"})

ex(id="kB-units", ch="B", lvl=3,
   title={"de": "Kraftangaben mit Einheit einlesen", "en": "Reading forces with units"},
   task={"de": "In einem Lastenheft stehen Kräfte als Text mit Einheit, z.B. `\"12.5 kN\"`, `\"300 N\"` oder `\"0,2 MN\"` (Zahl, Leerzeichen, Einheit; Dezimalkomma erlaubt). Schreiben Sie `to_newton(text)`, die die Kraft in N als `float` zurückgibt:\n- Zerlegen Sie den Text mit `split()` in Zahl und Einheit. Entstehen dabei nicht genau zwei Teile, lösen Sie einen `ValueError` mit der Meldung `Format: <Zahl> <Einheit>` aus.\n- Erlaubte Einheiten (Groß-/Kleinschreibung beachten): `N`, `kN`, `MN`. Speichern Sie die Faktoren in einem Dictionary; eine unbekannte Einheit führt zu einem `KeyError` beim Zugriff – fangen Sie ihn ab und lösen Sie stattdessen einen `ValueError` mit der Meldung `Unbekannte Einheit: <einheit>` aus.\n- Ist die Zahl ungültig, entsteht beim Umwandeln ohnehin ein `ValueError` – den lassen Sie durch.\n\nSchreiben Sie außerdem `total_force(texts)`, die die Summe einer Liste von Kraftangaben in kN zurückgibt.",
         "en": "A requirements specification lists forces as text with a unit, e.g. `\"12.5 kN\"`, `\"300 N\"` or `\"0,2 MN\"` (number, space, unit; decimal comma allowed). Write `to_newton(text)` that returns the force in N as a `float`:\n- Split the text with `split()` into number and unit. If this does not give exactly two parts, raise a `ValueError` with the message `Format: <number> <unit>`.\n- Allowed units (case-sensitive): `N`, `kN`, `MN`. Store the factors in a dictionary; an unknown unit leads to a `KeyError` on access – catch it and raise a `ValueError` with the message `Unbekannte Einheit: <unit>` (unknown unit) instead.\n- If the number is invalid, a `ValueError` occurs anyway when converting – let it through.\n\nAlso write `total_force(texts)` that returns the sum of a list of force entries in kN."},
   starter={"de": "FACTORS = {'N': 1.0, 'kN': 1e3, 'MN': 1e6}\n\ndef to_newton(text):\n    ...\n", "en": "FACTORS = {'N': 1.0, 'kN': 1e3, 'MN': 1e6}\n\ndef to_newton(text):\n    ...\n"},
   solution='FACTORS = {\'N\': 1.0, \'kN\': 1e3, \'MN\': 1e6}\n\ndef to_newton(text):\n    parts = text.split()\n    if len(parts) != 2:\n        raise ValueError("Format: <Zahl> <Einheit>")\n    number, unit = parts\n    try:\n        factor = FACTORS[unit]\n    except KeyError:\n        raise ValueError(f"Unbekannte Einheit: {unit}")\n    return float(number.replace(",", ".")) * factor\n\ndef total_force(texts):\n    total = 0.0\n    for t in texts:\n        total += to_newton(t)\n    return total / 1000\n\nprint(to_newton("12.5 kN"), to_newton("0,2 MN"), total_force(["300 N", "1.2 kN"]))\n',
   tests='''
ns, out = run()
f = ns.get("to_newton")
for t, e in [("12.5 kN", 12500.0), ("300 N", 300.0), ("0,2 MN", 200000.0), ("  7 kN ", 7000.0)]:
    check(approx(call(ns, "to_newton", t), e), f"to_newton({t!r}) = {e:g} N", f"to_newton({t!r}) = {e:g} N")
def msg_of(arg):
    try:
        f(arg)
    except ValueError as e:
        return "VE:" + str(e)
    except Exception as e:
        return "other:" + type(e).__name__
    return "none"
m1, m2, m3 = msg_of("12.5"), msg_of("5 kg"), msg_of("abc kN")
check(m1.startswith("VE:") and "Format" in m1, "Fehlende Einheit → ValueError mit 'Format…'", "Missing unit → ValueError with 'Format…'")
check(m2.startswith("VE:") and "kg" in m2, "Unbekannte Einheit → ValueError (kein KeyError), Meldung nennt 'kg'", "Unknown unit → ValueError (not KeyError), message names 'kg'")
check(m3.startswith("VE:") and msg_of("3 kn").startswith("VE:"), "Ungültige Zahl oder falsche Schreibweise → ValueError", "Invalid number or wrong spelling → ValueError")
check(approx(call(ns, "total_force", ["300 N", "1.2 kN", "0,001 MN"]), 2.5) and approx(call(ns, "total_force", []), 0), "total_force(['300 N', '1.2 kN', '0,001 MN']) = 2.5 kN", "total_force(['300 N', '1.2 kN', '0,001 MN']) = 2.5 kN")
''',
   require=["try", "raise", "dict"], refs=["B.4", "B.3", "8.3"])

ex(id="kB-statemachine", ch="B", lvl=3,
   title={"de": "Zustandsautomat einer Anlage", "en": "State machine of a plant"},
   task={"de": "Eine Anlage kennt die Zustände `\"aus\"`, `\"bereit\"`, `\"läuft\"` und `\"störung\"`. Erlaubt sind nur diese Übergänge:\n- `power_on()`: aus → bereit\n- `start()`: bereit → läuft\n- `stop()`: läuft → bereit\n- `fault(code)`: aus jedem Zustand außer „aus“ → störung (der Fehlercode wird im Attribut `last_fault` gespeichert)\n- `reset()`: störung → bereit\n- `power_off()`: bereit → aus\n\nSchreiben Sie die Klasse `Plant` (Startzustand `\"aus\"` im Attribut `state`, `last_fault` = `None`, `history` = Liste aller erreichten Zustände, beginnend mit `\"aus\"`). Ein nicht erlaubter Übergang löst einen `ValueError` mit einer Meldung wie `start() im Zustand 'aus' nicht erlaubt` aus; der Zustand bleibt dann unverändert.\n\nSchreiben Sie außerdem die Funktion `run_commands(plant, commands)`, die eine Liste von Methodennamen (z.B. `[\"power_on\", \"start\"]`; für `fault` wird der Code `\"E99\"` verwendet) der Reihe nach ausführt, ungültige Befehle per `try`/`except` überspringt und deren Anzahl zurückgibt. Unbekannte Befehlsnamen zählen ebenfalls als ungültig. Tipp: Ordnen Sie den Namen mit `if`/`elif` den Methodenaufruf zu.",
         "en": "A plant knows the states `\"aus\"` (off), `\"bereit\"` (ready), `\"läuft\"` (running) and `\"störung\"` (fault). Only these transitions are allowed:\n- `power_on()`: aus → bereit\n- `start()`: bereit → läuft\n- `stop()`: läuft → bereit\n- `fault(code)`: from any state except “aus” → störung (the error code is stored in the attribute `last_fault`)\n- `reset()`: störung → bereit\n- `power_off()`: bereit → aus\n\nWrite the class `Plant` (initial state `\"aus\"` in the attribute `state`, `last_fault` = `None`, `history` = list of all states reached, starting with `\"aus\"`). A transition that is not allowed raises a `ValueError` with a message like `start() im Zustand 'aus' nicht erlaubt`; the state then stays unchanged. Keep the German state names.\n\nAlso write the function `run_commands(plant, commands)` that executes a list of method names (e.g. `[\"power_on\", \"start\"]`; for `fault` the code `\"E99\"` is used) in order, skips invalid commands with `try`/`except` and returns their number. Unknown command names also count as invalid. Tip: map the name to the method call with `if`/`elif`."},
   starter={"de": "class Plant:\n    def __init__(self):\n        self.state = \"aus\"\n        self.last_fault = None\n        self.history = [\"aus\"]\n", "en": "class Plant:\n    def __init__(self):\n        self.state = \"aus\"\n        self.last_fault = None\n        self.history = [\"aus\"]\n"},
   solution='class Plant:\n    def __init__(self):\n        self.state = "aus"\n        self.last_fault = None\n        self.history = ["aus"]\n\n    def _go(self, name, allowed_from, new_state):\n        if self.state not in allowed_from:\n            raise ValueError(f"{name}() im Zustand {self.state!r} nicht erlaubt")\n        self.state = new_state\n        self.history.append(new_state)\n\n    def power_on(self):\n        self._go("power_on", ["aus"], "bereit")\n\n    def start(self):\n        self._go("start", ["bereit"], "läuft")\n\n    def stop(self):\n        self._go("stop", ["läuft"], "bereit")\n\n    def fault(self, code):\n        self._go("fault", ["bereit", "läuft", "störung"], "störung")\n        self.last_fault = code\n\n    def reset(self):\n        self._go("reset", ["störung"], "bereit")\n\n    def power_off(self):\n        self._go("power_off", ["bereit"], "aus")\n\n\ndef run_commands(plant, commands):\n    invalid = 0\n    for cmd in commands:\n        try:\n            if cmd == "power_on":\n                plant.power_on()\n            elif cmd == "start":\n                plant.start()\n            elif cmd == "stop":\n                plant.stop()\n            elif cmd == "fault":\n                plant.fault("E99")\n            elif cmd == "reset":\n                plant.reset()\n            elif cmd == "power_off":\n                plant.power_off()\n            else:\n                raise ValueError(f"Unbekannter Befehl: {cmd}")\n        except ValueError:\n            invalid += 1\n    return invalid\n\np = Plant()\nprint(run_commands(p, ["start", "power_on", "start", "fault", "start", "reset", "stop"]), p.history)\n',
   tests='''
ns, out = run()
p = call(ns, "Plant")
check(p.state == "aus" and p.history == ["aus"] and p.last_fault is None, "Startzustand 'aus'", "Initial state 'aus'")
check(raises(ValueError, lambda: p.start()) and p.state == "aus", "start() im Zustand 'aus' → ValueError, Zustand bleibt", "start() in state 'aus' → ValueError, state unchanged")
msg = ""
try:
    p.start()
except ValueError as e:
    msg = str(e)
except Exception:
    pass
check("start" in msg and "aus" in msg, "Die Meldung nennt Methode und Zustand", "The message names method and state")
method(p, "power_on"); method(p, "start")
check(p.state == "läuft", "power_on(), start() → 'läuft'", "power_on(), start() → 'läuft'")
check(raises(ValueError, lambda: p.power_off()) and p.state == "läuft", "power_off() im Zustand 'läuft' nicht erlaubt", "power_off() not allowed in state 'läuft'")
method(p, "fault", "E12")
check(p.state == "störung" and p.last_fault == "E12", "fault('E12') → 'störung', last_fault = 'E12'", "fault('E12') → 'störung', last_fault = 'E12'")
method(p, "reset"); method(p, "power_off")
check(p.history == ["aus", "bereit", "läuft", "störung", "bereit", "aus"], "history stimmt", "history is correct")
check(raises(ValueError, lambda: p.fault("E1")) and p.last_fault == "E12", "fault() im Zustand 'aus' nicht erlaubt", "fault() not allowed in state 'aus'")
q = call(ns, "Plant")
n0 = call(ns, "run_commands", call(ns, "Plant"), ["power_on", "start", "fault", "reset"])
n1 = call(ns, "run_commands", call(ns, "Plant"), ["xyz"])
check(n0 == 0 and n1 == 1, "run_commands: gültige Folge → 0, unbekannter Befehl → 1", "run_commands: valid sequence → 0, unknown command → 1")
n = call(ns, "run_commands", q, ["start", "power_on", "start", "fault", "start", "reset", "stop", "xyz"])
check(n == 4 and q.state == "bereit" and q.last_fault == "E99", "run_commands: 4 ungültige Befehle, Endzustand 'bereit'", "run_commands: 4 invalid commands, final state 'bereit'")
''',
   require=["class", "raise", "try"], refs=["B.4", "B.3", "10.3"])
