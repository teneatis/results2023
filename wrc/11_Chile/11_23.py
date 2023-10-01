import urllib.request
from bs4 import BeautifulSoup as soup
import requests
import re
import pandas as pd

link = 'https://rally-base.com/2023/rally-chile-2023/?ssId='
startat, no_ss=7872, int(16) # starting number of url, count of Special Stages
canceled = []

stages = [number for number in range(no_ss)]


rally_23 = []


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
    data = pd.read_html(page_html11)[1]
   
    data.columns = data.iloc[0]
    data = data[1:]
    data['ss']=ss+1
    #print(data.columns)
    
    equal = '-' in data['Pos.'].unique()
    if equal:
        data['Pos.'] = data['Pos.'].replace('-', method='ffill')
    
    data.to_csv('09_rally23_SS'+str(ss+1)+'.csv', index=False)

    rally_23.append(data)

rally2023_stages = pd.concat(rally_23, axis=0)
#rally2023_stages['Pos.'] = rally2023_stages['Pos.'].astype(str).astype(int)
rally2023_stages['No.'] = rally2023_stages['No.'].astype(str).astype(int)
rally2023_stages.to_csv('09_rally2023.csv', index=False)
rally2023_stages = rally2023_stages.fillna("-")
rally2023_temp=rally2023_stages.drop(['Group','SS time', 'Aver. speed sec/km', 'Diff.Leader Diff.Prev.'], axis=1)
rally2023_view = rally2023_temp.set_index(['No.','Driver / Co-driver Vehicle','ss'], drop=True).unstack('ss')

rally2023_temp2 = rally2023_temp[rally2023_temp['No.']<30]
rally2023_view2 = rally2023_temp2.set_index(['No.','Driver / Co-driver Vehicle','ss'], drop=True).unstack('ss')
rally2023_view = rally2023_view.fillna("-")

print(rally2023_view)
