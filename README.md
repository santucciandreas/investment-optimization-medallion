# ⬡ Optimización de Inversiones — Arquitectura Medallion

> Sistema cuantitativo de optimización de carteras que utiliza 10 años de datos reales del mercado para encontrar la estrategia de inversión óptima para cualquier sector o conjunto de acciones personalizado.

[![Investment Optimizer · Streamlit](https://img.shields.io/badge/▶%20Abrir%20App%20·%20Investment%20Optimizer-00E5FF?style=for-the-badge&logo=streamlit&logoColor=white)](https://optimizador-inversiones-ugcj2punrczubgsdi2oeij.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.10+-FFD700?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/Licencia-MIT-00FFB3?style=for-the-badge)](LICENSE)

---

## 🧪 Probá la App

No necesitás instalar nada. Entrá directamente a la app, seleccioná un sector o ingresá tus propias acciones, indicá el monto a invertir y obtené tu estrategia óptima en segundos.

📄 [Ver guía de testing completa](./TESTING_GUIDE.md)

---

## 🏗️ Arquitectura Medallion

El proyecto sigue una arquitectura de datos **Bronze → Silver → Gold**, transformando datos crudos del mercado en estrategias de inversión accionables.

```
📥 API Yahoo Finance
        │
        ▼
┌───────────────────┐
│   CAPA BRONZE     │  Datos OHLCV crudos · 10 años · Almacenamiento SQLite
│  bronze_market    │  Precios de cierre ajustados + volumen
│      _data        │  Formato largo · Todos los activos unificados
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│   CAPA SILVER     │  Cálculo de retornos diarios (función LAG)
│  silver_market    │  Volumen promedio móvil 10 días
│      _data        │  Integración sectorial via JOIN con Dim_Assets
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│    CAPA GOLD      │  Simulación de Montecarlo (5,000 carteras)
│  gold_final       │  Maximización del Sharpe Ratio
│    _metrics       │  Backtesting vs S&P 500 · Cálculo de Alpha
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│   APP STREAMLIT   │  Interfaz web interactiva
│ + Dashboard HTML  │  Experiencia sin código para el usuario
└───────────────────┘
```

---

## 🚀 Del Notebook a la App

El sistema evolucionó de un notebook de Google Colab a una **aplicación web completamente interactiva** accesible para cualquier usuario, sin necesidad de correr código.

| Versión | Descripción |
|---------|-------------|
| **Notebook** | Pipeline completo en Google Colab con capas SQL y dashboard HTML |
| **App Streamlit** | Interfaz para el usuario con selector de sectores, acciones personalizadas, selector de moneda y optimización en vivo |

---

## 📊 Dashboard Automático

El dashboard se genera automáticamente cada vez que se ejecuta el código. Incluye:

- **KPI Cards** — Capital Final, Max Drawdown, Multiplicadores de la Estrategia y del S&P 500
- **Gráfico de Líneas** — Crecimiento acumulado de la Estrategia vs S&P 500 (año a año)
- **Gráfico de Barras** — Ganancia generada por sector
- **Gráfico de Torta** — Distribución óptima del portafolio por activo

No se requiere configuración adicional — solo ejecutá el notebook y el HTML se genera automáticamente.

---

## 🛠️ Stack Tecnológico

| Herramienta | Uso |
|-------------|-----|
| **Python** | Lenguaje principal para procesamiento de datos y modelado cuantitativo |
| **Pandas & NumPy** | Manipulación de series de tiempo, retornos y métricas de riesgo |
| **SQL (SQLite)** | Almacenamiento estructurado y consultas analíticas |
| **yFinance API** | Ingesta automatizada de datos históricos del mercado |
| **Montecarlo** | Optimización de carteras mediante simulación aleatoria |
| **Plotly** | Generación de dashboards interactivos |
| **Streamlit** | Framework para la aplicación web |
| **Google Colab** | Entorno de ejecución en la nube |

---

## 📐 Conceptos Financieros Clave

**Optimización de Markowitz** — Marco matemático que encuentra la asignación óptima de activos maximizando el retorno para un nivel de riesgo dado (Frontera Eficiente).

**Sharpe Ratio** — Métrica de retorno ajustado por riesgo. Un Sharpe más alto significa mejor retorno por unidad de riesgo asumido.

**Max Drawdown** — Máxima caída desde un pico histórico. Mide la resiliencia del portafolio durante períodos de estrés del mercado.

**Alpha** — Retorno en exceso generado por encima del benchmark (S&P 500). Confirma que la estrategia agrega valor real frente a la inversión pasiva.

---

## 📁 Estructura del Proyecto

```
investment-optimization-medallion/
│
├── optimizadordeinversiones_usuario.ipynb   # Notebook con el pipeline completo
├── app.py                                   # Aplicación web Streamlit
├── requirements.txt                         # Dependencias de Python
├── TESTING_GUIDE.md                         # Cómo testear la app
└── README.md                                # Este archivo
```

---

## ⚠️ Aviso Legal

Los resultados están basados en datos históricos y no garantizan rendimientos futuros. Este proyecto es únicamente con **fines educativos** y no debe considerarse asesoramiento financiero.

---

*Datos provistos por Yahoo Finance vía `yfinance`. Construido con Python, Streamlit y ❤️*
