import json, os, shutil, subprocess, re
B = "/home/claude/law"; R = "/home/claude/business-law-"
cards = json.load(open(f"{B}/out/cards.json"))
os.makedirs(f"{R}/notes", exist_ok=True); os.makedirs(f"{R}/recall-decks", exist_ok=True)
os.makedirs(f"{R}/icons", exist_ok=True); os.makedirs(f"{R}/scripts/app", exist_ok=True); os.makedirs(f"{R}/practice", exist_ok=True)

names = {1:"unit-1-legal-system",2:"unit-2-entrepreneur",3:"unit-3-incorporation",4:"unit-4-general-meeting-directors",
         5:"unit-5-directors-liability",6:"unit-6-capital-increase-reduction",7:"unit-7-structural-changes",
         8:"unit-8-trademarks-patents",9:"unit-9-competition",10:"case-studies"}
for u, fn in names.items():
    cs = [c for c in cards if c["unit_no"] == u]
    out = [f"# {cs[0]['unit']}\n", f"{len(cs)} flashcards · same content as the app and the RECALL decks.\n"]
    sec = None
    for c in cs:
        if c["section"] != sec:
            sec = c["section"]; out.append(f"\n## {sec}\n")
        out.append(f"**Q: {c['front']}**\n\n{c['back']}\n")
        if c.get("explain"): out.append(f"> {c['explain'].replace(chr(10), chr(10)+'> ')}\n")
        out.append("")
    open(f"{R}/notes/{fn}.md", "w").write("\n".join(out))

# cases → markdown (HTML inside is rendered by GitHub)
js = open(f"{B}/app/extras.js").read()
node = "const fs=require('fs');" + js + ";fs.writeFileSync('/tmp/cases.json',JSON.stringify(CASES));"
subprocess.run(["node", "-e", node], check=True)
cases = json.load(open("/tmp/cases.json"))
md = ["# Case studies 1–3 – model answers\n", "Self-made model answers to the case dossier questions (check them against the seminar discussion). Case 4 (agency & banking) is for Units 10–12.\n"]
for c in cases:
    md.append(f"\n## {c['title']} ({c['units']})\n\n**Facts.** {c['facts']}\n")
    for q in c["qs"]:
        md.append(f"\n### {q['q']}\n\n{q['a']}\n\n*Key points:* " + " · ".join(q["keys"]) + "\n")
open(f"{R}/practice/case-model-answers.md", "w").write("\n".join(md))

for z in os.listdir(f"{B}/out"):
    if z.endswith(".zip"): shutil.copy(f"{B}/out/{z}", f"{R}/recall-decks/{z}")
subprocess.run(["python3", f"{B}/wrap.py", f"{B}/out/public.html", f"{R}/index.html"], check=True)
for f in ("manifest.webmanifest", "sw.js"): shutil.copy(f"{B}/pwa/{f}", f"{R}/{f}")
for f in os.listdir(f"{B}/pwa/icons"): shutil.copy(f"{B}/pwa/icons/{f}", f"{R}/icons/{f}")
shutil.copy(f"{B}/sheet/business-law-sheet.pdf", f"{R}/cheat-sheet.pdf")
mcs = open(f"{B}/mc.py").read()
a = mcs.index("# ─────────── OFFICIAL MOCK"); b = mcs.index("# ─────────────────────────── BANK")
open(f"{R}/scripts/mc.py", "w").write(mcs[:a] + "# (official 2022 mock questions omitted from the public repo – course material)\n" + mcs[b:])
for f in ("cards.py", "build.py", "wrap.py", "gen_repo.py"): shutil.copy(f"{B}/{f}", f"{R}/scripts/{f}")
shutil.copy(f"{B}/sheet/business-law-sheet.tex", f"{R}/scripts/business-law-sheet.tex")
for f in ("template.html", "lessons.js", "extras.js"): shutil.copy(f"{B}/app/{f}", f"{R}/scripts/app/{f}")
open(f"{R}/.nojekyll", "w").write("")
print("repo files ready")
