# 04 · X-Ray Vision — prompts

**Context:** You joined Rook two weeks ago as PM on Dispatch.
Release 4.2 shipped on 12 August, just before you arrived, and
landed badly. Last session the numbers showed you what happened: a
ping used to wait ninety seconds and now it waits sixty, people
missed pings they used to catch, and missing one counts the same as
turning one down — so four responders stopped hearing from us
altogether.

At the end of the session, type wrap up, and Claude Code saves the
prompts you wrote yourself below — not the starter prompt — updates
CLAUDE.md, and saves your work to GitHub. By Module 6 this file is a
prompt library built from your own questions.

---

### 1.

Open the folder 00-rook/code/dispatch-routing/. This is the part of our software that decides who gets asked to take a job. I have never read code before and I am not going to start now. Walk me through what happens from the moment something goes wrong somewhere to the moment a responder's phone buzzes, in plain English, no jargon. Then tell me which file each step lives in.

### 2.

1. give me the scoring formula including value bounds
2. simulate 10 different scoring situations with 5 people each. start with similar probabilities for ping and behaviour as in the data and plot all of this score devlopments over time (Context I want to see whether stastically we produce low ranked clusters)

### 3.

Based on what I found, the reason some responders are getting no pings at all is ___, because ___.


Fill the blanks, provide code evidence and validate it

### 4.

Show me every week for Farlight, how many times we pinged them, how many they took. Then tell me what happened to that person, week by week, in plain English. Also add which recent accepted score Farlight would have after each week

### 5.

recent accepted score can tank, but its just additive with the others , why would farlight never get a ping anymore?

### 6.

Look at all the topics we discussed so far,  give me a promt that provides an interactive story artifact of the entire problem like a cartoony teaching story for class members. The story needs to follow a classical Product structure: success metrics, insights/observation, problem, ranked possible solution. 
Go deep in linking data and artifacts so you did a due diligence before reporting an anyone can recheck the claims

### 7.

Ah, Okay I realised, most of my past promts where not there. so Conext and then please catch up: I am new PM and need to see if any fires have to be put out for the past release that I missed, So you need a deep critical view into The tickets, into the pings, into the interviews and then compile a challenged roundup on the current situation (you can look at past prompts on the wrapped up files) 
Finally:

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

### 8.

do it in an interactive html

### 9.

According to my findings in the code, for someone who's gone quiet, they would need to ___.

fill the blank, what do you feel the most confident ?

### 10.

If I'd only asked what the code does, not what it doesn't do, what would I have missed?
