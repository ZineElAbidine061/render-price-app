import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# --- CONFIG ---
TOKEN_ID = 'render-token'
CURRENCY = 'usd'
DAYS = 30

# --- Titre ---
st.title("📈 Évolution du prix de RENDER-TOKEN")
st.markdown(f"**Données mises à jour sur les {DAYS} derniers jours via l’API CoinGecko.**")

# --- Requête API ---
url = f"https://api.coingecko.com/api/v3/coins/{TOKEN_ID}/market_chart"
params = {
    'vs_currency': CURRENCY,
    'days': DAYS
}
response = requests.get(url, params=params)
data = response.json()

# --- Traitement des données ---
prices = data['prices']
df = pd.DataFrame(prices, columns=['Timestamp', 'Price'])
df['Date'] = pd.to_datetime(df['Timestamp'], unit='ms')
df.set_index('Date', inplace=True)

# --- Affichage interactif ---
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df.index,
    y=df['Price'],
    mode='lines',
    name=f'{TOKEN_ID.upper()} / {CURRENCY.upper()}',
    line=dict(color='royalblue', width=2)
))
fig.update_layout(
    title=f"Évolution du prix de {TOKEN_ID.upper()} (sur {DAYS} jours)",
    xaxis_title='Date',
    yaxis_title=f"Prix ({CURRENCY.upper()})",
    template="plotly_dark",
    height=500
)

st.plotly_chart(fig, use_container_width=True)