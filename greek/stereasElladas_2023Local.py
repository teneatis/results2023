import urllib.request
from bs4 import BeautifulSoup as soup
#import requests
import re
import pandas as pd
#link = 'https://www.ewrc-results.com/results/84073-rally-stereas-elladas-2023/?s='
#startat, no_ss=423761, int(5)
#monte_23 = pd.DataFrame(columns=['Pos.', 'Pilote / Co-pilote', 'Voiture', '#', 'Temps', 'Écart'])

stereas23_stages = pd.read_csv('StereasElladas_SS.csv')

print(stereas23_stages.dtypes)

dataview = stereas23_stages.drop(['Vehicle','Pos.','infos'], axis=1)
dataview = dataview.fillna('-')
data_view2 = dataview.set_index(['No', 'Crew', 'GR','Cl','ss'], drop=True).unstack('ss')
data_view2 = data_view2.fillna('-')
data_view2.to_csv('Stereas2023_comp.csv')
print(data_view2)
