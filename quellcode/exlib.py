EX = []


def ex(**kw):
    kw.setdefault("require", [])
    kw.setdefault("forbid", [])
    kw.setdefault("stdin", "")
    if any(e["id"] == kw["id"] for e in EX):
        raise ValueError("doppelte id " + kw["id"])
    EX.append(kw)
