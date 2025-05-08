import requests
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def afficher_prix(token_id, currency='usd', days=30, color='blue'):
    url = f"https://api.coingecko.com/api/v3/coins/{token_id}/market_chart"
    params = {
        'vs_currency': currency,
        'days': days
    }
    response = requests.get(url, params=params)
    data = response.json()

    prix = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
    prix['timestamp'] = pd.to_datetime(prix['timestamp'], unit='ms')

    fig, ax = plt.subplots()
    ax.plot(prix['timestamp'], prix['price'], color=color, label=f"{token_id.upper()} / {currency.upper()}")
    ax.set_title(f"Évolution du prix de {token_id.upper()} ({days} jours)")
    ax.set_xlabel("Date")
    ax.set_ylabel(f"Prix ({currency.upper()})")
    ax.legend()

    st.pyplot(fig)