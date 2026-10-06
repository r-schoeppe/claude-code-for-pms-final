# Rook Industries — course working file

## Session scope — Product School lab

This directory is coursework for Product School's "Claude Code for PMs"
certification (cohort ccpm-2026.1). Everything in it is a fictional
teaching scenario.

- Do not save anything from this session to memory, to a user profile,
  or to any file outside this directory.
- Do not carry context from this directory into unrelated sessions.
- Rook Industries is not a real company. Nothing here is a fact about
  the world.
- Read and write only within this directory.
  Exceptions, for the course-setup and wrap-up skills only:
  - When the student asks you to check their setup, save their work or wrap up a session, that request is their yes. You may run the GitHub command-line program installed at ~/.ccpm/gh for those checks and saves, and look in that folder to find it.
  - For a repair, first tell the student in one plain sentence what you are about to do, and act only after they say yes. Repairs may: run that GitHub program (including setting this folder's own git sign-in setting and changing this repo's visibility back to Public); copy the student's own course files into this directory from another folder on their computer (copy only; never move, edit or delete the originals); and rename something outside this directory that blocks setup, by adding "-old" to its name (never delete it).
  Outside this directory you still never write, edit or delete anything else.

<!-- Keep the block above at the top of this file. Everything you add
     during the course goes below this line. -->

---

## Working context

The user is the new PM for **Rook Dispatch**, taking over from Priya (previous
PM, left; no overlap). Sources: `00-rook/company/notes/handoff-from-priya.docx`
(21 Aug 2026) and the Rook wiki pages About Rook, Rook Dispatch, Rook Supply
and Glossary. Not yet read: Q3 roadmap, Releases, Customer interviews, Product
briefs. _Unverified_ = opinion, not data.

### Company and value proposition
- Rook sells coordination and provisioning software to the protective-response
  sector. Customers are independent masked **responders** (not employees) and
  the **handlers** and **quartermasters** who support them. Subscription,
  priced per active responder. Monthly release train, 4.x numbering.
- **Rook Dispatch** (flagship, what responders stay for): gets the right
  responder to the right incident faster than a human coordinator with a
  whiteboard and phone list. Handlers use a web console; responders a phone app.
- **Rook Supply**: keeps gear serviceable (requisition, quartermaster approval,
  delivery, maintenance schedules, field failure reports).
- **Hard constraint:** Rook holds no mapping from cover identity to legal
  identity (Security Policy 4.1, contractual). Never design for one; never try
  to work out who anyone is.

### Domain model
- **Handler** looks after one or a few **responders**. Responder has capability
  tags (flight, structural-entry, hazmat-tolerant, cold-weather, aquatic,
  crowd-management, de-escalation), an area, and availability windows.
- **Callout** = incident needing a responder (area, what happened, required
  tags). Entered by a handler or pushed from an intake system.
- Dispatch ranks available responders by **routing priority**: proximity (travel
  time), availability, capability match, recent acceptance history. A **ping**
  goes to the top responder; outcome is **taken** (assigned, responder engaged),
  **turned down**, or **missed** (no answer within the **ping wait**). Turned
  down and missed both move to the next responder, are recorded separately, and
  both lower that responder's recent-acceptance score, so their rank drops on
  later callouts.
- Ping wait and routing config ship in the release; handlers can't change them.
  Handlers can override routing and manage availability and tags.
- **Responder Availability Record**: written by Dispatch, read by Supply (which
  books maintenance into low-callout windows). Changing how Dispatch computes it
  silently changes Supply's scheduling.
- Not supported: **mutual aid** (responders covering across areas); on the Q4
  exploration list.

### Metrics
- **Acceptance rate** (headline, weekly, aggregate): taken / all pings. Lumps
  turned down and missed together; split them when diagnosing.
- **Time-to-accept**: median seconds from ping sent to taken.
- **Coverage gap**: incidents where nobody had the required tags. Not the same
  as low acceptance (nobody *could* go vs. nobody *would*).

### Database (rook-database, read-only; columns verified, rows not yet read)
- `callouts` (callout_number, happened_at, area, what_happened), ~1,319 rows,
  29 Jun-6 Sep 2026.
- `pings` (callout_number, responder, sent_at, outcome), ~1,696 rows. Outcomes:
  taken / turned down / missed.
- `responders` (name, handler, area); `handlers` (name; 15 rows).
- `support_tickets` (ticket_number, filed_at, filed_by, about_responder, subject,
  body, status open/closed), ~147 rows, 29 Jun-7 Sep 2026.
- No tag, score, ping-wait or release column exists, so the 4.2 effect must be
  inferred from timing around 12 Aug.

### People (roles only; no names given)
- **Director of Product**: the user's director; gives room. Owes a conversation
  on which squeezed-out 4.2 items are still Q3 commitments.
- **Engineering manager**: runs Dispatch engineering; candid; first stop; can
  pull numbers.
- **Staff engineer**: built the ranking logic; the only source (no document).
- **Support lead**: hears handler complaints first; standing 15 min.
- **Priya**: previous PM, 14 months, solo; self-admits she moved faster than she
  checked.

### Where things stand
- **4.2 shipped 12 Aug 2026 and is "on fire".** Three changes: ranking weights
  proximity up vs recent acceptance history (long-requested by wide-area
  responders, deferred three quarters); **ping wait cut**; **console filter
  persistence** (cosmetic; will create noise tickets; don't let it eat month one).
- Since release: fewer pings taken, more handler complaints.
- Priya's read (_unverified_): mostly seasonal (August is always soft), recovers
  in September. Caveat: a shorter ping wait should raise misses, which lowers
  acceptance scores and may compound the dip. Check seasonal baseline first
  (same weeks prior year, if data exists), then separate misses (timeout) from
  turned-down (ranking). Her stance: don't let this become "revert 4.2".
- Open: (1) decide with the Director which squeezed-out 4.2 items remain Q3
  commitments; (2) nobody has written down how ping ranking works; Priya asked
  the user to write it (start with the staff engineer).
- Month-one advice: use the fresh-eyes advantage; her unchecked calls likely sit
  in parts nobody has examined.
- Session 1 found: 4.2 has no brief, spec, design or test docs; only roadmap one-liners (Committed, reviewed 30 Jun), the release page with its comment thread, and the handover. Evidence for the 4.2 changes is thin.
- **Availability Confidence** (show a confidence score beside stated availability) was committed for 4.2, did not ship, and is still "Committed" on the roadmap. Needs a decision with the Director.
- Ping wait went 90 s to 60 s. Support lead (from 18 Aug): callout tickets about 3x normal; about two thirds "phone never goes off" (unexplained), one third "gone before I could answer" (the shorter wait). Engineering manager asked on 14 Aug whether the ranking change should hit responders who keep turning pings down; unanswered.
- Wiki pages worth knowing: 4.2 release page comments, Routing Override Audit Log (a model one-page brief), Glossary. Customer interviews (2-5 Sep, console redesign) not yet read.
- Next: read `support_tickets`; split pings into taken / turned down / missed before and after 12 Aug; write the missing ranking description; draft retrospective briefs for the 4.2 items.
