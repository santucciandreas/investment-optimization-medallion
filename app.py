import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime

# ── PAGE CONFIG ───────────────────────────────────────────────
st.set_page_config(
    page_title="Investment Optimizer",
    page_icon="⬡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── DARK TECH CSS ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;900&family=Share+Tech+Mono&family=Rajdhani:wght@400;500;600;700&display=swap');

:root {
    --bg: #0D1117;
    --card: #0D1F2D;
    --cyan: #00E5FF;
    --teal: #00FFB3;
    --border: #1E3A4A;
    --text: #E0F7FA;
    --sub: #546E7A;
    --rojo: #FF1744;
    --verde: #00E676;
    --grid: #1A2E3B;
}

html, body, [class*="css"] {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'Rajdhani', sans-serif !important;
}

.stApp { background-color: var(--bg) !important; }

/* Header */
.header-title {
    font-family: 'Orbitron', monospace;
    font-size: 28px;
    font-weight: 900;
    color: var(--cyan);
    text-shadow: 0 0 30px rgba(0,229,255,0.5);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 4px;
}
.header-sub {
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
    color: var(--sub);
    letter-spacing: 2px;
    margin-bottom: 24px;
}

/* KPI Cards */
.kpi-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-top: 2px solid var(--cyan);
    border-radius: 4px;
    padding: 16px 20px;
    margin-bottom: 12px;
}
.kpi-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--sub);
    margin-bottom: 8px;
}
.kpi-value {
    font-family: 'Orbitron', monospace;
    font-size: 26px;
    font-weight: 700;
    color: var(--cyan);
    text-shadow: 0 0 16px rgba(0,229,255,0.4);
}
.kpi-value-red { color: var(--rojo) !important; text-shadow: 0 0 16px rgba(255,23,68,0.4) !important; }
.kpi-value-green { color: var(--verde) !important; text-shadow: 0 0 16px rgba(0,230,118,0.4) !important; }

/* Sector buttons */
.sector-btn {
    background: var(--card);
    border: 1px solid var(--border);
    color: var(--text);
    font-family: 'Share Tech Mono', monospace;
    font-size: 12px;
    letter-spacing: 1px;
    padding: 10px 16px;
    border-radius: 3px;
    cursor: pointer;
    transition: all 0.2s;
    width: 100%;
    margin-bottom: 8px;
    text-align: left;
}
.sector-btn:hover { border-color: var(--cyan); color: var(--cyan); }

/* Divider */
.divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 20px 0;
}

/* Buttons */
.stButton > button {
    background: transparent !important;
    border: 1px solid var(--cyan) !important;
    color: var(--cyan) !important;
    font-family: 'Share Tech Mono', monospace !important;
    letter-spacing: 2px !important;
    font-size: 13px !important;
    padding: 10px 28px !important;
    border-radius: 3px !important;
    text-transform: uppercase !important;
    transition: all 0.3s !important;
}
.stButton > button:hover {
    background: rgba(0,229,255,0.1) !important;
    box-shadow: 0 0 20px rgba(0,229,255,0.3) !important;
}

/* Multiselect & inputs */
.stMultiSelect > div, .stTextInput > div > div {
    background: var(--card) !important;
    border-color: var(--border) !important;
    color: var(--text) !important;
    font-family: 'Share Tech Mono', monospace !important;
}

/* Section title */
.section-title {
    font-family: 'Share Tech Mono', monospace;
    font-size: 12px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--cyan);
    border-bottom: 1px solid var(--border);
    padding-bottom: 8px;
    margin-bottom: 16px;
}

/* Weight table */
.weight-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 12px;
    border-bottom: 1px solid var(--grid);
    font-family: 'Share Tech Mono', monospace;
    font-size: 13px;
}
.weight-bar {
    height: 4px;
    background: linear-gradient(90deg, var(--cyan), var(--teal));
    border-radius: 2px;
    margin-top: 4px;
}
</style>
""", unsafe_allow_html=True)

# ── SECTORES PREDEFINIDOS ──────────────────────────────────────
SECTORES = {
    "⚡ Energía":          ['XOM', 'CVX', 'SLB', 'COP', 'EOG', 'PSX', 'MPC', 'VLO', 'OXY', 'BKR'],
    "💻 Tecnología":       ['AAPL', 'MSFT', 'GOOGL', 'NVDA', 'META', 'AMZN', 'AMD', 'AVGO', 'QCOM', 'INTC'],
    "🏦 Bancos":           ['JPM', 'BAC', 'WFC', 'GS', 'MS', 'C', 'BLK', 'AXP', 'USB', 'PNC'],
    "🏥 Salud":            ['JNJ', 'PFE', 'UNH', 'ABBV', 'MRK', 'LLY', 'TMO', 'ABT', 'DHR', 'BMY'],
    "🛒 Consumo / Retail": ['AMZN', 'WMT', 'COST', 'TGT', 'HD', 'LOW', 'NKE', 'MCD', 'SBUX', 'CMG'],
    "⛏️ Minería":          ['FCX', 'NEM', 'AA', 'CLF', 'MP', 'VALE', 'BHP', 'RIO', 'GOLD', 'WPM'],
}

C_BG    = "#0D1117"
C_CARD  = "#0D1F2D"
C_CARD2 = "#0A1929"
C_CYAN  = "#00E5FF"
C_TEAL  = "#00FFB3"
C_GRID  = "#1A2E3B"
C_TEXT  = "#E0F7FA"
C_SUB   = "#546E7A"
C_ROJO  = "#FF1744"
C_VERDE = "#00E676"

COLORES = ["#00E5FF","#00FFB3","#1DE9B6","#00BCD4","#0097A7","#26C6DA","#80DEEA","#4DD0E1","#B2EBF2","#E0F7FA"]

# ── FUNCIONES ──────────────────────────────────────────────────
@st.cache_data(show_spinner=False)
def descargar_datos(tickers_tuple):
    acciones = list(tickers_tuple)
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now().replace(year=datetime.now().year - 10)).strftime('%Y-%m-%d')
    raw = yf.download(acciones, start=start_date, end=end_date, progress=False)
    prices = raw['Close'].stack(future_stack=True).reset_index()
    prices.columns = ['date', 'ticker', 'adj_close']
    return prices

def calcular_retornos(df_prices):
    pivot = df_prices.pivot(index='date', columns='ticker', values='adj_close')
    pivot = pivot.dropna(axis=1, thresh=int(len(pivot)*0.8))
    retornos = pivot.pct_change().dropna()
    return retornos, pivot

def optimizar_montecarlo(retornos, n=5000):
    acciones = retornos.columns.tolist()
    ret_anuales = retornos.mean() * 252
    cov = retornos.cov() * 252
    resultados = np.zeros((3, n))
    pesos_lista = []
    for i in range(n):
        p = np.random.random(len(acciones))
        p /= p.sum()
        pesos_lista.append(p)
        r = np.dot(p, ret_anuales)
        v = np.sqrt(np.dot(p.T, np.dot(cov, p)))
        resultados[0,i] = r
        resultados[1,i] = v
        resultados[2,i] = r / v
    idx = np.argmax(resultados[2])
    return acciones, pesos_lista[idx], resultados, idx

@st.cache_data(show_spinner=False)
def descargar_spy():
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now().replace(year=datetime.now().year - 10)).strftime('%Y-%m-%d')
    spy = yf.download('SPY', start=start_date, end=end_date, progress=False)
    return spy['Close'].pct_change().dropna()

# ── HEADER ─────────────────────────────────────────────────────
st.markdown('<div class="header-title">⬡ Investment Optimizer</div>', unsafe_allow_html=True)
st.markdown('<div class="header-sub">// OPTIMIZACIÓN DE CARTERAS · MONTECARLO · YAHOO FINANCE · 10 AÑOS DE DATOS</div>', unsafe_allow_html=True)
st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── SELECTOR ───────────────────────────────────────────────────
st.markdown('<div class="section-title">▸ Seleccioná un sector o ingresá tus propias acciones</div>', unsafe_allow_html=True)

col_sect, col_custom = st.columns([1, 2])

with col_sect:
    sector_seleccionado = st.radio(
        "Sectores predefinidos",
        options=list(SECTORES.keys()),
        label_visibility="collapsed"
    )
    tickers_sector = SECTORES[sector_seleccionado]

with col_custom:
    st.markdown("**Ingresá tus propias acciones** (opcional — reemplaza la selección del sector)")
    tickers_input = st.text_input(
        "Ej: AAPL, MSFT, GOOGL, NVDA, META",
        placeholder="Ej: AAPL, MSFT, GOOGL, NVDA, META",
        label_visibility="collapsed"
    )
    if tickers_input:
        tickers_custom = [t.strip().upper() for t in tickers_input.split(',') if t.strip()]
    else:
        tickers_custom = []

    tickers_finales = tickers_custom if tickers_custom else tickers_sector
    st.markdown(f"**Acciones a analizar:** `{'  |  '.join(tickers_finales)}`")

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── MONTO E INVERSIÓN ──────────────────────────────────────────
st.markdown('<div class="section-title">▸ ¿Cuánto querés invertir?</div>', unsafe_allow_html=True)

MONEDAS = {
    "🇺🇸 USD — Dólar estadounidense": ("USD", "$"),
    "🇦🇷 ARS — Peso argentino":       ("ARS", "$"),
    "🇪🇺 EUR — Euro":                 ("EUR", "€"),
    "🇧🇷 BRL — Real brasileño":       ("BRL", "R$"),
    "🇨🇱 CLP — Peso chileno":         ("CLP", "$"),
    "🇲🇽 MXN — Peso mexicano":        ("MXN", "$"),
    "🇬🇧 GBP — Libra esterlina":      ("GBP", "£"),
}

col_m1, col_m2 = st.columns([1, 1])
with col_m1:
    moneda_seleccionada = st.selectbox(
        "Moneda",
        options=list(MONEDAS.keys()),
        label_visibility="collapsed"
    )
    moneda_code, moneda_simbolo = MONEDAS[moneda_seleccionada]

with col_m2:
    monto_usuario = st.number_input(
        f"Monto a invertir",
        min_value=100,
        max_value=100_000_000,
        value=10_000,
        step=100,
        label_visibility="collapsed"
    )
    st.markdown(f"<span style='font-family:Share Tech Mono; font-size:12px; color:#546E7A'>MONTO: {moneda_simbolo}{monto_usuario:,.0f} {moneda_code}</span>", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── BOTÓN OPTIMIZAR ────────────────────────────────────────────
col_btn = st.columns([1, 2, 1])
with col_btn[1]:
    correr = st.button("▶  OPTIMIZAR CARTERA", use_container_width=True)

# ── RESULTADOS ─────────────────────────────────────────────────
if correr:
    with st.spinner("Descargando datos de Yahoo Finance..."):
        df_prices = descargar_datos(tuple(tickers_finales))

    with st.spinner("Ejecutando simulación Montecarlo (5,000 carteras)..."):
        retornos, pivot = calcular_retornos(df_prices)
        tickers_ok, mejores_pesos, resultados, idx = optimizar_montecarlo(retornos)

    with st.spinner("Comparando contra S&P 500..."):
        spy_ret = descargar_spy()

    # ── Cálculos finales ──
    cap_ini = monto_usuario
    port_ret_diario = (retornos[tickers_ok] * mejores_pesos).sum(axis=1)
    crecimiento = cap_ini * (1 + port_ret_diario).cumprod()

    port_ret_df = port_ret_diario.to_frame('ret_port')
    port_ret_df.index = pd.to_datetime(port_ret_df.index)
    spy_df = spy_ret.copy()
    if isinstance(spy_df, pd.DataFrame):
        spy_df = spy_df.iloc[:, 0]
    spy_df = spy_df.to_frame('ret_spy')
    spy_df.index = pd.to_datetime(spy_df.index)

    df_comp = port_ret_df.merge(spy_df, left_index=True, right_index=True, how='inner')
    df_comp['port'] = cap_ini * (1 + df_comp['ret_port']).cumprod()
    df_comp['spy']  = cap_ini * (1 + df_comp['ret_spy']).cumprod()

    ret_port = ((df_comp['port'].iloc[-1] / cap_ini) - 1) * 100
    ret_spy  = ((df_comp['spy'].iloc[-1]  / cap_ini) - 1) * 100
    alpha    = ret_port - ret_spy
    picos    = crecimiento.cummax()
    max_dd   = ((crecimiento - picos) / picos).min() * 100
    sharpe   = resultados[2, idx]
    cap_final = df_comp['port'].iloc[-1]

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">▸ Resultados de la Optimización</div>', unsafe_allow_html=True)
    
    def formatear_capital(valor, simbolo):
        if valor >= 1_000_000_000:
            return f"{simbolo}{valor/1_000_000_000:.2f}B"
        elif valor >= 1_000_000:
            return f"{simbolo}{valor/1_000_000:.2f}M"
        elif valor >= 1_000:
            return f"{simbolo}{valor/1_000:.1f}K"
        else:
            return f"{simbolo}{valor:,.0f}"

        # ── KPIs ──
        k1, k2, k3, k4, k5 = st.columns(5)
   
        with k1:
            st.markdown(f"""<div class="kpi-card">
                <div class="kpi-label">// Capital Final</div>
                <div class="kpi-value">{formatear_capital(cap_final, moneda_simbolo)}</div>
            </div>""", unsafe_allow_html=True)
        with k2:
            color = "kpi-value-green" if ret_port > 0 else "kpi-value-red"
            st.markdown(f"""<div class="kpi-card">
                <div class="kpi-label">// Retorno Total</div>
                <div class="kpi-value {color}">{ret_port:.1f}%</div>
            </div>""", unsafe_allow_html=True)
        with k3:
            color_a = "kpi-value-green" if alpha > 0 else "kpi-value-red"
            st.markdown(f"""<div class="kpi-card">
                <div class="kpi-label">// Alpha vs S&P 500</div>
                <div class="kpi-value {color_a}">{alpha:+.1f}%</div>
            </div>""", unsafe_allow_html=True)
        with k4:
            color_dd = "kpi-value-red" if max_dd < -20 else "kpi-value-green"
            st.markdown(f"""<div class="kpi-card">
                <div class="kpi-label">// Max Drawdown</div>
                <div class="kpi-value {color_dd}">{max_dd:.1f}%</div>
            </div>""", unsafe_allow_html=True)
        with k5:
            st.markdown(f"""<div class="kpi-card">
                <div class="kpi-label">// Sharpe Ratio</div>
                <div class="kpi-value">{sharpe:.2f}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # ── GRÁFICOS ──
    col_g1, col_g2 = st.columns([2, 1])

    with col_g1:
        st.markdown('<div class="section-title">▸ Backtesting vs S&P 500</div>', unsafe_allow_html=True)
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(
            x=df_comp.index, y=df_comp['port'],
            name='Estrategia', mode='lines',
            line=dict(color=C_CYAN, width=2),
            fill='tozeroy', fillcolor='rgba(0,229,255,0.05)'
        ))
        fig1.add_trace(go.Scatter(
            x=df_comp.index, y=df_comp['spy'],
            name='S&P 500', mode='lines',
            line=dict(color=C_SUB, width=1.5, dash='dot')
        ))
        fig1.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color=C_TEXT, family='Share Tech Mono'),
            height=300, margin=dict(t=10, b=30, l=50, r=10),
            legend=dict(orientation='h', x=0, y=1.1, bgcolor='rgba(0,0,0,0)'),
            xaxis=dict(showgrid=True, gridcolor=C_GRID, zeroline=False),
            yaxis=dict(showgrid=True, gridcolor=C_GRID, zeroline=False, tickprefix='$'),
            hoverlabel=dict(bgcolor=C_CARD2, font_color=C_CYAN)
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col_g2:
        st.markdown('<div class="section-title">▸ Pesos Óptimos</div>', unsafe_allow_html=True)
        fig2 = go.Figure()
        fig2.add_trace(go.Pie(
            labels=tickers_ok,
            values=mejores_pesos,
            hole=0.45,
            marker=dict(colors=COLORES[:len(tickers_ok)], line=dict(color=C_BG, width=2)),
            textinfo='percent+label',
            textfont=dict(size=10, color='#FFFFFF'),
        ))
        fig2.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color=C_TEXT, family='Share Tech Mono'),
            height=300, margin=dict(t=10, b=10, l=10, r=10),
            showlegend=False
        )
        st.plotly_chart(fig2, use_container_width=True)

    # ── DRAWDOWN + TABLA ──
    col_g3, col_g4 = st.columns([2, 1])

    with col_g3:
        st.markdown('<div class="section-title">▸ Perfil de Riesgo — Drawdown Histórico</div>', unsafe_allow_html=True)
        drawdowns = ((crecimiento - crecimiento.cummax()) / crecimiento.cummax()) * 100
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(
            x=drawdowns.index, y=drawdowns,
            fill='tozeroy', fillcolor='rgba(255,23,68,0.2)',
            line=dict(color=C_ROJO, width=1),
            name='Drawdown'
        ))
        fig3.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color=C_TEXT, family='Share Tech Mono'),
            height=250, margin=dict(t=10, b=30, l=50, r=10),
            xaxis=dict(showgrid=True, gridcolor=C_GRID, zeroline=False),
            yaxis=dict(showgrid=True, gridcolor=C_GRID, zeroline=False, ticksuffix='%'),
            showlegend=False
        )
        st.plotly_chart(fig3, use_container_width=True)

    with col_g4:
        st.markdown('<div class="section-title">▸ Distribución de Pesos</div>', unsafe_allow_html=True)
        st.markdown(f"<span style='font-family:Share Tech Mono; font-size:11px; color:#546E7A'>BASE: {moneda_simbolo}{monto_usuario:,.0f} {moneda_code}</span>", unsafe_allow_html=True)
        df_pesos = pd.DataFrame({'Acción': tickers_ok, 'Peso': mejores_pesos})
        df_pesos = df_pesos.sort_values('Peso', ascending=False)
        for _, row in df_pesos.iterrows():
            pct = row['Peso'] * 100
            st.markdown(f"""
                <div class="weight-row">
                    <span style="color:{C_CYAN}; font-family:'Share Tech Mono'">{row['Acción']}</span>
                    <span style="color:{C_TEXT}">{pct:.1f}% — {moneda_simbolo}{monto_usuario * row['Peso']:,.0f}</span>
                </div>
                <div class="weight-bar" style="width:{pct}%"></div>
            """, unsafe_allow_html=True)

    # ── SCATTER MONTECARLO ──
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">▸ Frontera Eficiente — Simulación Montecarlo (5,000 carteras)</div>', unsafe_allow_html=True)
    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(
        x=resultados[1]*100, y=resultados[0]*100,
        mode='markers',
        marker=dict(
            size=3, color=resultados[2],
            colorscale=[[0, '#1E3A4A'], [0.5, '#00B8CC'], [1, '#00FFB3']],
            showscale=True,
            colorbar=dict(
                    title=dict(text='Sharpe', font=dict(color=C_TEXT)),
                    tickfont=dict(color=C_TEXT)
                )
        ),
        name='Portafolios', hovertemplate='Volatilidad: %{x:.1f}%<br>Retorno: %{y:.1f}%<extra></extra>'
    ))
    fig4.add_trace(go.Scatter(
        x=[resultados[1, idx]*100], y=[resultados[0, idx]*100],
        mode='markers',
        marker=dict(size=14, color=C_CYAN, symbol='star', line=dict(color='white', width=1)),
        name='Óptimo (Max Sharpe)'
    ))
    fig4.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color=C_TEXT, family='Share Tech Mono'),
        height=350, margin=dict(t=10, b=40, l=60, r=10),
        xaxis=dict(title='Volatilidad Anual (%)', showgrid=True, gridcolor=C_GRID, zeroline=False),
        yaxis=dict(title='Retorno Anual (%)', showgrid=True, gridcolor=C_GRID, zeroline=False),
        legend=dict(orientation='h', x=0, y=1.1, bgcolor='rgba(0,0,0,0)'),
        hoverlabel=dict(bgcolor=C_CARD2, font_color=C_CYAN)
    )
    st.plotly_chart(fig4, use_container_width=True)

    # ── FOOTER ──
    st.markdown(f"""
    <div style="font-family:'Share Tech Mono'; font-size:10px; color:{C_SUB}; text-align:center; 
    margin-top:20px; padding-top:12px; border-top:1px solid #1E3A4A; letter-spacing:1px;">
    // DATOS: YAHOO FINANCE · SIMULACIÓN: MONTECARLO 5,000 CARTERAS · {datetime.now().strftime('%d/%m/%Y')} · SOLO FINES EDUCATIVOS
    </div>
    """, unsafe_allow_html=True)
