import json, subprocess, sys
B = "/home/claude/law"
subprocess.run([sys.executable, f"{B}/cards.py"], check=True, stdout=subprocess.DEVNULL)
subprocess.run([sys.executable, f"{B}/mc.py"], check=True, stdout=subprocess.DEVNULL)
cards = json.load(open(f"{B}/out/cards.json"))
slim = [{k: c[k] for k in ("id", "unit_no", "section", "front", "back", "tags") } | ({"explain": c["explain"]} if "explain" in c else {}) for c in cards]
mc = json.load(open(f"{B}/out/mc.json"))
t = open(f"{B}/app/template.html").read()
def mk(mcq):
    d = ("const CARDS=" + json.dumps(slim, ensure_ascii=False) + ";\nconst MCQ=" + json.dumps(mcq, ensure_ascii=False) + ";\n"
         + open(f"{B}/app/lessons.js").read() + "\n" + open(f"{B}/app/extras.js").read()).replace("</script", "<\\/script")
    return t.replace("/*__DATA__*/", d)
full = mk(mc); open(f"{B}/out/business-law-kit.html", "w").write(full)
pub = mk([q for q in mc if q["src"] != "mock2022"]); open(f"{B}/out/public.html", "w").write(pub)
print("built", len(full) // 1024, "KB", len(slim), "cards", len(mc), "mcq; public", len(pub)//1024, "KB")
