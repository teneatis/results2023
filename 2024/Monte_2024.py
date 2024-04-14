import urllib.request
from bs4 import BeautifulSoup as soup
#import requests
import re
import pandas as pd
link = 'https://www.ewrc-results.com/results/84715-rallye-automobile-monte-carlo-2024/?s='
startat, no_ss=431142, int(17)
#monte_23 = pd.DataFrame(columns=['Pos.', 'Pilote / Co-pilote', 'Voiture', '#', 'Temps', 'Écart'])
rally_24 = []
overall = []
canceled = []

stages = [number for number in range(no_ss)]

if canceled:
    for j in canceled: stages.remove(j-1)


#for ss in range(0,(no_ss)):
for ss in stages:
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
    rally_24.append(data) 

    overall_24 = pd.read_html(page_html11)[1]
    overall_24.columns=['Pos.', 'No', 'Crew', 'Gr/Cl','ss_time', 'Diff', 'Speed']
    overall_24['ss']=ss+1
    equal = '=' in overall_24['Pos.'].unique()
    if equal:
        overall_24['Pos.'] = overall_24['Pos.'].replace('=', method='ffill')
        overall_24['Pos.'] = overall_24['Pos.'].astype(str).astype(float)
    #print(data.dtypes)
    #print(data)
    overall.append(overall_24)

rally2024_stages = pd.concat(rally_24, axis=0)
rally2024_stages.columns=['Pos.', 'No', 'Crew', 'Gr/Cl','ss_time', 'Diff', 'Speed', 'ss']
rally2024_stages['Pos.'] = rally2024_stages['Pos.'].astype(int)
rally2024_stages.to_csv('Rally2024_st.csv', index=False)
#print(rally2024_stages)
#print(rally2024_stages.dtypes)

dataview = rally2024_stages.drop(['Diff','Speed','Pos.'], axis=1)
dataview = dataview.fillna('-')
data_view2 = dataview.set_index(['No', 'Crew', 'Gr/Cl','ss'], drop=True).unstack('ss')
data_view2 = data_view2.fillna('-')
data_view2.to_csv('Rally2024_comp.csv')
#print(data_view2)

overall2024_stages = pd.concat(overall, axis=0)
overall2024_stages.columns=['Pos.', 'No', 'Crew', 'Gr/Cl','ss_time', 'Diff', 'Speed', 'ss']
#overall2024_stages['Pos.'] = overall2024_stages['Pos.'].astype(int)
overall2024_stages.to_csv('Rally2024_ov.csv', index=False)

dataview_overall = overall2024_stages.drop(['Diff','Speed','Pos.'], axis=1)
dataview_overall = dataview_overall.fillna('-')
dataview_overall = dataview_overall.set_index(['No', 'Crew', 'Gr/Cl','ss'], drop=True).unstack('ss')
dataview_overall = dataview_overall.fillna('-')
dataview_overall.to_csv('Rally2024_overall_comp.csv')
#print(data_view2)