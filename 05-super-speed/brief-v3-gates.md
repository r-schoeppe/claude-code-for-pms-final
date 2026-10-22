# Brief: Quiet responders (hotfix proposal)

For Helen Achebe · Draft v3 · Data to 7 Sep 2026 · V verified, M modelled, U unknown. Earlier drafts: `brief-v0-full.md`, `brief-v1-options.md`.

## Problem

Since 4.2 (12 Aug), the four responders who went quiet (Farlight, The Undertow, Meteor Mite, Vesper) went from 49 pings a week together to 3, from 28% of all pings to 1.8% (V, `00-rook/data/callout-history.csv`). A missed ping costs the same as a refusal (-0.12) and a score only rises on a yes, so one bad run is permanent (`00-rook/code/dispatch-routing/history.py`, the 2019 note). Replaying their real pings through that rule leaves all four at 0.00 (M). Handlers cannot see why, because rankings are not stored.

- **Responder:** "starting to wonder if im still even in the system." (ticket 3121)
- **Handler (Kip):** "I just want it to look less like a coincidence." (`kip.md`)

## Proposal: one hotfix, two parts

No new settings; weights and the 60-second wait untouched. No disguised test pings.

1. **Recovery.** A responder not asked on a callout drifts back toward neutral (upward only). Replaying the four's real pings with a 10% daily pull leaves them at 0.25 to 0.37 on 7 Sep instead of 0.00 (M). **It is necessary but not enough:** they missed 59% of pings against 14% for everyone else. In simulation a responder like that gets about 10% of pings with or without recovery (11% at the strongest setting), so the misses need their own cause (push logs, 12 and 13 Aug) (M, U).
2. **Ranking record.** For every dispatched callout, save the ranked list, each responder's three parts, the weights and the outcome. No routing change. The handler screen and any responder message come in a later release, after Security agrees what handlers may see.

## Decision for Helen

**Approve a two-step path:**
1. **This week:** Wen Li (Staff Engineer, built the ranking) answers three questions in writing, through Marcus Oyelaran. Pass answers, agreed before she replies:

   | Question | Pass | Fail (do not ship) |
   |---|---|---|
   | (a) Does the score loop explain the silence? She shows the three score parts for callouts 40985, 41416, 40987, 40997. | The recent-acceptance part is what puts the four below their neighbours, and the release-day flip has a stated cause. | The gap comes from travel or skills, or the flip stays unexplained. |
   | (b) Does a deploy reset in-memory scores? | Scores survive a deploy, or we record every score before and after so the effect is measurable. | A reset we cannot see or avoid. |
   | (c) What is the "this afternoon" fix? | Described in writing, and held back until after this hotfix so the two do not blur. | Not described. |

2. **Ship only after Wen Li confirms all three passes in writing.** Silence is not a yes. Owned by Wen Li (Marcus to confirm), off the monthly release train. **Rollback:** setting the recovery rate to 0 restores today's behaviour; the ranking record is logging only and can be switched off.

## Pull-back trigger

Revert if, in any full week after launch, acceptance rate is below 66.7% or callouts nobody took exceed 12.9% (the worst figures of the week of 24 Aug; the week of 31 Aug was 72.7% and 5.5%) (V).

## Success

The four's share of weekly pings rises from 1.8% to at least 14% within two weeks (half their share before 4.2).

**Two-week check, PM reports to Helen:**
- Share at 14% or more: the hotfix did its job. Misses staying high is then a separate cause; start the push-delivery work.
- Share below 14%: Wen Li and the PM review with Marcus, and Helen decides whether to try the fallback (a real fair-share offer or a clearly labelled practice ping).

Misses falling from 59% toward 14% is a hoped-for effect, not the pass test. Also tell the Supply owner: quieter responders getting more pings moves maintenance windows.
