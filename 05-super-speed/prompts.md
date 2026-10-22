# 05 · Super Speed — prompts

**Context:** You joined Rook two weeks ago as PM on Dispatch.
Release 4.2 shipped on 12 August, just before you arrived, and
landed badly. You've spent three sessions finding out what went
wrong: the two piles of feedback that didn't agree, the numbers that
hid four people inside an average, and the code that settled it —
the shorter timeout is what did it.

At the end of the session, type wrap up, and Claude Code saves the
prompts you wrote yourself below — not the starter prompt — updates
CLAUDE.md, and saves your work to GitHub. By Module 6 this file is a
prompt library built from your own questions.

---

### 1.

@04-x-ray-vision/prompts.md "[A long block pasted from the story prompt file follows here; not saved.]" ass the actual query!

### 2.

check the directors request what it wants. who is when?

### 3.

05../ folder

### 4.

<!-- reply 1 -->
> Two audiences to design for. Something a handler like Kip would notice, and something a responder who’s gone quiet would feel differently about. She says “not a setting.”
> No code change yet. She doesn’t want to “quietly change a number and call it handled.” The code gets touched only after she has seen the one-pager.

Elaborate on those points what is meant here what are the details, giive me some travibility here

### 5.

Before starting a prototope lets start preparing a brief:
what and whoms problem we want to solve?
How we want to solve them?

### 6.

at at the beginning a executive overview and decisions needed

### 7.

Okay step back:
we need to solve this problem for two roles:

* responder should not got quiet (forever -> missed ping acceptance should be recoverable to be tested if its better to make a time based one or "testpings" that look like real ones but will just recover a score) and user should be aware of a currently low score 
* handlers need to understand how responders where ranked. so for an dispatched incident they should be able to review score parameters and responder ranking. 


So review as hellen what you need for a brief and which decisions are actually required by her to decide on targeting a hotfix here. Then provide a minimal executive brief with the details mentioned before to organise the path forward

### 8.

Whay to long, do a couple of review rounds with a helen persone model to reach a consice brief for her (before we stat doing prototypes=

### 9.

Wasnt the afternoon fix already clarified by you in the code comment?
review the open question load the data that is already available and come back with less open questions. The excutive cant solve them. Your job is to come back with the solution not open questions

### 10.

so problem definitions where clear, so you propose a 2 leveled approach:
hotfix: availability score penalties (when missing a ping) need to be time-based -> handler an responder should see a small info somwhere of a drained availability score (using domain langauge)
midterm backlog: post ranking review for handlers for dispatchers inlcluding scores)

### 11.

Do a pressure test on the brief as a helen (does she get info that is needed and what we are planing and why), less sections, and solid overview on the info needed for an exective.

### 12.

I asked for 1 HOtifx and backlog split the proposals accordingly - not 4 releases.

### 13.

the brief will be the basis of a clickable demonstrator to build later. DO you have a 95% confidence to build it. if not ask one question at a time get the confidence to build it, so it can be used to give the internal easy presentation of how we want to fix this for users

### 14.

mix of all above: 

- then walk through the incident journey think like a event map canvas, where one can click into the view of data or user screens in that journey. 
- and provide the screens in the context of a persona. (new elements in the screens should be highlighted as such) 
- visual presentation of a scenario on a Map, listing ranked potential responders. 
- find a good was to show score development. potentially in a sepate similator. 

Provide it as interactive html. before giving a result let subagent impersonate different users and give feedback and iterate.

### 15.

Use the Rook wiki and company tone, consider the data you have to assume/confirm features that already exist. IN the mockup I just want to see the elements highlighted that are part of the hotfix and of the backlog

### 16.

This is al over the place, be more focussed. Screens should be within the journey previewable. Simulator slides do not beling in a mockup, if they are even needed to visualize the the issue and the fix. 
Keep the simulator Tab that one is great

### 17.

on the journey I just want to see a diagram with application mockups for each event, reduce all the rest of it .

### 18.

Now I like the demostrator. give me a quick summary what would be the approach to directly come to such a result before you store that approach into memory and a skill

### 19.

okay, then write me a skill that is independent from rook or this personas, this is about getting to clear demonstrators for whatever problem/features faster.
