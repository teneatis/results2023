import urllib.request
from bs4 import BeautifulSoup as soup
import requests
import re
import pandas as pd
link = 'https://www.ewrc-results.com/results/77787-rallye-automobile-monte-carlo-2023/'
#monte_23 = pd.DataFrame(columns=['Pos.', 'Pilote / Co-pilote', 'Voiture', '#', 'Temps', 'Écart'])
monte_23 = []

my_url11 = link
req = urllib.request.Request(my_url11, headers={'User-Agent': 'Mozilla/5.0'})
uClient11 = urllib.request.urlopen(req)
page_html11 = uClient11.read()
uClient11.close()
data = pd.read_html(page_html11)[0]
data.head()