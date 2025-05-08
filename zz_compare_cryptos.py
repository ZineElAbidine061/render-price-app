from deve_lib.coingecko_template import CoinGeckoAPI
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta 

# Config
tokens = [
    {'id': 'fetch-ai', 'label': 'FET', 'color': 'blue'},
    {'id': 'render-token', 'label': 'RENDER', 'color': 'orange'}
]
currency = 'usd'
days = 30

# Init API
cg = CoinGeckoAPI()

# Initialiser la figure et les axes
fig, ax1 = plt.subplots(figsize=(12, 6))

# Pour la courbe de variation en %
ax2 = ax1.twinx()

for token in tokens:
    data = cg.get_coin_market_chart_by_id(id=token['id'], vs_currency=currency, days=days)
    prices = pd.DataFrame(data['prices'], columns=['timestamp', 'price_usd'])
    prices['datetime'] = pd.to_datetime(prices['timestamp'], unit='ms')

    # Courbe du prix
    ax1.plot(prices['datetime'], prices['price_usd'],
             label=f"{token['label']} / USD", color=token['color'])

    # Annotation max
    max_price = prices['price_usd'].max()
    max_date = prices.loc[prices['price_usd'].idxmax(), 'datetime']
    ax1.annotate(f"Max: {max_price:.2f}", xy=(max_date, max_price),
                 xytext=(max_date, max_price + 0.3),
                 fontsize=9, color=token['color'],
                 arrowprops=dict(facecolor=token['color'], arrowstyle="->"))

    # Annotation min
    min_price = prices['price_usd'].min()
    min_date = prices.loc[prices['price_usd'].idxmin(), 'datetime']
    ax1.annotate(f"Min: {min_price:.2f}", xy=(min_date, min_price),
                 xytext=(min_date + timedelta(days=1), min_price + 0.10),
                 fontsize=9, color=token['color'],
                 arrowprops=dict(facecolor=token['color'], arrowstyle="->"))

    # Courbe de variation en %
    prices['variation_%'] = (prices['price_usd'] - prices['price_usd'].iloc[0]) / prices['price_usd'].iloc[0] * 100
    ax2.plot(prices['datetime'], prices['variation_%'],
             linestyle='--', linewidth=1, alpha=0.4,
             label=f"{token['label']} (%)", color=token['color'])

# Axes et styles
ax1.set_title("Comparaison des prix sur 30 jours : FETCH.AI vs RENDER", fontsize=14, fontweight='bold')
ax1.set_xlabel("Date (UTC)", fontsize=12)
ax1.set_ylabel("Prix (USD)", fontsize=12)
ax2.set_ylabel("Variation (%)", fontsize=12)
fig.autofmt_xdate()

ax1.grid(True)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.style.use('seaborn-v0_8-whitegrid')
plt.tight_layout()
plt.xticks(rotation=45)

# Sauvegarde + affichage
plt.savefig("comparison_fet_render_full.png", dpi=300)
for token in tokens:
    data = cg.get_coin_market_chart_by_id(id=token['id'], vs_currency=currency, days=days)
    df = pd.DataFrame(data['prices'], columns=['timestamp', 'price_usd'])
    df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')
    df['variation_%'] = (df['price_usd'] - df['price_usd'].iloc[0]) / df['price_usd'].iloc[0] * 100

    # Sauvegarde CSV
    filename = f"{token['label'].lower()}_price_data_{days}d.csv"
    df[['datetime', 'price_usd', 'variation_%']].to_csv(filename, index=False)
plt.show()