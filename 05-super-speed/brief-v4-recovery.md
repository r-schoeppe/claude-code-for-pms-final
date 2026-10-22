# Brief: Quiet responders (hotfix proposal)

For Helen Achebe · Draft v4 · Data to 7 Sep 2026 · V verified from data or code, M modelled. Earlier drafts: `brief-v0-full.md`, `brief-v1-options.md`, `brief-v3-gates.md`.

## Problem

Since 4.2 (12 Aug), the four responders who went quiet (Farlight, The Undertow, Meteor Mite, Vesper) went from 49 pings a week together to 3, from 28% of all pings to 1.8% (V, `00-rook/data/callout-history.csv`). A missed ping costs the same as a refusal (-0.12) and a score only rises on a yes, so one bad run is permanent (V, `00-rook/code/dispatch-routing/history.py`). Replaying their real pings through that rule leaves all four at 0.00 (M). Handlers cannot see why, because rankings are not stored.

- **Responder:** "starting to wonder if im still even in the system." (ticket 3121)
- **Handler (Kip):** "I just want it to look less like a coincidence." (`kip.md`)

## The fix: what engineering's "this afternoon" change is

It is the question Wen left at `history.py:30` in 2019: should a score ease back toward neutral on its own? Yes, with one rule: **a responder below 0.5 who is not asked drifts toward 0.5 by 10% of the gap each idle day; nobody above 0.5 is pulled down.** From 0.00 that is 0.26 after 7 idle days and 0.39 after 14. Replaying the four's real pings with this rule leaves them at 0.25 to 0.37 on 7 Sep instead of 0.00 (M). Healthy responders are unaffected (simulation, mean score 0.92 either way) (M). Because the rate is one constant, rollback is setting it to 0.

Shipped with it: **a ranking record.** For every dispatched callout, save the ranked list, each responder's three score parts, the weights and the outcome. Logging only; no routing change. The handler screen follows in 4.3 in the console's activity view, with Security review as part of that work. No new settings, no disguised test pings, weights and the 60-second wait untouched.

## What the data already settled

| Question | Answer | Evidence |
|---|---|---|
| Is the 60-second wait real, or did 4.2 slow dispatch? | The wait is real; dispatch is not slower. Gap to the next ping: median 25 s → 61 s, longest 93 s → 63 s. First ping goes out in 14 s → 15 s. | V |
| Do the four miss because they are backups, asked late? | No. 40 of their 56 pings since 12 Aug were first pings; 28 of those (70%) were missed, against 16.5% for everyone else's first pings. | V |
| Is it about their own area? | No. They miss both at home (18 of 34) and elsewhere (15 of 22); none of the 22 pings outside their area was taken. | V |
| Does the score explain the silence? | It fits: the odds of Farlight being asked first fell as her score fell (4 of 11 callouts at 0.28 to 0.68, none of the last 20 at 0.16 or lower). One release-day callout does not fit. The ranking record will explain it next time. | M |
| Does a deploy reset scores? | Not needed: we log every score at launch and measure in the **second** full week, after any reset has settled. | design |

**Still not explained: why these four miss 70% of first pings** (the shorter wait, push delivery, or both). Recovery will not fix that alone. In simulation a responder like that gets about 10% of pings with or without recovery. So alongside the hotfix: Wen Li pulls push logs for the four on 12 and 13 Aug, and the support lead asks their four handlers to check each responder's app version and notification settings.

## Decision for Helen

**Approve the hotfix as written, owned by Wen Li (Marcus Oyelaran confirms), off the monthly train, with her written review of the change before launch. Silence is not a yes.**

## Pull-back trigger

Revert if, in any full week after launch, acceptance rate is below 66.7% or callouts nobody took exceed 12.9% (the worst of the week of 24 Aug; the week of 31 Aug was 72.7% and 5.5%) (V).

## Success

In the second full week after launch, the four get at least 14% of weekly pings (from 1.8%; half their 28% before 4.2).
- **At 14% or more:** the hotfix did its job. Misses staying high is then the push-delivery work.
- **Below 14%:** Wen Li and the PM review with Marcus, and Helen decides whether to try a real fair-share offer or a clearly labelled practice ping.

Also tell the Supply owner: quieter responders getting more pings moves maintenance windows.
