"""Multiple-choice: official 2022 mock (Model A) + self-made exam-style bank."""
import json
Q = []
def q(qid, unit, text, opts, ans, why, src="bank"):
    assert len(opts) == 4 and ans in "abcd"
    Q.append({"id": qid, "unit": unit, "q": text, "opts": opts, "ans": "abcd".index(ans), "why": why, "src": src})

M = "mock2022"
# (official 2022 mock questions omitted from the public repo – course material)
# ─────────────────────────── BANK ───────────────────────────
# Unit 1
q("b101", 1, "A Royal Decree appointing Mr. García as Director-General of a ministry:",
  ["Is a legal rule because it is enacted by the Government.", "Is not a legal rule because it lacks generality.",
   "Is a legal rule because it is published in the BOE.", "Is not a legal rule because it lacks coercibility."], "b",
  "It addresses one specific person → no generality. Publication or the author doesn't make it a rule.")
q("b102", 1, "Unless the rule provides otherwise, a Spanish state rule enters into force:",
  ["On the day of its publication in the BOE.", "20 days after its publication in the BOE.",
   "One month after its approval by Parliament.", "When the citizens affected have been notified."], "b",
  "20 days after publication = default vacatio legis.")
q("b103", 1, "The period between the publication of a rule and its entry into force is called:",
  ["Vacatio legis.", "Tacit repeal.", "Purposive approach.", "Lex specialis."], "a", "Vacatio legis.")
q("b104", 1, "A new act regulates the same matter as an older act of the same rank in a different way, without mentioning it:",
  ["Both remain fully in force until the older one is expressly repealed.", "The older act is tacitly repealed in everything inconsistent.",
   "The older act prevails because it was first.", "A court must decide which applies through case law, which is a source of law."], "b",
  "Tacit repeal: same or higher rank rule regulating differently invalidates the old one where inconsistent.")
q("b105", 1, "According to art. 1 CC, the sources of the Spanish legal system are:",
  ["Law, case law and custom.", "Law, custom and general principles of law.",
   "Constitution, acts and regulations.", "Law, custom, general principles and Supreme Court case law."], "b",
  "Case law only complements the system.")
q("b106", 1, "Custom applies:",
  ["Always before the law, given Business Law's customary origins.", "Only in the absence of applicable law, if not contrary to morals or public order and if proven.",
   "Only if it has been confirmed by the Supreme Court.", "Never, since it has been replaced by general principles."], "b", "Art. 1.3 CC.")
q("b107", 1, "Which statement about mandatory rules is correct?",
  ["They apply only if the parties have not agreed otherwise.", "Acts contrary to them are void by operation of law.",
   "Art. 314 CCom on interest on loans is an example.", "They can be excluded by a written contract."], "b",
  "Art. 6.3 CC. Art. 314 CCom is dispositive.")
q("b108", 1, "A Royal Decree contradicts a Royal Legislative Decree. Which is correct?",
  ["The Royal Decree prevails because it is more recent.", "The contradicting precept of the Royal Decree is null and void.",
   "Both have the same rank, so the later one prevails.", "The Autonomous Communities decide which applies."], "b",
  "RLD has the status of an act; a Royal Decree is lower.")
q("b109", 1, "A Royal Decree-Law is:",
  ["A rule of the Government with the status of an act, for cases of extraordinary and urgent need.",
   "A rule of Parliament delegating power to the Government.", "A regulation developing an act, below it in rank.",
   "An EU rule directly applicable in Spain."], "a", "RDL = urgency; RLD = express delegation through a framework law.")
q("b110", 1, "An international treaty containing stipulations contrary to the Spanish Constitution:",
  ["Prevails over the Constitution, as supranational law.", "Requires prior amendment of the Constitution (art. 95 CE).",
   "Is automatically void.", "Applies only in the Autonomous Communities that accept it."], "b", "Art. 95.1 CE.")
q("b111", 1, "The GDPR (Regulation (EU) 2016/679) is:",
  ["A Directive that Spain had to transpose.", "Directly applicable to citizens without any internal rule.",
   "Primary EU legislation.", "A Spanish regulation below an act."], "b", "EU Regulations are directly applicable.")
q("b112", 1, "Which is NOT part of interpretation criteria in art. 3 CC?",
  ["The proper meaning of the words.", "The historical and legislative background.",
   "The social reality of the time when applied.", "The personal opinion of the judge on fairness."], "d",
  "Words, context, background, social reality, spirit and purpose.")
q("b113", 1, "The relationship between national law and EU law is in principle one of competence, but in case of conflict:",
  ["National law prevails.", "EU law prevails.", "The more recent rule prevails.", "The Constitutional Court applies custom."], "b", "Primacy of EU law.")
# Unit 2
q("b201", 2, "Business Law is best defined as:",
  ["All rules that affect businesses, including tax and employment law.",
   "The part of private law for entrepreneurs and their legal status, regarding their market activities carried out through an enterprise.",
   "Public law regulating State intervention in the economy.", "The law of companies registered in the Mercantile Registry."], "b",
  "Tax and employment law are separate disciplines.")
q("b202", 2, "According to art. 2 CCom, acts of commerce are governed, failing the Commerce Code, by:",
  ["Ordinary civil law.", "Business practice observed in each place, and then civil law.",
   "Supreme Court case law.", "EU Directives."], "b", "Code → business usage → civil law (but art. 50 CCom for contracts).")
q("b203", 2, "Competence over commercial legislation in Spain belongs to:",
  ["The Autonomous Communities.", "Both State and Autonomous Communities equally.",
   "Exclusively the State (art. 149.1.6 CE).", "The European Commission."], "c", "Market unity.")
q("b204", 2, "The enterprise (empresa):",
  ["Has its own legal personality from registration.", "Lacks legal personality and must be linked to a natural or legal person.",
   "Is the same as the entrepreneur.", "Is the holder of the obligations arising from the business."], "b", "The enterprise is an organised set of capital and work; the holder of rights and obligations is the entrepreneur.")
q("b205", 2, "The general manager of a company, who signs contracts every day on its behalf, is:",
  ["An entrepreneur, since he organises the activity.", "Not an entrepreneur, because he acts in the name of another.",
   "An entrepreneur if he holds shares.", "An entrepreneur in the legal sense but not in the economic sense."], "b",
  "Legal entrepreneur = in whose name the activity is carried out. (He's an 'entrepreneur' only in the economic sense.)")
q("b206", 2, "Registration in the Mercantile Registry is:",
  ["Mandatory for all entrepreneurs.", "Optional for individual entrepreneurs and mandatory for companies.",
   "Optional for all.", "Mandatory only for public limited companies."], "b", "")
q("b207", 2, "A 16-year-old inherits his father's shop. Which is correct?",
  ["He cannot be an entrepreneur until he is 18.", "He can be an entrepreneur, acting through his legal representatives.",
   "He becomes an entrepreneur only with judicial authorisation and acts personally.", "The shop must be sold."], "b",
  "Exception to preserve the enterprise.")
q("b208", 2, "A director competes with his company without its consent and signs a contract with a bona fide client. The contract is:",
  ["Void.", "Valid; the director may be removed and liable for damages.",
   "Voidable at the request of the company.", "Valid only if ratified by the general meeting."], "b",
  "Breach doesn't invalidate contracts vs bona fide third parties.")
q("b209", 2, "A judge who wants to run a business in the province where he serves faces:",
  ["An absolute incompatibility.", "A relative incompatibility.", "A prohibition to compete.", "A disqualification."], "b",
  "Judges/prosecutors: relative (territorial).")
q("b210", 2, "Which is NOT a professional duty of every entrepreneur?",
  ["Keeping orderly accounts.", "Respecting free and fair competition.", "Registering in the Mercantile Registry as an individual.", "Documenting its operations."], "c",
  "Registration is optional for individuals.")
q("b211", 2, "A company operating without registration in the Mercantile Registry:",
  ["Has no liability at all.", "Is an irregular company: members answer like general partners and managers jointly and severally.",
   "Is treated as a capital company if its by-laws say so.", "Only answers with its own assets."], "b", "Art. 120 CCom.")
q("b212", 2, "The liability of a general partner for the partnership's debts is:",
  ["Limited to his contribution.", "Personal, unlimited, subsidiary and joint and several.",
   "Direct and limited.", "Only internal towards the other partners."], "b", "")
q("b213", 2, "In a limited partnership (sociedad comanditaria), limited partners:",
  ["Manage the partnership.", "Must appear in the business name.", "Answer only up to their contribution and cannot manage.", "Answer unlimitedly."], "c", "")
q("b214", 2, "Mr. Ruiz lets his name be used in the name of a general partnership although he is not a partner:",
  ["He has no liability.", "He is jointly and severally liable as if he were a partner (art. 126 CCom).",
   "He is liable only up to €3,000.", "The partnership must change its name; no liability arises."], "b", "")
q("b215", 2, "Lifting the corporate veil means:",
  ["Removing directors who breached their duties.", "Disregarding the company's separate personality to hold members personally liable for abuse.",
   "Publishing the company's accounts.", "Dissolving the company by court order."], "b", "Arts. 6.4 and 7 CC.")
q("b216", 2, "Which is a capital company under the LSC?",
  ["General partnership.", "Limited partnership.", "Partnership limited by shares.", "Cooperative."], "c",
  "S.A., S.L. and comanditaria por acciones.")
q("b217", 2, "The 'hybrid' character of the S.L. means:",
  ["Members are partly personally liable.", "It's capitalist towards third parties but allows personalistic elements internally (e.g. votes not proportional to capital).",
   "It can issue shares on the stock exchange.", "It combines a sole director with a board."], "b", "")
q("b218", 2, "A newborn baby who owns a bank account has:",
  ["Neither legal capacity nor capacity to operate.", "Legal capacity but not capacity to operate.",
   "Capacity to operate but not legal capacity.", "Both."], "b", "")
q("b219", 2, "According to art. 116 CCom, a trading company:",
  ["Acquires legal personality once incorporated according to the Code.", "Never has legal personality.",
   "Has legal personality only if it is a capital company.", "Acquires legal personality when it starts trading."], "a", "")
q("b220", 2, "The size of the enterprise:",
  ["Determines a different legal status for SMEs.", "Doesn't change the general status, but special rules (e.g. accounting) may differ.",
   "Is irrelevant in all legal matters.", "Is defined by the Commerce Code."], "b",
  "SME definition: Commission Regulation (EU) 651/2014.")
# Unit 3
q("b301", 3, "A capital company acquires legal personality as such:",
  ["When the founders sign a private contract.", "When the deed is executed before a notary.",
   "When the deed of incorporation is registered in the Mercantile Registry.", "When it opens a bank account."], "c", "")
q("b302", 3, "Which statement about single-member companies is correct?",
  ["Spanish law requires at least two founders.", "An S.A. or S.L. can be formed by one person (S.A.U./S.L.U.).",
   "Only S.L. can be single-member.", "A company that becomes single-member after incorporation must dissolve."], "b",
  "Later sole proprietorship → deed + registration.")
q("b303", 3, "In an S.A. with €200,000 capital, the minimum that must be paid up at incorporation is:",
  ["€200,000", "€60,000", "€50,000 (25%)", "€15,000"], "c", "25% of each share's par value; rest = called-up capital.")
q("b304", 3, "In an S.L., at incorporation the capital must be:",
  ["Paid up at least 25%.", "Fully subscribed and fully paid up.", "Paid within one year.", "At least €60,000."], "b", "")
q("b305", 3, "A founder of an S.A. contributes a building. Which is required?",
  ["Nothing special.", "A report by an independent expert appointed by the Registrar, as a rule.",
   "A report by the company's auditor only.", "Unanimous approval of all creditors."], "b",
  "S.L.: no report, but contributor liable for value (art. 30).")
q("b306", 3, "If the by-laws say nothing, the company's fiscal year ends on:",
  ["30 June", "31 December", "The anniversary of the deed", "31 March"], "b", "")
q("b307", 3, "Acts performed in the name of a company in formation that were NOT necessary for registration:",
  ["Automatically bind the company after registration.", "Bind the company only if it expressly accepts them after registration.",
   "Are void.", "Bind only the notary."], "b", "Art. 36 LSC.")
q("b308", 3, "If a company is not registered within one year of the deed:",
  ["It is automatically dissolved.", "Any member may request dissolution and refund of contributions.",
   "It becomes an S.L. by law.", "Nothing happens."], "b", "Arts. 39–40 LSC.")
q("b309", 3, "Ancillary commitments (prestaciones accesorias):",
  ["Form part of share capital.", "Are services by members beyond their contribution, not part of capital.",
   "Are mandatory in every S.L.", "Can only be free of charge."], "b", "Art. 86 LSC.")
q("b310", 3, "Which right is NOT a basic member right under the LSC?",
  ["Right to dividends.", "Pre-emptive right.", "Right to manage the company.", "Right to information."], "c",
  "Management belongs to directors.")
q("b311", 3, "A company has capital €100,000 (1,000 shares) and equity €160,000. The book value per share is:",
  ["€100", "€160", "€60", "€260"], "b", "160,000 ÷ 1,000.")
q("b312", 3, "Fair value of a share equals:",
  ["Par value × 2", "Book value ± expectations", "Capital ÷ shares", "Equity − capital"], "b", "")
q("b313", 3, "The principle that capital may not fall below €60,000 / €3,000 during the life of the company is the principle of:",
  ["Determination", "Integrity", "Minimum outlay (minimum capital)", "Full subscription"], "c", "")
q("b314", 3, "Which must appear in the company name?",
  ["The names of all founders.", "The indication S.A. or S.R.L./S.L.", "The corporate purpose.", "The registered office."], "b", "")
q("b315", 3, "The registered office of a Spanish capital company:",
  ["Can be anywhere in the EU.", "Must be in Spain, where effective management is or the main establishment.",
   "Must be in Madrid.", "Must be where the majority shareholder lives."], "b", "")
q("b316", 3, "In an S.L., attendance at general meetings:",
  ["Can be restricted to holders of a minimum number of stakes.", "Cannot be restricted.",
   "Is reserved to directors.", "Requires 5% of capital."], "b", "S.A. may require a minimum number of shares.")
q("b317", 3, "Equity at incorporation is €50,000 (= capital). After years, reserves are €30,000 and there are no losses. Then:",
  ["Book value = par value.", "Book value > par value.", "Book value < par value.", "Fair value must equal book value."], "b", "")
q("b318", 3, "Which is a correct pair?",
  ["S.A. – stakes – assume; S.L. – shares – subscribe", "S.A. – shares – subscribe; S.L. – stakes – take up/assume",
   "Both – shares – subscribe", "S.A. – stakes – subscribe; S.L. – shares – assume"], "b", "")
# Unit 4
q("b401", 4, "Which is NOT a competence of the general meeting under art. 160 LSC?",
  ["Approval of the annual accounts.", "Capital increase.", "Hiring the company's employees.", "Merger."], "c",
  "Day-to-day management belongs to directors.")
q("b402", 4, "The sale of an asset worth 30% of total assets on the last balance sheet:",
  ["Can be decided by the directors alone.", "Is a competence of the general meeting (core asset > 25%).",
   "Needs creditors' consent.", "Needs approval of the Registrar."], "b", "")
q("b403", 4, "The ordinary general meeting must be held:",
  ["Within the first three months of the fiscal year.", "Within the first six months of the fiscal year.",
   "At any time during the year.", "Within one month after the year-end."], "b", "Art. 164 LSC.")
q("b404", 4, "Members holding at least ___ of capital can require the directors to convene a general meeting.",
  ["1%", "3%", "5%", "10%"], "c", "")
q("b405", 4, "The minimum notice period for a general meeting is:",
  ["15 days in both S.A. and S.L.", "One month in S.A. and 15 days in S.L.", "One month in both.", "Two months in S.A."], "b", "")
q("b406", 4, "A universal general meeting requires:",
  ["Prior notice published on the website.", "All capital present or represented and unanimous agreement to hold it and on the agenda.",
   "A quorum of 50%.", "The presence of the Registrar."], "b", "Art. 178 LSC.")
q("b407", 4, "A minimum quorum to validly constitute the general meeting is required:",
  ["In both S.A. and S.L.", "Only in the S.A.", "Only in the S.L.", "In neither."], "b", "")
q("b408", 4, "The general meeting may adopt resolutions on matters NOT on the agenda only for:",
  ["Capital increases.", "Removal of directors and bringing a liability action against them.",
   "Approval of the accounts.", "Any matter if 75% agree."], "b", "")
q("b409", 4, "A member who voted against a resolution validly adopted by the general meeting:",
  ["Is not bound by it.", "Is bound by it but may challenge it in court under legal conditions.",
   "May veto it.", "Is automatically entitled to exit."], "b", "")
q("b410", 4, "Directors of a capital company:",
  ["Must always be members.", "Need not be members unless the by-laws require it.",
   "Must be natural persons.", "Must be Spanish nationals."], "b", "Art. 212.2 LSC; legal persons can be directors.")
q("b411", 4, "With joint and several directors (administradores solidarios):",
  ["Each director can act alone with full powers.", "All must sign together.",
   "They decide by majority in sessions.", "Only the oldest can act."], "a", "")
q("b412", 4, "An S.A. wants four directors who must act together. It must:",
  ["Appoint four joint directors.", "Set up a board of directors.", "Become an S.L.", "Appoint a sole director."], "b",
  "Max 2 joint directors in an S.A.")
q("b413", 4, "The board of directors of an S.L. may have:",
  ["2 to 12 members", "3 to 12 members", "3 members minimum, no maximum", "5 to 15 members"], "b", "")
q("b414", 4, "The general meeting approved a decision of the directors that caused damage to the company. The directors:",
  ["Are exonerated.", "Remain liable (GM approval never exonerates).",
   "Are liable only if the decision wasn't on the agenda.", "Become liable together with all shareholders."], "b", "Art. 236.2 LSC.")
q("b415", 4, "Which person cannot be appointed director?",
  ["A legal person.", "A non-member.", "A person disqualified under the Insolvency Act.", "A foreigner."], "c", "Art. 213 LSC.")
q("b416", 4, "A change in the way the managing body is organised:",
  ["Can be decided informally by the directors.", "Requires a public deed and registration in the Mercantile Registry.",
   "Requires CNMC authorisation.", "Is not possible after incorporation."], "b", "Art. 210.4 LSC.")
# Unit 5
q("b501", 5, "The standard of diligence required of directors is that of:",
  ["A good family father.", "An orderly entrepreneur.", "A faithful representative.", "An expert auditor."], "b",
  "Loyalty uses 'faithful representative'; care uses 'orderly entrepreneur'.")
q("b502", 5, "Under the business judgment rule (art. 226 LSC), the standard of diligence is met in business decisions if the director acted:",
  ["With a positive result for the company.", "In good faith, without personal interest, with sufficient information and an adequate procedure.",
   "With the approval of the general meeting.", "Following the advice of external consultants."], "b", "")
q("b503", 5, "The business judgment rule does NOT apply to:",
  ["Strategic investment decisions.", "Decisions personally affecting other directors or related persons.",
   "Expansion into new markets.", "Pricing decisions."], "b", "Art. 226.2.")
q("b504", 5, "The duty of secrecy of directors:",
  ["Ends when they leave office.", "Continues even after they leave office, except when the law allows/requires disclosure.",
   "Applies only to listed companies.", "Can be excluded by the by-laws."], "b", "")
q("b505", 5, "The duty of loyalty regime:",
  ["Can be freely limited by the by-laws.", "Is mandatory, but the GM may grant exemptions in specific cases (art. 230).",
   "Applies only to boards of directors.", "Applies only in S.A."], "b", "")
q("b506", 5, "A pandemic causes heavy losses. Directors had no risk-monitoring system for this event:",
  ["They breached the duty of care.", "Unforeseeable exogenous events are not a breach of the duty of care.",
   "They are automatically liable for all debts.", "They must resign."], "b", "Covid example in the notes.")
q("b507", 5, "Directors' liability for company debts is:",
  ["Direct and primary.", "Subsidiary – only if the company cannot pay.",
   "Limited to their remuneration.", "Only towards the Tax Agency."], "b", "")
q("b508", 5, "Directors failed to file for insolvency within the legal period. They may be liable for:",
  ["All company debts, earlier and later.", "Debts arising after the moment the filing should have been made.",
   "Nothing, as insolvency is the company's matter.", "Only debts towards employees."], "b", "")
q("b509", 5, "Losses reduce equity below half of the capital and directors don't convene the GM. They become liable for:",
  ["Debts existing before the cause.", "Company debts arising after the legal cause of dissolution.",
   "The losses themselves.", "Nothing if they are also shareholders."], "b", "")
q("b510", 5, "Which is NOT a requirement for directors' liability for damages (art. 236)?",
  ["Act contrary to law, by-laws or duties with fraud or fault.", "Damage.", "Causal link.", "That the company is insolvent."], "d", "")
q("b511", 5, "When a director's act is contrary to the law or the by-laws:",
  ["Fault must be proven by the claimant.", "Fault is presumed unless proven otherwise.",
   "No liability arises without criminal conviction.", "Only the company can sue."], "b", "")
q("b512", 5, "A board member who voted against a harmful resolution:",
  ["Is jointly liable anyway.", "Can be exonerated if he proves he expressly opposed it.",
   "Is liable for 50%.", "Is exonerated only if he resigned."], "b", "Art. 237.")
q("b513", 5, "A businessman who controls a company through a 'front' director without holding a post is:",
  ["Not liable, since he isn't registered.", "A de facto director, liable as a de jure director.",
   "Liable only criminally.", "A shareholder with no duties."], "b", "Art. 236.3.")
q("b514", 5, "The corporate liability action is first brought by:",
  ["Creditors.", "The company, by GM resolution.", "Any shareholder individually.", "The CNMC."], "b", "")
q("b515", 5, "Shareholders may bring the corporate action subsidiarily if they hold at least:",
  ["1%", "3%", "5%", "10%"], "c", "")
q("b516", 5, "A director's negligent false statement causes direct loss to a supplier. The supplier should bring:",
  ["The corporate liability action.", "The individual liability action (art. 241).",
   "A claim before the CNMC.", "A challenge of the GM resolution."], "b", "")
q("b517", 5, "The GM resolution to bring a corporate liability action against directors:",
  ["Must appear on the agenda.", "Can be adopted even if not on the agenda and implies removal of the affected directors.",
   "Needs unanimity.", "Needs creditors' approval."], "b", "")
q("b518", 5, "Creditors may bring the corporate liability action:",
  ["Always first.", "Only if company and members haven't, and the company's assets are insufficient.",
   "Never.", "Only in an S.A."], "b", "Art. 240.")
# Unit 6
q("b601", 6, "As a rule, by-law amendments are approved by:",
  ["The directors.", "The general meeting.", "The Registrar.", "Members with 5%."], "b", "Art. 285.1 LSC.")
q("b602", 6, "Unless the by-laws provide otherwise, moving the registered office from Barcelona to Madrid can be decided by:",
  ["Only the general meeting.", "The directors.", "The Registrar.", "The Autonomous Community."], "b", "Art. 285.2.")
q("b603", 6, "Moving the registered office to Portugal:",
  ["Is decided by the directors.", "Is a structural change decided by the general meeting.", "Is forbidden.", "Needs only a notarial deed."], "b", "")
q("b604", 6, "A by-law amendment imposing new obligations on members (e.g. ancillary commitments):",
  ["Needs only the ordinary majority.", "Needs the consent of the affected members.",
   "Is forbidden.", "Can be decided by the directors."], "b", "Art. 291 ff.")
q("b605", 6, "The GM substantially changes the corporate purpose. A dissenting member:",
  ["Must accept it.", "Has a right to exit and obtain fair value (art. 346).",
   "Can veto it.", "Can only sell to the majority at par value."], "b", "")
q("b606", 6, "Which capital increase does NOT increase equity?",
  ["Cash contributions.", "Non-cash contributions.", "Offsetting loans.", "Charged to reserves."], "d", "")
q("b607", 6, "In an S.A., a capital increase by offsetting loans requires:",
  ["100% of loans liquid, mature and payable.", "At least 25% liquid, mature and payable, the rest maturing within 5 years, plus an auditor's certificate.",
   "Creditors' unanimous consent only.", "An expert appointed by the Registrar."], "b", "S.L.: 100% liquid, mature, payable.")
q("b608", 6, "The pre-emptive right exists in capital increases with:",
  ["Any contribution.", "Cash contributions.", "Non-cash contributions only.", "Reserves only."], "b", "")
q("b609", 6, "The minimum period to exercise the pre-emptive right (non-listed) is:",
  ["15 days", "One month", "Two months", "Six months"], "b", "")
q("b610", 6, "A share premium is charged in a capital increase mainly to:",
  ["Pay the notary.", "Compensate old members for reserves and expectations created before new members enter.",
   "Increase the par value of old shares.", "Avoid registration."], "b", "")
q("b611", 6, "A capital increase must be registered:",
  ["When the GM adopts the resolution.", "Together with its execution (art. 315).",
   "Within 6 months, before execution.", "Only in S.A."], "b", "")
q("b612", 6, "In an S.A., the GM may delegate the decision to increase capital to:",
  ["The directors, within legal limits.", "The auditors.", "Any shareholder with 5%.", "Nobody."], "a", "Art. 297.")
q("b613", 6, "A capital increase charged to reserves requires a balance sheet approved by the GM no more than:",
  ["One month before.", "Six months before.", "One year before.", "Two years before."], "b", "Art. 303.")
q("b614", 6, "Mandatory capital reduction to compensate losses applies:",
  ["To S.A. and S.L. when equity < ½ capital.", "Only to S.A. when equity < 2/3 of capital and not recovered within one fiscal year.",
   "Only to S.L.", "Whenever there are any losses."], "b", "Art. 327.")
q("b615", 6, "Creditors' right to oppose a capital reduction exists when the reduction:",
  ["Restores the balance after losses.", "Funds the legal reserve.", "Refunds contributions to members (S.A.).", "Is mandatory."], "c", "")
q("b616", 6, "Creditors must exercise their right to oppose within:",
  ["15 days of the GM.", "One month after the last announcement.", "Three months.", "One year."], "b", "")
q("b617", 6, "An S.A. reduces its capital to €10,000 to compensate losses and simultaneously increases it to €80,000. This is:",
  ["Illegal, below minimum.", "The 'accordion' operation, valid if the reduction is conditional on the increase and both are registered together.",
   "A transformation.", "A merger."], "b", "Art. 343.")
q("b618", 6, "Which is a valid alternative to avoid dissolution when an S.A.'s capital must be reduced below €60,000?",
  ["Ignore the minimum.", "Transform into an S.L.", "Ask the CNMC.", "Issue bonds."], "b", "")
q("b619", 6, "Which is NOT a way to reduce capital?",
  ["Reducing par value.", "Redeeming shares.", "Grouping shares to exchange them.", "Issuing new shares."], "d", "")
q("b620", 6, "A capital reduction to compensate losses:",
  ["Reduces equity.", "Leaves equity unchanged – it's a book entry between capital and losses.",
   "Requires paying members.", "Needs creditor consent."], "b", "Annex example.")
# Unit 7
q("b701", 7, "Structural changes are regulated by:",
  ["The Commerce Code.", "Real Decreto-ley 5/2023 (RDLME).", "The Trademarks Act.", "The LDC."], "b", "")
q("b702", 7, "Which is NOT a structural change under the RDLME?",
  ["Transformation", "Merger", "Capital increase", "Global assignment of assets and liabilities"], "c", "")
q("b703", 7, "In a merger by creation of a new company:",
  ["Only one company is extinguished.", "All merging companies are extinguished.", "No company is extinguished.", "The members keep shares in the old companies."], "b", "")
q("b704", 7, "The common draft terms of merger must be approved by the GMs within:",
  ["One month.", "Six months from signature, otherwise it lapses.", "One year.", "Three months."], "b", "")
q("b705", 7, "An independent expert report on the merger draft is mandatory when:",
  ["Any participating company is an S.A.", "All companies are S.L.", "The merger is by absorption.", "Never."], "a", "")
q("b706", 7, "The exchange ratio is calculated on the basis of:",
  ["Par value.", "Fair value.", "Book value only.", "The number of employees."], "b", "")
q("b707", 7, "A merger becomes legally effective:",
  ["When the GMs approve it.", "When the draft is signed.", "Upon registration in the Mercantile Registry.", "After the 1-month creditor period."], "c", "")
q("b708", 7, "After registration, a merger can be challenged:",
  ["Never.", "Only for breach of the RDLME, within three months.", "Freely within one year.", "Only by the CNMC."], "b", "")
q("b709", 7, "In the absorption of a wholly-owned subsidiary, which is NOT required?",
  ["Common draft terms.", "Registration.", "Capital increase of the absorbing company.", "Public deed."], "c", "Art. 53 RDLME.")
q("b710", 7, "A merger between 'twin' companies (common 100% shareholder):",
  ["Requires no formalities.", "Is simplified, but still requires capital increase and expert report.",
   "Is prohibited.", "Requires CNMC authorisation in all cases."], "b", "Art. 49.2.")
q("b711", 7, "In a partial demerger (spin-off):",
  ["The company is extinguished.", "The company survives, reduces capital, and its members receive shares of the beneficiaries.",
   "The company receives the beneficiaries' shares.", "Members lose all participation."], "b", "")
q("b712", 7, "After a segregation, the relationship between the segregated company and the beneficiary is:",
  ["None.", "Parent–subsidiary.", "Merger.", "Partnership."], "b", "")
q("b713", 7, "Under art. 42 CCom, control is presumed when the parent:",
  ["Holds 10% of the votes.", "Holds or may hold the majority of votes, or can appoint/remove the majority of directors.",
   "Has the same registered office.", "Is a supplier."], "b", "")
q("b714", 7, "Two members with 50% each block every decision. This is:",
  ["Not relevant legally.", "Paralysis of corporate bodies – a legal cause of dissolution.",
   "A ground for merger.", "A competition infringement."], "b", "")
q("b715", 7, "Losses reduce an S.L.'s equity to 40% of its capital. This is:",
  ["A cause of mandatory capital reduction.", "A legal cause of dissolution unless capital is increased/reduced sufficiently (if insolvency isn't due).",
   "Irrelevant for S.L.", "A cause for merger."], "b", "Art. 363.1.e.")
q("b716", 7, "During liquidation:",
  ["The company loses legal personality.", "The company keeps legal personality and adds 'en liquidación' to its name.",
   "Directors keep managing.", "Members can distribute assets before paying creditors."], "b", "")
q("b717", 7, "With the opening of liquidation:",
  ["Directors become liquidators by force of law in all cases and nothing changes.", "Directors cease and liquidators assume representation.",
   "The GM ceases to exist.", "The Registrar manages the company."], "b", "Art. 375.")
q("b718", 7, "Liquidators must draw up an inventory and balance sheet within:",
  ["One month.", "Three months.", "Six months.", "One year."], "b", "")
q("b719", 7, "Members who didn't vote for the distribution proposal may challenge it within:",
  ["15 days.", "One month.", "Two months.", "Six months."], "c", "Art. 390.")
q("b720", 7, "The legal personality of a capital company ends:",
  ["With the dissolution resolution.", "With the start of liquidation.", "When its entries are cancelled in the Registry after liquidation.", "When the directors resign."], "c", "")
# Unit 8
q("b801", 8, "Industrial property includes:",
  ["Copyright and patents.", "Distinctive signs and industrial creations.", "Books and music.", "Trade secrets only."], "b", "")
q("b802", 8, "The essential element of a trademark is:",
  ["Registration in the EU.", "Its distinctiveness.", "Its graphic beauty.", "Its price."], "b", "")
q("b803", 8, "The right to a Spanish trademark is acquired by:",
  ["First use in the market.", "Valid registration at the OEPM.", "Registration in the Mercantile Registry.", "Notarial deed."], "b",
  "Constitutive registration (except renowned marks).")
q("b804", 8, "A Spanish trademark lasts:",
  ["20 years, not renewable.", "10 years from application, renewable indefinitely for 10-year periods.",
   "5 years renewable once.", "Indefinitely without renewal."], "b", "")
q("b805", 8, "A registered trademark not used in Spain for 5 years:",
  ["Becomes renowned.", "Lapses and its registration is cancelled.", "Is automatically renewed.", "Becomes a trade name."], "b", "")
q("b806", 8, "A trademark used by members of an association, which owns it, is a:",
  ["Guarantee trademark.", "Collective trademark.", "Renowned trademark.", "Trade name."], "b", "")
q("b807", 8, "A trademark certifying that products meet common quality requirements is a:",
  ["Collective trademark.", "Guarantee (warranty) trademark.", "International trademark.", "Shop sign."], "b", "")
q("b808", 8, "A renowned trademark:",
  ["Is protected only in its class.", "Can be protected beyond its class and even if not registered in Spain.",
   "Lasts 20 years.", "Doesn't need distinctiveness."], "b", "Art. 8 LM; ZARA case.")
q("b809", 8, "The nullity action against a trademark registered despite an ABSOLUTE prohibition:",
  ["Must be brought within 5 years.", "Has no time limit (imprescriptible).", "Must be brought within 2 months.", "Doesn't exist."], "b", "")
q("b810", 8, "Which is a RELATIVE prohibition?",
  ["A sign devoid of distinctiveness.", "A sign confusable with an earlier registered trademark for similar goods.",
   "A sign contrary to public order.", "A sign reproducing the Spanish flag."], "b", "")
q("b811", 8, "'BioFresh 100%' for vegetables that aren't organic would most likely be refused because it is:",
  ["Confusable with a competitor.", "Deceptive/descriptive – an absolute prohibition.", "A shop sign.", "Too long."], "b", "")
q("b812", 8, "The trade name identifies:",
  ["Specific products.", "The business/entrepreneur in trade.", "The physical store front.", "The patent owner."], "b", "")
q("b813", 8, "Shop signs (rótulos de establecimiento):",
  ["Are protected by the Trademarks Act.", "Are not protected by the Trademarks Act, but misuse may be unfair competition.",
   "Are patents.", "Must be registered."], "b", "")
q("b814", 8, "Which is NOT a patentability requirement?",
  ["Novelty", "Inventive step", "Industrial application", "Commercial success"], "d", "")
q("b815", 8, "Novelty for patent purposes means the invention:",
  ["Is not known in Spain.", "Is not part of the state of the art anywhere in the world before filing.",
   "Has not been patented in the EU.", "Is not sold yet."], "b", "Absolute novelty.")
q("b816", 8, "Which can be patented?",
  ["A mathematical method.", "A new machine with inventive step and industrial application.",
   "A computer program as such.", "A surgical method."], "b", "")
q("b817", 8, "A patent lasts:",
  ["10 years renewable.", "20 years, not renewable.", "25 years.", "Indefinitely if exploited."], "b", "")
q("b818", 8, "If a patent is not exploited within 3 years from grant publication (or 4 from filing):",
  ["It lapses immediately.", "A compulsory licence may be granted.", "It's extended.", "It becomes a trademark."], "b", "")
q("b819", 8, "An engineer hired to research develops an invention as part of his job. It belongs to:",
  ["The engineer.", "The employer (service invention).", "Both equally.", "The public domain."], "b", "")
q("b820", 8, "A salesperson (not hired to research) invents something using company resources. The employer:",
  ["Owns it automatically.", "May claim ownership or use, paying fair compensation (mixed invention).",
   "Has no rights.", "Must share it with competitors."], "b", "")
q("b821", 8, "A compulsory licence may be granted for:",
  ["Lack of exploitation, public interest, or anti-competitive practices.", "Any request from a competitor.",
   "The patent holder's death.", "Trademark disputes."], "a", "")
q("b822", 8, "Which is NOT considered an invention under the Patents Act?",
  ["A new chemical process.", "A scientific discovery.", "A new engine.", "A new manufacturing device."], "b", "")
# Unit 9
q("b901", 9, "The Spanish Defence of Competition Act (LDC) is:",
  ["Act 3/1991.", "Act 15/2007.", "Act 17/2001.", "Act 24/2015."], "b", "3/1991 = Unfair Competition; 17/2001 = Trademarks; 24/2015 = Patents.")
q("b902", 9, "For a collusive practice to be prohibited under art. 1 LDC:",
  ["Intent to harm competitors must be proven.", "It's enough that the agreement may restrict competition in all/part of the national market.",
   "Actual damage to consumers must be proven.", "It must be in writing."], "b", "Objective prohibition.")
q("b903", 9, "Which is an expressly listed collusive practice?",
  ["Opening a new store.", "Sharing markets or sources of supply.", "Advertising lower prices.", "Hiring employees from a competitor."], "b", "")
q("b904", 9, "Holding a dominant position in the market:",
  ["Is always prohibited.", "Is legal; only its abuse is prohibited.", "Requires CNMC authorisation.", "Requires at least 50% share to be illegal."], "b", "")
q("b905", 9, "Which is an example of abuse of dominant position?",
  ["Offering better quality.", "Unjustified refusal to supply.", "Lowering prices thanks to efficiency.", "Patenting an invention."], "b", "")
q("b906", 9, "Conduct between competitors is of minor importance if their combined market share does not exceed:",
  ["5%", "10%", "15%", "30%"], "b", "Non-competitors: 15% each.")
q("b907", 9, "Two competitors with a combined 4% share fix their selling prices. This is:",
  ["Allowed as de minimis.", "Prohibited – price fixing between competitors is never of minor importance.",
   "Allowed if consumers benefit.", "Only an unfair competition act."], "b", "")
q("b908", 9, "A concentration must be notified to the CNMC if it reaches a market share of at least:",
  ["10%", "25%", "30%", "50%"], "c", "Or turnover > €240M with ≥2 participants > €60M each.")
q("b909", 9, "Before CNMC authorisation, a notifiable concentration:",
  ["Can be executed if notified.", "Is suspended – it cannot be executed.", "Is automatically approved after 15 days.", "Needs only shareholder approval."], "b", "")
q("b910", 9, "Under EU law, State aid is:",
  ["Always allowed.", "In principle incompatible, with exceptions (e.g. natural disasters) and a de minimis of €200,000 over 3 years.",
   "Prohibited by the Spanish LDC.", "Only controlled by the CNMC."], "b", "")
q("b911", 9, "A cartel affecting several EU Member States is supervised by:",
  ["The CNMC.", "The European Commission.", "The Spanish Supreme Court.", "The OEPM."], "b", "")
q("b912", 9, "The maximum fine for very serious competition infringements is:",
  ["1% of turnover.", "5% of turnover.", "10% of turnover.", "€60,000."], "c", "Representatives: up to €60,000.")
q("b913", 9, "Under the leniency programme, the first cartel member to provide decisive evidence:",
  ["Gets a 10% reduction.", "Can be exempted from the fine.", "Must pay double.", "Is excluded from the market."], "b", "")
q("b914", 9, "Under the Unfair Competition Act, an act is unfair:",
  ["Only if the contract is concluded.", "Whether performed before, during or after a transaction, and whether or not the contract is concluded.",
   "Only if done by an entrepreneur.", "Only if intentional."], "b", "")
q("b915", 9, "The general clause (art. 4 LCD) defines as unfair any conduct:",
  ["Causing losses to a competitor.", "Objectively contrary to good faith.", "Not authorised by the CNMC.", "Involving low prices."], "b", "")
q("b916", 9, "Publicly stating true facts about a competitor's personal life to harm its reputation is:",
  ["Lawful because true.", "Unfair defamation – personal matters are not appropriate even if true.",
   "Comparative advertising.", "Misleading omission."], "b", "")
q("b917", 9, "Comparative advertising is lawful if, among others:",
  ["It compares products with different purposes.", "It objectively compares essential, relevant features and is true.",
   "It mentions only the competitor's weaknesses.", "It uses the competitor's reputation."], "b", "")
q("b918", 9, "Selling below cost is unfair:",
  ["Always.", "Only if systematic and misleading about price levels or aimed at eliminating a competitor.",
   "Never.", "Only for food."], "b", "")
q("b919", 9, "An airline advertises 'Barcelona for €1' but offers only two seats at that price. This is:",
  ["Lawful marketing.", "Bait advertising – a misleading practice.", "An aggressive practice.", "Comparative advertising."], "b", "")
q("b920", 9, "A sponsored magazine article not marked as advertising is:",
  ["Covert advertising – a misleading practice.", "Lawful journalism.", "Defamation.", "Imitation."], "a", "")
q("b921", 9, "Repeated unsolicited e-mails after the consumer asked to stop are:",
  ["Misleading practices.", "Aggressive practices.", "Lawful if the products are good.", "Collusive practices."], "b", "")
q("b922", 9, "A pyramid scheme where income comes mainly from recruiting other consumers is:",
  ["Lawful if registered.", "Always unfair (misleading practice).", "An abuse of dominant position.", "A concentration."], "b", "")
q("b923", 9, "Which body resolves competition matters at national level?",
  ["OEPM", "CNMC", "BORME", "Registrar"], "b", "Appeals to the Audiencia Nacional.")
q("b924", 9, "Trade secrets are specifically protected by:",
  ["Act 1/2019 on Trade Secrets.", "The Patents Act only.", "The Commerce Code art. 1.", "The LDC."], "a", "")

def stats():
    from collections import Counter
    return Counter(x["unit"] for x in Q), Counter(x["src"] for x in Q)

if __name__ == "__main__":
    ids = [x["id"] for x in Q]; assert len(ids) == len(set(ids))
    print(len(Q), stats())
    json.dump(Q, open("/home/claude/law/out/mc.json", "w"), ensure_ascii=False)
