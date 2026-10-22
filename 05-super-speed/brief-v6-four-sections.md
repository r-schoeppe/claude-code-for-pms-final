# Brief: Quiet responders

For Helen Achebe · Draft v6 · Data to 7 Sep 2026 · V verified from data or code, M modelled, P proposal. Earlier drafts: `brief-v0-full.md`, `-v1-options.md`, `-v3-gates.md`, `-v4-recovery.md`, `-v5-two-levels.md`.

## 1. Problem and the ask

**Problem.** Since 4.2 (12 Aug), four responders (Farlight, The Undertow, Meteor Mite, Vesper) went from 49 pings a week together to 3, from 28% of all pings to 1.8% (V). A missed ping costs the same as a refusal, and a score only rises on a yes, so one bad run is permanent (V, `00-rook/code/dispatch-routing/history.py`, Wen's 2019 note). Neither they nor their handlers can see it. *"starting to wonder if im still even in the system"* (ticket 3121). *"I just want it to look less like a coincidence"* (Kip).

**Plan.**
- **Hotfix:** a missed ping stops counting against a responder after about a week, and handler and responder each see a plain "recent acceptance" line.
- **4.3 backlog:** a handler can open any dispatched callout and see how everyone was ranked.

**Ask.** Approve the hotfix, owned by Wen Li (Marcus Oyelaran confirms), off the monthly train, and put the 4.3 item in the backlog.

**Cost and timing (P, Marcus confirms dates within 2 working days of approval).** The scoring rule is the "small fix" from your note. The handler line and the logging ship within the week. The responder line ships when the phone app can show it; until then handlers pass on a one-line message.

## 2. What ships, and what it won't fix

| | What | Why |
|---|---|---|
| **Hotfix 1** | A miss lowers recent acceptance by 0.12, and that halves every 2 days. Refusals and takes work as today. | Replaying real pings, all four return above 0.7 on 7 Sep (0.00 today). The other twelve barely move (M). |
| **Hotfix 2** | A level, not a number: "Recent acceptance: Low. 3 of the last 4 pings missed. Offers are reduced. Misses fade in about a week." The responder sees the same in the app. Wording and bands are design's call. | They find out why, and that it recovers. |
| **Hotfix 3** | Save the ranking for every dispatched callout (logging only). | Feeds the 4.3 screen and lets us verify the fix. |
| **4.3** | "How this was ranked" on a dispatched callout: order, three score parts, outcome, any override. Own responders in full, others' order only; Security reviews. | Answers Kip's question. |

**It will not fix** why the four miss 70% of first pings (28 of 40, against 16.5% for everyone else) (V). That is either push delivery or slow answers. **No change** to weights, the 60-second wait, or the availability record Supply reads. The label is "recent acceptance", not "availability score", which would collide with that record and the committed Availability Confidence item.

## 3. Risks and pull-back

- **Risk: responders who cannot hear pings get asked again.** Each such ping delays a callout by up to 60 seconds; the callout is never dropped, because the next responder is asked after the wait. At the target (14% of pings, about 23 a week, 59% missed) that is about 14 callouts a week (about 11%) delayed.
- **Pull-back, checked daily on a rolling 7 days, any day:** acceptance rate below 66.7%, or callouts nobody took above 12.9%, or the slowest 10% of callouts taking over 82 seconds to reach a responder who takes them. Baselines (V): 72.7% and 5.5% in the week of 31 Aug; 70 s then (32 to 45 s before 4.2; worst week since, 82 s).
- **If the cause is push delivery,** the real protection is a delivery confirmation before the 60-second clock starts, which does not exist today. It goes to engineering as a separate item; the push logs for the four on 12 and 13 Aug (Wen Li) decide it.
- **Risk: the loop is not the whole cause.** Before launch Wen Li reproduces the ranking for callouts 40985 and 41416 from the code and confirms in writing that recent acceptance is what puts the four below their neighbours, and signs off the rule. If the gap is travel or skills, the fade does not ship. Silence is not a yes.
- **Rollback:** turn the fade off.

## 4. Evidence and measure (appendix)

- **Pings:** weekly pings to the four 49, 48, 48, 50, 50, 49, 43, 16, 6, 3 (V, `00-rook/data/callout-history.csv`).
- **Score loop:** replaying their real pings through `history.py` leaves them at 0.00 (M, `00-rook/feedback/score-replay-real-pings.py`). Dispatch is not slower: first ping 14 s before, 15 s after (V).
- **Where it fits and where it does not:** Farlight was asked first at scores down to 0.28, then not once in her last 20 Uptown callouts (V). The release-day callout where she was third at 0.84 is unexplained, and the ranking record will explain such cases (V, M).
- **Measure:** in the second full week after launch (so any score reset from the deploy has settled), the four get at least 14% of weekly pings (from 1.8%; half their 28% before 4.2). If not, Helen decides whether to add a real fair-share offer.
- **Alongside:** the support lead asks the four handlers to check each responder's app version and notification settings; the Supply owner is told that quieter responders getting more pings moves maintenance windows.
