import random, json, sys

# ---- real values from dispatch-routing/config.py (4.2) and 4.1 (changelog / config comments)
CFG = {
 "4.2": dict(wp=0.60, wh=0.25, wc=0.15),
 "4.1": dict(wp=0.45, wh=0.40, wc=0.15),
}
CREDIT, PENALTY, FLOOR, CEIL, HORIZON, NEUTRAL = 0.08, 0.12, 0.0, 1.0, 45, 0.5
# ---- ping outcome rates from rook-database (pre = before 12 Aug, post = from 12 Aug)
BEHAV = {"pre": dict(miss=25/1085, decl=229/1085), "post": dict(miss=110/611, decl=110/611)}
N_CALLOUTS, N_PEOPLE, P_AVAIL, CONC = 250, 5, 0.7, 12
TAGS = list(range(7))

def beta_mean(rng, mean, conc):
    mean = min(max(mean, 0.005), 0.95)
    return rng.betavariate(mean*conc, (1-mean)*conc)

def make_situation(rng, behav):
    people = []
    for i in range(N_PEOPLE):
        miss = beta_mean(rng, BEHAV[behav]["miss"], CONC)
        decl = beta_mean(rng, BEHAV[behav]["decl"], CONC)
        if miss + decl > 0.95:
            s = 0.95/(miss+decl); miss, decl = miss*s, decl*s
        people.append(dict(base=rng.uniform(5, 35), miss=miss, decl=decl,
                           tags=set(rng.sample(TAGS, 3))))
    return people

def run(rng, people, w, record=True):
    H = [NEUTRAL]*N_PEOPLE
    traj = [list(H)]
    pings = [0]*N_PEOPLE
    taken = [0]*N_PEOPLE
    for _ in range(N_CALLOUTS):
        avail = [i for i in range(N_PEOPLE) if rng.random() < P_AVAIL] or [rng.randrange(N_PEOPLE)]
        need = set(rng.sample(TAGS, rng.choice([1, 2])))
        scored = []
        for i in avail:
            t = max(2.0, people[i]["base"] + rng.gauss(0, 8))
            P = 0.0 if t >= HORIZON else 1 - t/HORIZON
            C = len(need & people[i]["tags"]) / len(need)
            scored.append((w["wp"]*P + w["wh"]*H[i] + w["wc"]*C, i))
        scored.sort(reverse=True)
        for _, i in scored:
            pings[i] += 1
            r = rng.random(); p = people[i]
            if r < p["miss"] or r < p["miss"] + p["decl"]:
                H[i] = max(FLOOR, H[i] - PENALTY)
            else:
                H[i] = min(CEIL, H[i] + CREDIT); taken[i] += 1
                break
        if record: traj.append(list(H))
    return traj, H, pings, taken

def stats(cfg, behav, n, seed):
    rng = random.Random(seed)
    finals, takerate, pingshare = [], [], []
    sit_low = 0
    for _ in range(n):
        ppl = make_situation(rng, behav)
        _, H, pings, taken = run(rng, ppl, CFG[cfg], record=False)
        finals += H
        takerate += [taken[i]/pings[i] if pings[i] else None for i in range(N_PEOPLE)]
        tot = sum(pings)
        pingshare += [pings[i]/tot for i in range(N_PEOPLE)]
        if min(H) <= 0.2: sit_low += 1
    return finals, takerate, pingshare, sit_low/n

if __name__ == "__main__":
    out = {}
    # 10 showcase situations: 4.2 weights, post-12-Aug behaviour
    rng = random.Random(42)
    show = []
    for s in range(10):
        ppl = make_situation(rng, "post")
        traj, H, pings, taken = run(rng, ppl, CFG["4.2"])
        show.append(dict(traj=traj, pings=pings, taken=taken, people=[dict(base=p["base"], miss=p["miss"], decl=p["decl"]) for p in ppl]))
    out["show"] = show
    # statistical 2x2: weights x behaviour, 3000 situations (15000 people) each
    grid = {}
    for cfg in ("4.1", "4.2"):
        for beh in ("pre", "post"):
            f, tr, ps, sl = stats(cfg, beh, 3000, 7)
            low = sum(1 for x in f if x <= 0.2)/len(f)
            floor = sum(1 for x in f if x <= 0.0001)/len(f)
            high = sum(1 for x in f if x >= 0.8)/len(f)
            mid = 1-low-high
            lowshare = [p for x, p in zip(f, ps) if x <= 0.2]
            grid[f"{cfg}|{beh}"] = dict(final=f, takerate=tr, share=ps, low=low, floor=floor, high=high, mid=mid, sit_low=sl,
                                        low_pingshare=sum(lowshare)/len(lowshare) if lowshare else None)
    out["grid"] = grid
    json.dump(out, open(sys.argv[1], "w"))
    for k, v in grid.items():
        print(k, {a: (round(b, 3) if isinstance(b, float) else None) for a, b in v.items() if a not in ("final", "takerate", "share")})
