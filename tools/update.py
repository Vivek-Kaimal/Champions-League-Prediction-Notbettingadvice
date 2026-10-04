"""
Weekly update for the UCL 2026/27 portfolio tracker.

Reads the files in data/, works out the current table, runs a stress test
(Monte Carlo simulation of the remaining matches) and writes data.js,
which the tracker page (index.html) reads.

Usage:  python3 tools/update.py
Weekly routine: enter the matchday's scores in data/fixtures.csv,
update bet statuses in data/portfolio.json, then run this script.
"""
import csv, json, math, datetime
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "data"
RUNS = 40_000
SEED = 2026

# ---------- load ----------
ratings = {r["team"]: float(r["rating"]) for r in csv.DictReader(open(D / "ratings.csv", encoding="utf-8"))}
rating_src = {r["team"]: r["source"] for r in csv.DictReader(open(D / "ratings.csv", encoding="utf-8"))}
fixtures = list(csv.DictReader(open(D / "fixtures.csv", encoding="utf-8")))
forecast = list(csv.DictReader(open(D / "forecast.csv", encoding="utf-8")))
pf = json.load(open(D / "portfolio.json", encoding="utf-8"))
history = json.load(open(D / "history.json", encoding="utf-8"))

teams = list(ratings)
idx = {t: i for i, t in enumerate(teams)}
T = len(teams)

played = [f for f in fixtures if f["home_goals"] != ""]
future = [f for f in fixtures if f["home_goals"] == ""]
last_md = max((int(f["matchday"]) for f in played), default=0)

# ---------- current table ----------
P = np.zeros(T); GD = np.zeros(T); GF = np.zeros(T)
W = np.zeros(T, int); Dr = np.zeros(T, int); L = np.zeros(T, int); PL = np.zeros(T, int)
for f in played:
    i, j, hg, ag = idx[f["home"]], idx[f["away"]], int(f["home_goals"]), int(f["away_goals"])
    PL[i] += 1; PL[j] += 1
    GF[i] += hg; GF[j] += ag; GD[i] += hg - ag; GD[j] += ag - hg
    if hg > ag: P[i] += 3; W[i] += 1; L[j] += 1
    elif hg < ag: P[j] += 3; W[j] += 1; L[i] += 1
    else: P[i] += 1; P[j] += 1; Dr[i] += 1; Dr[j] += 1

order = sorted(range(T), key=lambda k: (-P[k], -GD[k], -GF[k], teams[k]))
current = [dict(position=n + 1, team=teams[k], played=int(PL[k]), won=int(W[k]), drawn=int(Dr[k]),
                lost=int(L[k]), goal_diff=int(GD[k]), points=int(P[k])) for n, k in enumerate(order)]
cur_pos = {r["team"]: r["position"] for r in current}

# ---------- stress test ----------
# Each run: team strength = rating + random form noise; goals ~ Poisson.
rng = np.random.default_rng(SEED)
K, HOME, BASE, FORM_SD = 0.04, 0.10, 1.30, 1.5
H = np.array([idx[f["home"]] for f in future]); A = np.array([idx[f["away"]] for f in future])
rv = np.array([ratings[t] for t in teams])
pos = np.zeros((RUNS, T), int)
for s in range(RUNS):
    r = rv + rng.normal(0, FORM_SD, T)
    d = r[H] - r[A]
    hg = rng.poisson(BASE * np.exp(K * d + HOME)); ag = rng.poisson(BASE * np.exp(-K * d - HOME))
    pts, gd, gf = P.copy(), GD.copy(), GF.copy()
    np.add.at(gf, H, hg); np.add.at(gf, A, ag); np.add.at(gd, H, hg - ag); np.add.at(gd, A, ag - hg)
    np.add.at(pts, H, 3 * (hg > ag) + (hg == ag)); np.add.at(pts, A, 3 * (ag > hg) + (hg == ag))
    key = pts * 1e6 + gd * 1e3 + gf + rng.random(T)
    o = np.argsort(-key); p = np.empty(T, int); p[o] = np.arange(1, T + 1); pos[s] = p

band = (pos >= 9) & (pos <= 24)

# Benfica (Europa League): simple per-game model against the points target
b = pf["benfica"]
need = b["target_points"] - b["points"]; pw, pd = b["assumed_win"], b["assumed_draw"]; n = b["remaining"]
p_benfica = sum(math.comb(n, w) * math.comb(n - w, dd) * pw**w * pd**dd * (1 - pw - pd)**(n - w - dd)
                for w in range(n + 1) for dd in range(n + 1 - w) if 3 * w + dd >= need)
benfica_hit = rng.random(RUNS) < p_benfica

returns = np.zeros(RUNS)
bets_out = []
for bet in pf["bets"]:
    if bet["competition"] == "UCL":
        win = np.all([band[:, idx[t]] for t, _ in bet["legs"]], axis=0)
    else:
        win = benfica_hit
    if bet["status"] == "won": win = np.ones(RUNS, bool)
    if bet["status"] in ("lost", "cashed_out"): win = np.zeros(RUNS, bool)
    returns += win * bet["returns"] + (bet.get("cashout", 0) if bet["status"] == "cashed_out" else 0)
    odds = bet["returns"] / bet["stake"]
    bets_out.append(dict(bet, odds=round(odds, 2), implied=round(1 / odds, 3), chance=round(float(win.mean()), 3)))

staked = sum(bt["stake"] for bt in pf["bets"])
exposure = {}
for bt in pf["bets"]:
    for t, _ in bt["legs"]:
        exposure[t] = exposure.get(t, 0) + bt["stake"]

team_risk = []
for t in exposure:
    if t not in idx: continue
    k = idx[t]
    team_risk.append(dict(team=t, exposure=exposure[t], rating=ratings[t], rating_source=rating_src[t],
                          forecast=next(int(r["position"]) for r in forecast if r["team"] == t),
                          current=cur_pos[t], chance_band=round(float(band[:, k].mean()), 3),
                          top8=round(float((pos[:, k] <= 8).mean()), 3),
                          bottom12=round(float((pos[:, k] >= 25).mean()), 3)))
team_risk.sort(key=lambda r: r["chance_band"])

summary = dict(
    staked=staked, max_return=round(sum(bt["returns"] for bt in pf["bets"]), 2),
    target_profit=pf["target_profit"], expected_return=round(float(returns.mean()), 0),
    chance_profit=round(float((returns > staked).mean()), 3),
    chance_target=round(float((returns >= staked + pf["target_profit"]).mean()), 3),
    chance_total_loss=round(float((returns == 0).mean()), 3),
    median_return=round(float(np.median(returns)), 0),
    p10=round(float(np.percentile(returns, 10)), 0), p90=round(float(np.percentile(returns, 90)), 0),
    benfica_chance=round(p_benfica, 3),
)

today = datetime.date.today().isoformat()
history = [h for h in history if h["matchday"] != last_md]
history.append(dict(matchday=last_md, date=today, chance_profit=summary["chance_profit"],
                    expected_return=summary["expected_return"],
                    bets={str(bt["id"]): bt["chance"] for bt in bets_out}))
history.sort(key=lambda h: h["matchday"])
json.dump(history, open(D / "history.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)

out = dict(updated=today, last_matchday=last_md, runs=RUNS, summary=summary, bets=bets_out,
           teams=team_risk, current=current,
           forecast=[dict(position=int(r["position"]), team=r["team"], points=int(r["points"])) for r in forecast],
           rules=pf["rules"], cash_reserve=pf["cash_reserve"], history=history)
(ROOT / "data.js").write_text("window.DATA = " + json.dumps(out, ensure_ascii=False, indent=1) + ";\n", encoding="utf-8")
print(json.dumps(summary, indent=1))
for r in team_risk: print(r["team"], r["chance_band"], r["top8"], r["bottom12"], r["current"])
