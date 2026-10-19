"""Business Law I (ESADE BBA) – midterm flashcards. Source of truth for the app + RECALL zips."""
import json, os, shutil, zipfile, sys

SUBJECT = "Business Law I"
U = {
 1: "Unit 1 – The Law, the Rule & the Legal System",
 2: "Unit 2 – Business Law & the Entrepreneur",
 3: "Unit 3 – Capital Companies: Incorporation",
 4: "Unit 4 – Corporate Bodies I: General Meeting & Directors",
 5: "Unit 5 – Corporate Bodies II: Directors' Duties & Liability",
 6: "Unit 6 – Amendments to the By-laws: Capital Increase & Reduction",
 7: "Unit 7 – Structural Changes & Company Termination",
 8: "Unit 8 – Distinctive Signs & Industrial Creations",
 9: "Unit 9 – Free Competition & Unfair Competition",
 10: "Case Studies 1–3 (Patinetes Eléctricos & IP/competition cases)",
}
SRC = {1: "Notes Unit 1", 2: "Notes Unit 2", 3: "Notes Unit 3 + annexes", 4: "Notes Unit 4", 5: "Notes Unit 5",
       6: "Notes Unit 6 + annex", 7: "Notes Unit 7", 8: "Notes Unit 8 + content guide", 9: "Notes Unit 9", 10: "Case Studies Dossier 2026-27"}

cards = []
_cur = {"u": 1, "s": ""}
def unit(n): _cur["u"] = n
def sec(s): _cur["s"] = s
def c(cid, front, back, explain=None, tags=()):
    u = _cur["u"]
    d = {"id": f"bl-u{u}-{cid}", "unit": U[u], "unit_no": u, "section": _cur["s"], "front": front.strip(), "back": back.strip(),
         "front_image": None, "back_image": None, "tags": ["midterm", *tags], "source": SRC[u]}
    if explain: d["explain"] = explain.strip()
    cards.append(d)

# ═══════════════════════════ UNIT 1 ═══════════════════════════
unit(1)
sec("1.1 Law: objective vs subjective")
c("objective", "What is law in the **objective** sense?",
  "The **organised set of rules** made by those with power to do so in a society, which can be **imposed coercively** (e.g. \"Spanish law\").",
  "Think of objective law as *the rule book* of a country. Every rule is part of a structured whole = the **legal system**.")
c("subjective", "What is law in the **subjective** sense?",
  "The **power of a person** to do, demand or prohibit something, **protected by objective law**, with the possibility of going to court (\"I have the right to…\").",
  "Subjective law only exists because objective law recognises it. Objective = the rule book; subjective = *your* right that comes out of it.")
sec("1.2 The legal rule: characters")
c("two-characters", "What are the **two characters** of a legal rule?",
  "1. **Generality**\n2. **Coercibility** (coercive / enforceable character)",
  "Mnemonic: a legal rule is **G**eneral and **C**an be forced – **GC**.")
c("generality", "What does **generality** of a legal rule mean? Give the example from the notes.",
  "Rules address **abstract categories**, not individual cases. A new formal obligation for *all* public limited companies = legal rule. A decree **appointing one person** to a public office = **not** a legal rule (no generality).",
  "Ask yourself: does it target a *type* of person/situation or *one specific* person? Only the first is a legal rule.", ["trap"])
c("coercibility", "What does **coercibility** mean? Why is saying \"good morning\" in class not a legal rule?",
  "If a rule is not obeyed voluntarily, compliance can be **imposed by institutionalised force** (power given to the **courts**). Greeting someone is a **social rule** – nobody can force you by institutional force.",
  "Social norms, manners and educational rules regulate coexistence too, but they lack institutionalised enforcement.")
c("three-elements", "Which three elements make sure legal rules are applied effectively?",
  "1. **Interpretation**\n2. **Validity** (birth → death of the rule)\n3. **Effectiveness** (ignorance of the law is no excuse)")
c("art3cc", "How must rules be **interpreted** (art. 3 CC)?",
  "According to the **proper meaning of their words**, in connection with the **context**, their **historical and legislative background** and the **social reality** of the time when applied, attending to their **spirit and purpose**.",
  "If the literal meaning is not enough, the usual next step is the **purposive approach**: what did the legislator want to achieve with the rule?")
c("purposive", "What is the **purposive approach** to interpretation?",
  "Interpreting a rule according to its **spirit and purpose** – the reason why the legislator included it – when the literal interpretation is insufficient.")
c("enactment", "When is a Spanish state rule **enacted (promulgated)** and when does it **enter into force**?",
  "Enacted by publication in the **BOE** (Boletín Oficial del Estado). It enters into force **20 days after publication**, unless the rule itself shortens or lengthens that period.",
  "Publication guarantees **legal certainty**: since it's in the BOE, nobody can claim not to know it.", ["numbers"])
c("vacatio", "What is the **vacatio legis**? Example?",
  "The period between **publication** and **entry into force**. Example: RDL 8/2019 (employers must record working hours) had a **two-month** vacatio legis to give companies time to adapt.", tags=["numbers"])
c("repeal", "Express vs tacit **repeal**?",
  "**Express**: the new rule explicitly derogates the old one.\n**Tacit**: a new rule (same or **higher** rank) regulates the same matter differently → the old rule is invalid in everything inconsistent, even without saying so.")
c("effectiveness", "State the **principle of effectiveness** (art. 6 CC).",
  "\"**Ignorance of the law does not excuse from compliance** thereof.\" Rules bind whether or not people know them, because they were published.",
  "Practical consequence: entrepreneurs should get advice from lawyers/consultants – not knowing a tax or employment rule is never a defence.")
sec("1.3 Mandatory vs dispositive rules")
c("mand-disp", "**Mandatory** vs **dispositive** rules?",
  "**Mandatory**: impose or prohibit conduct **absolutely**, even against the will of the parties. Acts against them are **void** (art. 6.3 CC).\n**Dispositive**: apply **only if the parties do not agree otherwise** (supplementary).",
  "DE: zwingendes Recht vs dispositives (abdingbares) Recht.")
c("art314", "Art. 314 CCom: loans do not accrue interest unless agreed in writing. Mandatory or dispositive?",
  "**Dispositive** – parties may agree interest; only if there is **no written agreement** does the default (no interest) apply.", tags=["trap"])
sec("1.4 Sources of law")
c("material-formal", "**Material** vs **formal** sources of law?",
  "**Material**: the **body with power to enact** rules (State, Autonomous Communities, EU institutions…).\n**Formal**: the **forms** the rules take – art. 1 CC: **law, custom, general principles of law**.")
c("art1cc", "What are the formal sources of Spanish law and in which **order** do courts apply them (art. 1 CC)?",
  "1. **Law** (statutes)\n2. **Custom** – only if there is no applicable law, if not contrary to morals/public order, and if **proven**\n3. **General principles of law** – if neither law nor custom",
  "Mnemonic **L-C-P**: Law → Custom → Principles.")
c("caselaw", "Is **case law** a source of law in Spain?",
  "**No.** Judges don't make rules. But the doctrine **repeatedly** upheld by the **Supreme Court** **complements** the legal system (art. 1.6 CC).",
  "Classic MC trap: \"case law is the 4th source of law\" → false. It only *complements*.", ["trap"])
c("custom", "What is **custom**?",
  "A source of law of **spontaneous creation** by social groups through their practices. Historically very important (Business Law was born customary), today less so because legislators regulate almost everything.")
c("principles", "Where are most **general principles of law** found? Give examples.",
  "In the **Constitution**: justice, freedom, equality… They resolve cases with **no law and no custom** and also shape the whole system.")
sec("1.5 Hierarchy of statutes")
c("hierarchy-rule", "State the **principle of hierarchy** (art. 9.3 CE).",
  "A rule of **lower rank** may not contradict, invalidate or repeal a rule of **higher rank** – the opposite is possible.")
c("pyramid", "List the Spanish **hierarchy pyramid** from top to bottom.",
  "1. **Constitution**\n2. **International treaties; EU law**\n3. **Acts** (ordinary & organic)\n4. **Royal Legislative Decrees; Royal Decree-Laws**\n5. **Royal Decrees** (regulations)\n6. Lower rules (ministerial orders…)",
  "Note: RDL and RLD are made by the Government but have the **status of an act** (same rank in practice). The notes' pyramid draws them just under acts.")
c("act", "What is an **act** (ley) in the technical sense? Who enacts it?",
  "A rule enacted by the body with **maximum legislative power**: Parliament = **Cortes Generales** (Congress + Senate).")
c("rdl", "**Royal Decree-Law** vs **Royal Legislative Decree**?",
  "Both are made by the **Government** with the **status of an act**.\n- **RDL**: for **extraordinary and urgent need**.\n- **RLD**: by **express delegation** of Parliament through a **framework law** (e.g. the LSC is RLD 1/2010).",
  "Why delegate? Urgency (Parliament is slow) or technical complexity.")
c("rd", "What is a **Royal Decree** and what happens if it contradicts an act?",
  "A rule from the **Government's own power** (not delegated), below acts/RDL/RLD – often a **regulation** developing an act (e.g. IRPF Regulation). If it contradicts an act it is **null and void**.")
sec("1.6 State, regions, international & EU law")
c("state-ccaa", "Is the relationship between **State law** and **Autonomous Communities' law** one of hierarchy?",
  "**No – it is one of competence.** Arts. **148 and 149 CE** + each **Statute of Autonomy** distribute the matters. Regional laws are published in their own gazettes (DOGC, BOCM…).",
  "Mock exam Q7(a) says State rules always rank above regional rules → **false**.", ["trap"])
c("treaties", "Where do **international treaties** sit and what if one contradicts the Constitution (art. 95 CE)?",
  "Above all internal statutes, **below the Constitution**. A treaty contrary to the Constitution requires **prior constitutional amendment**.")
c("eu-primary", "What is EU **primary** legislation?",
  "The **founding Treaties** – the \"rules of the game\" (similar to a constitution). **Directly applicable**.")
c("eu-secondary", "What are the two main types of EU **secondary** legislation?",
  "**Regulations** and **Directives**.")
c("regulation", "What is an **EU Regulation**? Example?",
  "Secondary law **directly applicable** to all citizens of Member States as if it were internal law – **no transposition** needed. Example: **GDPR** (Reg. 2016/679), which replaced the national data-protection rules.",
  "Don't confuse an **EU Regulation** (like a European act) with a Spanish **regulation** (a Royal Decree below an act).", ["trap"])
c("directive", "What is an **EU Directive**?",
  "Secondary law addressed to **Member States** to **harmonise** their laws; States must **implement (transpose)** it into national law. In principle it binds citizens only after transposition – but the Supreme Court (STS 428/2007) says national law must be **interpreted in accordance with EU law** anyway.",
  "Mock exam Q2: \"Directives are secondary EU provisions that standardise Member States' laws\" → **correct statement (d)**.", ["mock"])
c("eu-prec", "National law vs EU law: competence or hierarchy?",
  "In principle **competence** (the EU legislates where States gave it competence), but in case of **conflict EU law prevails**. Spain is in the EU since **1986**.", tags=["numbers"])

# ═══════════════════════════ UNIT 2 ═══════════════════════════
unit(2)
sec("2.1 Business Law: history & concept")
c("origin", "When and why did Business Law arise as a special law?",
  "In the **Middle Ages**, after the fall of the Roman Empire, as a **customary** law of **traders** (merchants, guilds, **Consulados del Mar**).")
c("codes", "Which Commercial Codes did Spain have?",
  "**1829** (first, after the French code of **1807**) and the **1885 Commerce Code**, still the framework code today – though heavily \"sifted\" (most articles repealed and replaced by special laws).", tags=["numbers"])
c("definition", "Define **Business Law** (notes).",
  "The part of the **private** legal system for **entrepreneurs** and their **legal status**, dealing with their **activities in the market** carried out **through an enterprise**.")
c("three-notes", "Three fundamental notes of Business Law?",
  "1. Part of **private law**\n2. **Special** private law (vs general civil law)\n3. The law of **entrepreneurs**")
c("not-bl", "Are **employment law** and **tax law** part of Business Law?",
  "**No.** They affect entrepreneurs but are separate disciplines. Not every rule affecting entrepreneurs is Business Law.", tags=["trap"])
sec("2.2 Sources of Business Law")
c("art38", "What does **art. 38 CE** say and why is it important?",
  "**Free enterprise** is recognised **within the framework of a market economy**; public authorities guarantee and protect it. It is the constitutional basis of trade activity and of competition law.")
c("art38-impacts", "Impacts of the constitutional market-economy framework?",
  "- Recognition of entrepreneurs' **private initiative**\n- Freedom is subordinate to **general interest** (e.g. anti-competitive practices are illegal)\n- **Market unity**\n- **Protection of consumers and users**")
c("art149", "Who has competence over commercial legislation in Spain?",
  "The **State, exclusively** (art. **149.1.6 CE**) – to guarantee **market unity**.")
c("art2ccom", "In what order are **acts of commerce** governed (art. 2 CCom)?",
  "1. **Commerce Code** (and laws replacing its provisions)\n2. **Business practice/usage** of each place\n3. **Ordinary civil law**",
  "Unlike in civil law, **business custom comes before civil law** – a trace of Business Law's customary origin.", ["trap"])
c("art50ccom", "What limitation does **art. 50 CCom** add?",
  "For **business contracts** without a specific law, **general civil law** applies directly – business usage does **not** take precedence. Important limit because contracts are exactly where customs matter most.", tags=["trap"])
c("lex-specialis", "What is the **lex specialis** principle?",
  "**Specialised acts prevail over general acts.** It explains the many special commercial laws (LSC, Trademarks Act, LDC…) next to the old CCom.")
c("eu-influence", "How does EU law shape Spanish Business Law today?",
  "Most commercial rules either **apply EU Regulations directly** (trademarks, consumer rights, free competition) or **implement Directives** (company law).")
sec("2.3 Enterprise vs entrepreneur")
c("enterprise", "Define **enterprise** (empresa). Does it have legal personality?",
  "An **organised set of capital** (material & immaterial elements) **and work** (people) used to produce/distribute goods or services for the market. It has **no legal personality** – it must be linked to a person: the **entrepreneur**.",
  "When people say \"the enterprise signed a contract\" they speak figuratively – legally it is the **entrepreneur** (the owner) who holds rights and obligations.", ["trap"])
c("entrepreneur", "Define **entrepreneur** in the legal sense.",
  "The **natural or legal person** that, **in its own name** and in an **organised and professional** manner, carries out an economic activity of producing/distributing goods or providing services **for the market**, assuming the **responsibilities** and holding the **rights** arising from it.",
  "Legal sense ≠ economic sense. Economically the \"entrepreneur\" is whoever makes decisions (directors, managers). Legally it is **in whose name** the activity is run.")
c("three-features", "Three defining features of the legal concept of entrepreneur?",
  "1. **Organisational** activity\n2. **Professional** activity (habitual, public, for the market, usually for profit)\n3. Acts **in its own name**",
  "Mnemonic **O-P-O**: Organises, Professional, Own name.")
c("business-est", "Why is \"buying an **enterprise**\" legally wrong? What do you buy?",
  "You buy a **business / business establishment** (negocio, establecimiento mercantil): the assets **plus** pre-existing legal and financial relationships (contracts, employees, reputation, brand). An enterprise as such is just a set of assets/people.",
  "Mock exam Q1: \"enterprise\", \"entrepreneur\" and \"business/commercial establishment\" are **different concepts** → answer **(b)**.", ["mock"])
c("business-value", "Why is a running business usually worth more than the sum of its isolated assets?",
  "Because of the **legal relationships in force and the track record**: reputation of the brand, profitable contracts, customers. Starting from isolated assets you'd have no market background.")
c("art1ccom", "Who are businesspersons under **art. 1 CCom**?",
  "1. Those with legal capacity who engage in commerce **habitually**\n2. **Business or industrial companies** incorporated under the Code")
c("collaborators", "Are **directors, attorneys or employees** entrepreneurs?",
  "**No** – they act **in the name and on behalf of another** (the entrepreneur), don't assume the obligations and don't receive the profits.")
sec("2.4 Types of entrepreneurs")
c("types", "Three classifications of entrepreneurs?",
  "1. **Natural** (individual / sole trader) vs **legal** person (business entity)\n2. By **size**: small, medium, large\n3. **Private** vs **public**")
c("size", "Does the size of the enterprise change the legal status?",
  "**No** – the CCom gives one status regardless of size. But special rules differ, e.g. **accounting** (General Accounting Plan vs SME plan; art. 25 CCom) and corporate tax for small companies. SME parameters: **Commission Regulation (EU) 651/2014, Annex I**.")
c("public-ent", "What is a **public enterprise**?",
  "An entity held **totally or partly by a public-law body** (town hall, Autonomous Community…) carrying out an **economic activity** with some autonomy from its public functions. Exceptional in a market economy.")
sec("2.5 Legal status of the entrepreneur")
c("status-blocks", "What does the **legal status of the entrepreneur** include?",
  "1. **Professional duties**\n2. **Rights**\n3. **Legal capacity**\n4. **Liability regime**")
c("duties", "Three **professional duties** of every entrepreneur?",
  "1. Keep **accounts** and documentation (art. **25** CCom)\n2. **Legal publicity** – registration in the **Mercantile Registry** (mandatory for companies, **optional for individual entrepreneurs**)\n3. Duty to respect **free and fair competition** (LDC + Unfair Competition Act)",
  "Trap: registration is **not** mandatory for sole traders.", ["trap"])
c("registry-purpose", "Double purpose of registering in the Mercantile Registry?",
  "1. **Presumption of legality** of registered elements (filter of lawfulness)\n2. **Market transparency** – publicity of sensitive information for third parties")
c("rights", "Rights conferred by the status of entrepreneur?",
  "1. **Participate in the market** competing freely\n2. **Demand fair competition** (stop abuse/restrictive practices)\n3. **Exclusive use** of distinctive signs (trademarks, trade names) and **exclusive exploitation** of industrial creations (patents)")
c("capacities", "**Legal capacity** vs **capacity to operate (act)**?",
  "**Legal capacity**: ability to **hold rights and obligations** – from **birth**, for life.\n**Capacity to operate**: ability to perform acts with legal effect – requires **legal age (18)** and **not being judicially incapacitated**.",
  "Baby example: a newborn can **own** a bank account (legal capacity) but cannot **dispose** of it (no capacity to operate). Mock Q6 → (a).", ["mock", "trap"])
c("art4ccom", "Who can be an **individual entrepreneur** (art. 4 CCom)?",
  "Those of **legal age** with **free disposal of their assets**.")
c("exceptions", "Two exceptions where minors/incapacitated persons can be entrepreneurs?",
  "1. A **minor or incapacitated heir** continuing the business of their **parents/testators**\n2. An entrepreneur who **becomes incapacitated** continuing his/her own previous business\n→ in both cases they act **through legal representatives**.",
  "Justified by the principle of **preserving the enterprise**.")
c("incompat", "**Incompatibilities (conflicts of interest)** – absolute vs relative?",
  "Restrictions on people with public functions to protect impartiality.\n**Absolute**: no business anywhere in Spain (members of Government, senior management of agencies).\n**Relative**: only in the territory where they serve (**judges, prosecutors**).")
c("prohibitions", "Three legal **prohibitions to compete**?",
  "1. **Agents/managers/representatives** vs their principal (art. **288 CCom**)\n2. **Workers** vs their employer (Workers' Statute)\n3. **Directors** vs their company (LSC) – unless **express consent** of the company",
  "Breach → removal/dismissal + damages, **but contracts concluded remain valid** vs bona fide third parties.", ["trap"])
c("disqual", "What is a **disqualification** (inhabilitación)?",
  "Prevention of business activity **as a sanction** for irregularities; can be **temporary or perpetual**. Some activities also need **prior administrative authorisation**.")
sec("2.6 Liability regime")
c("liab-three", "Three questions of the entrepreneur's liability?",
  "1. **For what facts?** Acts/omissions causing damage through fault or negligence – **contractual and non-contractual**\n2. **For whom?** Own acts **and** those of dependants (employees, representatives)\n3. **With what?** **All present and future assets** (art. **1911 CC**)",
  "Mock Q5 → (a): liable even for damages caused by workers in the exercise of their job.", ["mock"])
c("universal", "Individual entrepreneur: is there a separation between business and private assets?",
  "As a rule **no** – liable with **all present and future assets**, business and private. (Legislative trend to protect the habitual residence.)",
  "That's why sole traders often form an **S.L.U.** – a single-member company limits liability to the company's assets.")
sec("2.7 Business entities")
c("art116", "What is a trading company (art. 116 CCom) and when does it get legal personality?",
  "A contract by which **two or more persons** put goods/industry into a **common fund to obtain profit**. Once incorporated per the Code it has **legal personality** in all its acts and contracts.")
c("personality-effects", "Three effects of legal personality of a company?",
  "1. Subject of **rights and obligations** (full capacity externally and internally)\n2. Acquires **business status** (subject to its articles)\n3. **Owns its assets** separate from the members → separation of liability")
c("needs-person", "Why does a company need natural persons to act?",
  "\"It has no hands to sign nor a brain to decide\" → **representatives**: **legal** (scope set by law, e.g. directors) or **voluntary** (powers of attorney granted at will).")
c("entity-liab", "With what does a business entity answer for its debts?",
  "**Always with all its assets** (art. 1911 CC), whatever its type. *Whether members also answer* depends on the type: yes in partnerships, no in capital companies.")
c("irregular", "What is an **irregular company** and what liability does it face?",
  "A company operating **without registration** in the Mercantile Registry. Managers are **jointly and severally liable** to third parties (art. **120 CCom**) and members answer like a **general partnership** (personally) – **even if it is a capital company**.",
  "Internal liability agreements between members have no effect against third parties.", ["trap"])
c("art122", "Four basic types of trading companies (art. 122 CCom)? Closed list?",
  "1. **General partnership** (S. colectiva)\n2. **Limited partnership** (S. comanditaria)\n3. **Public limited company** (S.A.)\n4. **Private limited company** (S.R.L./S.L.)\nNot closed – \"**as a general rule**\" → the law may create new types.")
c("capital-cos", "Which are **capital companies** (art. 1 LSC)?",
  "**S.A.** (public limited), **S.R.L./S.L.** (private limited) and the **sociedad comanditaria por acciones** (partnership limited by shares). Regulated by the **LSC – RLD 1/2010**.")
c("key-difference", "Most important difference: partnerships vs capital companies?",
  "The **liability of members**. Partnership members: **personal, unlimited, subsidiary and joint & several**. Capital company members: **not personally liable** for company debts (art. 1 LSC).",
  "Mock Q8 → (b): members are liable for company debts **only in personalistic companies (partnerships)**.", ["mock"])
c("subsidiary", "What do **personal, unlimited, subsidiary, joint & several** mean for a general partner?",
  "- **Personal**: with own assets\n- **Unlimited**: for all debts, present and future assets\n- **Subsidiary**: only if the partnership can't pay\n- **Joint & several**: creditor can claim **the whole** from any partner, who can later claim the others' shares")
c("veil", "What is **lifting the corporate veil**?",
  "When members **abuse** the legal personality (mixing personal and company assets, acting as if the company didn't exist), courts **disregard the separation** and hold them **personally liable** (arts. **6.4 and 7 CC** – abuse of rights/fraud).")
c("gp", "General partnership: 3 characteristics + name rules?",
  "1. Partners **liable** (personal, unlimited, subsidiary, joint & several)\n2. **Personalistic** – trust; no transfer of partner status without consent (art. 143 CCom)\n3. Business **name and one signature**: name of all/some partners (+ \"y Cía.\") + \"S.C.\"/\"S.R.C.\". A non-partner whose name appears is **liable as a partner** (art. 126 CCom).")
c("lp", "Limited partnership: two kinds of partners?",
  "**General partners**: unlimited liability, **manage**, names in business name.\n**Limited partners**: liable only **up to their contribution**, **no management**, **name not allowed** in the business name, can transfer status **without consent**. Abbr. **S.Com. / S. en C.**")
c("lp-shares", "Limited partnership vs partnership limited by shares?",
  "Limited partnership: capital in **stakes**, CCom. Partnership limited by **shares**: capital in **shares** (securities) → treated as a **capital company** (LSC). Both have general + limited partners.")
c("sa-def", "Define the **S.A.** (public limited company).",
  "Company of **capitalist character**, capital divided into **shares**, made up of members' contributions, members **not personally liable** for company debts.")
c("sl-def", "Define the **S.R.L./S.L.** (private limited company). Why \"hybrid\"?",
  "Capitalist company, capital divided into **stakes (participaciones)**, members not personally liable. **Hybrid**: fully capitalist towards **third parties**, but **internally flexible/personalistic** – e.g. by-laws can give a minority member the majority of votes (impossible in an S.A.).",
  "S.L. is the **most used** company in Spain (lower minimum capital + flexibility).")

# ═══════════════════════════ UNIT 3 ═══════════════════════════
unit(3)
sec("3.1 S.A. vs S.L. – choosing")
c("min-capital", "Minimum share capital: **S.A.** vs **S.L.**?",
  "**S.A.: €60,000** · **S.L.: €3,000**",
  "Exam answer = the notes' figures. (Real-life update: Ley 18/2022 \"Crea y Crece\" allows an S.L. with **€1**, with extra safeguards – but answer **€3,000** in this course.)", ["numbers"])
c("paid-up", "How much capital must be **paid up at incorporation**?",
  "**S.L.: 100%** (fully paid). **S.A.: at least 25%** of each share's par value – the rest is **called-up capital (dividendos pasivos)** paid later (art. 79 LSC).",
  "Mock Q16(a) \"capital always needs to be fully paid-up\" → **false** (S.A. allows 25%).", ["numbers", "mock"])
c("which-type", "When **must** founders choose an S.A.?",
  "- Capital **< €60,000** → must be an **S.L.**\n- Shares to be **listed** on a stock exchange → must be an **S.A.**\n- Otherwise free choice: S.A. = more formalities but **free transfer**; S.L. = fewer formalities, presumes **stable membership**.")
c("quant-qual", "S.L. vs S.A.: quantitative vs qualitative importance?",
  "S.L. dominate **quantitatively** (SMEs, low capital, stable members). S.A. dominate **qualitatively** (large corporations, stock market, free transfer of shares).")
c("annex-table", "S.A. vs S.L. – non-cash contributions, transfer, attendance, votes?",
  "- Non-cash: **S.A. expert report** required (as a rule); **S.L. no report**\n- Shares (S.A.) = **negotiable securities**; stakes (S.L.) **not**\n- Transfer: **S.A. free** (by-laws may restrict); **S.L. restricted**\n- Attendance: **S.L. cannot be restricted**; S.A. may require a **minimum number of shares**\n- Votes: **S.L. one per stake** (unless by-laws); **S.A. per nominal value**",
  tags=["numbers"])
c("board-term", "Board size and directors' term: S.A. vs S.L.?",
  "Board: **min 3** in both; max **12 in S.L.**, **no max** in S.A.\nTerm: **S.A. max 6 years** (re-electable for the same max periods); **S.L. may be indefinite**.",
  tags=["numbers"])
sec("3.2 Deed of incorporation & by-laws")
c("incorp", "How is a capital company incorporated?",
  "By a **deed of incorporation** executed by the founders **before a notary public**, then **registered in the Mercantile Registry** (Registro Mercantil) of the province of the registered office → **legal personality** as a capital company.",
  "Mind map steps: **name certificate** (Central Registry) → **tax number (NIF)** → **by-laws** → **notary** → **registry**.")
c("founders", "Who are the **founders**? Minimum number of founders?",
  "The persons (natural or legal) who **execute the deed** and **subscribe all shares / take up all stakes**. **No minimum** – one person can found an **S.A.U.** or **S.L.U.** (single-member company).",
  "Wording: you **subscribe shares** (S.A.) but **take up / assume stakes** (S.L.).", ["trap"])
c("unipersonal", "Why do single-member companies exist? What if a company becomes single-member later?",
  "To overcome the **universal liability** of the sole trader: one person runs a business but is liable only with the company's assets. If it becomes single-member later → **deed declaring sole proprietorship** + registration. Same regime, some **added formalities**.")
c("deed-content", "Minimum content of the **deed of incorporation** (art. 22 LSC)?",
  "- **Identity** of founders + will to form an S.A./S.L.\n- **Contributions** of each + numbering of shares/stakes\n- The **by-laws**\n- Initial organisation of the **administration** and identity of directors\n- S.A.: approximate **incorporation expenses**")
c("bylaws", "What are the **by-laws** (estatutos sociales / articles of association)?",
  "The **rules of organisation and operation** of the company; part of the deed, registered → **binding** on members and directors.")
c("bylaws-content", "Minimum content of the **by-laws** (art. 23 LSC)?",
  "1. **Company name** (+ S.A./S.L.)\n2. **Corporate purpose**\n3. **Registered office** (in Spain)\n4. **Capital** (in euros; S.A.: unpaid part)\n5. **Shares/stakes** (number, par value…)\n6. **Structure of management body** & GM operation\n7. **Ancillary commitments** (if any)")
c("name", "Rules for the **company name**?",
  "Must include **S.A.** or **S.R.L./S.L.**; must not be **identical** to an existing company's name nor contrary to public order → certificate from the **Central Mercantile Registry**.")
c("office", "Where must the **registered office** be?",
  "In **Spanish territory**, where the **effective administration and management** is, or where the main establishment/centre of operations is.")
c("defaults", "Which defaults apply if the by-laws say nothing?",
  "**Duration: unlimited**; **start of operations: date of the deed**; **fiscal year ends 31 December**.", tags=["numbers"])
sec("3.3 Company in formation & registration")
c("in-formation", "What is a **company in formation**? Which acts bind the company after registration (art. 36 LSC)?",
  "The period between the deed and registration. Acts **necessary for registration** bind the company automatically; **other acts** bind it only if it **expressly accepts** them after registration – otherwise those who acted are liable.")
c("one-year", "Deadline to register? Consequence of missing it?",
  "**One year**. Otherwise it becomes an **irregular company**: any member may request **dissolution**, liquidation and refund of contributions (arts. 39–40 LSC). If it already started business: **general-partnership liability** of members for debts incurred before registration.",
  tags=["numbers"])
c("registry-function", "Why is publicity through the Registry so important for capital companies?",
  "Because members are **not personally liable**, third parties can only rely on the **company's assets**. They need reliable info on **capital, directors, accounts** → transparency and **legal security**. Registry = **filter of lawfulness + publicity**.")
c("register-what", "Which later acts must also be registered?",
  "**Amendments of by-laws**, **appointment/removal of directors**, **annual accounts** (deposit) and many other corporate acts.")
sec("3.4 Contributions")
c("contrib", "What can be contributed to capital? What can **never** be?",
  "**Cash** or any **asset/right with economic value** (real estate, machinery, trademarks, credit rights, goodwill…). **Never work or services** (art. **58.2 LSC**).",
  "Mock Q10(b) \"work by a member can be a non-cash contribution in an S.L.\" → **false**. Correct: (d) cash or non-cash in both S.A. and S.L.", ["mock", "trap"])
c("cash", "How are **cash contributions** proven?",
  "The notary attaches a **bank certificate** proving the deposit in an account in the name of the company in formation. Contributions in **euros**.")
c("noncash", "Valuation safeguards for **non-cash contributions**?",
  "**S.A. & S.L.**: contributing member is **liable** to company, members and third parties for the **reality and value** (art. 30 LSC).\n**S.A. additionally**: **independent expert report** appointed by the **Registrar** (art. 67 LSC), annexed to the deed (exceptions art. 69).",
  tags=["trap"])
c("ancillary", "What are **ancillary commitments** (prestaciones accesorias)?",
  "**Services** by members **beyond their capital contribution**, free or paid; **never part of capital** (art. 86 LSC). By-laws must set content, paid/free and consequences of breach.",
  "This is how Pedro's **work** can enter the company in Case 1 – not as capital, but as an ancillary commitment.", ["case"])
sec("3.5 Capital, equity, reserves")
c("capital", "What is **share capital** (capital social)?",
  "The **total amount of members' contributions**, stated in the by-laws (\"nominal capital\"). Stable figure.")
c("equity", "What is **equity** (patrimonio neto / real capital)?",
  "**Assets − liabilities (debts to third parties)** = Capital + reserves (undistributed profits) ± other items (grants, share premium, accumulated losses).",
  "At incorporation **capital = equity**. Later they diverge: profits kept → equity > capital; losses → equity < capital. Mock Q11 → (d).", ["mock"])
c("principles", "Four principles protecting capital?",
  "1. **Determination** – always stated in the by-laws; changes only by amending by-laws\n2. **Full subscription & minimum payment** – all shares subscribed (S.A. min 25% paid)\n3. **Integrity** – par value must match an effective contribution\n4. **Minimum outlay** – not below €60,000 / €3,000, at incorporation **and during life**")
c("reserves", "Types of **reserves**?",
  "**Legal** (imposed by law), **statutory** (by-laws), **voluntary** (decided by GM), other special reserves. All come from **undistributed profits** and increase equity.")
sec("3.6 Members' rights & obligations")
c("member-obl", "Members' only basic **obligations** after contributing?",
  "1. Pay **called-up capital** (S.A., if any)\n2. Perform **ancillary commitments** (if in by-laws)\nEverything else is a **right**, not an obligation.")
c("member-rights", "Six basic **rights** of members?",
  "1. **Dividends** (273 LSC)\n2. **Liquidation dividend** (391)\n3. **Pre-emptive (preferential subscription) right** (304)\n4. **Attend and vote** at GM (179)\n5. **Challenge** resolutions (204)\n6. **Information** (197)",
  "Mnemonic **D-L-P-V-C-I**: \"**D**on't **L**et **P**eople **V**ote **C**areless **I**deas\".")
c("votes", "How are **votes** allocated in S.A. vs S.L.?",
  "**S.A.**: strictly **proportional to par value** of shares (non-voting shares possible).\n**S.L.**: **one vote per stake**, but the by-laws may set a different system (e.g. extra votes for certain stakes).")
sec("3.7 Par, book and fair value")
c("par", "Define **par (nominal) value**.",
  "The value the founders **freely assign** to each share/stake in the deed (or in a capital increase deed).")
c("book", "Define **book value** (valor teórico). Formula?",
  "The aliquot part of the **company's equity** per share: **Book value = Equity ÷ number of shares**.")
c("fair", "Define **fair (market) value**. Formula?",
  "The value at which **two independent, informed and interested parties** would exchange the shares: **Fair value = Book value ± expectations** (business valuation).",
  "Fair value is partly **subjective** (market expectations). Par value = objective fact; book value = accounting calculation.")
c("annex-ex", "Annex example: 75 members, €75,000 capital, 750 shares of €100. Retained earnings €100,000; expectations +€200,000. Book and fair value per share?",
  "Equity = 75,000 + 100,000 = **€175,000** → BV = 175,000 ÷ 750 = **€233.33**/share (€2,333.33 per member's 10 shares).\nFV = 175,000 + 200,000 = **€375,000** → **€500**/share (€5,000 per member).",
  "Rules: no losses & retained earnings → **BV > PV**; positive expectations → **FV > BV**; negative → FV < BV.", ["numbers"])

# ═══════════════════════════ UNIT 4 ═══════════════════════════
unit(4)
sec("4.1 Two corporate bodies")
c("bodies", "What are the two **corporate bodies** of a capital company?",
  "1. **General meeting** (junta general) – forms the **will of the members**\n2. **Managing body** (órgano de administración, \"directors\") – **manages and represents** the company")
c("members-represent", "Can members, as members, represent the company?",
  "**No.** Members **choose the directors** who represent and manage it. Members sit higher in hierarchy but have **no power of representation**.", tags=["trap"])
c("separation", "Must directors be members?",
  "**No** – unless the by-laws require it (art. **212.2 LSC**). Principle of **separation** between ownership (members) and management (directors). One person can be both, wearing two hats.")
sec("4.2 General meeting")
c("gm-def", "Define the **general meeting**. Who is bound by its resolutions?",
  "A **meeting of members** that adopts decisions **by majority** on matters within its competence. **All members** are bound – including **dissenting and absent** ones (they may challenge).")
c("gm-single", "Can a 70% member take GM decisions alone without a meeting?",
  "**No** – formalities must be met to **protect minorities**. Only exception: a **single-member company** (the sole member exercises the GM's powers).", tags=["trap"])
c("art160", "Competences of the general meeting (art. 160 LSC)?",
  "a) **Annual accounts**, distribution of profit, approval of management\nb) **Appoint/remove directors**, liquidators, auditors; **liability action** against them\nc) **Amend the by-laws**\nd) **Capital increase/reduction**\ne) **Remove/limit pre-emptive rights**\nf) Acquire/dispose/contribute **core assets** (> **25%** of total assets)\ng) **Transformation, merger, division, global assignment**, transfer of office **abroad**\nh) **Dissolution**\ni) **Final liquidation balance**\nj) Others set by law/by-laws",
  "Mnemonic: **A-D-B-C-P-C-S-D-L** → \"**A**ll **D**irectors **B**ring **C**offee, **P**artners **C**hoose **S**ugar, **D**ON'T **L**eave\". It's a **closed list** – the GM can't decide outside it.", ["numbers"])
c("core-assets", "When is an asset a **core asset** requiring GM approval?",
  "When the transaction amount exceeds **25% of the total assets** on the last approved balance sheet.", tags=["numbers"])
c("ordinary", "What is the **ordinary general meeting** and when must it be held (art. 164 LSC)?",
  "The meeting to approve **management**, **annual accounts** of the previous year and **distribution of profit**; must meet within the **first six months** of each fiscal year. Everything else → **extraordinary** GM.",
  "Mock Q13 → (d): the GM is ordinary or extraordinary **depending on the matters** dealt with.", ["numbers", "mock"])
c("convene-who", "Who **convenes** the GM and when must they?",
  "The **directors**:\n- **Ordinary GM every year**\n- When **appropriate** for the company\n- When **law/by-laws** require\n- When requested by members with **≥ 5% of capital**\n- In case of a **mandatory dissolution** cause",
  tags=["numbers"])
c("notice", "How is a GM **announced** and with what notice period?",
  "On the **company website** (or, if none, in the **BORME** + a widely-read newspaper of the province); by-laws may provide **individual written notice** to each member. Notice period: **S.A. ≥ 1 month**, **S.L. ≥ 15 days**.",
  tags=["numbers"])
c("universal", "What is a **universal meeting** (art. 178 LSC)?",
  "A GM validly held **without prior notice** when **all the capital is present or represented** and attendees **unanimously** agree to hold it and on its agenda.",
  "Typical of companies with **very few members** – you can only know it is universal when everybody is actually there.")
c("steps", "Three steps for valid GM decisions?",
  "1. **Convene** the members\n2. **Constitute** the meeting (S.A.: minimum **quorum**)\n3. **Hold** it and **vote** with the legal/statutory **majorities** (different S.A./S.L.)")
c("quorum", "Is a minimum **quorum** required to constitute the GM?",
  "**S.A.: yes** – % of capital present/represented; depends on the **matter** and on **first or second call** (arts. 193–194 LSC; stricter for by-law amendments, transformation, merger, division). **S.L.: no quorum.**",
  "S.A. quorum (LSC): ordinary matters **25%** 1st call / **any** 2nd call; special matters **50%** 1st / **25%** 2nd.", ["numbers", "trap"])
c("agenda", "Can the GM decide on matters **not on the agenda**?",
  "Only two exceptions: **removal of directors** and bringing a **liability action** against them.", tags=["trap"])
c("majorities", "How are GM **majorities** regulated?",
  "Different regimes for **S.A.** (also depends on 1st/2nd call) and **S.L.**, and stricter majorities for important matters (arts. 198–201 LSC). Resolutions go into the **minutes book** legalised by the Registry.",
  "See the cheat-sheet table: S.L. ordinary = majority of votes cast ≥ **1/3** of all votes; by-law amendments/capital changes **> 1/2** of all votes; merger/transformation/exclusion of pre-emptive right **2/3**.", ["numbers"])
c("challenge", "What can a member do if he disagrees with a GM resolution?",
  "He is **bound** by it, but may **challenge** it in court if it violates the **law, the by-laws** or harms the **company's interest** (art. 204 LSC).")
sec("4.3 Managing body")
c("mb-def", "Define the **managing body**.",
  "The corporate body that **legally represents** the company and **manages** it under the law (art. **209 LSC**). Management isn't listed exhaustively – it covers all acts aimed at the **corporate purpose**.")
c("who-director", "Who **cannot** be a director?",
  "Non-emancipated **minors**, the legally **incompetent**, persons **disqualified** under the Insolvency Act, persons **convicted** of certain offences (art. 213 LSC), and those with **incompatible public posts** (art. 14 CCom: judges, magistrates, heads of government…). Directors can be **natural or legal persons**.")
c("gm-no-interfere", "Can the GM interfere in management?",
  "As a rule **no** – directors manage autonomously; the GM appoints/removes them and **evaluates** management annually. Directors are personally liable even if the GM **authorised or ratified** the act.", tags=["trap"])
c("four-models", "Four ways of organising the managing body (art. 210 LSC)?",
  "1. **Sole director** (administrador único)\n2. **Joint and several directors** (solidarios) – **each acts alone** with full powers\n3. **Joint directors** (mancomunados) – must **act together**; **S.A.: max 2**\n4. **Board of directors** (consejo) – collegiate, majority; **min 3**, S.L. **max 12**",
  "Mind map shorthand: **SD, JD, J&SD, BoD**. Listed companies must have a board (art. 529 bis).", ["numbers"])
c("solidarios", "Joint **and several** directors vs **joint** directors – who can sign alone?",
  "**Joint and several (solidarios)**: **each one alone**.\n**Joint (mancomunados)**: **together** – none alone.",
  "Mock Q12(a) \"directors acting severally and jointly → all have to act jointly\" → **false**. Spanish: solidario = jeder allein; mancomunado = gemeinsam.", ["trap", "mock"])
c("joint-sa", "S.A. wants 3 directors acting **jointly**. Possible?",
  "**No** – S.A. may have at most **2 joint directors**; with more than two acting jointly it must be a **board of directors**.", tags=["trap", "numbers"])
c("change-model", "How is the organisational model of the managing body changed?",
  "The by-laws choose one of the 4 models; any change → **public deed** + **registration** in the Mercantile Registry (art. 210.4 LSC).")
c("term", "Directors' term of office?",
  "**S.A.: max 6 years**, re-electable for periods of the same maximum length. **S.L.: indefinite** (unless the by-laws limit it). The GM can **remove** them at any time following formalities, even before the end of the term.",
  "Mock Q14: the **incorrect** statement is (b) – S.L. directors are **not \"always\"** indefinite \"on a mandatory basis\". Mock Q12 → (d) board acts collegiately.", ["mock", "numbers"])

# ═══════════════════════════ UNIT 5 ═══════════════════════════
unit(5)
sec("5.1 Directors' obligations & duties")
c("art209", "What is the general competence of directors (art. 209 LSC)?",
  "To **manage and represent** the company. The law doesn't list specific acts – it sets **principles** for how they must act.")
c("framework", "Within which framework must directors act?",
  "1. **Law** (legal provisions)\n2. **General meeting & by-laws** (instructions not contrary to law)\n3. **Duty of care** and **duty of loyalty** (arts. 225–232 LSC)")
c("specific-obl", "Examples of specific legal obligations of directors?",
  "**Prepare annual accounts**, **convene the ordinary GM** yearly, convene the **extraordinary GM** when mandatory (e.g. dissolution cause), request **insolvency** in time.")
c("care", "**Duty of care / diligence** (art. 225 LSC)?",
  "Act with the diligence of an **orderly entrepreneur** (ordenado empresario), considering the nature of the post; subordinate **personal interest** to the company's; **adequate dedication**; duty to **demand and right to obtain information**.")
c("care-five", "Five manifestations of the duty of care?",
  "1. **Prudence**\n2. **Professional competence**\n3. **Dedication**\n4. **Information**\n5. **Surveillance & control** (vigilance)",
  "Mnemonic **P-P-D-I-S**: \"**P**edro **P**lans **D**aily **I**n **S**ilence\".")
c("orderly", "Two perspectives of the \"**orderly entrepreneur**\" standard?",
  "1. **Prudence** – no risks beyond what's reasonable after planning/analysis\n2. **Professional competence** – expertise appropriate to the company's complexity (a bank's directors need more than a small shop's)")
c("loyalty", "**Duty of loyalty** (art. 227 LSC)?",
  "Perform duties with the loyalty of a **faithful representative**, in **good faith** and in the **best interest of the company**.")
c("loyalty-list", "Basic obligations derived from loyalty (art. 228 LSC)?",
  "1. Use powers only for their **purpose**\n2. **Secrecy** – even **after** leaving office\n3. **Abstain** in conflicts of interest (except own appointment/removal)\n4. **Personal responsibility**, independent judgement\n5. **Avoid conflicts of interest** – **no competing** with the company")
c("loyalty-mandatory", "Can the by-laws limit the duty of loyalty? Can directors be exempted?",
  "The loyalty regime is **mandatory** – by-law clauses limiting it are void. But the **GM** may **exempt** a director in a specific case (use of assets, business opportunity, third-party advantage) when no damage to the company is expected (art. **230 LSC**).", tags=["trap"])
sec("5.2 Business judgment rule & risk monitoring")
c("bjr", "What is the **business judgment rule** (art. 226 LSC)?",
  "In **strategic and business decisions**, the orderly-entrepreneur standard is **deemed met** if the director acted:\n1. in **good faith**\n2. **without personal interest**\n3. with **sufficient information**\n4. following an **adequate decision procedure**",
  "It protects **managerial discretion**: a bad *result* alone does not mean a breach. It is a **rebuttable presumption** – whoever sues must prove the standards weren't met. Mnemonic **G-N-I-P**: Good faith, No interest, Information, Procedure.")
c("bjr-excl", "Which decisions are **excluded** from the business judgment rule?",
  "Decisions that **personally affect other directors or related persons**, especially those authorising **art. 230** operations (conflicts of interest).", tags=["trap"])
c("bjr-why", "Why does the law protect managerial discretion?",
  "To **remove the fear** of liability for unsuccessful decisions, **encourage risk-taking**, and avoid members **interfering** in management via liability actions.")
c("risk-mon", "Why is **risk monitoring** part of the duty of care?",
  "Directors must have an internal **information system** that detects gradual deterioration (profitability, finance) **in time**. No monitoring → possible **liability in vigilando** (breach of duty of care). **Unforeseeable** events (e.g. **Covid-19**) are **not** a breach.")
c("dno", "What is **D&O insurance** (mind map, Unit 5)?",
  "**Directors & Officers liability insurance**: the company buys a policy covering directors' personal liability and **legal defence costs**; it has **coverage limits and exclusions** (typically intentional/fraudulent acts).",
  "Not developed in the notes – just know what it is.")
sec("5.3 Liability of directors")
c("two-types", "Two types of directors' financial liability?",
  "1. **Liability for debts** (of the company, in crisis situations)\n2. **Liability for damages** (any damage caused by breach)\n(+ possible **criminal** liability, outside the course)")
c("debts-nature", "Is liability for company debts **direct** or **subsidiary**?",
  "**Subsidiary** – creditors can claim from directors only if the company **cannot** pay (not merely doesn't want to).")
c("debts-cases", "Two cases of **liability for debts**?",
  "1. Not filing for **insolvency** within **2 months** of insolvency → liable for debts arising **after** it should have been filed (culpable insolvency, art. 444 TRLC)\n2. Not **convening the GM** to dissolve when losses reduce **equity < ½ of capital** (art. 363.1.e LSC) → liable for debts arising **after** that point",
  "Key: only **later debts**, not earlier ones.", ["numbers"])
c("art236", "Three requirements of liability for damages (art. 236 LSC)?",
  "1. Act/omission **contrary to law/by-laws or duties**, with **fraud or fault**\n2. **Damage**\n3. **Causal link**\nFault is **presumed** if the act is contrary to law or by-laws.")
c("gm-ratify", "Director: \"The GM approved my decision, so I'm not liable.\" Correct?",
  "**No.** Authorisation or ratification by the GM **never exonerates** (art. 236.2 LSC).", tags=["trap"])
c("de-facto", "Who is a **de facto director**? Are they liable?",
  "A person who in reality performs director functions **without title**, with a **null/expired** title, or under another title, **or** the person whose **instructions** the directors follow. **Yes** – same liability as a de jure director (art. 236.3).")
c("art237", "Board adopts a harmful resolution. Who is liable (art. 237 LSC)?",
  "**All members** who adopted/executed it, **jointly and severally** – except those who **prove** they (a) **expressly opposed** it, (b) were **unaware** of it, or (c) knowing it, did **everything possible** to avoid the damage.",
  "Burden of proof is on the **director**.")
sec("5.4 Liability actions")
c("actions", "Two **liability actions** against directors?",
  "1. **Corporate action** (art. 238) – damage to the **company**\n2. **Individual action** (art. 241) – **direct** damage to **members or third parties**")
c("corp-action", "Who can bring the **corporate liability action**, in which order?",
  "1. The **company** (GM resolution – even **not on the agenda**; it implies **removal** of the directors)\n2. **Members with ≥ 5%** if: GM not convened when requested, company doesn't sue within **1 month**, or GM voted against (for **loyalty** breaches they may sue **directly**)\n3. **Creditors** if not brought by company/members and the company's assets are **insufficient** (art. 240)",
  tags=["numbers"])
c("ind-action", "Requirements of the **individual action**?",
  "- **Direct damage** to members/third parties\n- **Act of directors** in office\n- **Unlawfulness**\n- **Causal link** – burden of proof on the claimant")
c("public", "Can **public bodies** (Tax Agency, Social Security) hold directors liable?",
  "Yes – besides the commercial regime, **tax** and **labour law** have their own rules making directors liable for unpaid taxes/contributions in certain cases.")

# ═══════════════════════════ UNIT 6 ═══════════════════════════
unit(6)
sec("6.1 Amending the by-laws")
c("who-amends", "Who amends the by-laws?",
  "As a rule **only the general meeting** (art. 285.1 LSC). The GM may amend freely unless unlawful or against the principles of the company type (art. 28).")
c("reqs", "Requirements for a by-law amendment?",
  "1. Points clearly stated in the **notice/agenda**\n2. Full **text** of the proposal (+ **written report** in the **S.A.**, art. 286)\n3. Notice states members' right to **examine/receive** the documents free\n4. Adopted with legal **quorum & majorities** (arts. 194, 201)\n5. **Public deed** + **Registry**")
c("office-change", "Who can move the **registered office**?",
  "**Within Spain**: the **directors** (unless the by-laws expressly deny it) – art. **285.2 LSC**. **Abroad**: GM (structural change, RDL 5/2023).",
  "Mock Q17(d) \"GM has no power to approve a transfer within Spain, exclusive competence of directors\" → **false**. Correct: (c).", ["trap", "mock"])
c("consent", "When does an amendment need the **consent of the affected member**?",
  "When it creates **new obligations** for members (e.g. payments to compensate losses, ancillary commitments) or, in the **S.A.**, restricts the **transfer** of registered shares or affects **classes** of shares (art. 291 ff.).")
c("exit", "What is the **right to exit** (derecho de separación) and when for a corporate purpose change?",
  "The right to **leave** the company and get the **fair value** of the shares/stakes. Granted when the GM **substitutes or substantially modifies the corporate purpose** (art. **346 LSC**) – the nature of the investment changes.")
sec("6.2 Capital increase")
c("inc-ways", "Two **ways** to increase capital?",
  "1. **Issue new shares / create new stakes**\n2. **Increase the par value** of existing ones (art. 295.1 LSC)")
c("inc-types", "Four types of capital increase by **exchange value** (contravalor)?",
  "1. **Cash** contributions\n2. **Non-cash** contributions\n3. **Offsetting loans** (credit compensation)\n4. Charged to **profits or reserves**",
  "Mind map: **Cash, Non-cash, Loans, Reserves**.")
c("inc-who", "Who decides a capital increase? Can it be delegated?",
  "The **GM** (by-law amendment). In the **S.A.**, the GM may **delegate** to the directors within limits (art. 297 LSC).")
c("inc-steps", "Three general steps of a capital increase?",
  "1. **Resolution** of the GM (directors' report, art. 286)\n2. **Execution** – subscription/take-up and payment\n3. **Registration** of resolution **and** execution **simultaneously** (art. 315)")
c("art315", "Why must resolution and execution be registered **together**?",
  "So the Registry publishes only increases that **actually happened** (who subscribed, how it was paid) – otherwise capital would lose credibility as a solvency indicator.")
c("inc-cash", "Effect of a **cash** increase on equity and liquidity?",
  "**+ cash → + capital → + equity**. More immediate liquidity and better long-term solvency. Need a **bank certificate**.")
c("inc-noncash", "Effect of a **non-cash** increase? Extra requirement in S.A.?",
  "**+ net assets → + capital → + equity**; liquidity not necessarily. **S.A.**: **independent expert report** (Registrar); not required in S.L.")
c("inc-loans", "Capital increase by **offsetting loans**: effect and requirements?",
  "**− debt → + capital → + equity** (no new cash). **S.A.**: ≥ **25%** of the loans **liquid, mature and payable** and the rest due within **5 years** + **auditor's certificate**. **S.L.**: **100%** liquid, mature and payable (art. 301).",
  "Mock Q20 → (c): increase by offsetting loans **does** increase equity.", ["numbers", "mock"])
c("inc-reserves", "Capital increase charged to **reserves**: effect on equity?",
  "**Equity unchanged** – just a reclassification (reserves → capital). Requires a balance sheet (audited if mandatory) approved **≤ 6 months** before (art. 303). Effect: reserves become **unavailable** capital → stronger solvency image.",
  "Mock Q20(a) \"always increases equity\" → false; (d) \"increases equity if made by reserves\" → false.", ["trap", "numbers", "mock"])
c("premium", "What is a **share premium** (prima de emisión) and why use it?",
  "Paying **more than par value** for new shares/stakes (art. 298), fully paid on subscription. Used when **new members** enter: compensates the old members for **reserves and expectations** built before → avoids **dilution of value**.")
sec("6.3 Pre-emptive right")
c("pre-emptive", "What is the **pre-emptive right**? In which increases?",
  "The old members' right to subscribe/take up new shares/stakes **in proportion** to their par value **before third parties** – in increases with **cash contributions** (art. 304 LSC). Called \"preferential subscription right\" in S.A.",
  "Purpose: keep their **relative share** (% of capital).", ["trap"])
c("pre-period", "Period to exercise the pre-emptive right?",
  "Set by the directors, **not less than one month** (different for listed companies).", tags=["numbers"])
c("pre-loss", "What do members risk if they don't exercise the pre-emptive right?",
  "Lower % → **smaller dividends**; drop in **book value** per share (unless a premium is charged); and they may fall **below 5%**, losing minority rights (e.g. requesting a GM, liability action).")
c("pre-waive", "How can the pre-emptive right be removed?",
  "The **GM** may **exclude** it fully/partly (with specific requirements), or each member may **individually waive** it.")
sec("6.4 Capital reduction")
c("red-ways", "Three ways to reduce capital (art. 317.2)?",
  "1. **Reduce par value**\n2. **Redeem** (amortise) shares/stakes\n3. **Group** them to exchange them")
c("red-purposes", "Purposes of a capital reduction (art. 317.1)?",
  "1. **Restore balance** between capital and equity reduced by **losses**\n2. Create/increase **legal or voluntary reserves**\n3. **Refund** contributions to members\n4. S.A.: **release** members from **called-up capital**",
  "Mind map: balance restoration, reserve creation, refund contributions. Forms: voluntary, mandatory, **accordion**.")
c("red-mandatory", "When is a capital reduction **mandatory**?",
  "Only in the **S.A.**: when losses reduce **equity below 2/3 of capital** and it isn't recovered within **one fiscal year** (art. **327 LSC**). It must affect all shares proportionally (art. 320).",
  "Don't mix up: **2/3 + 1 year → mandatory reduction (S.A.)** vs **½ → mandatory dissolution cause (S.A. and S.L.)**.", ["numbers", "trap"])
c("red-annex", "Annex: S.A. capital €100,000, losses €50,000. Equity? Reduction of €30,000 – result?",
  "Equity = €50,000 = 50% < 2/3 → after 1 year reduction mandatory. Reduce by €30,000: capital **€70,000**, losses **€20,000**, equity still **€50,000** = **71%** of capital > 2/3 ✔.\nBook entry: €30,000 (Capital) to (Accumulated losses) €30,000 – **no money moves**.",
  tags=["numbers"])
c("red-steps", "Steps of a capital reduction?",
  "1. **GM resolution** (by-law amendment; directors' report justifying reason, amount, procedure…)\n2. **Execution**\n3. **Creditors' right to oppose** (S.A., certain cases)\n4. **Registration**")
c("creditor-opp", "When do creditors have a **right to oppose** a capital reduction?",
  "In the **S.A.**, when the reduction **really reduces equity** (refund of contributions, release from called-up capital). **Not** when it restores the balance after losses or funds reserves (art. 335). Exercise within **1 month** of the last announcement; the reduction can't be executed until the debt is **secured** (e.g. bank guarantee).",
  "Mock Q15 → (a). (c) \"always granted\" → false; (b) \"directors decide\" → false.", ["numbers", "mock", "trap"])
c("accordion", "What is the **\"accordion\"** operation (art. 343 LSC)?",
  "A **reduction to compensate losses below the legal minimum** combined with a **simultaneous increase**. Conditions: (a) increased to **≥ legal minimum**, (b) **pre-emptive right** respected, (c) reduction **conditional** on the increase being executed, (d) **registered together**.",
  "Alternative to avoid dissolution: **transform** the S.A. into an **S.L.** (min €3,000).")

# ═══════════════════════════ UNIT 7 ═══════════════════════════
unit(7)
sec("7.1 Structural changes")
c("sc-law", "Which law regulates **structural changes**?",
  "**Real Decreto-ley 5/2023, of 28 June (RDLME)** – applies to all commercial companies (and partnerships).")
c("sc-list", "Closed list of structural changes?",
  "1. **Transformation**\n2. **Merger**\n3. **Division** (demerger)\n4. **Global assignment of assets and liabilities**\n(+ international transfer of registered office) – domestic and cross-border.")
c("sc-phases", "Three phases of the merger procedure?",
  "1. **Preparation**\n2. **Approval**\n3. **Execution**")
sec("7.2 Mergers")
c("merger-def", "Legal definition of a **merger**?",
  "A corporate operation affecting **two or more companies** that entails the **extinction of all or some** of them and the **integration of their assets and members** into a **single company**.")
c("merger-types", "Two types of merger?",
  "1. **By creation of a new company** – **all** merging companies are extinguished; a new one acquires everything by universal succession\n2. **By absorption** – one company **absorbs** the others, which are dissolved and extinguished (absorber usually **increases capital**)",
  "Mock Q18(d) merger by absorption is a distractor – the block transfer where the transferring company receives shares is **segregation**.")
c("merger-why", "Typical economic reasons for mergers?",
  "**Synergies, economies of scale, vertical integration, optimised financing**, growth in size.")
c("draft", "What is the **common draft terms of merger** (art. 39 RDLME) and its timing?",
  "Drawn up by the **managing bodies of all companies**; published in the **Registry or on each website** at least **1 month** before the GMs. Must be approved within **6 months** of signature, otherwise it **lapses**.",
  tags=["numbers"])
c("reports", "Which reports accompany the merger draft?",
  "A **directors' report** of each company justifying it + an **independent expert** report – **mandatory when any company is an S.A.**")
c("exchange", "What is the **exchange ratio** (exchange equation)?",
  "The number of shares/stakes in the absorbing/new company given to members of the extinguished companies **in proportion to their participation**, calculated at **fair value** – so members' equity value is **not diminished**.")
c("approval", "Approval phase of a merger?",
  "**GM of every company** approves the **common draft** strictly (art. 47), with LSC quorums/majorities. Notice **≥ 1 month** before; **merger balance sheet** ≤ **6 months** old (audited if required). **Consent** needed from members who become **unlimitedly liable**.",
  tags=["numbers"])
c("universal-merger", "Can merger formalities be simplified by unanimity?",
  "Yes: if approved at a **universal GM by unanimity** in **each** company → no prior publication/deposit and **no directors' report** needed.")
c("publication", "How is the adopted merger resolution published?",
  "In the **BORME** and a leading **newspaper** of each province – or by **individual written notice** to all members **and creditors**.")
c("execution", "Execution phase of a merger? When is it legally effective?",
  "After the **1-month creditor opposition** period → **public deed** → **registration** in the Mercantile Registry. The merger takes legal effect **upon registration**. Afterwards it can only be challenged for breach of the RDLME, within **3 months**.",
  tags=["numbers"])
c("special", "What are **special mergers** (art. 53 ff. RDLME)?",
  "Simplified mergers where the **same persons decide** in all companies. Main case: **absorption of a wholly-owned (100%) subsidiary** – simplified draft, **no expert reports**, **no capital increase** of the absorber, **no GM approval** of the absorbed company.",
  "This is exactly **Case 2, Facts 3** (PATINETES absorbs PTEL S.L.U.).", ["case"])
c("twins", "What is a merger of **\"twin\" companies** (art. 49.2)?",
  "Absorption where the absorbing company **indirectly** owns 100% of the absorbed one (a **common shareholder** owns both 100%). Simplified, but **capital increase** and **expert report** are still required. Simplifications also from **90%** ownership (art. 54).",
  tags=["numbers"])
sec("7.3 Divisions")
c("division-why", "Why divide a company?",
  "To **reorganise**: separate activities or production phases into different companies, or distribute assets according to different financial needs. The inverse of a merger; merger rules apply (art. 63).")
c("total", "**Total demerger** (split-up), art. 59?",
  "The company is **extinguished**; all its assets are divided into **two or more blocks**, each transferred to a new or existing company; the **members** receive shares of the beneficiaries in proportion.",
  "Mock Q4 → (d): members of the divided company become members of the beneficiaries and the divided company is **extinguished**.", ["mock"])
c("partial", "**Partial demerger** (spin-off), art. 60?",
  "Block transfer of **one or more parts** of the assets to beneficiaries; the **members** receive their shares; the divided company **survives** but **reduces its capital**.")
c("segregation", "**Segregation**, art. 61?",
  "Block transfer of one or more parts of the assets to beneficiaries, but the **transferring company itself** receives the shares → **parent–subsidiary** relationship.",
  "Mock Q18 → (a) segregation. Mock Q4(b) is wrong: in segregation members do **not** become direct owners of the beneficiaries' shares.", ["mock", "trap"])
c("who-receives", "Quick test: who receives the beneficiary's shares, and does the original company survive?",
  "- **Total demerger**: members · company **extinguished**\n- **Partial demerger**: members · company **survives** (capital ↓)\n- **Segregation**: **the company itself** · company **survives**")
c("group", "What is a **group of companies** (art. 42 CCom)?",
  "Companies under **single management** of a **parent** company over **subsidiaries**. Control is presumed when the parent holds (or can hold by agreement) the **majority of votes** or can **appoint/remove the majority of directors**. Consequences: **consolidated accounts**, tax consolidation, related-party valuation.")
sec("7.4 Dissolution, liquidation, extinction")
c("three-phases-end", "Three phases of company termination?",
  "1. **Dissolution** (declaratory act)\n2. **Liquidation**\n3. **Extinction** (termination)",
  "The company does **not** end in a single act. Mock Q19(d) → false.", ["trap"])
c("causes", "Causes of dissolution (art. 363 LSC + voluntary)?",
  "1. **Term** in by-laws expires\n2. **GM resolution**\n3. **Cessation** of the activity / **impossibility** of the corporate purpose\n4. **Paralysis** of corporate bodies\n5. **Losses** → equity **< ½ of capital** (unless capital increased/reduced enough, and if insolvency isn't due)\n6. Capital **below the legal minimum**",
  "Mock Q19 → (b): the law sets **legal causes** of mandatory dissolution.", ["mock"])
c("paralysis", "Example of **paralysis of corporate bodies**?",
  "Two members with **50% each** who always vote opposite → no resolutions possible in GM or managing body → legal cause of dissolution.",
  "Very relevant for Case 1 (Pedro & María 50/50!) → use a shareholders' agreement with a deadlock clause.", ["case"])
c("dissolution-who", "Who declares dissolution and what if the GM doesn't?",
  "The **GM**. With a legal cause, directors **must convene** it (any member may request it, art. 365.1). If the GM rejects or can't agree → directors must request **judicial dissolution**. Failure → directors liable for debts arising **after** the cause. Formalised in **public deed + Registry** (or court judgment).")
c("liquidation", "What happens in **liquidation**?",
  "The company **keeps legal personality**, adds \"**en liquidación**\" to its name, stops its corporate purpose. **Directors cease**; **liquidators** take over (art. 375). Tasks: **inventory & balance** within **3 months**, **pay creditors**, final balance, **distribute** the remainder to members in proportion to their capital.",
  tags=["numbers"])
c("distribution-challenge", "Can the distribution proposal be challenged?",
  "Yes – members who **didn't vote in favour** can challenge the GM approval within **2 months** (art. 390). And **nothing** may be distributed to members until **all debts** are paid (otherwise → insolvency rules).",
  tags=["numbers", "trap"])
c("extinction", "When is the company **extinguished**?",
  "When, after liquidation and distribution, the liquidators grant a **public deed of extinction** and its entries are **cancelled** in the Registry; books are deposited there. → **End of legal personality**.")
c("simplified-end", "Can dissolution, liquidation and extinction happen in one act?",
  "Yes – if there are **no assets or liabilities** left, a deed of **dissolution and extinction** can be granted in the same act (initial balance = final balance).")

# ═══════════════════════════ UNIT 8 ═══════════════════════════
unit(8)
sec("8.1 Intellectual property")
c("ip-split", "Two categories of **intellectual property** law?",
  "1. **Copyright** – literary/artistic works, software, films, performers\n2. **Industrial property** – creations with **industrial application**: **distinctive signs** (trademarks, trade names) and **industrial creations** (patents, utility models, industrial designs)")
c("ip-why", "Double economic function of industrial property law?",
  "1. **Private interest**: reward and incentivise the author's effort\n2. **General interest**: distinctive signs → **market transparency**; patents → inventions are **disclosed** and help progress")
c("ip-how", "How does the law protect industrial property?",
  "By granting the author an **exclusive right of use**, which means **others are prohibited** from using it unless authorised.")
c("ip-laws", "Which laws regulate trademarks and patents in Spain?",
  "**Trademarks Act 17/2001** (LM) for trademarks & trade names; **Patents Act 24/2015** (LP) for patents & utility models.")
sec("8.2 Trademarks")
c("tm-def", "Define a **trademark** (art. 4.1 LM).",
  "**Any sign** (words, names, drawings, letters, numbers, colours, shape/packaging, sounds…) **capable of distinguishing the products or services** of one company from those of others.",
  "Essential element: **distinctiveness**.")
c("tm-vs-name", "Trademark vs **trade name** vs company name?",
  "**Trademark** → distinguishes **products/services** (Zara, Bershka).\n**Trade name** (art. 87 LM) → identifies **the business/entrepreneur** in trade (GRUPO INDITEX).\n**Company name** → legal name (Industria de Diseño Textil, S.A.).\nA trade name does **not** let you mark products – you need a trademark.",
  tags=["trap"])
c("shop-sign", "Are **shop signs** (rótulos) protected by the Trademarks Act?",
  "**No.** Using a shop sign to the detriment of an earlier one can be **unfair competition** (misleading act).", tags=["trap"])
c("specialty", "What is the **principle of specialty**?",
  "A trademark is registered for specific **classes** of goods/services (**Nice Classification**) and protected only within them – except **renowned** trademarks.")
c("tm-types", "Five types of trademarks?",
  "1. **Collective** – members of an **association** (owner = association), e.g. Barcelona Bar\n2. **Guarantee/warranty** – certifies common **quality/requirements** (e.g. CE marking)\n3. **Known / renowned** (art. 8) – generally known; protected **even unregistered** and **beyond its class**\n4. **EU trademark** – Reg. 2017/1001, whole EU\n5. **International** – protected in Spain on request (art. 79)")
c("renowned", "How are **renowned** trademarks protected? Example?",
  "Owner can prohibit use **even for other classes** (and protection even without registration in Spain). **ZARA vs \"Zara Tanzania Adventures\"**: EUIPO let Inditex win against a travel company.")
c("tm-birth", "How is the **right to a trademark** acquired?",
  "By **valid registration** at the **OEPM** (Spanish Patent & Trademark Office) – **constitutive** effect. After a **2-month opposition period**, the grant is published in the official gazette.",
  tags=["numbers"])
c("tm-content", "Content of the trademark right (art. 34 LM)?",
  "1. **Exclusive use** in trade\n2. **Prohibit** others from using identical/similar signs for the same/similar goods\n3. **Legal standing** to oppose registrations and seek **nullity** of confusing later marks")
c("tm-duration", "Duration of a trademark?",
  "**10 years from application**, **renewable indefinitely** for 10-year periods (art. 31).",
  "Trademark can live forever; patent can't (20 years, no renewal).", ["numbers", "trap"])
c("tm-use", "Obligation to use a trademark?",
  "**Effective and real use in Spain**. Not used for **5 years** after registration (or **5 uninterrupted years**) → **lapse (caducidad)**, registration cancelled (art. 39).",
  tags=["numbers"])
c("tm-license", "Can a trademark be transferred or licensed?",
  "Yes – it's an **intangible asset** (value = prestige + customer loyalty). **Licence** (art. 48): licensor authorises licensee for a **royalty**; for all/part of Spain, all/some classes, **exclusive or non-exclusive**.")
c("abs-rel", "**Absolute** vs **relative** prohibitions – the key difference for nullity actions?",
  "**Absolute** (art. 5): sign itself unfit / contrary to public order → nullity action **imprescriptible** (no time limit).\n**Relative** (art. 6 ff.): conflict with **earlier rights of others** → nullity action within **5 years**.",
  tags=["numbers", "trap"])
c("absolute-list", "Main **absolute** prohibitions (art. 5 LM)?",
  "1. Not a valid sign (art. 4)\n2. **Devoid of distinctive character**\n3. Exclusively **descriptive** (kind, quality, geographical origin…)\n4. Exclusively **customary** in current language/trade\n5. Contrary to **public policy/morality**\n6. Reproduce **flags/emblems** of Spain, regions, towns without consent\n7. **Deceptive** (nature, quality, geographical origin)",
  "Examples from class: \"ECO PURE\", \"BioFresh 100%\", \"Barcelona Tapas\" → descriptive/deceptive (absolute).")
c("relative-list", "Main **relative** prohibitions?",
  "Signs **confusable** with **earlier registered** trademarks/trade names for identical/similar goods, or taking **unfair advantage** of a **renowned** mark.",
  "Class examples: \"Coca-Kola\", \"GOOGLE for Kids\" → relative. Apple Corps vs Apple Computer (iTunes).")
c("geo", "How are **designations of origin / geographical indications** protected?",
  "Deceptive geographic signs are an absolute prohibition; unauthorised use of a designation of origin can even be a **criminal offence** (art. 275 Criminal Code).")
c("tn-def", "Define a **trade name** (art. 87 LM). What can it consist of?",
  "Any sign capable of graphic representation that **identifies a business** in trade and distinguishes it from businesses with identical/similar activities. Can be: personal names, company names, **imaginary** names, names alluding to the activity, anagrams, logos, images… Need not equal the company name. Specialty applies; **trademark rules apply** where compatible.")
sec("8.3 Industrial creations & patents")
c("ind-creation", "What is an **industrial creation**? Invention vs discovery?",
  "The result of human activity offering a **new technical solution** to a problem or improving an industrial process. A **discovery** doesn't necessarily have direct industrial application → **not** an invention.")
c("creation-types", "Types of industrial creations?",
  "a) **Inventions** (patents) – substantive\nb) **Utility models** – configuration with a practical advantage\nc) **Industrial designs** – aesthetic/ornamental appearance")
c("monopoly-why", "Why does the law grant an exclusive right, if it restricts free competition?",
  "To protect a **higher good**: without reward, less inventive effort. A **temporary** monopoly fosters **technological progress**; afterwards the invention enters the **public domain**.")
c("patent-def", "What is a **patent**?",
  "A **title** granted by the State recognising an **invention capable of industrial application** and the rights derived from it – the inventor's **exclusive** right to exploit it.")
c("patentability", "Three requirements for patentability (art. 4.1 LP)?",
  "1. **Novelty**\n2. **Inventive step**\n3. **Industrial application**",
  "Mnemonic **N-I-I**: \"**N**ew **I**dea, **I**ndustrial\".")
c("novelty", "When is an invention **new** (art. 6)?",
  "When it's not part of the **state of the art** = everything made **available to the public in Spain or abroad** (written, oral, use…) before the filing date. **Absolute, worldwide** novelty.")
c("inv-step", "When is there an **inventive step** (art. 8)?",
  "When it **doesn't follow obviously** from the state of the art for a **person skilled** in the field.")
c("ind-app", "When is it capable of **industrial application** (art. 9)?",
  "When it can be manufactured or used in **any kind of industry, including agriculture**.")
c("not-inventions", "What is **not** considered an invention (art. 4)?",
  "**Discoveries, scientific theories, mathematical methods**; literary/artistic/aesthetic works; schemes/rules/methods for mental acts, games or **business**; **computer programs**; presentations of information. (May be protected otherwise, e.g. copyright.)",
  tags=["trap"])
c("non-patentable", "Inventions **excluded** from patents even if they meet the requirements (art. 5)?",
  "Contrary to **public order/morality**; **plant varieties and animal breeds**; essentially biological processes; **surgical/therapeutic/diagnostic methods** on humans/animals; **human cloning**, commercial use of human embryos.")
c("owner", "Who owns the right to a patent?",
  "The **inventor** (or heirs/successors); several inventors → **in common**. If a non-entitled person applies → action before the OEPM (before grant) or **claim of ownership** in court (after grant), arts. 11–12.")
c("employee-inv", "Employee inventions – three types (art. 15 ff.)?",
  "1. **Service/employer** inventions – research is the **object of the contract** → belong to the **employer**\n2. **Mixed** – employee not hired to research, but used **company knowledge/resources** → employer **can claim** ownership or use, **paying compensation**\n3. **Free** – otherwise → belong to the **employee**",
  "EcoTech case (researcher invents at home with company lab equipment): he *is* a researcher → if it falls within his research duties = **service** invention; if outside them but using company equipment = **mixed**.", ["trap"])
c("patent-content", "Content of the patent right?",
  "**Exclusive right to exploit** + prevent others from manufacturing, offering, introducing on the market or using; for **process patents** also covers the **products directly obtained**.")
c("patent-duration", "Duration and territory of a patent?",
  "**20 years, NOT renewable**, limited to **Spanish territory**. Then → public domain.", tags=["numbers", "trap"])
c("exploit", "Obligation to **exploit** a patent?",
  "Exploit (directly or via licensee) within **3 years from publication of the grant** or **4 years from filing**, enough to supply the Spanish market (art. 90). Otherwise → **compulsory licence**.",
  "Content guide shorthand: \"loss due to no exploitation (3 years)\".", ["numbers"])
c("compulsory", "When can a **compulsory licence** be imposed (art. 91)?",
  "**Lack or insufficient exploitation**; **public interest** (public health, national defence); to stop practices contrary to **competition law**.")
c("patent-invalid", "Grounds of **patent invalidity**?",
  "Patentability requirements not met; invention **insufficiently described**; subject goes **beyond the application**; holder **not entitled**.")
c("patent-transfer", "How can patent rights be transferred?",
  "Sold, **licensed** (contractual licence – licensor keeps ownership; exclusive or not; royalties), given as security (usufruct, chattel mortgage).")

# ═══════════════════════════ UNIT 9 ═══════════════════════════
unit(9)
sec("9.1 Free competition")
c("why-compete", "Why protect free competition?",
  "Market economy (art. **38 CE**) assumes competition allocates resources **most efficiently** → **lower prices, more quantity, variety and quality** for consumers. Pure freedom leads firms to **agree not to compete**, so the law must intervene.")
c("ldc", "Main Spanish competition law? Four controlled conducts?",
  "**Act 15/2007 on the Defence of Competition (LDC)**.\n**Prohibited**: 1. **Collusive practices**, 2. **Abuse of dominant position**.\n**Controlled**: 3. **Economic concentrations**, 4. **State aid**.",
  tags=["trap"])
sec("9.2 Collusive practices & abuse")
c("collusion-def", "What does art. 1 LDC prohibit?",
  "Any **agreement, collective decision or recommendation, or concerted or consciously parallel practice** that has the **object or effect** (actual or potential) of **preventing, restricting or distorting competition** in all or part of the **national market**.")
c("collusion-3", "Three conditions of a prohibited collusive practice?",
  "1. A **collusive practice** exists\n2. **Actual or potential** restriction of competition\n3. Effect on all/part of the **national market**")
c("collusion-list", "Expressly prohibited collusive practices (art. 1)?",
  "a) **Fixing prices** or trading conditions\nb) **Limiting** production, distribution, development, investment\nc) **Sharing markets** or sources of supply\nd) **Discriminatory** conditions for equivalent transactions\ne) **Tying** – supplementary obligations unrelated to the contract")
c("objective", "Is intention relevant for a collusive practice?",
  "**No** – it's an **objective** prohibition: the mere **agreement capable** of restricting competition suffices; intent and actual effect are irrelevant. Also applies to foreign firms/acts **if effects reach the Spanish market**.", tags=["trap"])
c("null", "Consequence of a prohibited agreement? Exemption?",
  "**Null and void**. Exempted if it improves production/distribution or promotes **technical/economic progress**, with consumers getting a **fair share** of the benefits.")
c("dominance", "Is having a **dominant position** illegal?",
  "**No** – only its **abusive exploitation** (art. 2 LDC), even of a legal monopoly. Dominance = factual market power (market share), to be proven.", tags=["trap"])
c("abuse-list", "Examples of **abuse** of dominant position (art. 2)?",
  "a) Imposing **unfair prices** or conditions\nb) **Limiting** production/development to the detriment of firms/consumers\nc) Unjustified **refusal to supply**\nd) **Unequal conditions** for equivalent services\ne) **Tying** unrelated services\n(Non-exhaustive list)")
c("exempt", "Conducts **exempted** from the prohibitions (arts. 4–6)?",
  "1. Conduct resulting from **application of a law**\n2. Conduct of **minor importance** (de minimis)")
c("deminimis", "**De minimis** thresholds (LDC Regulation, art. 1)?",
  "- **Competitors**: combined share **≤ 10%**\n- **Non-competitors**: each **≤ 15%**\n- Unclear: **10%** each\n- **Cumulative** parallel networks: **5%** (only if networks cover ≥ **30%** of the market)",
  tags=["numbers"])
c("hardcore", "Which conducts are **never** of minor importance?",
  "**Price fixing, limiting production/sales, sharing markets/customers** between competitors, and **fixed or minimum resale prices** imposed on buyers (even between non-competitors).", tags=["trap"])
sec("9.3 Concentrations & State aid")
c("concentration", "What is an **economic concentration** (art. 7 LDC)? Is it prohibited?",
  "A **stable change of control** of all or part of one or more companies (mergers, acquisitions). **Not prohibited** – but **controlled** if it may restrict competition.")
c("thresholds", "When must a concentration be notified (art. 8 LDC)?",
  "If **either**:\na) it acquires/increases a market share **≥ 30%**, or\nb) combined Spanish turnover **> €240 million** and at least **two** participants each **> €60 million**",
  tags=["numbers"])
c("procedure", "Concentration control procedure?",
  "1. **Notify the CNMC** before execution\n2. **Suspension** – can't execute until authorised\n3. CNMC **authorises**, authorises **with conditions**, or **prohibits**\nNot notifying = **administrative offence**.")
c("aid", "State aid under EU law?",
  "In principle **incompatible** with the internal market (privileged position). Automatically allowed: aid of a **social** nature or for **natural disasters**/exceptional events (art. 107.2 TFEU); possible for regional development, projects of common European interest, serious economic disturbance. **De minimis: ≤ €200,000 over 3 fiscal years.**",
  tags=["numbers"])
c("aid-spain", "What does the Spanish LDC do about State aid?",
  "It does **not prohibit** it – the **CNMC** may **analyse** aid and its effects on competition and report. Breaches by a State can be taken to the **CJEU** by the Commission or another State.")
sec("9.4 Supervisory bodies & sanctions")
c("bodies", "Who supervises competition?",
  "**National** market → **CNMC** (Comisión Nacional de los Mercados y la Competencia); appeals to the **Audiencia Nacional**.\n**Cross-border/EU** market → **European Commission** (DG Competition); appeals to the **General Court**, then the **Court of Justice**.")
c("fines", "Sanctions under the LDC?",
  "Graduated: **minor** up to **1%**, … **very serious** up to **10%** of total **turnover** of the previous year. Plus up to **€60,000** for **legal representatives/managers** involved (art. 63).",
  tags=["numbers"])
c("leniency", "What is the **leniency** programme?",
  "The **first** cartel member to provide decisive evidence gets **full immunity** from the fine; later ones can get a **reduction** (arts. 65–66 LDC).")
sec("9.5 Unfair competition")
c("lcd", "Which law regulates **unfair competition**? Purpose?",
  "**Act 3/1991 on Unfair Competition (LCD)**. Not against *intense* competition, but against competition by **dishonest means** harming competitors, the market or consumers.")
c("scope", "Objective and subjective scope of the LCD?",
  "Any unfair act **before, during or after** a transaction, **whether or not the contract is concluded** (art. 2). Applies to entrepreneurs, professionals **and any person** acting in the market.")
c("general-clause", "General clause of unfair competition (art. 4 LCD)?",
  "Any conduct **objectively contrary to good faith** (intention irrelevant). Presumed towards consumers if: (1) contrary to **professional diligence** and (2) it **distorts or may distort** the economic behaviour of the **average consumer**.")
c("open-list", "Is the list of unfair acts closed?",
  "**No** – listed acts are unfair per se; others are judged under the **general good-faith clause**.")
c("competitor-acts", "Unfair acts addressed to a **specific competitor**?",
  "1. **Defamation** (denigration)\n2. **Comparison**\n3. **Imitation**\n4. Exploiting another's **reputation**\n5. Violation of **business secrets**\n6. **Inducing breach** of contract")
c("defamation", "When is a statement about a competitor **defamation**?",
  "Public statements that may **harm its reputation**, unless **true, accurate and appropriate**. Statements on **personal matters** are unfair **even if true**.", tags=["trap"])
c("comparison", "When is **comparative advertising** lawful?",
  "(a) compares goods with the **same purpose**, (b) refers **objectively** to **essential, relevant** features, (c) is **true** and doesn't exploit the competitor's **reputation**.",
  "Case 3: the KFC vs McDonald's tweet.", ["case"])
c("imitation", "When is **imitation** unfair?",
  "Imitation of non-exclusive creations is in principle free, but unfair if it creates **risk of association** by consumers or **unfairly exploits** the competitor's reputation or effort.")
c("secrets", "Violation of **business secrets** – which special law?",
  "Disclosing/using trade secrets under a duty of confidentiality or obtained unfairly. Special law: **Act 1/2019 on Trade Secrets** (implements Directive 2016/943).")
c("induction", "When is **inducing breach of contract** unfair?",
  "Inducing workers, suppliers or customers to breach basic contractual duties. Inducing a *regular* termination is unfair only if aimed at **secrets**, uses **deception**, or aims to **eliminate a competitor**.")
c("market-acts", "Unfair acts against the **proper functioning of the market**?",
  "1. **Misleading acts**\n2. Acts of **confusion**\n3. **Misleading omissions**\n4. **Aggressive practices**\n5. **Infringement of laws** (gaining a significant advantage)\n6. **Sale below cost**")
c("misleading", "Misleading **act** vs act of **confusion**?",
  "**Misleading**: false info, or true info that can induce **error** about **essential characteristics**, influencing economic behaviour.\n**Confusion**: creating confusion with a **competitor's** activity, products or establishment (incl. **risk of association**).",
  tags=["trap"])
c("omissions", "What are **misleading omissions**?",
  "Advertising inducing error by **omitting/hiding** necessary info, or giving it **unclear, unintelligible, ambiguous**, **at the wrong time**, or **subliminal** advertising.")
c("below-cost", "When is **selling below cost** unfair?",
  "Only when done **systematically** and it **misleads** consumers about the price level of other products in the same store, or aims to **eliminate a competitor**.", tags=["trap"])
c("consumer-practices", "Two groups of **unfair practices towards consumers** (arts. 19–31 LCD)?",
  "**Misleading** practices (arts. 20–27) and **aggressive** practices (arts. 28–31). Purpose: protect consumers' **freedom of choice**.")
c("misleading-cons", "Examples of **misleading practices** towards consumers?",
  "1. Causing **confusion** with competitors' marks\n2. False claims of **codes of conduct / quality marks**\n3. **Bait advertising** (\"Barcelona for €1\" with almost no seats)\n4. False claims about **properties** (\"cures diseases\")\n5. **Pyramid schemes** (Ponzi/Madoff)\n6. **Covert advertising** (advertorials not marked as ads)")
c("aggressive-cons", "Examples of **aggressive practices** towards consumers?",
  "1. **Coercion** – making consumers believe they can't leave without buying\n2. **Harassment** – home visits ignoring requests to leave\n3. **Unsolicited, repeated** offers by phone/e-mail (Margus newsletter example)")

# ═══════════════════════════ UNIT 10: CASES ═══════════════════════════
unit(10)
sec("Case 1 – Setting up the start-up")
c("c1-form", "Case 1: Pedro & María want to grow, attract Business Angels then VC, and sell. Which company type?",
  "A **capital company** – most likely an **S.L.** now (low capital, flexible, cheap), possibly **transformed into an S.A.** later (many investors, free transfer, listing).",
  "Growth + investors + exit ⇒ limited liability and a capital split into transferable units. A partnership doesn't fit (unlimited liability, no transfer without consent).")
c("c1-why-capital", "Case 1: why a capital company rather than a partnership (María wants to protect her wealth)?",
  "- Members **not personally liable** (art. 1 LSC) – María risks only her contribution\n- Easier **entry of investors** and **transfer** of shares/stakes\n- **Separation** of ownership/management (investors don't need to manage)\n- Credibility, standard for VC",
  "In a general partnership she would be **personally, unlimitedly, jointly & severally** liable.")
c("c1-sl-sa", "Case 1: S.L. or S.A.? Arguments.",
  "**S.L.**: min **€3,000**, 100% paid, **no expert report**, fewer formalities, flexible by-laws (vote allocation, transfer restrictions keep control).\n**S.A.**: min **€60,000**, shares **freely transferable**, needed for **listing**, more formalities.\n→ **S.L. now**, transform later if needed.")
c("c1-steps", "Case 1: main steps to set up the S.L.?",
  "1. **Name certificate** (Central Mercantile Registry)\n2. **Bank account** + deposit capital → **bank certificate**\n3. Provisional **NIF** (tax ID)\n4. Draft **by-laws**\n5. **Deed of incorporation before a notary**\n6. Tax formalities\n7. **Register** in the Mercantile Registry of the province (within 1 year) → legal personality; definitive NIF")
c("c1-capital", "Case 1: capital amount, proportions, Pedro's work, investing via a company?",
  "- Capital: at least **€3,000** (more for credibility/needs)\n- Proportions: **free** (e.g. 50/50 – but beware **deadlock = paralysis**; add a deadlock clause)\n- Pedro's **work** can't be capital (art. 58.2) → **ancillary commitment** (art. 86)\n- **Yes**, they can invest through their own S.L. (legal persons can be members/founders)")
c("c1-sha", "Case 1: what is a **shareholders' agreement** (pacto de socios)?",
  "A **private contract** between (some) shareholders regulating their relationship beyond the by-laws. Binds **only signatories** (not the company/third parties), **confidential**, not registered.",
  "Not in the unit notes – needed for the case answer.")
c("c1-sha-content", "Case 1: typical content of a shareholders' agreement + when to sign?",
  "Governance (board seats, **reserved matters/veto**), **transfer restrictions** (lock-up, **right of first refusal**, **tag-along**, **drag-along**), **anti-dilution**, founders' **dedication & non-compete**, **vesting / good & bad leaver**, **deadlock** resolution, exit.\nSign **at incorporation** (founders) and **renegotiate** when investors enter.")
sec("Case 2 – Patinetes Eléctricos S.L.")
c("c2-impair", "Case 2: equity €30,000, capital €90,000 (S.L.). Legal situation?",
  "Equity = **33% < ½ of capital** → **legal cause of mandatory dissolution** (art. 363.1.e LSC), unless capital is increased/reduced enough (or insolvency applies). (The **2/3 mandatory reduction** applies only to the **S.A.**)",
  "Calculation: 30,000 ÷ 90,000 = 0.33; threshold ½ × 90,000 = 45,000 > 30,000.", ["numbers"])
c("c2-liab", "Case 2: are Pedro & María liable – as directors? as shareholders?",
  "**As directors**: yes, if they don't **convene the GM** (within **2 months**) to dissolve or fix the situation (or request judicial dissolution) → **liable for company debts arising after** the cause (subsidiary, joint & several).\n**As shareholders**: **no** – capital company.")
c("c2-models", "Case 2: other management systems? Would a board change their liability?",
  "S.L./S.A.: **sole director, joint & several, joint (S.A. max 2), board** (min 3; S.L. max 12). On a board the regime is the same: **all members who adopted** the harmful decision are **jointly and severally liable** unless they prove they opposed, didn't know, or did everything to avoid it (art. 237).")
c("c2-fix", "Case 2: how to reverse the capital impairment?",
  "- **Capital increase** (e.g. the Business Angel's €100,000 in cash; or offsetting shareholder loans)\n- **Capital reduction to compensate losses** (S.L. capital ≥ €3,000)\n- **Accordion** (reduction + simultaneous increase)\n- Members' **contributions to equity** / returning to profit\nGoal: equity **≥ ½ of capital**.")
c("c2-type", "Case 2: type of capital increase for the Business Angel? Steps?",
  "A **cash** increase by **creating new stakes with a share premium**. Steps: **directors' report** & proposal → **GM resolution** (by-law amendment, S.L. > ½ of all votes) → **pre-emptive right** handled (waiver) → **subscription & payment** (bank certificate) → **public deed** → **registration** of resolution + execution.")
c("c2-preempt", "Case 2: do Pedro & María have a pre-emptive right? How to manage it?",
  "**Yes** – cash increase. They **individually waive** it (or the GM **excludes** it) so the stakes can go to the Business Angel.")
c("c2-valuation", "Case 2: BA invests €100,000 for 10%. Pre-money value?",
  "Post-money = 100,000 ÷ 10% = **€1,000,000** → pre-money = **€900,000** → **€10 per existing stake** (900,000 ÷ 90,000).",
  tags=["numbers"])
c("c2-numbers", "Case 2: capital €90,000 in €1 stakes. Fill in the capital increase for 10% at €100,000.",
  "New stakes N: N ÷ (90,000 + N) = 10% → **N = 10,000**.\n- Increase: **€10,000**, 10,000 new stakes numbered **90,001–100,000**\n- Total stakes **100,000** of €1\n- Premium: **€90,000** total = **€9 per stake**\n- Capital + premium = **€100,000**\n- New capital **€100,000** (stakes 1–100,000)",
  "The **share premium** is the anti-dilution mechanism: the BA pays €10 per stake (€1 par + €9 premium) = the real value, so the founders' value isn't diluted. Bonus: equity becomes 30,000 + 100,000 = **€130,000 > ½ × 100,000** → impairment cured.", ["numbers"])
c("c2-absorber", "Case 2: which company should absorb which?",
  "**PATINETES ELÉCTRICOS S.L. absorbs PTEL S.L.U.** – Patinetes holds the 40 employees, all client/supplier contracts, IP rights and **licences/permits**; absorbing the other way would require transferring all of these (and licences may not be transferable).")
c("c2-merger-type", "Case 2: what type of merger, and what can be avoided?",
  "**Merger by absorption of a wholly-owned subsidiary** (special merger, art. 53 RDLME): simplified draft; **no exchange ratio**, **no directors' and experts' reports**, **no capital increase** of the absorber, **no approval by the absorbed company's GM**.")
c("c2-procedure", "Case 2: order of the merger procedure?",
  "1. **Common draft terms** signed by both managing bodies\n2. **Publication/deposit** (Registry or websites) ≥ **1 month** before the GM\n3. **Merger balance sheets** (≤ 6 months)\n4. **GM approval** of Patinetes (within 6 months of the draft)\n5. **Publication** of the resolution (BORME + newspaper, or individual notice)\n6. **1-month creditor opposition** period\n7. **Public deed** of merger\n8. **Registration** → effective; PTEL extinguished & cancelled")
c("c2-effective", "Case 2: when is the merger effective – legally and for accounting?",
  "**Legally**: on **registration** in the Mercantile Registry. **Accounting**: from the **date set in the merger draft** (per accounting rules; typically retroactive to the start of the financial year for group companies).")
c("c2-reasons", "Case 2: reasons for the merger?",
  "PTEL lost its purpose (only serves the parent): **simplify the structure**, **cut costs** (one set of accounts, filings, governance), **synergies**, concentrate employees/assets. Stating them (draft/report) helps **transparency** and justifies **valid economic reasons** (e.g. for tax neutrality).")
sec("Case 3 – Competition & IP")
c("c3-kfc", "Case 3: KFC's \"nuclear button\" tweet mocking Ronald McDonald – what advertising, lawful?",
  "**Comparative advertising** (implicit reference to a competitor). Lawful only if it compares goods with the **same purpose**, **objectively** on **essential, verifiable** features, is **true**, not **denigrating**, doesn't exploit the competitor's **mark/reputation** (Dir. 2006/114 art. 4). \"Bigger and more powerful\" isn't verifiable and it ridicules McDonald's mascot → arguably **unlawful**; counter-argument: obvious humour/puffery no consumer takes literally.")
c("c3-natural", "Case 3: products labelled \"100% natural\" contain chemicals. What is it and what actions exist?",
  "**Misleading advertising** (misleading act/practice about essential characteristics). Actions (art. 32 LCD): **declaratory**, **cessation/prohibition**, **removal of effects**, **rectification**, **damages** (if fault), **unjust enrichment**; consumers' associations can sue; complaints to consumer authorities.")
c("c3-cartel", "Case 3: what is a **cartel**? Examples.",
  "A secret **agreement between competitors** to **fix prices**, **share markets/customers**, or **limit output** (art. 101 TFEU / art. 1 LDC). Examples: price-fixing cartels (e.g. EU truck makers), bid rigging, market sharing.")
c("c3-algo", "Case 3: travel agencies' software caps discounts at 3%; poster seller uses repricing algorithm. Sanctionable?",
  "**Travel agencies**: common cap known and applied by competitors = **concerted practice** (price fixing) → sanctionable (EU *Eturas* case). **Posters**: a purely **unilateral** pricing algorithm is lawful; it becomes a **cartel** if used to implement an **agreement not to undercut** competitors (UK posters case on Amazon). Fines up to **10% of turnover**, nullity, leniency.")
c("c3-blackfriday", "Case 3: a company claims royalties for its registered \"Black Friday\" trademark. Can shops ignore it?",
  "**Yes, largely**: \"Black Friday\" is a **generic/descriptive** term for a sales event – an **absolute** prohibition (no distinctiveness, customary in trade) → **nullity action** (**no time limit**); using it **descriptively** isn't trademark use. (Spanish courts did annul most of that registration.) Famous marks = Zara, Coca-Cola – broader protection (art. 8 LM).")
c("c3-design", "Case 3: competitors copy a start-up's registered EU design (webcam cover). Measures?",
  "**Prevent**: register **designs** (EU), **trademark**, **patent/utility model** if technical, NDAs. **After copying**: cease-and-desist letter, **infringement action** (cessation, removal/seizure of copies, damages, publication), **interim measures**, **customs** measures; alternatively **unfair imitation** under the LCD.")
c("c3-secrets", "Case 3: legal mechanisms to protect innovations – differences?",
  "- **Patent**: public, registered, **20 years**, absolute exclusivity\n- **Utility model / design**: registered, shorter, for practical/aesthetic creations\n- **Trademark**: signs, **10 years renewable**\n- **Copyright**: works/software, no registration\n- **Trade secret** (Act 1/2019): **no registration, unlimited** while secret + **reasonable measures** (NDAs), but no protection against **independent discovery / reverse engineering**\n- **Unfair competition** as a backstop")


# ───────────────────────────── build ─────────────────────────────
def validate():
    ids = [x["id"] for x in cards]
    dup = {i for i in ids if ids.count(i) > 1}
    assert not dup, dup
    import re
    for x in cards:
        for t in x["tags"]:
            assert re.match(r"^[a-z0-9-]+$", t), t
    return len(cards)

def build(units, zip_name, out):
    sel = [x for x in cards if x["unit_no"] in units]
    deck_cards = [{k: v for k, v in x.items() if k != "unit_no"} for x in sel]
    deck = {"format": "recall-v1", "subject": SUBJECT,
            "units": [{"name": U[n], "order": n} for n in units], "cards": deck_cards}
    tmp = f"{out}/build/{zip_name}"
    shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp + "/images")
    with open(tmp + "/cards.json", "w", encoding="utf-8") as f:
        json.dump(deck, f, ensure_ascii=False, indent=2)
    with zipfile.ZipFile(f"{out}/{zip_name}.zip", "w", zipfile.ZIP_DEFLATED) as z:
        z.write(tmp + "/cards.json", "cards.json")
    return len(sel)

if __name__ == "__main__":
    n = validate()
    out = "/home/claude/law/out"; os.makedirs(out, exist_ok=True)
    print("cards", n)
    for u in range(1, 11):
        print(u, sum(1 for x in cards if x["unit_no"] == u))
    print("ALL", build(list(range(1, 11)), "BusinessLaw_Midterm_ALL", out))
    print("U1-3", build([1, 2, 3], "BusinessLaw_U1-3_Law_Entrepreneur_Incorporation", out))
    print("U4-5", build([4, 5], "BusinessLaw_U4-5_Corporate_Bodies", out))
    print("U6-7", build([6, 7], "BusinessLaw_U6-7_ByLaws_StructuralChanges", out))
    print("U8-9", build([8, 9], "BusinessLaw_U8-9_IP_Competition", out))
    print("Cases", build([10], "BusinessLaw_Case_Studies", out))
    with open(f"{out}/cards.json", "w", encoding="utf-8") as f:
        json.dump(cards, f, ensure_ascii=False)
