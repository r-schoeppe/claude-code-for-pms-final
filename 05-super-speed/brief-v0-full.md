# Brief: Quiet responders

One-pager · Product, Dispatch · Draft v0 for Helen Achebe · Data to 7 Sep 2026
Status key: **V** verified from data or files, **M** modelled, **I** inferred, **U** unknown.

## Executive overview

Since 4.2 shipped on 12 Aug, four responders have almost stopped getting offers: 49 pings a week down to 3 (V). Their handlers get no explanation and the responders are asking whether they are still in the system. The cause is in how recent acceptance is scored: a missed ping costs as much as a refusal, and nothing lets a score recover without a yes (M). Overall acceptance fell from 76.6% to 64.0%, driven by misses (V). We propose three experience-first changes, not a new setting: a miss stops counting as a refusal, there is a way back, and quiet is visible and explained to the handler. Nothing in the code changes until you have seen and approved this.

## Decisions needed from Helen

| # | Decision | Our recommendation | Needed by |
|---|---|---|---|
| 1 | **Which fix does engineering mean** by "ship this afternoon"? Hold it until this brief is agreed. | Hold. Confirm it is a number in `config.py` and not a change to how scores work. | Before any code change |
| 2 | **Scope.** Two audiences (quiet responders and their handlers). The 60-second ping wait is decided separately. | Agree as written. | This week (U: no deadline given) |
| 3 | **The way back.** Scores ease toward neutral over time, or anyone with no offer for N days gets a guaranteed first offer. | Guaranteed first offer: it answers the 2019 note's worry that someone who stopped taking work should not stay high. | After the diagnostics |
| 4 | **A 7-day trial.** Reset two of the four to neutral and keep two as comparison. | Yes, with the success measure below agreed first. | Before the trial starts |
| 5 | **Engineering time** for four diagnostics: score components for callouts 40985, 41416, 40987, 40997; push logs for 12 and 13 Aug; whether the 4.2 deploy reset scores; travel times for the four. | Yes, via the engineering manager and the staff engineer. | This week |
| 6 | **Visibility.** Does the handler card and a responder-facing message need design capacity, and can the phone app show one? | Handler card first; responder message once the phone-app question is answered. | After decision 2 |

## Whose problem, and what is it

| Who | The problem, in their words | Evidence |
|---|---|---|
| **A responder who has gone quiet** (Farlight, The Undertow, Meteor Mite, Vesper) | Nobody asks them any more, nobody tells them why, and the one offer that does come is gone before they can answer. "starting to wonder if im still even in the system." | Pings to the four fell 49 a week to 3 (V, `00-rook/data/callout-history.csv`). Tickets 3120, 3121, 3110, 3140 (V). They missed 59% of the few pings they got, against 13.9% for everyone else (V). |
| **A handler like Kip** | Two responders on two cards, one "dead quiet" and one "on fire", and nothing on screen to explain it. "I just want it to look less like a coincidence." | `00-rook/wiki/research/customer-interviews/kip.md` (V). Meteor Mite 1.09 to 0.12 jobs a day, The Gale 1.45 to 1.85 (V, SQL-L). |
| **Rook** (secondary) | Pricing is per active responder, so a responder who stops getting work is a retention risk. | CLAUDE.md, About Rook (V); churn itself is not shown (U). |

**Why it happens (M).** The recent-acceptance score only goes up when someone says yes, a miss costs the same as a refusal (-0.12 against +0.08), and nothing lets it recover on its own (`00-rook/code/dispatch-routing/history.py`, the 2019 TODO). Replaying real pings through that rule leaves exactly these four at 0.00 (`00-rook/feedback/score-replay-real-pings.py`). Score alone is worth at most about 19 minutes of travel, and Farlight was still asked first at 0.28, so it is not the whole story (M).

## How we want to solve it

Start from what each person would notice. Three moves, in order:

1. **A missed ping stops counting as a refusal.** *Responder feels:* "one bad week doesn't push me out." *Handler feels:* nothing changes, nothing breaks. Changes `record_declined` so a miss costs less or nothing, and a turn-down stays as is.
2. **There is a way back.** *Responder feels:* "I get asked again." Either scores ease toward neutral over time, or anyone with no offer for N days gets a guaranteed first offer on the next callout in their area. Trade-off from the 2019 note: someone who has stopped taking work should not stay high, so the fair-share offer is the safer option (I).
3. **Quiet becomes visible and explained.** *Handler feels:* the responder's card says "No offers in 9 days. Last 3 offers missed." *Responder feels:* a message that says they are still in rotation. This needs scores and reasons to be recorded, which they are not today (U), and a decision on whether the phone app can show it (U).

## Not in scope

- A new setting or a handler switch ("not a setting").
- The 60-second ping wait, which affects the healthy twelve too. Decide it separately.
- Any change to the shape of `availability.current_record()`, which Rook Supply reads.
- Any code change before Helen has seen this brief.

## Success measure (proposal, I)

Baseline: the four averaged under 1 ping a week each in the 31 Aug week, against about 12 before.
- **Within 7 days of the change:** each of the four gets at least 1 ping a day. Try it on two and keep two as comparison.
- **Missed pings from the four:** fall from 59% toward the 14% of everyone else.
- **Quiet tickets:** no new "phone has not gone off" or "still on the list" tickets (83 of 108 post-release tickets are still open, V).
- **Track two metrics we have none for:** ping share per responder, and callouts nobody took.

## Open questions (U)

- Which fix engineering means by "ship this afternoon", and when Helen needs this.
- Whether the 4.2 deploy reset scores, and whether scores are saved anywhere.
- Why the four miss so much: the shorter wait, push delivery, or both. Push logs for 12 and 13 Aug would show it.
- Score components for callouts 40985, 41416, 40987 and 40997, and travel times, to explain why a home responder ranks below a neighbour.
- Whether to design for Kip's own ask for different alert sounds per responder as part of this or separately.

## Owner and next step

Owner: PM, Dispatch, with the staff engineer. Next: agree the problem statement with Helen, then build a click-through of the handler card and the responder message.
