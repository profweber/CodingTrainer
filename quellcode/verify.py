import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness, bank
home = os.getcwd()
bad = 0
for e in bank.EX:
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
print(len(bank.EX), "exercises,", bad, "problems")
from collections import Counter
print(Counter((e["ch"], e["lvl"]) for e in bank.EX))
