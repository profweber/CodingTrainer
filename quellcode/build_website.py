"""Erzeugt index.html und worker.js der Website neu.

Aufruf im Ordner quellcode:  python3 build_website.py
(schreibt in den Ordner ohne-tutor/ der Version ohne KI-Tutor;
 ein anderer Zielordner kann als Argument angegeben werden).
Die Ordner py/ und fonts/ sowie config.json dort bleiben unverändert.
Die Claude-Version mit KI-Tutor wird über Claude veröffentlicht (siehe LIESMICH.txt).
Vorher prüfen:  python3 verify.py   (alle Musterlösungen bestehen, Startcode fällt durch)

python3 build_website.py --claude
erzeugt stattdessen die Claude-Version (KI-Tutor eingebaut) im Ordner claude/:
index.html und worker.js; claude/config.json ist die Semester-Einstellung dieser Version.
Veröffentlicht wird sie mit dem Artifact-Werkzeug von Claude: index.html als Seite,
worker.js und config.json als zusätzliche Dateien, an dieselbe Adresse wie bisher
(die Python-Dateien unter py/ liegen dort bereits und bleiben erhalten).
"""
import json, re, sys
import harness, bank

CLAUDE = "--claude" in sys.argv
args = [a for a in sys.argv[1:] if a != "--claude"]
target = args[0] if args else ("claude" if CLAUDE else "../ohne-tutor")
js_safe = lambda s: s.replace("</", "<\\/")
tpl = open("template.html", encoding="utf-8").read()
for e in bank.EX:   # Themen für config.json (Bibliotheken, die die Musterlösung braucht)
    found = harness.analyze(e["solution"])
    e["topics"] = [t for t in ("numpy", "pandas") if t in found]
cons = {k: list(v) for k, v in harness.C.items()}
page = tpl.replace("/*BANK*/", js_safe(json.dumps(bank.EX, ensure_ascii=False))).replace("/*CONSTRUCTS*/", js_safe(json.dumps(cons, ensure_ascii=False)))
if CLAUDE:
    open(target + "/index.html", "w", encoding="utf-8").write(page)
    worker = open("worker_template.js", encoding="utf-8").read().replace('/*HARNESS*/""', json.dumps(open("harness.py", encoding="utf-8").read()))
    open(target + "/worker.js", "w", encoding="utf-8").write(worker)
    print("Claude-Version geschrieben nach", target, "-", len(bank.EX), "Aufgaben")
    sys.exit()
page = page.replace("/*STANDALONE*/false", "true")
page = re.sub(r"<!--FONTS-->.*?<!--/FONTS-->", '<link rel="stylesheet" href="fonts/fonts.css">', page, flags=re.S)
title = re.search(r"<title>.*?</title>", page).group(0)
page = page.replace(title, "", 1)
html = ('<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n' + title +
        '\n<meta name="description" content="Python-Übungen zum Skript „Programmierung für Ingenieurinnen und Ingenieure“ (Hochschule Trier)">\n<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}body{margin:0;font:14px system-ui}img{max-width:100%}[hidden]{display:none!important}</style>\n</head>\n<body>\n' + page + '\n</body>\n</html>\n')
open(target + "/index.html", "w", encoding="utf-8").write(html)
worker = open("worker_template.js", encoding="utf-8").read().replace('/*HARNESS*/""', json.dumps(open("harness.py", encoding="utf-8").read())).replace("/*B64*/true", "false")
open(target + "/worker.js", "w", encoding="utf-8").write(worker)
print("index.html und worker.js geschrieben nach", target, "-", len(bank.EX), "Aufgaben")
