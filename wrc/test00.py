season_url = "https://api.wrc.com/contel-page/83388/calendar/active-season/"
season2_url = 'https://www.wrc.com/en/results-standings/rally-results/rally-monte-carlo/results/'
import urllib.request
from bs4 import BeautifulSoup as soup

import requests
import re
import pandas as pd

req2 = urllib.request.Request(season2_url,  headers={'User-Agent': 'Mozilla/5.0'})
uClient12 = urllib.request.urlopen(req2)
page_html12 = uClient12.read()
uClient12.close()
print(page_html12)
data = pd.read_html(page_html12)[1]