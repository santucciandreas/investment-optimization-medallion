# investment-optimization-medallion
# 📊 Investment Optimization System — Medallion Architecture

> Quantitative investment pipeline using Medallion Architecture, Markowitz Portfolio Optimization and automated interactive dashboard.  
> **Backtesting result: +1,821% return vs +300% S&P 500 (10-year period)**

![Dashboard Preview](dashboard%20investment-optimization-medallion.JPG)

---

## 🏛️ Architecture Overview

```
Bronze Layer  →  Silver Layer  →  Gold Layer  →  Dashboard
(Raw Data)       (Clean Data)     (Strategy)      (Plotly HTML)
```

| Layer | Description |
|-------|-------------|
| 🥉 **Bronze** | Raw historical data ingested from yFinance API (10 years, 10 assets) |
| 🥈 **Silver** | Cleaned data + financial metrics calculated via SQL Window Functions |
| 🥇 **Gold** | Markowitz Optimization, Sharpe Ratio maximization, backtesting |
| 📊 **Dashboard** | Auto-generated interactive HTML dashboard (Plotly) |

---

## 📈 Results

| Metric | Value |
|--------|-------|
| 💰 Initial Capital | $10,000 USD |
| 💎 Final Capital | $192,025 USD |
| 📈 Strategy Return | +1,821% |
| 📉 S&P 500 Return | +300% |
| ⚡ Alpha Generated | +1,521% |
| 🛡️ Max Drawdown | -29.22% |
| ✖️ Strategy Multiplier | 19.2x |
| ✖️ S&P 500 Multiplier | 4.0x |

---

## 🗂️ Asset Selection

| Sector | Assets |
|--------|--------|
| Technology & Growth | Apple (AAPL), Microsoft (MSFT), Google (GOOGL), Nvidia (NVDA), Meta (META) |
| Finance | JPMorgan (JPM) |
| Energy | ExxonMobil (XOM) |
| Consumer & Disruption | Amazon (AMZN), Tesla (TSLA) |
| Safe Haven | Gold ETF (GLD) |

---

## 📊 Dashboard

The dashboard is automatically generated every time the code runs. It includes:

- **KPI Cards** — Final Capital, Max Drawdown, Strategy & S&P 500 Multipliers
- **Line Chart** — Strategy vs S&P 500 cumulative growth (year by year)
- **Bar Chart** — Profit generated per sector
- **Pie Chart** — Optimal portfolio allocation per asset

No additional setup needed — just run the notebook and the HTML is generated automatically.

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)

| Tool | Usage |
|------|-------|
| **Python** | Core language for data processing and quantitative modeling |
| **Pandas & NumPy** | Time series manipulation, returns and risk metrics |
| **SQL (SQLite)** | Structured storage and analytical queries |
| **yFinance API** | Automated historical market data ingestion |
| **SciPy** | Markowitz portfolio optimization |
| **Plotly** | Interactive dashboard generation |
| **Google Colab** | Cloud execution environment |

---

## 🚀 How to Run

1. Open the notebook in **Google Colab**
2. Mount your Google Drive when prompted
3. Run all cells in order (`Runtime → Run all`)
4. The dashboard will be generated automatically at the end

```python
# Output files generated automatically:
# ├── bi_kpis.csv
# ├── bi_pesos.csv
# ├── bi_historico_anual.csv
# ├── bi_rubros.csv
# └── dashboard.html  ← Interactive dashboard
```

---

## 💡 Key Concepts

**Markowitz Portfolio Optimization** — Mathematical framework that finds the optimal asset allocation by maximizing return for a given level of risk (Efficient Frontier).

**Sharpe Ratio** — Risk-adjusted return metric. A higher Sharpe means better return per unit of risk taken.

**Max Drawdown** — Maximum peak-to-trough decline. Measures portfolio resilience during market stress.

**Alpha** — Excess return generated above the benchmark (S&P 500). Confirms the strategy adds real value over passive investing.

---

## ⚠️ Disclaimer

> This project is for **educational purposes only**. Past performance does not guarantee future results. This is not financial advice.

---

*Built with Python · Data from Yahoo Finance · Architecture: Medallion (Bronze / Silver / Gold)*
