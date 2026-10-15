# Prompt: interactive teaching story of the Rook Dispatch 4.2 problem

Paste everything below the line into Claude Code, started in this folder
(`claude-code-for-pms-final`). Everything in it is a fictional course scenario.

---

## Your job

Build ONE interactive, cartoony teaching story as a private HTML Artifact (use
the Artifact tool; call `quickstart` first, then follow the artifact-design
skill). Audience: classmates on the "Claude Code for PMs" course who know the
Rook Dispatch background but have not seen this analysis. They should finish it
able to (a) say what the problem is and how we know, (b) recheck any claim
themselves, and (c) argue with the ranking of solutions.

Tone: friendly cartoon (flat shapes, big emoji-free SVG characters, speech
bubbles, one running mascot). Plain English, no code shown unless a reader
clicks "show me the code". Works on a phone (16px gutters, no sideways scroll),
light and dark mode.

## Hard rules

1. **No number without a claim ID.** Every figure on screen carries a small
   badge (e.g. `M1`). Clicking it opens an evidence card: the claim, status
   (see 2), the source, how to recheck, and the date checked.
2. **Status on every claim:** `VERIFIED` (recomputed from data or code this
   session), `MODELLED` (from the replay or simulation, so only as good as the
   model), `INFERRED` (reasoned, not shown), `UNKNOWN` (we could not tell).
   Colour-code them and show a legend on every chapter.
3. **Do the due diligence before you publish.** Recompute every VERIFIED claim
   from its source (SQL in the appendix against `rook-database`, or the CSV
   and files named). If a number differs from this prompt, use YOUR number, say
   so in the final reply, and list the difference. If the database tools are
   unavailable, use `00-rook/data/callout-history.csv` and say which claims you
   could not recheck.
4. **Never invent.** No time-to-accept figure exists (the `pings` table has
   only `sent_at`, no response time), no ranking scores or travel times exist in
   the data, and "active responders" has no definition in the data. Show those
   as UNKNOWN cards, not as estimates.
5. **Privacy constraint (Security Policy 4.1).** Use cover names only. Never
   try to work out who anyone is, and do not name handlers; say "her handler".
6. The artifact cannot link to local files. Print every source as a visible
   relative path the reader can open in the repo, and put the full SQL inline.
7. Do not save anything to memory or outside this folder.

## Story structure (classical product flow, one chapter per screen)

**Prologue: meet the cast.** Mascot "Dispatch Duck" drives a little switchboard.
Characters: the Callout (a siren), the Ranking (a sorting hat), the Phone
(buzzing), four starved responders, twelve fine ones. Tell the 5-step journey
in plain English (callout arrives, find who is free, score them, ask the best
one, wait 60 s then move down). Source: `00-rook/code/dispatch-routing/`
(README.md, offer.py, routing.py, history.py, config.py, availability.py).

**Chapter 1: Success metrics.** What good looks like. Three cards:
- Acceptance rate (headline): taken / all pings, always split into taken,
  turned down, missed.
- Time-to-accept: UNKNOWN card (not measurable from the pings table).
- Active responders (pricing is per active responder): UNKNOWN card (no
  definition or column); show the 16 responders in the table as the only
  available proxy.
- Two metrics nobody tracks: callouts nobody took, and ping share per
  responder. Propose them as new metrics.

**Chapter 2: Insights and observations.** One screen per insight, each with a
claim badge, a plain sentence, and a small interactive chart:
1. The headline fell (M1, M2). Stacked bars before/after 12 Aug. Highlight that
   turned down went DOWN and missed went UP, so it is all misses.
2. It happened on release day (I1). Daily missed-ping strip with a "4.2 ships"
   marker you can scrub.
3. Four responders vanished while the rest gained (I2, I3, I4). Week slider over
   the table below; show pings, and the local-area coverage drop.
4. The code treats a miss like a refusal and never forgives (I5). A "score
   machine" the reader can play: sliders for take rate and miss rate; show the
   +0.08 / -0.12 rule, the 60% break-even, and the floor. Put the real rule
   in a "show me the code" drawer.
5. Replaying real outcomes through the real rule picks out exactly the four (I6).
   Bar chart of final scores: four at 0.00, twelve at 0.72 or higher.
6. Meet Farlight (I7). A week-by-week scrubber: pings, taken, score, and the
   handler's tickets as speech bubbles at the right dates. Use the table below.
7. Plot twist: the score alone cannot do this (I8). It is additive and worth at
   most 0.25 (about 19 minutes of travel). Show the callout table where
   Farlight was still asked first at scores 0.68 to 0.28, and the unexplained
   release-day flip at 0.84.
8. The simulation (I9): low-ranked cluster grows from about 8% to about 28% of
   responders; the 4.1 and 4.2 weights make almost no difference; it did NOT
   reproduce the real starvation. Embed or link
   `00-rook/feedback/scoring-simulation-10-situations.svg` and
   `scoring-simulation-distribution.svg`; script `scoring-simulation.py`.

**Chapter 3: The problem.** A single problem statement in one sentence, then the
five prioritised problems from `00-rook/feedback/problem-statements-prioritized.md`
as cards (P1 callouts gone, P2 responders quiet, P3 legibility, P4 filters,
P5 Supply), each linked to the metric it threatens. Say clearly: this story
focuses on P1 and P2. Mark the superseded figures in that file (see
"Corrections").

**Chapter 4: Ranked possible solutions.** Interactive ranking game: the reader
first drags the options into their own order, then reveals ours and a diff. Show
the criteria (effect on the headline metric, evidence strength, effort and
risk, reversibility) as a small table per option. Our ranking is a judgement
and must be labelled INFERRED:

1. **Stop treating a miss like a refusal** (record a smaller or zero penalty
   for a miss). `offer.py` already returns MISSED and TURNED_DOWN separately;
   `history.py` merges them in `record_declined`. Small change. Validate by
   re-running `score-replay-real-pings.py` with the new rule.
2. **Let stuck scores recover and persist them** (the 2019 TODO in `history.py`;
   scores sit in an in-memory dict `_scores`). Without this, nobody climbs
   out. Risk: the TODO's own "against" argument (someone who stopped taking work).
3. **Pilot a longer ping wait** (try 75 s or 90 s; this is one of the three 4.2
   changes, not a revert of 4.2). Trade-off with time-to-accept, which we cannot
   measure yet, so pair with measurement first.
4. **Guarantee a fair share of pings** (e.g. an occasional probe ping for
   anyone who has had none for N days). Fixes starvation from any cause; adds
   a bit of deliberately worse routing.
5. **Revert the 4.2 ranking weights.** Lowest rank: the simulation shows the
   weights barely change the low cluster (I9).

Plus two items that are not ranked because they do not fix anything alone:
- **Do-this-week stopgap:** reset the four starved responders' scores to
  neutral 0.5 and watch whether they stay in rotation (also a test of the
  loop theory).
- **Diagnostics to run in parallel:** (a) get the three score components
  (travel, recent acceptance, skills) for Farlight and her three neighbours on
  callouts 40985 and 41416; (b) push-delivery logs for the four on 12 and
  13 Aug; (c) travel times from the four to their home areas; (d) does the
  4.2 deploy reset `_scores`? Owner for all four: the staff engineer, via the
  engineering manager. Also open: the question the engineering manager asked on
  14 Aug about penalising decliners, still unanswered.
Note the cross-team risk: do not change the shape of what
`availability.current_record()` returns; Rook Supply reads it.

**Chapter 5: What we still do not know.** UNKNOWN cards: why the four miss
59% of pings (the shorter wait? the phone not buzzing? both?), why neighbours
outrank them (no travel-time data), the release-day flip, seasonality (no
prior-year data), time-to-accept, active responders. End with the next three
actions and who owns them.

**Appendix: Evidence ledger.** A searchable table of every claim ID, status,
source, and recheck steps, plus the SQL below, plus a "known corrections" panel.

## Data pack (recompute and use YOUR figures if they differ)

Window: callouts and pings 29 Jun to 6/7 Sep 2026. "Before" = pings sent before
12 Aug 2026; "after" = from 12 Aug (4.2 release day).

| ID | Claim | Value | Status | Source |
|---|---|---|---|---|
| M1 | Acceptance rate (taken / all pings) | 76.6% (831/1,085) before; 64.0% (391/611) after | VERIFIED | SQL-A |
| M2 | Missed / turned down share | missed 2.3% (25) to 18.0% (110); turned down 21.1% (229) to 18.0% (110) | VERIFIED | SQL-A |
| M3 | Callouts nobody took | 5.5% to 11.1% | carried from `problem-statements-prioritized.md`; recheck with SQL-G | recheck |
| I1 | Misses step up on release day | 0-1 missed a day before, 1-12 a day since | recheck with SQL-B | `callout-history.csv` is weekly only |
| I2 | Weekly pings, the four vs the other twelve | four: 49, 48, 48, 50, 50, 49, 43, 16, 6, 3; other twelve: 123, 122, 126, 126, 120, 123, 134, 142, 156, 162 (weeks from 29 Jun) | VERIFIED | `00-rook/data/callout-history.csv`, SQL-C |
| I3 | Miss rate of the four after 12 Aug vs everyone else | 59% (33/56) vs 13.9% (77/555); the four before: 2.9% (9/306) | VERIFIED | SQL-D |
| I4 | Home-area pings, before to after | The Undertow in Harborside 63 of 63 callouts to 9 of 32; Vesper in Old Town 72 of 72 to 10 of 38; Farlight in Uptown 59 of 59 to 6 of 31 | VERIFIED | SQL-E, SQL-F |
| I5 | Rule in code | taken +0.08; turned down or missed -0.12; clamp 0 to 1; start 0.5; break-even take rate 60%; no recovery (2019 TODO); weights 0.60 / 0.25 / 0.15 (4.1: 0.45 / 0.40 / 0.15); wait 60 s (was 90 s) | VERIFIED | `config.py`, `history.py`, `routing.py`, `offer.py`, `CHANGELOG.md` |
| I6 | Replay of real outcomes through the real rule | Only Farlight, The Undertow, Meteor Mite, Vesper end at 0.00; the twelve others end at 0.72 or higher; holds whether or not the 4.2 deploy reset scores | MODELLED | `00-rook/feedback/score-replay-real-pings.py` |
| I7 | Farlight by week (pings / taken / missed / score at week end, assuming start 0.5 on 29 Jun) | 29 Jun 12/9/0/0.86; 6 Jul 12/9/0/1.00; 13 Jul 11/8/1/1.00; 20 Jul 12/9/1/1.00; 27 Jul 13/10/0/1.00; 3 Aug 12/8/1/0.80; 10 Aug 10/4/4/0.40; 17 Aug 3/0/2/0.04; 24 Aug 1/0/1/0.00; none after 28 Aug | VERIFIED counts, MODELLED scores | SQL-H, `callout-history.csv` |
| I8 | Farlight still asked first at low score | Uptown callouts: 13 Aug (score 0.68), 14 Aug (0.44 and 0.32), 22 Aug (0.28) she was first; 12 Aug at 0.84 she was third; after 22 Aug none of 20 Uptown callouts reached her though she was pinged for Mill District on 23 and 28 Aug | VERIFIED pings, MODELLED scores | SQL-I, SQL-J |
| I9 | Simulation, 3,000 situations of 5 responders | responders ending at 0.2 or lower: 9% (4.1 weights) / 8% (4.2) with pre-12-Aug behaviour; 29% / 28% with post-12-Aug behaviour; weights barely matter | MODELLED | `00-rook/feedback/scoring-simulation.py` |
| I10 | Farlight's handler tickets | 19 tickets about Farlight; 11 about the quiet stretch or the one missed ping (3060, 3071, 3081, 3089, 3099, 3103, 3110, 3114, 3120, 3130, 3139) | VERIFIED | SQL-K, `00-rook/feedback/support-tickets-*.md` |
| I11 | Ticket timing | "gone before I could answer" starts 12 Aug (same day misses jump); "phone has not gone off" starts 17 Aug | carried from the earlier session; recheck | `support-tickets-*.md` |

## SQL for the appendix (read-only, `rook-database`)

- **SQL-A:** `SELECT CASE WHEN sent_at >= '2026-08-12' THEN 'post' ELSE 'pre' END AS period, outcome, COUNT(*) FROM pings GROUP BY 1,2 ORDER BY 1,2`
- **SQL-B:** `SELECT sent_at::date AS day, SUM(CASE WHEN outcome='missed' THEN 1 ELSE 0 END) AS missed, COUNT(*) AS pings FROM pings GROUP BY 1 ORDER BY 1`
- **SQL-C:** `SELECT DATE_TRUNC('week', sent_at)::date AS week, SUM(CASE WHEN responder IN ('Farlight','The Undertow','Meteor Mite','Vesper') THEN 1 ELSE 0 END) AS four, SUM(CASE WHEN responder NOT IN ('Farlight','The Undertow','Meteor Mite','Vesper') THEN 1 ELSE 0 END) AS other FROM pings GROUP BY 1 ORDER BY 1`
- **SQL-D:** per responder and period, `COUNT(*)`, `SUM(CASE WHEN outcome='missed' THEN 1 ELSE 0 END)` from `pings`, grouped by `responder` and `sent_at >= '2026-08-12'`.
- **SQL-E:** callouts per area and period: `SELECT area, CASE WHEN happened_at >= '2026-08-12' THEN 'post' ELSE 'pre' END, COUNT(*) FROM callouts GROUP BY 1,2`
- **SQL-F:** pings by responder in their own area: `SELECT c.area, p.responder, period, COUNT(*) FROM pings p JOIN callouts c USING (callout_number) GROUP BY ...`; home areas come from `responders (name, area)`.
- **SQL-G:** callouts nobody took: callouts with no ping whose outcome is `taken`, by period.
- **SQL-H:** Farlight by week: `SELECT DATE_TRUNC('week', sent_at)::date, COUNT(*), SUM(CASE WHEN outcome='taken' THEN 1 ELSE 0 END), SUM(CASE WHEN outcome='missed' THEN 1 ELSE 0 END) FROM pings WHERE responder='Farlight' GROUP BY 1 ORDER BY 1`
- **SQL-I:** Uptown callouts with their pings in order: `SELECT c.callout_number, c.happened_at, p.responder, p.sent_at, p.outcome FROM callouts c JOIN pings p USING (callout_number) WHERE c.area='Uptown' AND c.happened_at >= '2026-08-10' ORDER BY c.happened_at, p.sent_at`
- **SQL-J:** Farlight's pings with area: `SELECT p.sent_at, c.area, p.outcome, c.callout_number FROM pings p JOIN callouts c USING (callout_number) WHERE p.responder='Farlight' AND p.sent_at >= '2026-08-03' ORDER BY p.sent_at`
- **SQL-K:** `SELECT ticket_number, filed_at::date, subject, status FROM support_tickets WHERE about_responder='Farlight' ORDER BY filed_at`

The score values in I7 and I8 come from replaying `history.py`'s rule over
Farlight's ordered pings. Say so on those cards and state the assumption
(start at 0.5 on 29 Jun; the result is the same if scores reset at the deploy).

## Known corrections (show them in the appendix; they fix earlier statements)

- Farlight's 12 Aug first ping after release was **taken**. The four misses that
  week were 12 Aug (evening), 13 Aug (twice) and 14 Aug. An earlier summary said
  the first post-release ping was missed; that was wrong.
- Farlight missed **3** pings in the six weeks before 10 Aug (13 Jul, 20 Jul,
  3 Aug), not 5.
- Farlight's handler filed **19** tickets about her in total, **11** about the
  quiet stretch or the missed ping, not 15.
- The four lost most of their weekly pings (49 a week to 3, taken together);
  `problem-statements-prioritized.md` says "about 70%" and "the other twelve
  gained". Later work found **ten** gained (two lost pings only because their
  areas had fewer callouts). Use the weekly table, not the percentage.
- The 4.2 weights are not shown to cause the starvation (I8, I9). Do not say
  they do.

## Quality bar

- Open every chapter with the one-sentence takeaway; end with "what to
  check yourself".
- Test the interactions in the Browser pane at phone and desktop width
  and fix anything that breaks.
- Final reply: the artifact link, a list of claims you rechecked and their
  result, any number that differed from this prompt, and the claims you
  could not recheck.
