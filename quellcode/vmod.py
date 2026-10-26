# Schnellprüfung einzelner Aufgaben-Module: python3 vmod.py bank2_k4
import json, sys, os, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness, exlib
home = os.getcwd()
for modname in sys.argv[1:]:
    before = len(exlib.EX)
    importlib.import_module(modname)
    items = exlib.EX[before:]
    bad = 0
    for e in items:
        for lang in ["de", "en"]:
            r = json.loads(harness.api_check(e["solution"], e["tests"], e["ch"], e["require"], e["forbid"], lang))
            os.chdir(home)
            fails = [c for c in r["checks"] if not c["ok"]]
            con = r["constructs"]
            problems = []
            if r["error"]: problems.append("ERROR " + r["error"])
            if fails: problems.append("FAIL " + "; ".join(c[lang] for c in fails))
            if not r["checks"]: problems.append("NO CHECKS")
            if con["items"]: problems.append("CONSTRUCTS " + str([(i["key"], i["status"], i.get("chapter")) for i in con["items"]]))
            if con["missing"] or con["forbidden"]: problems.append("REQ/FORBID " + str(con["missing"]) + str(con["forbidden"]))
            if problems:
                bad += 1; print(e["id"], lang, *problems, sep="\n   ")
        for lang in ["de", "en"]:
            r = json.loads(harness.api_check(e["starter"][lang], e["tests"], e["ch"], e["require"], e["forbid"], lang))
            os.chdir(home)
            if not r["error"] and r["checks"] and all(c["ok"] for c in r["checks"]) and not r["constructs"]["missing"]:
                bad += 1; print(e["id"], "STARTER PASSES", lang)
            rep = harness.construct_report(e["starter"][lang], e["ch"])
            if rep["items"]:
                bad += 1; print(e["id"], "STARTER CONSTRUCTS", lang, [i["key"] for i in rep["items"]])
    from collections import Counter
    print(modname, len(items), "Aufgaben,", bad, "Probleme", sorted(Counter((e["ch"], e["lvl"]) for e in items).items()))
