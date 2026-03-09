# 🧪 Guía de Testing — Investment Optimizer

> Probá el sistema de optimización de carteras **sin instalar nada ni correr código**.

---

## 🚀 Acceder a la app
[![▶ Open App · Investment Optimizer](https://img.shields.io/badge/▶%20Open%20App%20·%20Investment%20Optimizer-00E5FF?style=for-the-badge&logo=streamlit&logoColor=white)](https://optimizador-inversiones-ugcj2punrczubgsdi2oeij.streamlit.app)

## ¿Cómo funciona?

El sistema descarga 10 años de datos reales de Yahoo Finance, calcula retornos diarios y corre una simulación de Montecarlo con 5,000 carteras para encontrar la **combinación óptima de acciones** que maximiza el Sharpe Ratio.

---

## ✏️ Cómo testearlo

### Opción 1 — Sectores predefinidos
1. Entrá a la app
2. Seleccioná un sector del panel izquierdo (Energía, Tecnología, Bancos, etc.)
3. Click en **▶ OPTIMIZAR CARTERA**
4. Esperá ~30 segundos mientras descarga los datos
5. Explorá los resultados

### Opción 2 — Tickers personalizados
1. Entrá a la app
2. En el campo de texto ingresá tus propios tickers separados por coma
3. Click en **▶ OPTIMIZAR CARTERA**

---

## 📋 Ejemplos para testear

### 💻 Tecnología
```
AAPL, MSFT, GOOGL, NVDA, META, AMZN, AMD, AVGO, QCOM, INTC
```

### 🏦 Bancos / Finanzas
```
JPM, BAC, WFC, GS, MS, C, BLK, AXP, USB, PNC
```

### ⚡ Energía
```
XOM, CVX, SLB, COP, EOG, PSX, MPC, VLO, OXY, BKR
```

### 🏥 Salud / Farmacéuticas
```
JNJ, PFE, UNH, ABBV, MRK, LLY, TMO, ABT, DHR, BMY
```

### 🛒 Consumo / Retail
```
AMZN, WMT, COST, TGT, HD, LOW, NKE, MCD, SBUX, CMG
```

### ⛏️ Minería / Materias Primas
```
FCX, NEM, AA, CLF, MP, VALE, BHP, RIO, GOLD, WPM
```

### 🌍 Cartera Diversificada Multi-Sector
```
AAPL, JPM, XOM, JNJ, WMT, NEM, MSFT, CVX, BAC, PFE
```

---

## 📊 Qué muestra la app

| Métrica | Descripción |
|--------|-------------|
| **Capital Final** | Valor de $10,000 USD invertidos hace 10 años |
| **Retorno Total** | Rendimiento acumulado de la estrategia |
| **Alpha vs S&P 500** | Ventaja (o desventaja) contra el mercado |
| **Max Drawdown** | Mayor caída histórica del portafolio |
| **Sharpe Ratio** | Retorno ajustado por riesgo |
| **Backtesting** | Curva histórica vs S&P 500 |
| **Pesos Óptimos** | Cuánto % invertir en cada acción |
| **Frontera Eficiente** | Mapa de las 5,000 carteras simuladas |

---

## ⚠️ Consideraciones

- Usá entre **8 y 12 tickers** para mejores resultados
- Evitá empresas **adquiridas o delistadas** — yfinance no devuelve datos completos
- Los resultados son **históricos** y no garantizan rendimientos futuros
- Solo con **fines educativos**

---

*Datos provistos por Yahoo Finance vía `yfinance`. Arquitectura Medallion (Bronze → Silver → Gold).*
