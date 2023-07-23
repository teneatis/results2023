import urllib.request
from bs4 import BeautifulSoup as soup
import requests
import re
import pandas as pd
import dataframe_image as dfi

participants = pd.read_csv('Fthiotidas2_Participants.csv', index_col=0)
participants = participants.fillna("-")
stagesTimes = pd.read_csv('Fthiotidas2_SS.csv', index_col=1)


stages = pd.merge(participants,stagesTimes, on="No")
stages = stages.sort_values(by=['SS','Time'])
#stagesTimes['cou']= stagesTimes.groupby(['SS', 'Gr']).cumcount()


stages['cou']= stages.groupby(['SS', 'Gr']).cumcount()+1
print(stages)

optionGr = ['C6']

C6_GR = stages[stages['Gr'].isin(optionGr)])
