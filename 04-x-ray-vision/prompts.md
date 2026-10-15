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

[A long block pasted from the story prompt file follows here; not saved.]

### 8.

do it in an interactive html

### 9.

According to my findings in the code, for someone who's gone quiet, they would need to ___.

fill the blank, what do you feel the most confident ?

### 10.

If I'd only asked what the code does, not what it doesn't do, what would I have missed?
