import pandas as pd
data = pd.read_csv('Livadia2023_st.csv')
data = data.fillna('-')

data['No'] = data['No'].str[1:]
data['No'] = data['No'].astype(str).astype(int)

dataview = data.drop(['Diff','Speed','Pos.'], axis=1)
dataview = dataview.fillna('-')

data_view2 = dataview.set_index(['No', 'Crew','Gr/Cl','ss'], drop=True).unstack('ss')
data_view2 = data_view2.fillna('-')
dataview2 = data_view2.sort_values(by=['No'])

#rally2023_temp=data.drop(['No', 'Diff','Speed','Gr/Cl','ss_time'], axis=1)
rally2023_temp=data.drop(['Diff','Speed','Gr/Cl','ss_time'], axis=1)
rally2023_temp['Pos.']=rally2023_temp['Pos.'].astype(int)

rally2023_view = rally2023_temp.set_index(['No', 'Crew','ss'], drop=True).unstack('ss')
rally2023_view=rally2023_view.fillna('-')
rally2023_view.to_csv('Livadia_2023_posit.csv')

