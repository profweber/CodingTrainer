# CodingTrainer

Übungsaufgaben zum Skript **„Programmierung für Ingenieurinnen und Ingenieure“** (Prof. Dr. Maik Weber, Hochschule Trier) – direkt im Browser, ohne Installation, mit eingebautem KI-Tutor.

**Zum Trainer:** https://profweber.github.io/CodingTrainer/

- Aufgaben zu den Programmierkapiteln 4–10 und den Anhängen A (Dateien) und B (Fehlerbehandlung), in drei Schwierigkeitsstufen – wie viele es aktuell sind, zeigt die Startseite (abhängig von `config.json`)
- Jede Aufgabe lässt sich nur mit dem lösen, was bis zu ihrem Kapitel im Skript steht; der Trainer weist auf Konstrukte hin, die erst später oder gar nicht im Skript vorkommen.
- Automatische Tests mit verständlichen Rückmeldungen und Verweisen auf die passenden Abschnitte im Skript
- Klausurtraining mit zufälligen Aufgaben aus den gewählten Kapiteln
- KI-Tutor direkt in der Seite: gibt Hinweise und Feedback, verrät aber keine fertigen Lösungen
- Neue Aufgaben auf Knopfdruck: Claude erfindet zusätzliche Aufgaben passend zu Kapitel und Niveau; der Trainer prüft sie automatisch (Musterlösung besteht alle Tests, Startcode nicht, nur Konstrukte aus dem Skript), bevor sie erscheinen
- Fortschritt sichern und in eine andere Kopie oder einen anderen Browser übertragen
- Formeln sauber gesetzt (KaTeX, lokal eingebunden)
- Deutsch und Englisch

## So funktioniert es für Studierende

Die Startseite erklärt Schritt für Schritt, was man braucht, und führt zum Trainer auf claude.ai:

1. **CodingTrainer öffnen** – mit dem eigenen, kostenlosen Claude-Konto (die Startseite erklärt auch, wie man eines anlegt).
2. **„Kopieren“** klicken – in der Leiste von claude.ai ganz oben, links beim Titel „CodingTrainer“. claude.ai lässt KI-Funktionen in einem per Link geteilten Artefakt nur für dessen Eigentümer zu; in der eigenen Kopie funktioniert der Tutor mit dem Konto der Studierenden. Die Anfragen zählen zu deren eigenem Kontingent – nicht zu dem der Lehrenden.
3. **In der eigenen Kopie üben** und ein Lesezeichen setzen.

Wer den Trainer über den geteilten Link öffnet, sieht oben einen Hinweis mit derselben Anleitung. Python läuft vollständig im Browser (Pyodide); der Lernfortschritt wird nur im Browser gespeichert und lässt sich unter Info (oben rechts) → „Fortschritt übertragen“ in eine andere Kopie mitnehmen.

**Neue Versionen** erreichen bestehende Kopien nicht von selbst. Im Trainer führt Info (oben rechts) → „Auf neue Version prüfen“ zur Startseite; sie zeigt, ob die Kopie aktuell ist, was neu ist und wie man umsteigt (Fortschritt sichern, neu kopieren, Fortschritt übernehmen).

Wer kein Claude-Konto nutzen möchte, findet unter https://profweber.github.io/CodingTrainer/ohne-tutor/ dieselben Aufgaben ohne KI-Tutor (eigener Lernfortschritt, keine Daten an Dritte).

Version 1.1 · abgestimmt auf Skriptversion 4.0

---

## Für Lehrende

### Aufbau des Repositorys

| Pfad | Inhalt |
|---|---|
| `index.html` | Startseite: Knopf zur Claude-Version, Anleitung (Konto, eigene Kopie), Versionsprüfung mit Versionshinweisen, Link zur Version ohne Tutor. Die Adresse der Claude-Version steht dreimal in der Datei. |
| `ohne-tutor/` | vollständige Website ohne KI-Tutor (läuft direkt auf GitHub Pages; `katex/` enthält die Formelschrift). `info.json` enthält die aktuelle Versionsnummer und die Aufgabenzahlen für die Startseite. |
| `quellcode/` | Aufgabenbank, Prüfwerkzeuge und Vorlage, aus der beide Versionen erzeugt werden – Details in `quellcode/LIESMICH.txt` |
| `quellcode/claude/` | die Claude-Version zum Veröffentlichen auf claude.ai, mit ihrer eigenen `config.json` |

### Semester einstellen

Jede Version hat eine `config.json`; beide sollten gleich sein (die Startseite berechnet die angezeigte Aufgabenzahl aus `ohne-tutor/config.json`):

- **Claude-Version:** `quellcode/claude/config.json`. Nach einer Änderung muss die Version neu auf claude.ai veröffentlicht werden (z.B. in einer Claude-Sitzung mit diesem Repository: „Veröffentliche die Claude-Version neu“). **Wichtig:** Kopien, die Studierende schon angelegt haben, behalten ihre alte Einstellung. Stellen Sie das Semester deshalb ein, bevor die Studierenden kopieren – oder bitten Sie sie, neu zu kopieren.
- **Version ohne Tutor:** `ohne-tutor/config.json`. Ändern direkt auf GitHub: Datei anklicken → Stift-Symbol → Wert ändern → „Commit changes“. Nach 1–2 Minuten gilt die neue Einstellung.

```json
{
  "semester": "",
  "chapters": ["4", "5", "6", "7", "8", "9", "10", "A", "B"],
  "topics": { "numpy": true, "pandas": false },
  "tutor": {
    "claude_link": true,
    "artifact_url": "https://claude.ai/artifact/BJzRVf2JWj36M7LE2x9yV3"
  }
}
```

| Einstellung | Wirkung |
|---|---|
| `"pandas": false` (Voreinstellung) | pandas-Aufgaben verschwinden (auch im Klausurtraining), Kapitel 9 zeigt „ohne pandas“, der Tutor empfiehlt pandas nicht; Aufgabenzahl im Trainer und auf der Startseite passen sich an. Mit `true` erscheinen sie (dann 10 Aufgaben mehr). Gleiches gilt für `"numpy"`. |
| Kapitel aus `"chapters"` löschen | Das Kapitel wird ausgeblendet; Kapitelangaben und Aufgabenzahl passen sich an. |
| `"semester": "SoSe 2027"` | Erscheint im Info-Fenster. |
| `"artifact_url"` | Nur Version ohne Tutor: Der Tutor-Bereich zeigt einen Knopf zur Claude-Version. Leer (`""`): Der Tutor öffnet stattdessen Claude in einem neuen Tab mit vorbereiteter Anfrage. |
| `"claude_link": false` | Nur Version ohne Tutor: blendet den Tutor-Bereich ganz aus. |

Ist die Datei fehlerhaft oder fehlt sie, gilt einfach alles.

### Aufgaben ändern oder ergänzen

1. Aufgabe in einer der Dateien `quellcode/bank*.py` bearbeiten.
2. Im Ordner `quellcode`: `python3 verify.py` (alle Musterlösungen bestehen, alle Startcodes fallen durch, nur Konstrukte aus dem Skript).
3. `python3 build_website.py` erneuert `ohne-tutor/index.html`, `ohne-tutor/worker.js` und `ohne-tutor/info.json`; `python3 build_website.py --claude` erneuert die Claude-Version in `quellcode/claude/`.
4. Geänderte Dateien hochladen und die Claude-Version neu veröffentlichen.

Python 3.11 oder neuer; für die NumPy- und pandas-Aufgaben müssen `numpy` und `pandas` installiert sein.

### Neue Version veröffentlichen

1. In `quellcode/template.html` die Zeile `const VERSION = "1.1";` hochsetzen.
2. In `index.html` (Startseite) im Block `<script type="application/json" id="changes">` einen Eintrag mit den Neuerungen ergänzen (Deutsch und Englisch).
3. Beide Versionen erzeugen (siehe oben), hochladen und die Claude-Version neu veröffentlichen.

Die Startseite liest die Versionsnummer aus `ohne-tutor/info.json`; Studierende sehen über Info → „Auf neue Version prüfen“, dass es eine neue Version gibt. Kündigen Sie größere Updates zusätzlich in der Vorlesung oder auf der Lernplattform an.
