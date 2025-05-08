import pandas as pd
import matplotlib.pyplot as plt
from pycoingecko import CoinGeckoAPI

def afficher_prix(token_id='ethereum', currency='usd', days=1, color='orange', save=False):
    """Affiche le graphique de prix d'un token sur N jours"""
    cg = CoinGeckoAPI()
    data = cg.get_coin_market_chart_by_id(id=token_id, vs_currency=currency, days=days)

    # Créer le DataFrame
    df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
    df['date'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Tracer
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['price'], label=f"{token_id.upper()} / {currency.upper()}", color=color)
    plt.title(f"Évolution du prix de {token_id.upper()} ({days} jour{'s' if days > 1 else ''})")
    plt.xlabel("Date")
    plt.ylabel(f"Prix ({currency.upper()})")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Sauvegarde optionnelle
    if save:
        filename = f"{token_id}_price_chart.png"
        plt.savefig(filename)
        print(f"[✓] Graphique sauvegardé dans : {filename}")

    plt.show()