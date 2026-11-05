# UCL 2026/27 League-Phase Portfolio

**Vivek Prasad Kaimal** · Accounting & finance professional · CPA Australia candidate

A season-long test of one idea: that historical data, structure and judgement can be turned into measurable, risk-managed decisions. Forecast locked **4 October 2026**, before Matchday 2. Every later change is visible in this repository's history.

> **Ground rule: we cannot predict football; we can only forecast it with probability.** Results change every matchday, there are too many teams, and their results are linked to each other, so no forecast is accurate enough to hold a bet to the end on conviction. Profits are taken when they appear.
>
> **This is trading, not long-term investing.** Like a futures contract, every bet has a fixed expiry, so targets are set when a bet is placed and the exit is taken at the target, whatever happens.

**Live tracker:** https://vivek-kaimal.github.io/Champions-League-Prediction-Notbettingadvice/

## Thesis

1. **Top 8 is unpredictable.** In each of the last two league phases, about three of the eight places went to teams nobody expected.
2. **Bottom 12 is mostly predictable,** apart from one to three overperformers.
3. **The edge is in the middle.** 9th–24th is 16 of 36 places. Predict the edges correctly and the middle falls into place.

## Method

- Selections only from the top five leagues and Portugal
- Inputs: Opta power and league rankings, match footage, form, injuries, squad depth, fixtures, home advantage, previous league phases
- Waited for Matchday 1 to finish before committing
- Forecast table updated every matchday; positions are reviewed whenever results stop agreeing with it
- **Rolling strategy (from MD2):** a multi-team bet is all-or-nothing, so one team failing loses the whole bet. Positions are cashed out once they are in profit and risk starts rising, then rebuilt after the matchday with the new information. Each matchday makes the table more certain, so every rebuild is made on better data.

## Portfolio

| | |
|---|---|
| Stake | **$8,000** |
| Realised profit | **+$1,848.16** (+23.1% on stake · 62% of target) |
| Portfolio value | **$9,848.16**, all in cash · no open bets (5 Nov) |
| Round 1 | $7,500 across 8 bets · **UCL bets cashed out 14 Oct, +$445.54** · **Benfica cashed out 24 Oct, +$763.30** |
| Round 2 | **$6,000 across 4 four-folds, placed 20 Oct** · 2 Stuttgart bets cashed out at stake 21 Oct · 2 open ($3,000), **cash-out value $4,539.67 on 22 Oct (+$1,539.67)** |
| Round 3 | **$3,500 across 4 trebles, placed 24 Oct**: Brugge/Dortmund/Shakhtar $1,000 · Villarreal/Sporting/PSV $1,000 · Atlético/Sporting/Stuttgart $750 · Napoli/Roma/Bodø $750 |
| Round 4 | 3 four-folds, 9 teams, $4,500 (27 Oct) · **all closed 4–5 Nov: +$639.32** (bet 9 +$698.53 · bet 12 +$15.79 · bet 20 −$75.00) |
| Target | **+$3,000 profit** (37.5% on stake) · floor: capital returned |
| Rules | **Take profit at +20%** · **pots of two teams from MD5** · capital first: cash out when in profit and risk rises, rebuild after each matchday |

Details: [portfolio.md](portfolio.md) · Proof: [evidence/](evidence/) · Forecast (updated 24 Oct): [forecast.md](forecast.md) · Weekly reports: [reports/](reports/)

## Results

| After | Bets won | Bets lost | Chance of profit* | Notes |
|---|---|---|---|---|
| MD1 | – | – | 37% | Portfolio opened 4 Oct |
| MD2 | – | – | – | **All 6 UCL bets cashed out 14 Oct: +$445.54 realised (+8.1% on $5,500).** Benfica ($2,000) still open |
| MD3 (Tue) | – | – | 36% | Round 2 rebuilt 20 Oct: 4 × $1,500 four-folds, 8 teams. Stuttgart 1–1 Atlético moves Stuttgart to 3rd (7 pts): both Stuttgart bets cashed out at stake 21 Oct |
| MD3 | – | – | – | Inter, Como, Club Brugge all won. Open bets valued at $4,539.67 on $3,000 staked (+51%) |
| UEL MD3 | – | – | – | **Benfica cashed out 24 Oct after 3 wins from 3: +$763.30 (+38%).** Realised to date: **+$1,208.84** |
| Pre-MD4 | – | – | – | Restructured 27 Oct to 3 four-folds on 9 teams ($4,500). If all three win: +$15,481.82 for the season |
| MD4 | – | – | – | **All bets closed 4–5 Nov: +$639.32.** Inter won 3–0, Como 9–1, Brugge 2–1, but Napoli lost 1–4 and Villarreal 0–6. Values had peaked on 22 Oct. Realised to date **+$1,848.16**, no capital lost. [Review](reports/md04.md) |

\*Stress test: 40,000 simulated seasons ([tools/update.py](tools/update.py)), built with Claude as a check on my own judgement.

---
Personal record for analytical purposes only. Not betting advice.
