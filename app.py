import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Titre de la page
st.set_page_config(page_title="Évolution du prix RENDER", page_icon="📈", layout="wide")
st.title("📈 Évolution du prix de RENDER-TOKEN")
st.markdown("Données mises à jour sur les **30 derniers jours** via l’API CoinGecko.")

# Chargement des données
df = pd.read_csv("render_price_data_30d.csv")  # Assure-toi que ce fichier est bien dans le repo

# Affichage du graphique
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['Price'],
    mode='lines+markers',
    name='RENDER / USD',
    line=dict(color='blue')
))

fig.update_layout(
    title="Prix du token RENDER en USD",
    xaxis_title="Date",
    yaxis_title="Prix (USD)",
    template="plotly_dark",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)