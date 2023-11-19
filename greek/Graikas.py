import urllib.request
from bs4 import BeautifulSoup as soup
#import requests
import re
import pandas as pd
link = 'https://www.ewrc-results.com/results/85677-rally-sprint-graikas-2023/?s='
startat, no_ss=440947, int(3)
#monte_23 = pd.DataFrame(columns=['Pos.', 'Pilote / Co-pilote', 'Voiture', '#', 'Temps', 'Écart'])
graikas_23 = []

for ss in range(0,(no_ss)):
    val= startat + ss
    ss_a = str(val)
    my_url11 = link + ss_a
    #print(my_url11)
    req = urllib.request.Request(my_url11, headers={'User-Agent': 'Mozilla/5.0'})
    uClient11 = urllib.request.urlopen(req)
    page_html11 = uClient11.read()
    uClient11.close()
    data = pd.read_html(page_html11)[0]
    data.columns=['Pos.', 'No', 'Crew', 'Gr/Cl','ss_time', 'Diff', 'Speed']
    data['ss']=ss+1
    equal = '=' in data['Pos.'].unique()
    if equal:
        data['Pos.'] = data['Pos.'].replace('=', method='ffill')
        data['Pos.'] = data['Pos.'].astype(str).astype(float)
    #print(data.dtypes)
    #print(data)
    graikas_23.append(data) 


graikas23_stages = pd.concat(graikas_23, axis=0)
graikas23_stages.columns=['Pos.', 'No', 'Crew', 'Gr/Cl','ss_time', 'Diff', 'Speed', 'ss']
graikas23_stages['Pos.'] = graikas23_stages['Pos.'].astype(int)
graikas23_stages.to_csv('graikas2023_st.csv', index=False)
#print(graikas23_stages)
#print(graikas23_stages.dtypes)

dataview = graikas23_stages.drop(['Diff','Speed','Pos.'], axis=1)
dataview = dataview.fillna('-')
data_view2 = dataview.set_index(['No', 'Crew', 'Gr/Cl','ss'], drop=True).unstack('ss')
data_view2 = data_view2.fillna('-')
data_view2.to_csv('graikas2023_comp.csv')
#print(data_view2)
