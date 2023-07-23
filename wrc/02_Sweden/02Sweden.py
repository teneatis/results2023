import urllib.request
from bs4 import BeautifulSoup as soup
import requests
import re
import pandas as pd

link = 'https://rally-base.com/2023/rally-sweden-2023/?ssId='
startat, no_ss=7337, int(18) # starting number of url, count of Special Stages

sweden_23 = []

for ss in range(0,(no_ss)):
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
    
    data.to_csv('02_sweden23_SS'+str(ss+1)+'.csv', index=False)

    sweden_23.append(data)

sweden2023_stages = pd.concat(sweden_23, axis=0)
#sweden2023_stages['Pos.'] = sweden2023_stages['Pos.'].astype(str).astype(int)
sweden2023_stages['No.'] = sweden2023_stages['No.'].astype(str).astype(int)
sweden2023_stages.to_csv('02_sweden2023.csv', index=False)

sweden2023_temp=sweden2023_stages.drop(['Group','SS time', 'Aver. speed sec/km', 'Diff.Leader Diff.Prev.'], axis=1)
sweden2023_view = sweden2023_temp.set_index(['No.','Driver / Co-driver Vehicle','ss'], drop=True).unstack('ss')

sweden2023_temp2 = sweden2023_temp[sweden2023_temp['No.']<30]
sweden2023_view2 = sweden2023_temp2.set_index(['No.','Driver / Co-driver Vehicle','ss'], drop=True).unstack('ss')
print(sweden2023_view)