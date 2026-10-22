# Brief: Quiet responders and visible ranking

Executive brief · Product, Dispatch · Draft v1 for Helen Achebe · Data to 7 Sep 2026
Status key: **V** verified from data or files, **M** modelled, **I** inferred, **U** unknown. The earlier long draft is `brief-v0-full.md`.

## In one paragraph

Since 4.2 (12 Aug), four responders have almost stopped getting offers: 49 pings a week down to 3 (V). A missed ping costs as much as a refusal and nothing lets a score recover without a yes, so a bad run becomes permanent (M, `00-rook/code/dispatch-routing/history.py`). Handlers cannot see why, because ranking is never recorded (V: no score column exists). We propose a small hotfix for two people: **responders get a way back and are told when their score is low; handlers can open any dispatched callout and see how everyone was ranked.** No new settings, and no change to the weights or the 60-second wait.

## The two problems

| Who | Problem | Evidence |
|---|---|---|
| **Responder** | Goes quiet and stays quiet; nobody tells them why. "starting to wonder if im still even in the system." | Pings to the four 49 → 3 a week (V, `00-rook/data/callout-history.csv`). 59% of their few pings missed, against 13.9% for others (V). Tickets 3120, 3121, 3110, 3140 (V). |
| **Handler** | Cannot tell why one responder is on fire and another is silent. "I just want it to look less like a coincidence." | `kip.md` (V). Ranking scores are not stored anywhere (V). Handlers can already override routing, and overrides are logged since 4.0 (V, release 4.0 page), but the reason for the ranking is not. |

## What we propose

**1. A way back for responders (hotfix).** Test two mechanisms, then pick:

| Option | Responder feels | Fixes quiet? | Risk |
|---|---|---|---|
| **A. Time-based recovery**: an idle responder's score eases back toward neutral each day without a ping | Nothing; offers return | Yes, and a responder who keeps declining still drops again when asked | Smallest change; the 2019 worry (someone who stopped working stays high) is limited because recovery only runs while idle |
| **B. Real fair-share offer**: after N idle days they get a first offer on a real callout in their area | They are asked again | Yes | Real callout goes to a lower-ranked person once |
| **C. Test ping that looks real but is not** | A buzz for nothing | Yes | **Deceives responders in a safety product (I).** They may gear up or travel; trust is lost when found out; it pollutes acceptance rate and pings-per-callout unless excluded |
| **D. Labelled practice ping** | A clearly marked check-in | Yes | Needs phone-app work (U) |

We recommend **A for the hotfix**, B as the follow-up if A is not enough, and **no disguised pings (C)**. Compare A, B and D offline first by extending `00-rook/feedback/scoring-simulation.py`; four affected responders are too few for a live statistical test (I).

**2. Responders know their score is low (hotfix or next release).** A plain message in the phone app: offers are lower because of recent missed or declined pings, with how it recovers. Whether the app can show it is **U**.

**3. Handlers can review any ranking (hotfix for the data, next release for the screen).**
- **Hotfix:** save, for every dispatched callout, the ranked list with each responder's three parts (proximity, recent acceptance, skills), the weights used and the outcome. This changes no routing behaviour.
- **Next release:** show it in the console's existing activity view next to the callout, the same place the override audit log was designed to go.

## Decisions needed from Helen

| # | Decision | Our recommendation |
|---|---|---|
| 1 | **Approve a hotfix** for 1A and the ranking data in 3, outside the monthly release train (routing config normally ships with the release). | Yes. Hold engineering's "this afternoon" number change until this is agreed. |
| 2 | **Are disguised test pings acceptable at all?** | No. If we test pings, label them. |
| 3 | **Transparency:** may responders see their own low-score status, and handlers the full score parts and ranking for any callout? | Yes to both. Wording and layout are ours. |
| 4 | **Blast radius:** recovery applies to all responders, not only the four. | Yes: the rule is the same for everyone. |

**We decide within these limits** (not for Helen): recovery rate and idle days, wording, screen layout, how long ranking data is kept.

## How we will know

- **Quiet ends:** each of the four gets at least 1 ping a day within 7 days of the hotfix (baseline: under 1 a week each).
- **Misses from the four** move from 59% toward the 14% of others.
- **Handler can answer "why wasn't X asked?"** within a minute on 3 handlers (try Kip), and 100% of dispatched callouts have a saved ranking.
- **Guardrails:** acceptance rate, pings per callout, and callouts nobody took do not get worse; test pings, if used, are excluded from them.

## Not in scope

The 60-second wait; the weights; any change to the shape of `availability.current_record()` (Rook Supply reads it); splitting the miss penalty from the refusal penalty (an option if recovery is not enough).

## Path forward

| Step | Who | What |
|---|---|---|
| 0 | Staff engineer via engineering manager | Answer four questions: does a deploy reset scores in memory (a hotfix deploy could reset everyone to 0.5 and hide the effect) (U); score components for callouts 40985, 41416, 40987, 40997; push logs for 12 and 13 Aug; travel times for the four. |
| 1 | PM | Offline comparison of options A, B, D. |
| 2 | Helen | Decisions 1 to 4. |
| 3 | Engineering | Hotfix: recovery rule plus ranking data. |
| 4 | PM, designer | Handler ranking view and responder message, then click-through. |

## Open questions (U)

Which fix engineering means by "this afternoon"; Helen's deadline; whether scores are saved anywhere; why the four miss so much (the shorter wait, push delivery, or both).
