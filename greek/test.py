import pandas as pd
data = pd.read_csv('Livadia2023_st.csv')
data = data.fillna('-')

data['No'] = data['No'].replace('#','_',inplace=True)
print(data)
