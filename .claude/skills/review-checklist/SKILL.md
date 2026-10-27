---
name: review-checklist
description: Checks a product brief so the person who must decide can decide, and the rest of the company understands the decision. It tests five things: the brief names who owns it, asks for one clear decision, says how we will know it worked, keeps the same scope from start to finish, and explains the problem before the fix. It leads with whether the decider can decide today. Use it when the user points at a brief (a file path, a pasted brief, or "this brief") and asks to review it, check it, run the review checklist, or see whether it is ready. Read-only: it reports; it does not rewrite the brief unless asked.
---

# Review checklist

Review one brief the way the person who has to decide would read it, and the way someone outside the team would repeat it. Report what passes, what does not, and the smallest edits that fix it. Be exact and quote the brief. Do not guess.

## How to run

1. Get the brief. If the user gave a path, read the whole file (with line numbers). If they pasted it, use that. If several documents could be meant, ask which one in one short question.
2. Read the whole brief before judging anything.
3. First do the **two reader tests** below, then the five checks. For each check record a result and the evidence: a short quote and where it is (section heading or line number).
4. Report in the format at the end. Do not edit the brief unless the user asks for the fixes to be applied.
5. If a check cannot be judged from the text, say "not found in the brief" instead of inferring it from elsewhere. Judge structure and clarity only, not whether the numbers are right.

## Two reader tests (do these first)

- **Restate test.** Using only the brief, write the ask as one sentence an outsider could repeat: what is being decided, by whom, and what happens next. If you cannot write it without guessing, or the brief contains more than one ask bundled together, say so.
- **First-screen test.** Read only the first section (about the first 150 words). Does it contain the problem, the ask and the owner? Name what is missing from it.

## The five checks

### 1. Names who owns it

- **Pass:** one named person or one named role owns the outcome. Where several people are involved, the brief says who leads and who only confirms or reviews.
- **Partial:** only a team is named, several owners have no lead, a backlog or measure has no owner, or the owner is contradicted elsewhere.
- **Fail:** no owner is named.
- Look for: "owner", "owned by", "accountable", "DRI", a name or role in the header or the ask.

### 2. Asks for one clear decision

- **Pass:** the brief states the decision in one place; says who decides; says by when (a date or a trigger); says what happens if nothing is decided, or what waiting costs; and offers a recommendation.
- **Partial:** the ask is clear but the date, the cost of waiting, or the recommendation is missing, or two or three decisions are bundled into one ask.
- **Fail:** there is no ask, or the reader has to infer what to approve.
- Look for: "approve", "decide", "decision", "ask", "by", "if we do nothing", "cost of delay".

### 3. Says how we will know it worked

- **Pass:** a measure with a baseline, a target, a time window, and where it is measured. Better still: a pull-back or failure condition. Every deliverable has a measure or the brief says it has none.
- **Partial:** a measure is named but the baseline, target, time window or source is missing, or one deliverable has no measure.
- **Fail:** only vague goals ("improve", "better experience", "reduce complaints") or nothing at all.
- Look for: "success", "measure", "metric", "target", "baseline", "within", "by", numbers with units.

### 4. Keeps the same scope from start to finish

Build a scope inventory for each section (summary, problem, plan or proposal, success measure, risks, next steps): the list of things the brief says it will deliver, change or leave alone. Then compare.

- **Pass:** the same set of deliverables appears wherever scope is stated, with the same names and the same count (for example the same number of releases or phases). Items marked out of scope never appear in the plan.
- **Partial:** small drift: a renamed item, a count that changes, a deliverable or condition mentioned once only.
- **Fail:** an item appears in a later section that is not in the plan, an item in the plan disappears or becomes "later", the number of releases or phases changes, or an out-of-scope item shows up as work.
- Report each drift as: item, where it first appears, where it changes, and the exact wording in both places.

### 5. Explains the problem before the fix, in plain words

- **Pass:** the problem (who is affected, what happens, evidence) is stated first and is understandable without reading the fix. Every part of the fix can be traced back to something in the problem. Terms an outsider would not know are explained on first use.
- **Partial:** a short ask or summary comes first but the problem follows immediately, some fixes have no matching problem, or the first section leans on undefined shorthand.
- **Fail:** the fix, the plan or the decision comes before the problem is explained, or the problem is only implied by the fix.
- Method: find the first sentence that proposes a solution and the first sentence that states the problem. Compare the order. List each fix element and mark whether the problem section justifies it. List up to five terms in the first section that an outsider would not understand.

## Report format

Start with the bottom line, in this order:

1. **Brief and verdict:** the brief's name and one of: ready, ready with small fixes, not ready.
2. **Can the decider decide today?** Yes, or "Not yet: " and the one thing that blocks it.
3. **The ask in one sentence** (from the restate test), or "cannot be stated without guessing".

Then the table:

| Check | Result | Evidence |
|---|---|---|
| Owner named | pass, partial or fail | quote and location, or "not found" |
| One clear decision | pass, partial or fail | quote and location, or what is missing |
| How we will know it worked | pass, partial or fail | quote and location, or "not found" |
| Same scope throughout | pass, partial or fail | the drift, or "consistent" |
| Problem before fix, in plain words | pass, partial or fail | order found, unmatched fix, undefined terms |

Then **Fix first** (at most three edits, most important first). Tag each one **Blocks the decision** or **Polish**. Each edit says what to add or change and where, in one sentence. Do not write long replacement text unless the user asks.

Keep the whole report to half a page. Use plain words. State what you could not judge.
