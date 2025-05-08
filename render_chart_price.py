import sys
sys.path.append('./deve_lib')  # permet d'accéder à ta librairie

from coingecko_template import afficher_prix

afficher_prix(token_id='render-token', currency='usd', days=30, color='blue')