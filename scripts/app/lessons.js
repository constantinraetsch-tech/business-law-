// Lessons: one per unit. body = trusted HTML. Diagrams use .dia classes from the app stylesheet.
const LESSONS = [
{u:1, title:"The Law, the Rule & the Legal System",
 tldr:"A legal rule is <b>general</b> and <b>enforceable</b>. Rules are born (BOE + 20 days), live and die (repeal). Courts apply <b>law → custom → principles</b>. A lower rule can never beat a higher one. State vs regions = <b>competence</b>, not hierarchy. The EU makes <b>Regulations</b> (directly applicable) and <b>Directives</b> (must be transposed).",
 sections:[
 {h:"Objective vs subjective law", body:`
 <p><b>Objective law</b> = the rule book of a society: an organised set of rules that can be imposed by force (Spanish law, German law). All those rules together form the <b>legal system</b>.</p>
 <p><b>Subjective law</b> = <i>your</i> right that comes out of the rule book: "I have the right to…". You can go to court to enforce it.</p>
 <div class="dia vs"><div><h5>Objective</h5>The rules<br><small>"Spanish law says…"</small></div><div><h5>Subjective</h5>A person's power<br><small>"I have the right to…"</small></div></div>`},
 {h:"What makes a rule a legal rule?", body:`
 <p>Two characters – remember <b>G + C</b>:</p>
 <ul><li><b>Generality</b>: it targets abstract categories, not one person. A new duty for <i>all</i> S.A.s = legal rule. A decree appointing <i>Mr. X</i> to a post = <b>not</b> a legal rule.</li>
 <li><b>Coercibility</b>: if you don't obey, <b>institutionalised force</b> (the courts) can make you. Saying "good morning" is a social rule – nobody can force you.</li></ul>
 <p>To work in practice, rules need <b>interpretation</b>, <b>validity</b> and <b>effectiveness</b>.</p>`},
 {h:"Interpretation (art. 3 CC)", body:`
 <p>Read the <b>words</b> → in their <b>context</b> → with their <b>history</b> → in today's <b>social reality</b> → always looking at their <b>spirit and purpose</b>. When the words aren't enough, use the <b>purposive approach</b>: what did the legislator want to achieve?</p>`},
 {h:"Life of a rule: birth, life, death", body:`
 <div class="dia flow"><span>Published in the <b>BOE</b><small>enactment</small></span><span><b>Vacatio legis</b><small>20 days by default</small></span><span><b>In force</b><small>binding</small></span><span><b>Repeal</b><small>express or tacit</small></span></div>
 <p><b>Express repeal</b>: the new rule says "rule X is repealed". <b>Tacit repeal</b>: a new rule of the same or higher rank regulates the same thing differently – the old one dies where they conflict.</p>
 <p><b>Effectiveness</b> (art. 6 CC): <i>"Ignorance of the law does not excuse from compliance."</i> Once in the BOE, everybody is assumed to know it.</p>`},
 {h:"Mandatory vs dispositive rules", body:`
 <div class="dia vs"><div><h5>Mandatory</h5>Apply no matter what the parties want. Acts against them are <b>void</b> (art. 6.3 CC).</div><div><h5>Dispositive</h5>Apply only <b>if the parties don't agree otherwise</b>. Example: art. 314 CCom – loans bear no interest unless agreed in writing.</div></div>`},
 {h:"Sources of law and their order", body:`
 <p>Art. 1 CC: <b>law, custom, general principles of law</b>, in that order.</p>
 <div class="dia steps"><div><b>1 Law</b><small>written rules from the State, regions, EU…</small></div><div><b>2 Custom</b><small>only if no law, not against morals/public order, and <b>proven</b></small></div><div><b>3 General principles</b><small>justice, freedom, equality (mostly in the Constitution)</small></div></div>
 <p><b>Case law is NOT a source</b>. Repeated Supreme Court doctrine only <b>complements</b> the system.</p>
 <p><b>Material</b> sources = <i>who</i> makes rules (State, regions, EU). <b>Formal</b> sources = <i>what form</i> they take (law, custom, principles).</p>`},
 {h:"The hierarchy pyramid", body:`
 <div class="dia pyr"><div style="--w:30%">Constitution</div><div style="--w:46%">International treaties · EU law</div><div style="--w:62%">Acts (ordinary & organic)</div><div style="--w:76%">Royal Legislative Decree · Royal Decree-Law</div><div style="--w:88%">Royal Decrees (regulations)</div><div style="--w:100%">Ministerial orders & lower rules</div></div>
 <p>Rule: a <b>lower rule can't contradict, invalidate or repeal a higher one</b> (art. 9.3 CE). A Royal Decree that contradicts an act is <b>null</b>.</p>
 <ul><li><b>Act</b>: made by Parliament (Cortes Generales = Congress + Senate).</li>
 <li><b>Royal Decree-Law</b>: Government, <b>urgent</b> need – status of an act.</li>
 <li><b>Royal Legislative Decree</b>: Government, <b>delegated</b> by a framework law – status of an act. (The LSC is RLD 1/2010!)</li>
 <li><b>Royal Decree</b>: Government's own power, e.g. a regulation developing an act.</li></ul>`},
 {h:"State, regions, treaties and the EU", body:`
 <p><b>State vs Autonomous Communities</b>: <b>competence, not hierarchy</b> (arts. 148–149 CE + Statutes of Autonomy). Regional laws go in their own gazettes (DOGC, BOCM).</p>
 <p><b>Treaties</b>: above all internal law, but below the Constitution – a treaty contrary to it needs a <b>constitutional amendment first</b> (art. 95 CE).</p>
 <p><b>EU</b> (Spain since 1986): competence-based, but EU law <b>prevails</b> in conflicts.</p>
 <div class="dia vs"><div><h5>EU Regulation</h5>Like a European act. <b>Directly applicable</b> to everyone. No transposition. Ex: GDPR.</div><div><h5>EU Directive</h5>Addressed to <b>Member States</b> to harmonise. Must be <b>transposed</b>. National law is interpreted in line with it anyway (STS 428/2007).</div></div>
 <p class="tip">Don't confuse an <b>EU Regulation</b> (top level, like an act) with a Spanish <b>regulation</b> (a Royal Decree under an act).</p>`}
 ],
 traps:["Case law is a source of law → <b>false</b> (it complements).","State law always ranks above regional law → <b>false</b> (competence).","All internal law ranks above treaties → <b>false</b> (treaties are above, except the Constitution).","Directives are directly applicable like Regulations → <b>false</b>.","A rule enters into force on the day of publication → <b>false</b> (20 days unless stated)."],
 check:[["What are the two characters of a legal rule?","Generality and coercibility."],["In which order do courts apply the sources?","Law → custom → general principles."],["Which ranks higher: an RDL or a Royal Decree?","The Royal Decree-Law (status of an act)."],["Regulation or Directive – which needs transposition?","The Directive."]]},

{u:2, title:"Business Law & the Entrepreneur",
 tldr:"Business Law is <b>special private law for entrepreneurs</b>. The <b>enterprise</b> (assets + work) has no legal personality; the <b>entrepreneur</b> (natural or legal person acting in its own name) does. Entrepreneurs must keep accounts, publicise (companies must register) and compete fairly. They answer with <b>all present and future assets</b>. Partners in partnerships are personally liable; members of capital companies are <b>not</b>.",
 sections:[
 {h:"Where Business Law comes from", body:`
 <p>Born in the <b>Middle Ages</b> as a <b>customary</b> law of traders (guilds, <i>Consulados del Mar</i> in Barcelona, Valencia, Bilbao…). Codified in the <b>1829</b> Commerce Code and replaced by the <b>1885</b> Commerce Code – still the framework today, though most of it has been replaced by special laws (<b>lex specialis</b>: special laws prevail over general ones).</p>
 <p><b>Definition</b>: the part of <b>private</b> law for <b>entrepreneurs</b> and their <b>legal status</b>, about their <b>market activity through an enterprise</b>. Employment law and tax law affect entrepreneurs but are <b>not</b> Business Law.</p>`},
 {h:"Sources of Business Law", body:`
 <ul><li><b>Art. 38 CE</b>: free enterprise within a market economy (basis of competition law).</li>
 <li><b>Art. 149.1.6 CE</b>: commercial legislation = <b>exclusive State competence</b> → market unity.</li>
 <li><b>Art. 2 CCom</b>: acts of commerce → <b>Code</b> → <b>business usage</b> → <b>civil law</b>. Usage beats civil law, a trace of the customary origin.</li>
 <li><b>Art. 50 CCom</b> limit: for <b>contracts</b>, civil law applies directly (no usage in between).</li>
 <li>Today most rules = EU <b>Regulations</b> applied directly, or <b>Directives</b> transposed.</li></ul>`},
 {h:"Enterprise vs entrepreneur vs business", body:`
 <div class="dia three"><div><h5>Enterprise</h5>Organised capital + work. <b>No legal personality.</b></div><div><h5>Entrepreneur</h5>Natural or legal person acting <b>in its own name</b>. Holds rights & obligations.</div><div><h5>Business / establishment</h5>Assets <b>+ contracts, staff, reputation</b>. What you buy, sell or lease.</div></div>
 <p>Saying "I bought an enterprise" is legally wrong – you buy a <b>business (establishment)</b>, which is usually worth more than its isolated assets because of contracts, brand and clients.</p>
 <p>Three features of the legal entrepreneur – <b>O-P-O</b>: <b>O</b>rganises means, acts <b>P</b>rofessionally (habitually, publicly, for the market), in its <b>O</b>wn name. Directors, attorneys and employees act in someone else's name → <b>not</b> entrepreneurs.</p>`},
 {h:"Types of entrepreneurs", body:`
 <ul><li><b>Natural person</b> (individual, sole trader) vs <b>legal person</b> (business entity, born from a partnership agreement).</li>
 <li>By <b>size</b>: no different general status, but special rules (accounting plans for SMEs, corporate tax). EU SME definition: Reg. 651/2014.</li>
 <li><b>Private vs public</b>: a public enterprise is held by a public body but carries on an economic activity.</li></ul>`},
 {h:"The legal status: duties, rights, capacity, liability", body:`
 <div class="dia vs"><div><h5>Duties</h5>1. Keep <b>accounts</b> (art. 25 CCom)<br>2. <b>Publicity</b>: Mercantile Registry – <b>mandatory for companies, optional for individuals</b><br>3. Respect <b>free & fair competition</b></div><div><h5>Rights</h5>1. <b>Compete</b> in the market<br>2. Demand <b>fair</b> competition<br>3. <b>Exclusive</b> trademarks, trade names, patents</div></div>
 <p><b>Legal capacity</b> (from birth: hold rights) vs <b>capacity to operate</b> (18 + not incapacitated: perform valid acts). Individual entrepreneur: legal age + free disposal of assets (art. 4 CCom). Exceptions: a <b>minor heir</b> continuing the parents' business, or an entrepreneur who <b>becomes incapacitated</b>, both acting through representatives.</p>
 <p><b>Restrictions</b>: <b>incompatibilities</b> (absolute: ministers; relative: judges in their territory), <b>prohibitions to compete</b> (agents art. 288 CCom, workers, directors – contracts stay valid), <b>disqualifications</b> (sanction), administrative <b>authorisations</b>.</p>
 <p><b>Liability</b>: for <b>contractual and non-contractual</b> damage, for <b>own acts and dependants'</b>, with <b>all present and future assets</b> (art. 1911 CC). A sole trader doesn't separate private and business assets.</p>`},
 {h:"Business entities & liability", body:`
 <p>A trading company (art. 116 CCom) gets <b>legal personality</b> once incorporated → own rights, own assets, separate liability. It acts through <b>representatives</b> (legal or voluntary) – "no hands, no brain".</p>
 <p>The company always answers with <b>all its assets</b>. The question is whether the <b>members</b> answer too:</p>
 <table class="tbl"><tr><th></th><th>General partnership</th><th>Limited partnership</th><th>S.A. / S.L.</th></tr>
 <tr><td>Members liable?</td><td>Yes: personal, unlimited, <b>subsidiary</b>, joint & several</td><td>General partners yes; limited partners up to contribution</td><td><b>No</b> (art. 1 LSC)</td></tr>
 <tr><td>Character</td><td>Personalistic</td><td>Personalistic (hybrid)</td><td>Capitalist (S.L. hybrid inside)</td></tr>
 <tr><td>Name</td><td>Partners' names + "y Cía." + S.C./S.R.C.</td><td>Only general partners + S.Com.</td><td>Any name + S.A./S.L.</td></tr>
 <tr><td>Transfer</td><td>Needs consent</td><td>Limited partners free</td><td>S.A. free / S.L. restricted</td></tr></table>
 <p><b>Irregular company</b> (not registered): managers jointly & severally liable (art. 120 CCom) and members liable like general partners – <b>even if it's an S.A./S.L.</b></p>
 <p><b>Lifting the veil</b>: if members abuse the company (mix assets, act as if it didn't exist), courts ignore the separation (arts. 6.4, 7 CC).</p>`}
 ],
 traps:["Enterprise = entrepreneur → <b>false</b>.","All entrepreneurs must register → <b>false</b> (optional for individuals).","Capacity to act is acquired at birth → <b>false</b> (that's legal capacity).","Contracts concluded in breach of a prohibition to compete are void → <b>false</b>.","Members of a capital company are never liable → careful: <b>irregular company</b> or <b>veil lifting</b> can make them liable."],
 check:[["Who is the entrepreneur: the S.L. or its manager?","The S.L. (in whose name the activity is carried out)."],["Three duties of every entrepreneur?","Accounts, publicity (registry), fair competition."],["Liability of a general partner?","Personal, unlimited, subsidiary, joint & several."]]},

{u:3, title:"Capital Companies: Incorporation",
 tldr:"S.A. needs <b>€60,000</b> (25% paid), S.L. <b>€3,000</b> (100% paid). Founders sign a <b>deed before a notary</b> containing the <b>by-laws</b> and <b>register</b> it (within 1 year) → legal personality. Contributions: cash or assets – <b>never work</b>. Capital ≠ equity: equity = capital + reserves ± losses. Value a share three ways: <b>par</b>, <b>book</b>, <b>fair</b>.",
 sections:[
 {h:"S.A. or S.L.?", body:`
 <table class="tbl"><tr><th></th><th>S.L. (private limited)</th><th>S.A. (public limited)</th></tr>
 <tr><td>Minimum capital</td><td><b>€3,000</b></td><td><b>€60,000</b></td></tr>
 <tr><td>Paid at incorporation</td><td><b>100%</b></td><td>min <b>25%</b> (rest = called-up capital)</td></tr>
 <tr><td>Non-cash contribution</td><td>No expert report</td><td><b>Independent expert report</b> (as a rule)</td></tr>
 <tr><td>Units</td><td><b>Stakes</b> (participaciones) – not securities</td><td><b>Shares</b> (acciones) – negotiable securities</td></tr>
 <tr><td>Transfer</td><td>Restricted</td><td>Free (by-laws may restrict)</td></tr>
 <tr><td>GM attendance</td><td>Can't be restricted</td><td>Minimum number of shares possible</td></tr>
 <tr><td>Votes</td><td>1 per stake (by-laws can change)</td><td>By nominal value</td></tr>
 <tr><td>Board</td><td>3–12</td><td>3–no max</td></tr>
 <tr><td>Director term</td><td>May be indefinite</td><td>Max 6 years, re-electable</td></tr></table>
 <p>Choose: capital &lt; €60,000 → <b>S.L.</b>; want to be <b>listed</b> → <b>S.A.</b>; otherwise weigh formalities vs free transfer. S.L. win in <b>numbers</b> (SMEs); S.A. win in <b>weight</b> (big corporations).</p>`},
 {h:"Incorporation step by step", body:`
 <div class="dia flow"><span>Name certificate<small>Central Registry</small></span><span>Bank deposit<small>certificate</small></span><span>NIF<small>tax number</small></span><span>Deed + by-laws<small>before a <b>notary</b></small></span><span><b>Mercantile Registry</b><small>within 1 year → personality</small></span></div>
 <p><b>Founders</b> sign the deed and subscribe all shares (S.A.) / take up all stakes (S.L.). <b>No minimum number</b>: one person can form an <b>S.A.U./S.L.U.</b> – a sole trader's way to limit liability.</p>
 <p><b>Deed</b> (art. 22 LSC): founders' identity, contributions & numbering, <b>by-laws</b>, initial directors, (S.A.) incorporation expenses.</p>
 <p><b>By-laws</b> (art. 23 LSC): name (+S.A./S.L., not identical to another), corporate purpose, registered office (in Spain), capital, shares/stakes, management body & GM rules, ancillary commitments. Defaults if silent: unlimited duration, starts on the deed date, year ends <b>31 Dec</b>.</p>`},
 {h:"Company in formation & irregular company", body:`
 <p>Between the deed and registration = <b>company in formation</b>. Acts <b>needed for registration</b> bind the company automatically; <b>other acts</b> only if the company accepts them after registration – otherwise whoever acted is liable (art. 36).</p>
 <p>Not registered within <b>1 year</b> (or clearly never going to be) → <b>irregular company</b>: any member can ask for dissolution and refund; if it already traded, members answer like <b>general partners</b> for those debts.</p>
 <p><b>Why registration matters</b>: members aren't personally liable, so third parties need public, verified information on capital, directors and accounts → the Registry is a <b>filter of lawfulness + publicity</b>.</p>`},
 {h:"Contributions", body:`
 <ul><li><b>Cash</b>: in euros, proven with a <b>bank certificate</b>.</li>
 <li><b>Non-cash</b>: any asset with economic value (building, machine, trademark, credit, goodwill). Contributor <b>liable for its value</b> (both types); <b>S.A.</b> also needs an <b>independent expert</b> appointed by the Registrar.</li>
 <li><b>Never work or services</b> (art. 58.2). Work can enter as an <b>ancillary commitment</b> (art. 86) – outside capital, free or paid.</li></ul>`},
 {h:"Capital, equity, reserves", body:`
 <div class="dia bal"><div class="l"><h5>Assets</h5>goods & rights</div><div class="r"><div class="eq"><h5>Equity (own funds)</h5>Capital + reserves ± losses, grants, premium…</div><div class="li"><h5>Liabilities</h5>debts to third parties</div></div></div>
 <p><b>Equity = assets − liabilities.</b> At incorporation capital = equity. Then profits kept as <b>reserves</b> (legal, statutory, voluntary) push equity <b>above</b> capital; <b>losses</b> push it <b>below</b>.</p>
 <p>Four principles protect capital: <b>determination</b> (fixed in by-laws), <b>full subscription & minimum payment</b>, <b>integrity</b> (real contributions), <b>minimum outlay</b> (€60k/€3k, always).</p>`},
 {h:"Members: obligations & rights", body:`
 <p>Obligations: only pay <b>called-up capital</b> (S.A.) and do <b>ancillary commitments</b> (if any). Everything else is a right.</p>
 <p>Rights – <b>D-L-P-V-C-I</b>: <b>D</b>ividends, <b>L</b>iquidation dividend, <b>P</b>re-emptive right, <b>V</b>ote & attend, <b>C</b>hallenge resolutions, <b>I</b>nformation.</p>`},
 {h:"Par, book and fair value (annex example)", body:`
 <div class="dia steps"><div><b>Par value</b><small>chosen freely by founders<br>€75,000 ÷ 750 = <b>€100</b></small></div><div><b>Book value</b><small>equity ÷ shares<br>(75,000 + 100,000 reserves) ÷ 750 = <b>€233.33</b></small></div><div><b>Fair value</b><small>book value ± expectations<br>(175,000 + 200,000) ÷ 750 = <b>€500</b></small></div></div>
 <p>No losses & retained profits → BV &gt; PV. Positive expectations → FV &gt; BV.</p>`}
 ],
 traps:["Capital must always be fully paid → <b>false</b> (S.A. 25%).","S.L. capital is divided into shares → <b>false</b> (stakes).","Work can be contributed to an S.L. → <b>false</b>.","S.L. non-cash contributions need an expert → <b>false</b> (only S.A.).","Capital and equity are the same → <b>false</b>.","All shares must have the same par value → <b>false</b>."],
 check:[["Minimum paid-up capital of an S.A. with €80,000 capital?","€20,000 (25%)."],["What makes members' liability limited?","Registration of the deed in the Mercantile Registry."],["Equity €90,000, 1,000 shares. Book value?","€90 per share."]]},

{u:4, title:"Corporate Bodies I: General Meeting & Directors",
 tldr:"Two bodies: the <b>general meeting</b> (members decide, art. 160 closed list) and the <b>managing body</b> (directors manage & represent). Members can't represent the company. GM must be <b>convened</b> (1 month S.A. / 15 days S.L.), <b>constituted</b> (quorum only in S.A.) and <b>vote</b>. Four director models: <b>sole, joint & several, joint (S.A. max 2), board (3–12 in S.L.)</b>.",
 sections:[
 {h:"Who does what?", body:`
 <div class="dia vs"><div><h5>General meeting</h5>Members' <b>will</b>. Appoints & removes directors, approves accounts, changes by-laws, capital, structural changes, dissolution.</div><div><h5>Managing body</h5><b>Represents & manages</b> (art. 209). Signs contracts, hires, prepares accounts, convenes GMs.</div></div>
 <p>Members are higher in hierarchy but <b>cannot represent</b> the company. Directors <b>need not be members</b> (art. 212.2), can be legal persons, and the GM <b>cannot interfere</b> in management (but evaluates it yearly).</p>`},
 {h:"Competences of the GM (art. 160)", body:`
 <ol class="cols"><li>Annual accounts, profit distribution, approval of management</li><li>Appoint/remove directors, liquidators, auditors; liability action</li><li>Amend the by-laws</li><li>Increase/reduce capital</li><li>Remove/limit pre-emptive rights</li><li>Core assets (&gt; 25% of total assets)</li><li>Transformation, merger, division, global assignment, office abroad</li><li>Dissolution</li><li>Final liquidation balance</li><li>Others by law/by-laws</li></ol>
 <p>Closed list: the GM can't decide outside it. No single member – even with 90% – can exercise it alone (except a <b>single-member</b> company).</p>
 <p><b>Ordinary GM</b>: accounts + management + profits, within the <b>first 6 months</b>. Everything else = <b>extraordinary</b> GM.</p>`},
 {h:"Convene → constitute → vote", body:`
 <div class="dia flow"><span><b>Convene</b><small>directors; website/BORME+paper or individual notice</small></span><span><b>Constitute</b><small>S.A.: quorum (1st/2nd call). S.L.: none</small></span><span><b>Vote</b><small>majorities by law/by-laws</small></span><span><b>Minutes</b><small>minutes book</small></span></div>
 <p><b>Notice</b>: S.A. ≥ <b>1 month</b>, S.L. ≥ <b>15 days</b>. Directors must convene: yearly ordinary GM, when useful, when law/by-laws require, when <b>≥ 5%</b> asks, and when there's a <b>mandatory dissolution cause</b>.</p>
 <p><b>Universal meeting</b>: no notice needed if <b>100% of capital</b> is present and <b>everyone agrees</b> to hold it and on the agenda.</p>
 <p>Only <b>agenda</b> items can be decided – except <b>removal of directors</b> and the <b>liability action</b>.</p>
 <p>Resolutions bind <b>everyone</b>, incl. absent and dissenting members, who may <b>challenge</b> them.</p>`},
 {h:"Quorum & majorities (LSC numbers)", body:`
 <table class="tbl"><tr><th></th><th>S.A.</th><th>S.L.</th></tr>
 <tr><td>Quorum, ordinary matters</td><td>1st call <b>25%</b> · 2nd call <b>any</b></td><td rowspan="2"><b>No quorum</b></td></tr>
 <tr><td>Quorum, by-law amendment, capital, merger…</td><td>1st call <b>50%</b> · 2nd call <b>25%</b></td></tr>
 <tr><td>Majority, ordinary</td><td>More votes for than against (present)</td><td>Majority of votes cast, ≥ <b>1/3 of all votes</b></td></tr>
 <tr><td>Majority, special matters</td><td>Absolute majority; <b>2/3 of present</b> if only 25–50% attend</td><td>Capital change & by-laws: <b>&gt; ½ of all votes</b><br>Merger, transformation, exclusion of pre-emptive right, member exclusion, director competition: <b>≥ 2/3 of all votes</b></td></tr></table>
 <p class="tip">The notes only say "see arts. 193–201 LSC". The numbers above come from the LSC – good to know, but the notes' focus is: <b>quorum only in the S.A.</b> and <b>stricter rules for important decisions</b>.</p>`},
 {h:"Four models for the managing body (art. 210)", body:`
 <div class="dia four"><div><h5>Sole director</h5>One person does everything.</div><div><h5>Joint & several</h5><i>Solidarios</i>: <b>each acts alone</b> with full power.</div><div><h5>Joint</h5><i>Mancomunados</i>: must <b>act together</b>. <b>S.A.: max 2.</b></div><div><h5>Board</h5>Collegiate, majority. <b>Min 3</b>; S.L. max 12. Listed cos must have one.</div></div>
 <p>The model is in the by-laws; changing it → <b>public deed + registry</b>.</p>
 <p><b>Who can't be director</b>: non-emancipated minors, incapacitated, persons disqualified (insolvency), convicted of certain offences, incompatible public officials (judges…).</p>
 <p><b>Term</b>: S.A. max <b>6 years</b> (re-electable); S.L. <b>can be indefinite</b>. The GM can <b>remove</b> directors any time.</p>`}
 ],
 traps:["Members represent the company → <b>false</b>.","S.L. needs a quorum → <b>false</b>.","Joint & several directors must sign together → <b>false</b> (each alone).","An S.A. can have 3 joint directors → <b>false</b> (max 2, else board).","Ordinary GM = all matters; extraordinary only when the call failed → <b>false</b>.","Every director in capital companies: max 6 years → <b>false</b> (only S.A.)."],
 check:[["Notice period S.L.?","15 days."],["What % can force directors to convene a GM?","5%."],["Can a GM decide on removing a director if it's not on the agenda?","Yes – one of the two exceptions."]]},

{u:5, title:"Corporate Bodies II: Directors' Duties & Liability",
 tldr:"Directors act within <b>law + GM/by-laws + duty of care + duty of loyalty</b>. Care = <b>orderly entrepreneur</b> (prudence, competence, dedication, information, vigilance). Loyalty = <b>faithful representative</b> (no conflicts, secrecy, no competing). The <b>business judgment rule</b> protects good-faith, informed, disinterested decisions. Liability: for <b>debts</b> (insolvency not filed / dissolution not convened → later debts) and for <b>damages</b> (fault + damage + causal link). Actions: <b>corporate</b> (company → 5% → creditors) and <b>individual</b>.",
 sections:[
 {h:"The framework of directors' conduct", body:`
 <div class="dia steps"><div><b>Law</b><small>e.g. prepare accounts, convene GM, file insolvency</small></div><div><b>GM & by-laws</b><small>instructions, unless illegal</small></div><div><b>Duty of care</b><small>art. 225</small></div><div><b>Duty of loyalty</b><small>arts. 227–230</small></div></div>`},
 {h:"Duty of care – the orderly entrepreneur", body:`
 <p>Art. 225: act with the diligence of an <b>orderly entrepreneur</b>, put the company's interest first, dedicate enough time, and <b>demand information</b>. Five faces – <b>P-P-D-I-S</b>:</p>
 <ul><li><b>Prudence</b> – no unreasonable risks</li><li><b>Professional competence</b> – more for a bank than for a bakery</li><li><b>Dedication</b></li><li><b>Information</b></li><li><b>Surveillance & control</b> – watch collaborators and the business</li></ul>
 <p><b>Risk monitoring</b>: having an early-warning information system is part of diligence. No system → liability <i>in vigilando</i>. But <b>unforeseeable</b> shocks (Covid-19) are not a breach.</p>`},
 {h:"Duty of loyalty – the faithful representative", body:`
 <p>Art. 227: good faith, best interest of the company. Art. 228 obligations:</p>
 <ul><li>Use powers only for their purpose</li><li><b>Secrecy</b> – also after leaving</li><li><b>Abstain</b> in conflicts (except own appointment/removal)</li><li>Independent, personal judgement</li><li><b>Avoid conflicts</b>, <b>don't compete</b> with the company</li></ul>
 <p>Mandatory – by-laws can't soften it. The <b>GM may exempt</b> a director for a specific case if no harm is expected (art. 230).</p>`},
 {h:"Business judgment rule (art. 226)", body:`
 <div class="dia check"><div>✔ Good faith</div><div>✔ No personal interest</div><div>✔ Sufficient information</div><div>✔ Adequate procedure</div><div class="res">→ diligence presumed, even if the result is bad</div></div>
 <p>A <b>rebuttable presumption</b>: whoever sues must prove the standard wasn't met. Purpose: no fear of honest mistakes, encourage risk-taking, stop members meddling via lawsuits. <b>Excluded</b>: decisions affecting other directors/related persons personally (art. 230 operations).</p>`},
 {h:"Liability for debts", body:`
 <p>Directors pay company debts <b>subsidiarily</b> (only if the company <b>can't</b> pay) in two crisis cases:</p>
 <div class="dia vs"><div><h5>Insolvency</h5>Didn't file for insolvency within <b>2 months</b> → culpable insolvency → liable for debts arising <b>after</b> the filing date.</div><div><h5>Losses</h5>Equity &lt; <b>½ of capital</b> and they didn't convene the GM to dissolve (or fix it) → liable for debts arising <b>after</b> the cause.</div></div>`},
 {h:"Liability for damages (art. 236–237)", body:`
 <div class="dia flow"><span>Breach with <b>fraud or fault</b><small>fault presumed if against law/by-laws</small></span><span><b>Damage</b></span><span><b>Causal link</b></span></div>
 <ul><li>GM <b>approval or ratification never exonerates</b>.</li>
 <li><b>De facto directors</b> (no/expired title, or the person giving instructions behind a front man) are liable too.</li>
 <li>On a board: all who adopted/executed it are <b>jointly & severally</b> liable, unless they <b>prove</b> they opposed, didn't know, or did everything to prevent it.</li></ul>`},
 {h:"Liability actions", body:`
 <div class="dia vs"><div><h5>Corporate action (art. 238)</h5>Damage to the <b>company</b>.<br>1. Company (GM resolution, even off-agenda → removes directors)<br>2. Members ≥ <b>5%</b> (if GM not convened, company doesn't sue in <b>1 month</b>, or GM says no; loyalty breach: directly)<br>3. Creditors (if assets insufficient, art. 240)</div><div><h5>Individual action (art. 241)</h5><b>Direct</b> damage to a <b>member or third party</b>: act of a director in office + unlawfulness + causal link (claimant proves).</div></div>
 <p>Tax and labour law add their own liability towards the Tax Agency and Social Security.</p>`}
 ],
 traps:["A bad result proves negligence → <b>false</b> (business judgment rule).","GM approval exonerates directors → <b>false</b>.","Directors are liable for <i>all</i> company debts → <b>false</b> (only later debts, subsidiarily, in the two cases).","By-laws can limit loyalty → <b>false</b>.","Only registered directors are liable → <b>false</b> (de facto too)."],
 check:[["Four conditions of the business judgment rule?","Good faith, no personal interest, sufficient information, adequate procedure."],["Which debts are directors liable for if they didn't convene the GM?","Debts arising after the dissolution cause."],["Who brings the corporate action first?","The company (GM)."]]},

{u:6, title:"Amendments to the By-laws: Capital Increase & Reduction",
 tldr:"Only the <b>GM</b> amends by-laws (directors may move the office <b>within Spain</b>). Capital <b>increases</b>: cash, non-cash, offsetting loans, reserves (reserves don't increase equity). Old members have a <b>pre-emptive right</b> in cash increases (≥ 1 month). A <b>premium</b> avoids value dilution. <b>Reductions</b>: restore balance after losses, reserves, refunds. S.A. must reduce if equity &lt; <b>2/3</b> for a year. S.A. creditors can oppose reductions that really cut equity. <b>Accordion</b> = reduce below minimum + increase at once.",
 sections:[
 {h:"How to amend the by-laws", body:`
 <div class="dia flow"><span>Agenda states the change</span><span>Full text<small>+ written report in S.A.</small></span><span>Members can see/receive docs</span><span>GM quorum & majority</span><span>Public deed + Registry</span></div>
 <p><b>Registered office</b>: within Spain → <b>directors</b> (unless by-laws expressly deny it, art. 285.2). Abroad → structural change, GM.</p>
 <p><b>Member protection</b>: new obligations (payments, ancillary commitments) or, in S.A., transfer restrictions/class changes need the <b>affected member's consent</b>. Substantial change of corporate purpose → <b>right to exit</b> at fair value (art. 346).</p>`},
 {h:"Capital increase: two ways, four exchange values", body:`
 <p><b>Ways</b>: new shares/stakes, or higher par value. <b>Who</b>: GM (S.A. may delegate to directors, art. 297). <b>Steps</b>: resolution → execution (subscription + payment) → <b>register both together</b> (art. 315).</p>
 <table class="tbl"><tr><th>Exchange value</th><th>Equity</th><th>Special rule</th></tr>
 <tr><td><b>Cash</b></td><td>↑ (more cash)</td><td>Bank certificate. Pre-emptive right.</td></tr>
 <tr><td><b>Non-cash</b></td><td>↑ (more assets)</td><td>S.A.: independent expert report</td></tr>
 <tr><td><b>Offsetting loans</b></td><td>↑ (less debt)</td><td>S.A.: ≥ 25% liquid/mature/payable, rest ≤ 5 yrs + auditor. S.L.: 100%</td></tr>
 <tr><td><b>Reserves</b></td><td><b>= (no change)</b></td><td>Balance sheet ≤ 6 months old</td></tr></table>`},
 {h:"Pre-emptive right & share premium", body:`
 <p>When new members come in, old members' % shrinks. So in <b>cash</b> increases, old members can subscribe <b>in proportion</b> first – period <b>≥ 1 month</b>. Not using it means: smaller dividends, lower book value per share, maybe dropping below <b>5%</b>. It can be <b>excluded by the GM</b> or <b>waived</b> individually.</p>
 <p><b>Premium</b>: new members pay <b>above par</b> to buy into reserves and expectations built before. Example (Case 2): BA pays €10 per €1 stake = €1 capital + €9 premium.</p>
 <div class="dia calc"><div>BA wants <b>10%</b> for <b>€100,000</b></div><div>Post-money = 100,000 ÷ 10% = <b>€1,000,000</b> → pre-money <b>€900,000</b></div><div>90,000 stakes → <b>€10/stake</b></div><div>New stakes: N ÷ (90,000+N) = 10% → <b>N = 10,000</b></div><div>Capital +€10,000 · Premium €90,000 (€9/stake)</div></div>`},
 {h:"Capital reduction", body:`
 <p><b>Ways</b>: lower par value, redeem, or group shares. <b>Purposes</b>: restore capital/equity balance after <b>losses</b>; create <b>reserves</b>; <b>refund</b> contributions; S.A.: release called-up capital.</p>
 <p><b>Mandatory (S.A. only)</b>: equity &lt; <b>2/3 of capital</b> and not recovered within <b>one fiscal year</b> (art. 327).</p>
 <div class="dia calc"><div>Capital 100,000 · losses 50,000 → equity <b>50,000 = 50%</b> &lt; 2/3</div><div>Reduce capital by 30,000 against losses</div><div>Capital 70,000 · losses 20,000 → equity <b>50,000 = 71%</b> ✔</div><div><small>Book entry only – no money moves</small></div></div>
 <p><b>Creditors (S.A.)</b> can oppose within <b>1 month</b> of the last announcement when equity really falls (refunds, release of called-up capital) – <b>not</b> for loss compensation or reserves. Reduction waits until their debt is secured (e.g. bank guarantee).</p>
 <p><b>Accordion</b> (art. 343): reduce below the minimum to absorb losses + <b>simultaneous increase</b> ≥ minimum; pre-emptive right respected; reduction conditional on the increase; registered together. Alternative: transform S.A. → S.L.</p>`}
 ],
 traps:["A capital increase always increases equity → <b>false</b> (reserves).","Directors alone can amend the by-laws → <b>false</b> (except the office within Spain).","The GM can't move the office within Spain → <b>false</b>.","Creditors can always oppose a reduction → <b>false</b>.","Mandatory reduction applies to S.L. → <b>false</b> (S.A. only, 2/3)."],
 check:[["Which increase doesn't change equity?","Charged to reserves."],["Pre-emptive right – which increases, how long?","Cash increases, at least 1 month."],["S.A.: equity 60% of capital for over a year – consequence?","Mandatory capital reduction (below 2/3)."]]},

{u:7, title:"Structural Changes & Company Termination",
 tldr:"RDL 5/2023 lists <b>transformation, merger, division, global assignment</b> (+ office abroad). Mergers: <b>new company</b> or <b>absorption</b>; phases <b>preparation → approval → execution</b>; effective on <b>registration</b>. Divisions: <b>total</b> (company dies, members get shares), <b>partial</b> (company lives, members get shares), <b>segregation</b> (company itself gets shares). End of a company: <b>dissolution → liquidation → extinction</b>.",
 sections:[
 {h:"Structural changes", body:`<p>Bigger than a by-law amendment: they change the company's legal identity and assets. Closed list in the <b>RDLME (RDL 5/2023)</b>: <b>transformation, merger, division, global assignment of assets & liabilities</b>, plus international transfer of office.</p>`},
 {h:"Mergers: types", body:`
 <div class="dia merge"><div><h5>By creation</h5><span class="co">A</span> + <span class="co">B</span> → <span class="co new">NEW</span><small>A and B extinguished</small></div><div><h5>By absorption</h5><span class="co">A</span> + <span class="co">B</span> → <span class="co new">A</span><small>B extinguished, A increases capital</small></div></div>
 <p>Members of the extinguished companies become members of the new/absorbing company. Motives: synergies, scale, vertical integration, financing, growth.</p>`},
 {h:"Merger procedure", body:`
 <div class="dia steps"><div><b>1 Preparation</b><small>Common draft by all managing bodies · published ≥ <b>1 month</b> before GMs · directors' reports · expert report if any <b>S.A.</b> · <b>exchange ratio</b> at fair value</small></div><div><b>2 Approval</b><small>GM of <b>each</b> company within <b>6 months</b> of the draft · merger balance ≤ <b>6 months</b> · consent of members becoming unlimitedly liable · publish in BORME + newspaper (or individual notice)</small></div><div><b>3 Execution</b><small><b>1-month</b> creditor opposition · public deed · <b>registration = legal effect</b> · challenge only within <b>3 months</b> for RDLME breaches</small></div></div>
 <p>Universal GM + unanimity in each company → no prior publication and no directors' report.</p>`},
 {h:"Special (simplified) mergers", body:`
 <p>When the <b>same people decide</b> on both sides. Main case: absorbing a <b>100%-owned subsidiary</b> (art. 53): simplified draft, <b>no expert reports, no capital increase, no GM of the absorbed</b>. <b>Twin companies</b> (common 100% parent, art. 49.2): simplified but still <b>capital increase + expert</b>. Simplifications also from <b>90%</b> (art. 54).</p>
 <p class="tip">Case 2 Facts 3: PATINETES absorbs its 100% subsidiary PTEL S.L.U. → art. 53.</p>`},
 {h:"Divisions", body:`
 <div class="dia divs"><div><h5>Total demerger</h5><span class="co dead">X</span> → <span class="co">B1</span> <span class="co">B2</span><small>X <b>extinguished</b> · <b>members</b> get shares</small></div><div><h5>Partial demerger</h5><span class="co">X</span> → <span class="co">B1</span><small>X <b>survives</b> (capital ↓) · <b>members</b> get shares</small></div><div><h5>Segregation</h5><span class="co">X</span> → <span class="co">B1</span><small>X survives · <b>X itself</b> gets shares → parent/subsidiary</small></div></div>
 <p>Divisions reorganise (separate activities). Merger rules apply. All of them can create a <b>group of companies</b> (art. 42 CCom): parent controls subsidiaries (majority of votes or power to appoint the majority of directors) → consolidated accounts, tax effects.</p>`},
 {h:"Dissolution → liquidation → extinction", body:`
 <p><b>Causes</b> (art. 363 + voluntary): term expired · GM resolution · activity ceased/impossible · <b>paralysis</b> (50/50 deadlock) · <b>equity &lt; ½ capital</b> (unless fixed, and if insolvency isn't due) · capital below legal minimum.</p>
 <div class="dia flow"><span><b>Dissolution</b><small>GM (directors must convene; else court) · deed + registry</small></span><span><b>Liquidation</b><small>"en liquidación" · liquidators replace directors · inventory in <b>3 months</b> · pay creditors · distribute rest</small></span><span><b>Extinction</b><small>deed · entries cancelled · books deposited · personality ends</small></span></div>
 <p>Personality <b>continues</b> during liquidation. Nothing goes to members before <b>all debts</b> are paid. Members who didn't vote for the distribution can challenge it within <b>2 months</b>. No assets/debts left → dissolution and extinction in <b>one deed</b>.</p>`}
 ],
 traps:["A merger is effective when the GMs approve → <b>false</b> (registration).","In segregation the members receive the shares → <b>false</b> (the company).","Dissolution ends legal personality → <b>false</b> (extinction does).","Directors decide dissolution → <b>false</b> (GM).","Partial demerger extinguishes the company → <b>false</b>."],
 check:[["Who receives the beneficiary's shares in a segregation?","The transferring company itself."],["Three phases of a merger?","Preparation, approval, execution."],["When does the legal personality end?","With the cancellation of entries (extinction)."]]},

{u:8, title:"Distinctive Signs & Industrial Creations",
 tldr:"Industrial property = <b>distinctive signs</b> (trademark, trade name – Act 17/2001) + <b>industrial creations</b> (patents, utility models, designs – Act 24/2015). Trademark: registered at the <b>OEPM</b>, <b>10 years renewable forever</b>, lapses after <b>5 years</b> without use. Prohibitions: <b>absolute</b> (no time limit) vs <b>relative</b> (5 years). Patent: <b>new + inventive step + industrial application</b>, <b>20 years, not renewable</b>, must be exploited (3/4 years) or compulsory licence.",
 sections:[
 {h:"The IP family tree", body:`
 <div class="dia tree"><div class="root">Intellectual property</div><div class="kids"><div><b>Copyright</b><small>books, music, software, films</small></div><div><b>Industrial property</b><div class="kids"><div><b>Distinctive signs</b><small>trademarks, trade names</small></div><div><b>Industrial creations</b><small>patents, utility models, designs</small></div></div></div></div></div>
 <p>Why protect? <b>Private</b> interest (reward effort) + <b>general</b> interest (signs → market transparency; patents → inventions are disclosed). How? An <b>exclusive right</b> = others are prohibited from using it.</p>`},
 {h:"Trademark, trade name, company name", body:`
 <div class="dia three"><div><h5>Trademark</h5>Distinguishes <b>products/services</b><br><small>ZARA, Bershka, Nescafé</small></div><div><h5>Trade name</h5>Identifies the <b>business</b> in trade<br><small>GRUPO INDITEX, Nestlé</small></div><div><h5>Company name</h5>Legal name<br><small>Industria de Diseño Textil, S.A.</small></div></div>
 <p>Trademark (art. 4 LM): <b>any sign</b> – words, names, drawings, letters, numbers, colours, shapes, packaging, sounds – able to <b>distinguish</b>. Trade name (art. 87): identifies a business; can be a personal, company, imaginary name, logo…; trademark rules apply. Registering a trade name doesn't let you mark products. <b>Shop signs</b> aren't protected by the LM (only via unfair competition).</p>`},
 {h:"Types & life of a trademark", body:`
 <ul><li><b>Collective</b>: members of an association (owner = association) – Barcelona Bar.</li><li><b>Guarantee</b>: certifies quality/requirements – CE marking.</li><li><b>Renowned/known</b> (art. 8): protected even unregistered and <b>beyond its class</b> – ZARA vs "Zara Tanzania Adventures".</li><li><b>EU trademark</b> (Reg. 2017/1001) · <b>International</b> (art. 79).</li></ul>
 <div class="dia flow"><span>Apply at <b>OEPM</b><small>with Nice classes (specialty)</small></span><span><b>2-month</b> opposition</span><span>Grant published<small>constitutive</small></span><span><b>10 years</b> from application<small>renewable ∞</small></span><span>No use <b>5 years</b> → lapse</span></div>
 <p>Rights (art. 34): exclusive use, <b>prohibit</b> identical/similar signs for similar goods, <b>oppose & seek nullity</b>. It's an asset: sell or <b>license</b> (royalty; exclusive/non-exclusive; all/part of Spain or classes).</p>`},
 {h:"Absolute vs relative prohibitions", body:`
 <div class="dia vs"><div><h5>Absolute (art. 5) – nullity: no time limit</h5>No distinctiveness · purely descriptive (kind, quality, origin) · customary words · against public order · flags/emblems · deceptive<br><small>ECO PURE · BioFresh 100% · Barcelona Tapas · Black Friday</small></div><div><h5>Relative (art. 6 ff.) – nullity: 5 years</h5>Confusable with <b>earlier marks/names</b> of others · unfair advantage of a <b>renowned</b> mark<br><small>Coca-Kola · GOOGLE for Kids · Apple Corps vs Apple</small></div></div>
 <p>Geographical indications: using a designation of origin without permission can even be a <b>crime</b> (art. 275 CP).</p>`},
 {h:"Patents", body:`
 <p>Invention = <b>technical solution</b> with industrial application (≠ discovery). A patent is a State <b>title</b> giving a temporary <b>monopoly</b> – a justified exception to free competition to foster progress.</p>
 <div class="dia check"><div>✔ <b>Novelty</b> – not in the state of the art anywhere in the world</div><div>✔ <b>Inventive step</b> – not obvious to an expert</div><div>✔ <b>Industrial application</b> – incl. agriculture</div></div>
 <p><b>Not inventions</b>: discoveries, theories, maths, artistic works, business/game methods, <b>software as such</b>. <b>Excluded</b>: against public order, plant varieties/animal breeds, surgical/diagnostic methods, cloning humans.</p>
 <div class="dia vs"><div><h5>Trademark</h5>10 yrs, renewable forever · lapses after 5 yrs non-use</div><div><h5>Patent</h5><b>20 yrs, not renewable</b> · exploit within 3 yrs (grant) / 4 yrs (filing) or compulsory licence</div></div>
 <p><b>Employee inventions</b>: <b>service</b> (research = job) → employer · <b>mixed</b> (not hired to research but used company resources) → employer may claim, <b>pays compensation</b> · <b>free</b> → employee.</p>
 <p><b>Compulsory licence</b>: no/insufficient exploitation, public interest (health, defence), competition breaches. <b>Invalidity</b>: requirements missing, insufficient description, beyond application, not entitled.</p>`}
 ],
 traps:["Trademark right is acquired by use → <b>false</b> (registration, except renowned).","Patents can be renewed → <b>false</b>.","Relative-prohibition nullity has no time limit → <b>false</b> (5 years).","Software as such is patentable → <b>false</b>.","Shop signs are protected by the Trademarks Act → <b>false</b>."],
 check:[["Duration of a trademark vs a patent?","10 years renewable vs 20 years not renewable."],["Three patentability requirements?","Novelty, inventive step, industrial application."],["Researcher's invention made as part of his job belongs to?","The employer (service invention)."]]},

{u:9, title:"Free Competition & Unfair Competition",
 tldr:"LDC (Act 15/2007) <b>prohibits</b> collusive practices and abuse of dominance, and <b>controls</b> concentrations and State aid. Collusion is an <b>objective</b> prohibition. Dominance is legal, <b>abuse</b> isn't. De minimis: <b>10%</b> competitors / <b>15%</b> non-competitors – never for hardcore cartels. Concentrations: notify CNMC if <b>≥30%</b> share or <b>€240M/€60M</b>. Fines up to <b>10%</b> of turnover; leniency. Unfair competition (Act 3/1991): anything <b>objectively against good faith</b>.",
 sections:[
 {h:"Why competition law?", body:`<p>Art. 38 CE chooses a <b>market economy</b>. Competition gives consumers <b>lower prices and more choice and quality</b>. Left alone, firms prefer to <b>agree not to compete</b> – so the law must intervene (paradox!). EU and Spanish systems are the same; Spanish law: <b>LDC – Act 15/2007</b>.</p>
 <div class="dia vs"><div><h5>Prohibited</h5>1. Collusive practices (art. 1)<br>2. Abuse of dominant position (art. 2)</div><div><h5>Controlled</h5>3. Economic concentrations (art. 7–8)<br>4. State aid</div></div>`},
 {h:"Collusive practices (art. 1 LDC)", body:`
 <p>Any agreement, collective decision/recommendation or <b>concerted or consciously parallel</b> practice with the <b>object or effect</b> (actual or <b>potential</b>) of restricting competition in all/part of the <b>national market</b>.</p>
 <ul><li>a) <b>Fixing prices</b>/conditions · b) <b>limiting</b> production/investment · c) <b>sharing markets</b> · d) <b>discrimination</b> · e) <b>tying</b></li></ul>
 <p><b>Objective</b>: intent and actual effect don't matter. Foreign firms are caught if effects reach Spain. Consequence: <b>null and void</b> – unless it brings progress with a fair share for consumers.</p>`},
 {h:"Abuse of dominant position (art. 2)", body:`
 <p>Being dominant is <b>fine</b>; <b>abusing</b> it is not (even a legal monopoly): unfair prices/conditions, limiting production, <b>refusal to supply</b>, unequal conditions, <b>tying</b>. Open list.</p>
 <p><b>Exemptions</b>: conduct imposed by <b>law</b>; conduct of <b>minor importance</b>:</p>
 <table class="tbl"><tr><th>Situation</th><th>Threshold</th></tr><tr><td>Competitors</td><td>combined ≤ <b>10%</b></td></tr><tr><td>Non-competitors</td><td>each ≤ <b>15%</b></td></tr><tr><td>Unclear</td><td><b>10%</b> each</td></tr><tr><td>Cumulative parallel networks</td><td><b>5%</b> (if networks ≥ 30% of market)</td></tr></table>
 <p class="tip">Never minor: <b>price fixing, output limits, market/customer sharing</b> between competitors, and <b>fixed/minimum resale prices</b>.</p>`},
 {h:"Concentrations & State aid", body:`
 <p><b>Concentration</b> = stable change of control (mergers, acquisitions). Legal, but <b>notify the CNMC</b> before closing if: <b>≥ 30%</b> market share, <b>or</b> Spanish turnover <b>&gt; €240M</b> with ≥ 2 parties <b>&gt; €60M</b> each.</p>
 <div class="dia flow"><span>Notify CNMC</span><span><b>Suspension</b><small>can't execute yet</small></span><span>Authorise · with conditions · prohibit</span></div>
 <p><b>State aid</b>: EU principle = <b>incompatible</b>. Automatic: social aid, natural disasters (art. 107.2 TFEU). Possible: regional development, common European interest, serious disturbance. <b>De minimis: €200,000 / 3 fiscal years.</b> The Spanish LDC doesn't prohibit aid; the CNMC can <b>analyse</b> it.</p>`},
 {h:"Who enforces & sanctions", body:`
 <div class="dia vs"><div><h5>National market</h5><b>CNMC</b> → appeal to <b>Audiencia Nacional</b></div><div><h5>EU / cross-border</h5><b>European Commission</b> (DG COMP) → <b>General Court</b> → <b>Court of Justice</b></div></div>
 <p>Fines: minor up to <b>1%</b>, very serious up to <b>10%</b> of total turnover; managers involved up to <b>€60,000</b>. <b>Leniency</b>: first to reveal a cartel → immunity; later ones → reduction.</p>`},
 {h:"Unfair competition (Act 3/1991, LCD)", body:`
 <p>Targets <b>dishonest</b> competition, not intense competition. Applies <b>before, during or after</b> a transaction, contract or not, to <b>anyone</b> acting in the market. <b>General clause</b> (art. 4): conduct <b>objectively contrary to good faith</b> (towards consumers: against professional diligence + distorts the average consumer's behaviour). The list is <b>open</b>.</p>
 <div class="dia vs"><div><h5>Against a competitor</h5>Defamation (true personal facts too!) · comparison · imitation · exploiting reputation · business secrets (Act 1/2019) · inducing breach of contract</div><div><h5>Against the market</h5>Misleading acts · confusion · misleading omissions · aggressive practices · infringing laws · systematic sale below cost (misleading or to eliminate)</div></div>
 <p><b>Consumer practices</b> – <b>misleading</b>: confusion with marks, fake quality seals, <b>bait</b> ("€1 flights"), false properties ("cures"), <b>pyramid</b> schemes, <b>covert</b> advertising. <b>Aggressive</b>: coercion (can't leave without buying), harassment (home visits), repeated unsolicited calls/e-mails.</p>
 <p><b>Comparative advertising</b> is lawful if: same purpose · objective, essential, relevant features · true and not riding on the rival's reputation.</p>`}
 ],
 traps:["A dominant position is illegal → <b>false</b>.","Intent is needed for a collusive practice → <b>false</b>.","De minimis protects small price cartels → <b>false</b>.","A concentration can be executed once notified → <b>false</b> (suspension).","True statements can never be defamation → <b>false</b> (personal matters).","Selling below cost is always unfair → <b>false</b>."],
 check:[["Two prohibited and two controlled conducts?","Collusion & abuse; concentrations & State aid."],["Notification thresholds?","≥30% share, or >€240M turnover with two >€60M."],["Max fine?","10% of turnover."]]}
];
