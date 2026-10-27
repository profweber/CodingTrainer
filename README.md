# CodingTrainer

Übungsaufgaben zum Skript **„Programmierung für Ingenieurinnen und Ingenieure“** (Prof. Dr. Maik Weber, Hochschule Trier) – direkt im Browser, ohne Installation, mit eingebautem KI-Tutor.

**Zum Trainer:** https://profweber.github.io/CodingTrainer/

- 250 Aufgaben in drei Schwierigkeitsstufen: je 30 zu den Kapiteln 4–10, je 20 zu den Anhängen A (Dateien) und B (Fehlerbehandlung)
- Jede Aufgabe lässt sich nur mit dem lösen, was bis zu ihrem Kapitel im Skript steht; der Trainer weist auf Konstrukte hin, die erst später oder gar nicht im Skript vorkommen.
- Automatische Tests mit verständlichen Rückmeldungen und Verweisen auf die passenden Abschnitte im Skript
- Klausurtraining mit zufälligen Aufgaben aus den gewählten Kapiteln
- KI-Tutor direkt in der Seite: gibt Hinweise und Feedback, verrät aber keine fertigen Lösungen
- Formeln sauber gesetzt (KaTeX, lokal eingebunden)
- Deutsch und Englisch

Die Startseite erklärt kurz, was man braucht, und führt zum Trainer auf claude.ai. Dort läuft der KI-Tutor; Studierende melden sich mit ihrem eigenen (kostenlosen) Claude-Konto an, und die Anfragen zählen zu ihrem eigenen Kontingent – nicht zu dem der Lehrenden. Python läuft vollständig im Browser (Pyodide), der Lernfortschritt wird nur im Browser gespeichert.

Wer kein Claude-Konto nutzen möchte, findet unter https://profweber.github.io/CodingTrainer/ohne-tutor/ dieselben Aufgaben ohne KI-Tutor (eigener Lernfortschritt, keine Daten an Dritte).

Version 1.0 · abgestimmt auf Skriptversion 4.0

---

## Für Lehrende

### Aufbau des Repositorys

| Pfad | Inhalt |
|---|---|
| `index.html` | Startseite mit Knopf zur Claude-Version und Link zur Version ohne Tutor (die Adresse der Claude-Version steht dreimal in der Datei). Wer „beim nächsten Besuch überspringen“ wählt, wird direkt weitergeleitet; mit `?start` am Ende der Adresse erscheint die Startseite wieder. |
| `ohne-tutor/` | vollständige Website ohne KI-Tutor (läuft direkt auf GitHub Pages; `katex/` enthält die Formelschrift) |
| `quellcode/` | Aufgabenbank, Prüfwerkzeuge und Vorlage, aus der beide Versionen erzeugt werden – Details in `quellcode/LIESMICH.txt` |
| `quellcode/claude/` | die Claude-Version zum Veröffentlichen auf claude.ai, mit ihrer eigenen `config.json` |

### Semester einstellen

Jede Version hat eine `config.json`:

- **Claude-Version:** `quellcode/claude/config.json`. Nach einer Änderung muss die Version neu auf claude.ai veröffentlicht werden (z.B. in einer Claude-Sitzung mit diesem Repository: „Veröffentliche die Claude-Version neu“).
- **Version ohne Tutor:** `ohne-tutor/config.json`. Ändern direkt auf GitHub: Datei anklicken → Stift-Symbol → Wert ändern → „Commit changes“. Nach 1–2 Minuten gilt die neue Einstellung.

```json
{
  "semester": "",
  "chapters": ["4", "5", "6", "7", "8", "9", "10", "A", "B"],
  "topics": { "numpy": true, "pandas": true },
  "tutor": {
    "claude_link": true,
    "artifact_url": "https://claude.ai/artifact/BJzRVf2JWj36M7LE2x9yV3"
  }
}
```

| Einstellung | Wirkung |
|---|---|
| `"pandas": false` | pandas-Aufgaben verschwinden (auch im Klausurtraining), Kapitel 9 zeigt „ohne pandas“, der Tutor empfiehlt pandas nicht. Gleiches gilt für `"numpy"`. |
| Kapitel aus `"chapters"` löschen | Das Kapitel wird ausgeblendet. |
| `"semester": "SoSe 2027"` | Erscheint im Info-Fenster. |
| `"artifact_url"` | Nur Version ohne Tutor: Der Tutor-Bereich zeigt einen Knopf zur Claude-Version. Leer (`""`): Der Tutor öffnet stattdessen Claude in einem neuen Tab mit vorbereiteter Anfrage. |
| `"claude_link": false` | Nur Version ohne Tutor: blendet den Tutor-Bereich ganz aus. |

Ist die Datei fehlerhaft oder fehlt sie, gilt einfach alles.

### Aufgaben ändern oder ergänzen

1. Aufgabe in einer der Dateien `quellcode/bank*.py` bearbeiten.
2. Im Ordner `quellcode`: `python3 verify.py` (alle Musterlösungen bestehen, alle Startcodes fallen durch, nur Konstrukte aus dem Skript).
3. `python3 build_website.py` erneuert `ohne-tutor/index.html` und `ohne-tutor/worker.js`; `python3 build_website.py --claude` erneuert die Claude-Version in `quellcode/claude/`.
4. Geänderte Dateien hochladen und die Claude-Version neu veröffentlichen.

Python 3.11 oder neuer; für die NumPy- und pandas-Aufgaben müssen `numpy` und `pandas` installiert sein.
