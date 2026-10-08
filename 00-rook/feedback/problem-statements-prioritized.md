# Rook Dispatch: prioritized problem statements (4.2 feedback)

Sources: 4 handler interviews (2-5 Sep 2026, Research section of the wiki), all 147 support tickets (29 Jun-7 Sep), pings and callouts tables. "Before/after" = before/after 4.2 shipped on 12 Aug 2026.

## Prioritized table

| Priority | Problem statement | Evidence | Success criterion it threatens | Why this rank | Next step |
|---|---|---|---|---|---|
| **1** | **P1: Callouts go to someone else before the responder can answer.** | 15 tickets (0 before, 15 after, all open). 3 of 4 interviews. Missed pings 2.3% -> 18.0%, jumping on 12 Aug. Turned down fell 21% -> 18%, so the acceptance drop is all misses. | **Acceptance rate** (headline): taken / all pings. Misses are the whole drop. Also **time-to-accept**: the 60 s wait was meant to speed it up, so check its trade-off. | Direct hit on the headline metric. Known cause (ping wait 90 s -> 60 s). Fastest lever: it is release config. | Decide whether 60 s is the right wait. Split missed from turned down in reporting. |
| **2** | **P2: Some responders went quiet and nobody can say why.** | 30 tickets (0 before, 30 after, all open), covering Farlight, The Undertow, Corporal Ashgrove, Halfmoon. Farlight, The Undertow, Meteor Mite and Vesper lost about 70% of pings; the other twelve gained. Vesper and Meteor Mite filed no tickets, so tickets undercount. 2 of 4 interviews. | **Acceptance rate**, indirectly: those four missed 53-64% of the few pings they got. Also the business outcome of **active responders** (pricing is per active responder; retention risk): "starting to wonder if im still even in the system." | Most severe for the people affected, and the cause is unknown, so it needs investigation before it can be fixed. | Ask the staff engineer if the ranking change was meant to penalise decliners (engineering manager's open question, 14 Aug). Check whether the four are recovering. |
| **3** | **P3: Handlers can't see or hear callouts in time or at a glance** (alerts, small text, status badges, dark mode). | 13 tickets (7 before, 6 after, so already there). 3 of 4 interviews (alerts and legibility); dark mode raised by Kip. No data covers it. | **Time-to-accept**: if handlers notice sooner they can alert the responder sooner. Plausible, not measured. | Real and cheap to fix in the redesign, but not caused by 4.2 and not linked to a metric shift. | Put alerts per responder, bigger badges and dark mode in the console redesign scope. |
| **4** | **P4: Console filters reset silently and can't be trusted.** | 16 tickets (2 before, 14 after; 6 open): 12 complaints, 2 thank-yous, 2 old requests. 1 of 4 interviews (Ambrose). | No Dispatch success criterion. It affects handler efficiency, which isn't a defined metric. | A 4.2 feature with rough edges. Small cost per handler, high ticket count. | Warn on reset, add a clear-all, and give each sign-in its own filters. |
| **5** | **P5: Supply requests, failure reports and catalog search are slow or opaque.** | 26 tickets (10 before, 16 after; 9 open). 1 of 4 interviews (Halloran). | A **Rook Supply** criterion (gear serviceability). None is defined in my notes. | Outside Dispatch scope. Weekly ticket rate rose (about 1.6 a week before, 4.3 after), cause unknown. | Pass to the Supply owner. |
| 6 | Other console and account requests, plus duplicate-notification glitches. | 47 tickets. The 6 glitch tickets (6 before, 0 after) fit the 4.2 duplicate-notification fix. | None. | Background noise. | Triage normally. |

## Metric gaps worth knowing
- **Callouts nobody took** doubled, from 5.5% to 11.1%. This is not the **coverage gap** metric (nobody had the tags), because here nobody *would* go. No metric tracks it today.
- **Distribution of pings across responders** is not measured either, and P2 is exactly that.

## Limits
- No prior-year data (callouts start 29 Jun), so seasonality can't be tested.
- No geography or ranking-score data, so the cause of P2 is untested.
- The ticket groups are keyword-based on subject lines; all bodies were read.
