# Brief: Quiet responders, two levels

For Helen Achebe · Draft v5 · Data to 7 Sep 2026 · V verified from data or code, M modelled (replay or simulation), P proposal. Earlier drafts are `brief-v0-full.md`, `-v1-options.md`, `-v3-gates.md`, `-v4-recovery.md`.

## Problem

Since 4.2 (12 Aug), the four responders who went quiet (Farlight, The Undertow, Meteor Mite, Vesper) went from 49 pings a week together to 3, from 28% of all pings to 1.8% (V, `00-rook/data/callout-history.csv`). A missed ping costs the same as a refusal (-0.12) and nothing lets a score recover without a yes, so one bad run is permanent (V, `00-rook/code/dispatch-routing/history.py`, the 2019 note). Replaying their real pings leaves all four at 0.00 (M). Neither they nor their handlers can see this happening.

- **Responder:** "starting to wonder if im still even in the system." (ticket 3121)
- **Handler (Kip):** "I just want it to look less like a coincidence." (`kip.md`)

## Level 1: hotfix

**1. A missed ping costs less over time.** A miss still lowers a responder's recent acceptance by 0.12, and that penalty halves every 2 days, so it is mostly gone after about a week. Refusals and takes work as today. This answers Wen's 2019 question: yes, it should ease back, for misses.

- **The four, replayed on real pings:** all four go from 0.00 to 0.71 to 0.81 on 7 Sep (fade half-lives of 1 to 3 days) (M).
- **The other twelve:** their average moves from 0.90 to between 0.92 and 0.84, so no one is pushed down in a way they weren't before (M).
- **A responder who keeps missing:** if they miss 59% of pings (like the four) and keep being asked, they settle at about 0.13 instead of 0.03, so they stay low and are not shut out. A healthy responder settles higher than today (0.82 against 0.78) (M).
- **Honest limit:** this brings them back into rotation; it does not explain why they miss 70% of first pings (V: 28 of 40, against 16.5% for everyone else).

**2. A small, plain line for handler and responder.** Not a number: a level, in the Glossary's own word, **recent acceptance** (Good, Lowered, Low).
- **Handler, on the responder's card in the console:** "Recent acceptance: Low. 3 of the last 4 pings missed. Offers are reduced. Misses fade in about a week."
- **Responder, in the phone app:** "Your recent acceptance is low, so you will be offered fewer callouts. Missed pings fade within about a week, and taking a ping raises it straight away."
- **Levels (P):** Good at 0.6 or above, Lowered 0.3 to 0.6, Low under 0.3.
- **Not called "availability score":** that collides with the Responder Availability Record (Supply reads it) and the committed "Availability Confidence" item. The line could be the first slice of Availability Confidence if Helen wants.
- **If the phone app cannot show a line in the hotfix:** the handler line ships first and the support lead gives handlers a one-line message to pass on, so the responder is still told.

**3. Recommended add-on, logging only:** for every dispatched callout, save the ranked list, each responder's three score parts, the weights and the outcome. It changes no routing and feeds Level 2.

**Rollback:** turn the fade off to restore today's rule. No change to weights, the 60-second wait, or the availability record's shape (V).

## Level 2: midterm backlog (4.3)

**Post-dispatch ranking review for handlers.** On any dispatched callout, a handler opens "How this was ranked": each responder in order, the three parts (proximity, recent acceptance, skills) and the weights, the outcome, and any override already logged since 4.0. A handler sees full scores for their own responders and the order only for others; Security reviews that as part of this item. It goes in the console's activity view, the same place the override audit log uses.

## Decision for Helen

**Approve Level 1 as written, owned by Wen Li (Marcus Oyelaran confirms), off the monthly train, with her written review before launch** (silence is not a yes), and **accept Level 2 into the 4.3 backlog.**

## Pull-back trigger

Revert if, in any full week after launch, acceptance rate is below 66.7% or callouts nobody took exceed 12.9% (the worst of the week of 24 Aug; the week of 31 Aug was 72.7% and 5.5%) (V).

## Success

In the second full week after launch (so any reset from the deploy has settled), the four get at least 14% of weekly pings (from 1.8%; half their 28% before 4.2). If not, Wen Li and the PM review with Marcus, and Helen decides whether to add a real fair-share offer.

## Alongside, no decision needed

Wen Li pulls push logs for the four on 12 and 13 Aug. The support lead asks their four handlers to check each responder's app version and notification settings. The Supply owner is told that quieter responders getting more pings moves maintenance windows.
