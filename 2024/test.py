import urllib.request
from bs4 import BeautifulSoup as soup
#import requests
import re
import pandas as pd
link = 'https://www.ewrc-results.com/results/84715-rallye-automobile-monte-carlo-2024/?s='
startat, no_ss=431142, int(17)
#monte_23 = pd.DataFrame(columns=['Pos.', 'Pilote / Co-pilote', 'Voiture', '#', 'Temps', 'Écart'])
rally_24 = []
overall_24 = []
canceled = []

stages = [number for number in range(no_ss)]

for ss in stages:
    val= startat + ss
    ss_a = str(val)
    my_url11 = link + ss_a
    #print(my_url11)
    req = urllib.request.Request(my_url11, headers={'User-Agent': 'Mozilla/5.0'})
    uClient11 = urllib.request.urlopen(req)
    page_html11 = uClient11.read()
    uClient11.close()
    overall = pd.read_html(page_html11)[1]
    overall.columns=['Pos_change', 'No', 'Crew', 'Gr/Cl','time+pen', 'Diff', 'SpeedAndDiff']
    overall['ss']=ss+1
    
    data = pd.read_html(page_html11)[0]
    data.columns=['Pos.', 'No', 'Crew', 'Gr/Cl','ss_time', 'Diff', 'Speed']
    data['ss']=ss+1
    equal = '=' in data['Pos.'].unique()
    if equal:
        data['Pos.'] = data['Pos.'].replace('=', method='ffill')
        data['Pos.'] = data['Pos.'].astype(str).astype(float)
    
    rally_24.append(data)
    
    overall_24.append(overall) 

print(overall_24)

rally2024_overall = pd.concat(overall_24, axis=0)
rally2024_stage = pd.concat(rally_24, axis=0)

rally2024_overall.to_csv('test2_overall_test.csv')
rally2024_overall.to_csv('test2_stage_test.csv')
