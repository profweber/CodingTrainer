# CodingTrainer

Übungsaufgaben zum Skript **„Programmierung für Ingenieurinnen und Ingenieure“** (Prof. Dr. Maik Weber, Hochschule Trier) – direkt im Browser, ohne Installation.

**Zum Trainer:** https://profweber.github.io/CodingTrainer/

- 236 Aufgaben zu den Kapiteln 4–10 und den Anhängen A und B, je Kapitel in drei Schwierigkeitsstufen
- Jede Aufgabe lässt sich nur mit dem lösen, was bis zu ihrem Kapitel im Skript steht; der Trainer weist auf Konstrukte hin, die erst später oder gar nicht im Skript vorkommen.
- Automatische Tests mit verständlichen Rückmeldungen und Verweisen auf die passenden Abschnitte im Skript
- Klausurtraining mit zufälligen Aufgaben aus den gewählten Kapiteln
- KI-Tutor: öffnet Claude mit einer vorbereiteten Anfrage (eigenes, kostenloses Claude-Konto genügt)
- Deutsch und Englisch

Python läuft vollständig im Browser (Pyodide). Der Lernfortschritt wird nur im Browser der Studierenden gespeichert; die Seite selbst sendet keine Daten an Dritte. Nur wer den KI-Tutor benutzt, schickt Aufgabe und Code an Claude.

Version 1.0 · abgestimmt auf Skriptversion 4.0

---

## Für Lehrende

### Semester einstellen

Die Datei [`config.json`](config.json) legt fest, was im laufenden Semester behandelt wird. Ändern direkt auf GitHub: Datei anklicken → Stift-Symbol → Wert ändern → „Commit changes“. Nach 1–2 Minuten gilt die neue Einstellung.

```json
{
  "semester": "",
  "chapters": ["4", "5", "6", "7", "8", "9", "10", "A", "B"],
  "topics": { "numpy": true, "pandas": true },
  "tutor": { "claude_link": true }
}
```

| Einstellung | Wirkung |
|---|---|
| `"pandas": false` | pandas-Aufgaben verschwinden (auch im Klausurtraining), Kapitel 9 zeigt „ohne pandas“, der Tutor empfiehlt pandas nicht. Gleiches gilt für `"numpy"`. |
| Kapitel aus `"chapters"` löschen | Das Kapitel wird ausgeblendet. |
| `"semester": "SoSe 2027"` | Erscheint im Info-Fenster. |
| `"claude_link": false` | Blendet den KI-Tutor aus. |

Ist die Datei fehlerhaft oder fehlt sie, gilt einfach alles.

### Aufbau des Repositorys

| Pfad | Inhalt |
|---|---|
| `index.html`, `worker.js`, `config.json`, `py/`, `fonts/` | die Website (wird von GitHub Pages ausgeliefert) |
| `quellcode/` | Aufgabenbank, Prüfwerkzeuge und Vorlage, aus der `index.html` und `worker.js` erzeugt werden – Details in `quellcode/LIESMICH.txt` |

### Aufgaben ändern oder ergänzen

1. Aufgabe in einer der Dateien `quellcode/bank*.py` bearbeiten.
2. Im Ordner `quellcode`: `python3 verify.py` (alle Musterlösungen bestehen, alle Startcodes fallen durch, nur Konstrukte aus dem Skript) und `python3 build_website.py` (schreibt `index.html` und `worker.js` neu).
3. Die beiden geänderten Dateien hochladen.

Python 3.11 oder neuer; für die NumPy- und pandas-Aufgaben müssen `numpy` und `pandas` installiert sein.
