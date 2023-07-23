import urllib.request
from bs4 import BeautifulSoup as soup
import requests
import re
import pandas as pd
link = 'aa.html'
#monte_23 = pd.DataFrame(columns=['Pos.', 'Pilote / Co-pilote', 'Voiture', '#', 'Temps', 'Écart'])
headers = []

page_html11 = soup(open(link, encoding="utf8"), "html.parser")

table = page_html11.find('table')


table = str(table)
table = re.sub(r'class.*"','', table)
table = re.sub(r'<br\/\>','', table)
table = re.sub(r'<img.*?>','', table)
table = re.sub(r'<a.*?>','', table)
table = re.sub(r'</a>.*^<','', table)
table = re.sub(r'\n','', table)
table = soup(table, "html.parser")


#result = table.prettify().splitlines()
#print('\n'.join(result[:70] ))

for i in table.find_all('tr')[0]:
    title = i.text
    headers.append(title)

#print(headers)
monte_2023 = pd.DataFrame(columns=headers)


for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(monte_2023)
    monte_2023.loc[length]=row

monte_2023_temp=monte_2023.drop(['Διαφ. πρώτ.Διαφ. προηγ.','Οδηγός / ΣυνοδηγόςΑυτοκίνητο',
'Μέση ταχύτηταδλ/χλμ',], axis=1)

m22 = pd.read_html(table.prettify())
print(monte_2023_temp)

print(m22)