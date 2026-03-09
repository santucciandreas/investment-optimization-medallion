# 🧪 Guía de Testing — Estrategia de Inversión por Rubro

> Probá el modelo con cualquier sector o conjunto de acciones cambiando **una sola línea de código**.

---

## 🚀 Cómo correr el proyecto

1. Abrí el apartado de "app optimizador de inversiones" 

2. Ejecutá **todas las celdas en orden** (`Runtime > Run all`)

3. Al finalizar se genera automáticamente el dashboard interactivo

---

## ✏️ Cómo testear con tu propio rubro

Buscá esta línea al inicio del notebook:

```python
# ✅ TOCÁS SOLO ESTO
tickers = ['XOM', 'CVX', 'SLB', 'COP', 'EOG', 'PSX', 'MPC', 'VLO', 'OXY', 'BKR']
```

Reemplazá los tickers con las acciones que quieras analizar y volvé a ejecutar todo.

---

## 📋 Ejemplos de rubros para testear

### 💻 Tecnología
```python
tickers = ['AAPL', 'MSFT', 'GOOGL', 'NVDA', 'META', 'AMZN', 'AMD', 'AVGO', 'QCOM', 'INTC']
```

### 🏦 Bancos / Finanzas
```python
tickers = ['JPM', 'BAC', 'WFC', 'GS', 'MS', 'C', 'BLK', 'AXP', 'USB', 'PNC']
```

### ⚡ Energía
```python
tickers = ['XOM', 'CVX', 'SLB', 'COP', 'EOG', 'PSX', 'MPC', 'VLO', 'OXY', 'BKR']
```

### 🏥 Salud / Farmacéuticas
```python
tickers = ['JNJ', 'PFE', 'UNH', 'ABBV', 'MRK', 'LLY', 'TMO', 'ABT', 'DHR', 'BMY']
```

### 🛒 Consumo / Retail
```python
tickers = ['AMZN', 'WMT', 'COST', 'TGT', 'HD', 'LOW', 'NKE', 'MCD', 'SBUX', 'CMG']
```

### ⛏️ Minería / Materias Primas
```python
tickers = ['FCX', 'NEM', 'AA', 'CLF', 'MP', 'VALE', 'BHP', 'RIO', 'GOLD', 'WPM']
```

---

## ⚠️ Consideraciones

- Usá entre **8 y 12 tickers** para mejores resultados en la optimización
- Evitá empresas **adquiridas o delistadas** (ej: PXD, HES) — yfinance no devuelve datos históricos completos
- Los **ETFs** (GLD, SLV, XLK, etc.) funcionan pero no tienen sector/industry automático
- El modelo descarga **10 años de datos históricos** — la primera ejecución puede tardar ~2 minutos

---

## 📊 Qué genera el modelo

| Output | Descripción |
|--------|-------------|
| **Matriz de correlación** | Qué tan relacionadas están las acciones entre sí |
| **Pesos óptimos** | Cuánto % invertir en cada acción (Máximo Sharpe Ratio) |
| **Backtesting** | Cómo hubiera rendido la estrategia en los últimos 10 años |
| **vs S&P 500** | Comparación contra el mercado general |
| **Dashboard** | Visualización interactiva exportada en HTML |

---

## 🗂️ Arquitectura del Proyecto

```
Bronze Layer  →  Descarga raw data de Yahoo Finance (10 años)
Silver Layer  →  Cálculo de retornos diarios + integración sectorial
Gold Layer    →  Optimización Montecarlo + Backtesting + Dashboard
```

---

*Datos provistos por Yahoo Finance vía `yfinance`. Solo con fines educativos.*
