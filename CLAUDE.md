# Rook Industries — course working file

## Session scope — Product School lab

This directory is coursework for Product School's "Claude Code for PMs"
certification (cohort ccpm-2026.1). Everything in it is a fictional
teaching scenario.

- Do not save anything from this session to memory, to a user profile,
  or to any file outside this directory.
- Do not carry context from this directory into unrelated sessions.
- Rook Industries is not a real company. Nothing here is a fact about
  the world.
- Read and write only within this directory.
  Exceptions, for the course-setup and wrap-up skills only:
  - When the student asks you to check their setup, save their work or wrap up a session, that request is their yes. You may run the GitHub command-line program installed at ~/.ccpm/gh for those checks and saves, and look in that folder to find it.
  - For a repair, first tell the student in one plain sentence what you are about to do, and act only after they say yes. Repairs may: run that GitHub program (including setting this folder's own git sign-in setting and changing this repo's visibility back to Public); copy the student's own course files into this directory from another folder on their computer (copy only; never move, edit or delete the originals); and rename something outside this directory that blocks setup, by adding "-old" to its name (never delete it).
  Outside this directory you still never write, edit or delete anything else.

<!-- Keep the block above at the top of this file. Everything you add
     during the course goes below this line. -->

---

## Working context

The user is the new PM for **Rook Dispatch**, taking over from Priya (previous
PM, left; no overlap). Sources: `00-rook/company/notes/handoff-from-priya.docx`
(21 Aug 2026) and the Rook wiki pages About Rook, Rook Dispatch, Rook Supply
and Glossary. Not yet read: Q3 roadmap, Releases, Customer interviews, Product
briefs. _Unverified_ = opinion, not data.

### Company and value proposition
- Rook sells coordination and provisioning software to the protective-response
  sector. Customers are independent masked **responders** (not employees) and
  the **handlers** and **quartermasters** who support them. Subscription,
  priced per active responder. Monthly release train, 4.x numbering.
- **Rook Dispatch** (flagship, what responders stay for): gets the right
  responder to the right incident faster than a human coordinator with a
  whiteboard and phone list. Handlers use a web console; responders a phone app.
- **Rook Supply**: keeps gear serviceable (requisition, quartermaster approval,
  delivery, maintenance schedules, field failure reports).
- **Hard constraint:** Rook holds no mapping from cover identity to legal
  identity (Security Policy 4.1, contractual). Never design for one; never try
  to work out who anyone is.

### Domain model
- **Handler** looks after one or a few **responders**. Responder has capability
  tags (flight, structural-entry, hazmat-tolerant, cold-weather, aquatic,
  crowd-management, de-escalation), an area, and availability windows.
- **Callout** = incident needing a responder (area, what happened, required
  tags). Entered by a handler or pushed from an intake system.
- Dispatch ranks available responders by **routing priority**: proximity (travel
  time), availability, capability match, recent acceptance history. A **ping**
  goes to the top responder; outcome is **taken** (assigned, responder engaged),
  **turned down**, or **missed** (no answer within the **ping wait**). Turned
  down and missed both move to the next responder, are recorded separately, and
  both lower that responder's recent-acceptance score, so their rank drops on
  later callouts.
- Ping wait and routing config ship in the release; handlers can't change them.
  Handlers can override routing and manage availability and tags.
- **Responder Availability Record**: written by Dispatch, read by Supply (which
  books maintenance into low-callout windows). Changing how Dispatch computes it
  silently changes Supply's scheduling.
- Not supported: **mutual aid** (responders covering across areas); on the Q4
  exploration list.

### Metrics
- **Acceptance rate** (headline, weekly, aggregate): taken / all pings. Lumps
  turned down and missed together; split them when diagnosing.
- **Time-to-accept**: median seconds from ping sent to taken.
- **Coverage gap**: incidents where nobody had the required tags. Not the same
  as low acceptance (nobody *could* go vs. nobody *would*).

### Database (rook-database, read-only; columns verified, rows not yet read)
- `callouts` (callout_number, happened_at, area, what_happened), ~1,319 rows,
  29 Jun-6 Sep 2026.
- `pings` (callout_number, responder, sent_at, outcome), ~1,696 rows. Outcomes:
  taken / turned down / missed.
- `responders` (name, handler, area); `handlers` (name; 15 rows).
- `support_tickets` (ticket_number, filed_at, filed_by, about_responder, subject,
  body, status open/closed), ~147 rows, 29 Jun-7 Sep 2026.
- No tag, score, ping-wait or release column exists, so the 4.2 effect must be
  inferred from timing around 12 Aug.

### People (roles only; no names given)
- **Director of Product**: the user's director; gives room. Owes a conversation
  on which squeezed-out 4.2 items are still Q3 commitments.
- **Engineering manager**: runs Dispatch engineering; candid; first stop; can
  pull numbers.
- **Staff engineer**: built the ranking logic; the only source (no document).
- **Support lead**: hears handler complaints first; standing 15 min.
- **Priya**: previous PM, 14 months, solo; self-admits she moved faster than she
  checked.

### Where things stand
- **4.2 shipped 12 Aug 2026 and is "on fire".** Three changes: ranking weights
  proximity up vs recent acceptance history (long-requested by wide-area
  responders, deferred three quarters); **ping wait cut**; **console filter
  persistence** (cosmetic; will create noise tickets; don't let it eat month one).
- Since release: fewer pings taken, more handler complaints.
- Priya's read (_unverified_): mostly seasonal (August is always soft), recovers
  in September. Caveat: a shorter ping wait should raise misses, which lowers
  acceptance scores and may compound the dip. Check seasonal baseline first
  (same weeks prior year, if data exists), then separate misses (timeout) from
  turned-down (ranking). Her stance: don't let this become "revert 4.2".
- Open: (1) decide with the Director which squeezed-out 4.2 items remain Q3
  commitments; (2) nobody has written down how ping ranking works; Priya asked
  the user to write it (start with the staff engineer).
- Month-one advice: use the fresh-eyes advantage; her unchecked calls likely sit
  in parts nobody has examined.
- Session 1 found: 4.2 has no brief, spec, design or test docs; only roadmap one-liners (Committed, reviewed 30 Jun), the release page with its comment thread, and the handover. Evidence for the 4.2 changes is thin.
- **Availability Confidence** (show a confidence score beside stated availability) was committed for 4.2, did not ship, and is still "Committed" on the roadmap. Needs a decision with the Director.
- Ping wait went 90 s to 60 s. Support lead (from 18 Aug): callout tickets about 3x normal; about two thirds "phone never goes off" (unexplained), one third "gone before I could answer" (the shorter wait). Engineering manager asked on 14 Aug whether the ranking change should hit responders who keep turning pings down; unanswered.
- Wiki pages worth knowing: 4.2 release page comments, Routing Override Audit Log (a model one-page brief), Glossary. Customer interviews (2-5 Sep, console redesign) not yet read.
- Next: read `support_tickets`; split pings into taken / turned down / missed before and after 12 Aug; write the missing ranking description; draft retrospective briefs for the 4.2 items.
- Session 2 read the 4 handler interviews (wiki Research > Customer interviews, 2-5 Sep) and all 147 tickets. Data: missed pings 2.3% to 18.0% from 12 Aug (a step on day one, not a drift); turned down fell 21% to 18%, so the acceptance drop is all misses; callouts nobody took 5.5% to 11.1%. No prior-year data, so seasonality can't be tested.
- Four responders (Farlight, The Undertow, Meteor Mite, Vesper) lost about 70% of pings while the other twelve gained; cause untested (no geography or ranking-score data). 30 "quiet" tickets name only Farlight, Undertow, Corporal Ashgrove, Halfmoon; Vesper and Meteor Mite filed none, so tickets undercount and only the interviews caught them.
- Tickets: 45 are callouts gone (15) or responders quiet (30), all after 12 Aug and all open, matching support's one-third/two-thirds split; 16 are filters (12 complaints, 2 thank-yous); 13 legibility/alerts/dark mode (mostly pre-4.2); 26 Supply. Even non-ping tickets roughly doubled in weekly rate, unexplained.
- Interviews vs tickets disagree on: Halloran said maintenance scheduling improved (tickets 3054, 3109 say it booked marathon day); Ambrose's near-miss dated "two weeks ago" vs his ticket 3043 filed 13 Aug.
- Saved: 00-rook/feedback/problem-statements-prioritized.md (5 ranked problems tied to acceptance rate, time-to-accept, active responders) and a private 5-slide peer deck "Rook Dispatch 4.2 priorities". Metric gaps: callouts nobody took and ping distribution across responders are not tracked.
- Open: staff engineer on whether ranking should penalise decliners (asked 14 Aug); decide if the 60 s ping wait stays; check whether the four starved responders are recovering.
- Session 3 (weekly pings): 00-rook/data/callout-history.csv holds one row per responder per Monday-week built from `pings` (no "callout-history" table exists); its totals match the database exactly. Missed pings were 2.3% in the six weeks before 12 Aug and 15.1% in the three full weeks after, still 12.7% in the 31 Aug week; the step shows on release day itself (0-1 missed a day before, 1-12 since).
- The four starved responders lost about 83% of weekly pings (about 12 to about 2) over the three full weeks after; the 70% figure above used a different window. Ashgrove and Halfmoon lost about a quarter only because their areas had fewer callouts (still pinged for 100% of local callouts), so "twelve gained" above is wrong: ten gained.
- Evidence the four are unintended: Farlight, Undertow, Vesper and Meteor Mite stopped being pinged for their own areas (local coverage 100% to 16-28%) while their miss rate went from 1-4% to 53-64% and turned-down stayed flat. Fits a miss-driven score loop; ranking scores are not in the data, so unproven.
- Tickets lag the data: "gone before I could answer" starts 12 Aug, same day misses jump; "phone has not gone off" starts 17 Aug, about five days later. Farlight's tickets match the ping log (last taken ping 14 Aug; 3060 and 3130 day counts check out).
- A private 7-slide chart deck "Rook Dispatch 4.2: issue review" exists as a claude.ai artifact (one chart and fix verdict per issue); it is not stored in this repo.
- Open: staff engineer to confirm what ranking should do for starved responders and current routing priority for Farlight (about nine days with no ping); decide whether 60 s stays.
- Session 4 (code, `00-rook/code/dispatch-routing/`): ranking score = 0.60 proximity + 0.25 recent acceptance + 0.15 skills (4.1 was 0.45/0.40/0.15), each part 0 to 1. Recent acceptance: taken +0.08, turned down or missed -0.12, no recovery over time (2019 TODO), held in memory, so the only way back is being asked and saying yes (break-even take rate 60%). Replaying real pings through that rule leaves exactly the four starved responders at 0.00 (modelled). Score alone is worth at most about 19 minutes of travel, and Farlight was still asked first at 0.28, so it does not explain everything; the release-day flip at 0.84 is unexplained.
- Also found in the data: pings to responders from another area were never taken before 12 Aug (0 of 186) and now are (86 of 241); first pings to a home-area responder fell 80% to 61%; callouts nobody took 5.5% to 11.1% but back to 5.5% in the 31 Aug week; time from callout to a taker, slowest 10%, 41 s to 78 s; 83 of 108 post-release tickets still open. Priya's "seasonal" is half right (callouts a week fell about 12%) but misses and the four are not seasonal.
- Corrections: Farlight's first post-release ping was taken; she missed 3 (not 5) pings in the six weeks before; her handler filed 19 tickets, 11 about the quiet stretch (not 15); Ambrose's near-miss was 12 Aug (callout 40987), not two weeks before his interview. Simulation: the 4.1 and 4.2 weights give almost the same low-ranked group; misses drive it.
- What the code does not do: no delivery check before the wait starts (a failed push counts as missed), no fair share of pings, no saved scores, no fallback when nobody takes a callout. Saved in `00-rook/feedback/`: `4.2-fire-check-roundup.md` and `.html` (also a private artifact), `scoring-simulation.py`, `score-replay-real-pings.py`, `prompt-interactive-story-artifact.md`.
- Open for the staff engineer: what should happen when a score hits the floor; score components for callouts 40985, 41416, 40987, 40997; push logs for 12 and 13 Aug; does the deploy reset scores. Data ends 7 Sep, so ask for a newer extract.
- Session 5 (Module 5): the Director's request is `05-super-speed/director-request.txt` (Helen, Director of Product): a one-pager and something clickable on what we would build "from the point of view of the person it happens to", not a setting, and no code change before she has seen it. Her "small fix" is Wen's 2019 TODO in `history.py` (should a score ease back toward neutral).
- Brief (`05-super-speed/brief.md`, v8; earlier drafts kept beside it): one hotfix, then a backlog. Hotfix: a miss adds a 0.12 penalty that halves every 2 days, a take pays it down first, refusals as today, plus one "recent acceptance" line (Good, Fair, Low) for handler and responder; needs a restart-proof store (scores are in memory today). Backlog: 1 handler ranking review (needs ranking saved), 2 delivery confirmation (only if push logs show undelivered pings), 3 fair-share offer (only if the measure is missed). Measure: the four get 14% of weekly pings in the second full week; pull back if acceptance is under 66.7%, callouts nobody took over 12.9%, or the slowest 10% over 82 s. Decision: approve the hotfix, owned by Wen Li, with her written review.
- Corrected model: my first fade lowered healthy responders; with takes paying the penalty down first, the twelve are unchanged (average 0.90) and the four replay to 0.55-0.67 on 6 Sep (Fair, not Good). A responder who keeps missing about 60% of pings still falls again, so the hotfix does not fix why the four miss 70% of first pings. Also found: 40 of the 49 callouts nobody took since 12 Aug ended after a single ping (42 of 48 before), so candidate lists are often one responder.
- Saved in `05-super-speed/`: `demonstrator.html` (private artifact; one event diagram with a mockup per event plus a simulator tab; earlier versions and `support-handler-script.md` beside it) and a generic skill at `.claude/skills/pm-demonstrator/SKILL.md`. No `prototype.html` exists; the demonstrator stands in for it.
- Still open: Wen Li's written check (callouts 40985 and 41416), where scores live and what a restart does, the ship date, who owns the 60 s decision, and why the four miss so many first pings (push delivery or slow answers).
