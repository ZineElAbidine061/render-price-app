import sys
sys.path.append('./deve_lib')  # ou juste "." si tout est dans le même dossier

import streamlit as st
from coingecko_template import afficher_prix

st.set_page_config(page_title="Évolution RENDER-TOKEN", layout="wide")
st.title("📈 Évolution du prix de RENDER-TOKEN")

# Affiche le graphique depuis ta fonction perso
afficher_prix(token_id='render-token', currency='usd', days=30, color='blue')