import urllib.request
from bs4 import BeautifulSoup as soup
#import requests
import re
import pandas as pd
link = 'https://www.ewrc-results.com/results/85679-rally-kritis-2023/?s='
startat, no_ss=440950, int(8)
#monte_23 = pd.DataFrame(columns=['Pos.', 'Pilote / Co-pilote', 'Voiture', '#', 'Temps', 'Écart'])
kritis_23 = []

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
    kritis_23.append(data) 


kritis23_stages = pd.concat(kritis_23, axis=0)
kritis23_stages.columns=['Pos.', 'No', 'Crew', 'Gr/Cl','ss_time', 'Diff', 'Speed', 'ss']
kritis23_stages['Pos.'] = kritis23_stages['Pos.'].astype(int)
kritis23_stages.to_csv('kritis2023_st.csv', index=False)
#print(kritis23_stages)
#print(kritis23_stages.dtypes)

dataview = kritis23_stages.drop(['Diff','Speed','Pos.'], axis=1)
dataview = dataview.fillna('-')
data_view2 = dataview.set_index(['No', 'Crew', 'Gr/Cl','ss'], drop=True).unstack('ss')
data_view2 = data_view2.fillna('-')
data_view2.to_csv('kritis2023_comp.csv')
#print(data_view2)
