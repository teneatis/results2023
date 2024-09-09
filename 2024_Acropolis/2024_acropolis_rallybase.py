import urllib.request
from bs4 import BeautifulSoup as soup
import requests
import re
import pandas as pd

link = 'https://rally-base.com/2024/eko-acropolis-rally-2024/?ssId='
startat, no_ss=8436, int(15) # starting number of url, count of Special Stages
canceled = []

stages = [number for number in range(no_ss)]


stages_24 = []
overall_24 = []

if canceled:
    for j in canceled: stages.remove(j-1)
#print(stages)

for ss in stages:
    val= startat + ss
    ss_a = str(val)
    my_url11 = link + ss_a
    #print(ss, val, ss_a, "\n", my_url11)
    
    req = urllib.request.Request(my_url11, headers={'User-Agent': 'Mozilla/5.0'})
    uClient11 = urllib.request.urlopen(req)
    page_html11 = uClient11.read()
    uClient11.close()
    data = pd.read_html(page_html11)[2]
   
    data.columns = ['Pos.', 'No', 'Prev_Pos.', 'Crew', 'Gr-Pos','time_and_pen', 'total_time', 'Diff']
    data = data[1:]
    data['ss']=ss+1

    overall = pd.read_html(page_html11)[2]
   
    overall.columns = overall.iloc[0]
    overall = overall[1:]
    overall['ss']=ss+1

    print(overall.columns)
    
    equal = '-' in data['Pos.'].unique()
    if equal:
        data['Pos.'] = data['Pos.'].replace('-', method='ffill')
    

    stages_24.append(data)
    overall_24.append(overall)

#rally stages Separately classification
rally2024_stages = pd.concat(stages_24, axis=0)
rally2024_stages['Pos.'] = rally2024_stages['Pos.'].astype(str).astype(int)
rally2024_stages['No'] = rally2024_stages['No'].astype(str).astype(int)
rally2024_stages[['Group', 'Group_Pos']] = rally2024_stages['Gr-Pos'].str.split(' ', expand=True)
rally2024_stages[['stages_time', 'Penalty']] = rally2024_stages['time_and_pen'].str.split(' ', expand=True)
rally2024_stages[['Diff_first', 'Diff_Prev']] = rally2024_stages['Diff'].str.split(' ', expand=True)
rally2024_stages.to_csv('rally2024_overallStages.csv', index=False)
'''
rally2024_stages = rally2024_stages.fillna("-")
rally_stages_time_temp=rally2024_stages.drop(['Aver. speed sec/km','Pos.', 'Diff.Leader Diff.Prev.'],axis=1)
rally_stages_position_temp=rally2024_stages.drop(['Aver. speed sec/km','SS time', 'Diff.Leader Diff.Prev.'],axis=1)
#prepare for export
rally2024_Positions_view = rally_stages_position_temp.set_index(['No.','Driver / Co-driver Vehicle','ss', 'Group'], drop=True).unstack('ss')
rally2024_times_view = rally_stages_time_temp.set_index(['No.','Driver / Co-driver Vehicle','ss', 'Group'], drop=True).unstack('ss')
#export
rally2024_times_view.to_csv('stageTimes.csv')
rally2024_Positions_view.to_csv('stagePositions.csv')


#rally overall clasification
rally2024_overall = pd.concat(overall_24, axis=0)
rally2024_overall['Pos.'] = rally2024_overall['Pos.'].astype(str).astype(int)
rally2024_overall['No.'] = rally2024_overall['No.'].astype(str).astype(int)
rally2024_overall.to_csv('rally2024_overall.csv', index=False)
rally2024_overall = rally2024_overall.fillna("-")
'''