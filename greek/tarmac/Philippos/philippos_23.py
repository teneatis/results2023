import pandas as pd

no_ss = 2

philippos_23 = []

for ss in range(0,(no_ss)):
    val= ss + 1
    ss_a = str(val)
    
    data = pd.read_csv('Philippos_S0'+ ss_a + '.csv')
    data.columns=['Pos.', 'No', 'F2','Crew', 'Gr/Cl','ss_time', 'Speed', 'meas']
    data['ss']=ss+1
    '''equal = '=' in data['Pos.'].unique()
    if equal:
        data['Pos.'] = data['Pos.'].replace('=', method='ffill')
        data['Pos.'] = data['Pos.'].astype(str).astype(float)
    
    print(data.dtypes)
    print(data)
    '''
    philippos_23.append(data) 


philippos23_stages = pd.concat(philippos_23, axis=0)
print(philippos23_stages)


philippos23_stages['Pos.'] = philippos23_stages['Pos.'].astype(int)
philippos23_stages.to_csv('philippos2023_st.csv', index=False)
#print(philippos23_stages)
#print(philippos23_stages.dtypes)

dataview = philippos23_stages.drop(['meas','Speed','Pos.'], axis=1)
dataview = dataview.fillna('-')
data_view2 = dataview.set_index(['No', 'Crew', 'Gr/Cl','ss'], drop=True).unstack('ss')
data_view2 = data_view2.fillna('-')
data_view2.to_csv('philippos2023_comp.csv')
#print(data_view2)
