# Brief: Quiet responders (decision version)

For Helen Achebe · v9 · Data to 6 Sep 2026 · V verified from data or code, M modelled (a replay of real pings), P proposal. Replaces `brief.md` (v8); earlier drafts are `brief-v0` to `brief-v7`. A clickable walk-through is `demonstrator.html`.

## 1. Problem, decisions and owner

**Problem.** Rook Dispatch offers each incident (a *callout*) to one responder's phone at a time; each offer is a *ping*. Since release 4.2 on 12 Aug, four responders (Farlight, The Undertow, Meteor Mite, Vesper) went from 49 pings a week together to 3, from 28% of all pings to 1.8% (V). The cause in the code: a *recent acceptance score* decides who is asked first. A missed ping costs the same as a refusal (-0.12) and the score only rises when a responder takes a ping, so one bad run becomes permanent (V, `00-rook/code/dispatch-routing/history.py`, where Wen Li's 2019 comment asks whether the score should ease back toward neutral). The four also miss 70% of their first pings (28 of 40, against 16.5% for everyone else); why is not yet known, either push delivery or slow answers (V). Neither they nor their handlers can see any of this: *"starting to wonder if im still even in the system"* (ticket 3121); *"I just want it to look less like a coincidence"* (Kip, a handler).

**Decisions for Helen (recommended: yes to all three).**
1. **Approve the hotfix** in section 2: a missed ping stops counting against a responder after about a week, and the handler and the responder each see one plain line about it.
2. **Allow it to ship outside the monthly release train** (the normal monthly release cycle), with Wen Li's written review before launch.
3. **Accept the backlog** in the order in section 2.

**Decide by:** within a week of receiving this (P; set a date if you prefer). **Cost of waiting:** the four stay out of rotation, and the handler tickets about them stay open (83 of 108 filed since 12 Aug) (V).

**Owners (P).** Hotfix: Wen Li, staff engineer. Marcus Oyelaran, engineering manager, confirms the ship date within 2 working days of approval. Measure: Ravi Menon, data analyst, reports it weekly; the PM is accountable. Backlog owners are in section 2.

**How we will know it worked.** In the second full week after launch, the four get at least 14% of all pings (from 1.8%, which is half their 28% before 4.2). Source, pull-back and rollback are in section 3.

## 2. The plan: one hotfix, then a backlog

**Hotfix (one release).**

| Part | What | Why |
|---|---|---|
| **Time-based miss penalty** | A miss adds a 0.12 penalty that halves every 2 days; a take pays outstanding penalty down first; refusals work as today. Replaying real pings with no restarts, all four go from 0.00 to 0.55 to 0.67 on 6 Sep and the other twelve change little (0.90 on average either way) (M). | Answers Wen's 2019 question. Stops one bad run being permanent. |
| **Restart-proof store** | Scores live in memory today, so a restart resets everyone to 0.5. The fade needs the penalty, the base score and a timestamp per responder to survive restarts. | Without it, every deploy wipes the fade and hides the effect. |
| **One line for handler and responder** | A level, not a number: "Recent acceptance: Low. 3 of the last 4 pings missed. Offers are reduced. Misses fade in about a week." On the handler's responder card and in the responder's phone app. Wording and bands are design's call. | They see why, and that it recovers. If a screen cannot take the line in this release, the fade still ships and that line moves to the top of the backlog. |
| **Gate before launch** | Wen Li reproduces the ranking for callouts 40985 and 41416 from the code, confirms in writing that recent acceptance puts the four below their neighbours, and signs off the rule. If the gap is travel or skills, the fade does not ship. Silence is not a yes. | The loop may not be the whole cause. |
| **Launch support (no decision needed)** | The support lead asks the four handlers to check each responder's app version and notification settings. The Supply owner is told that quieter responders getting more pings moves maintenance windows. | Checks the delivery cause and protects Supply's scheduling. |

**Backlog, in this order.**

| # | What | Owner (P) | Starts |
|---|---|---|---|
| 1 | **Post-dispatch ranking review for handlers.** On a dispatched callout: order, each responder's three score parts and the weights, the outcome, any override. Own responders in full, others' order only; Security reviews. Needs the ranking saved for every dispatched callout. | Sofia Marino, product designer (screen); Wen Li (saving the ranking) | After the hotfix |
| 2 | **Delivery confirmation before the 60-second clock starts** (none today). | Wen Li | Only if the push logs for the four on 12 and 13 Aug show undelivered pings |
| 3 | **A real fair-share offer** (a real callout offered first to someone with no recent offers). | PM with Wen Li; Helen decides | Only if the hotfix misses its measure |

**The hotfix will not fix** why the four miss 70% of first pings; backlog item 2 covers that. A responder who keeps missing about 60% of pings still falls again, and the replay is not a forecast because they would be asked more. **No change** to the ranking weights, the 60-second wait, or the availability record Supply reads. The label is "recent acceptance", not "availability score", which would collide with that record and the committed Availability Confidence item.

## 3. How we will know it worked

- **Measure:** in the second full week after launch (so any score reset from the deploy has settled), the four get at least 14% of weekly pings. Baseline 1.8% in the week of 31 Aug. Read from the pings table, weekly (`00-rook/data/callout-history.csv` is built from it). Owner: Ravi Menon, with the PM accountable (P). At about 0.57 (Fair) a responder is roughly 5 minutes of travel behind a healthy neighbour instead of 16, so they are asked when close (M); the replay cannot predict their share, so 14% is our proposal. If it is missed, backlog item 3 starts and Helen decides.
- **The line for handler and responder:** no separate measure; the signal is that the 30 "quiet" tickets (all open) stop growing within two weeks (P). Backlog items get their own measures when they start.
- **Pull-back, checked daily on a rolling 7 days, any day:** acceptance rate below 66.7%, or callouts nobody took above 12.9%, or the slowest 10% of callouts taking over 82 seconds to reach a responder who takes them. Baselines (V): 72.7% and 5.5% in the week of 31 Aug; 70 s then (32 to 45 s before 4.2; worst week since, 82 s).
- **Rollback:** turn the fade off; the line goes with it.

## 4. Risks and limits

- **Responders who cannot hear pings get asked again.** Each such ping delays a callout by up to 60 seconds; the callout then moves to the next responder, if there is one. At the target (14% of pings, about 23 a week, 59% missed) that is about 14 callouts a week (about 11%) delayed.
- **Failed pushes still count as misses** until backlog item 2.
- **Callout lists are often short:** 40 of the 49 callouts nobody took since 12 Aug ended after a single ping (V).
- **The replay assumes scores survive restarts** and holds pings fixed; it is not a forecast.

## 5. Evidence (appendix)

- **Pings:** weekly pings to the four 49, 48, 48, 50, 50, 49, 43, 16, 6, 3 (V, `00-rook/data/callout-history.csv`).
- **Score loop:** replaying their real pings through `history.py` leaves them at 0.00 (M, `00-rook/feedback/score-replay-real-pings.py`). Dispatch is not slower: first ping 14 s before, 15 s after (V).
- **Where it fits and where it does not:** Farlight was asked first at scores down to 0.28, then not once in her last 20 Uptown callouts (V). One release-day callout, where she was third at 0.84, is unexplained; the saved rankings in backlog item 1 would explain such cases.
