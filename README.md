# UCL 2026/27 League-Phase Portfolio

**Vivek Prasad Kaimal** · Accounting & finance professional · CPA Australia candidate

A season-long test of one idea: that historical data, structure and judgement can be turned into measurable, risk-managed decisions. Forecast locked **4 October 2026**, before Matchday 2. Every later change is visible in this repository's history.

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
| Staked | $7,500 across 8 bets · **UCL bets closed 14 Oct, +$445.54** |
| Target | **+$3,000 profit** (40%) · floor: capital returned |
| Rules | Max $1,000 per bet · max $2,000 per team |

Details: [portfolio.md](portfolio.md) · Proof: [evidence/](evidence/) · Forecast: [forecast.md](forecast.md) · Weekly reports: [reports/](reports/)

## Results

| After | Bets won | Bets lost | Chance of profit* | Notes |
|---|---|---|---|---|
| MD1 | – | – | 37% | Portfolio opened 4 Oct |
| MD2 (Tue) | – | – | – | **All 6 UCL bets cashed out 14 Oct: +$445.54 realised (+8.1% on $5,500).** Benfica ($2,000) still open |

\*Stress test: 40,000 simulated seasons ([tools/update.py](tools/update.py)), built with Claude as a check on my own judgement.

---
Personal record for analytical purposes only. Not betting advice.
