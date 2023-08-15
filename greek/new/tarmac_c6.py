import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import glob

data =[]
files = []
for f in glob.glob('*_Stages_Times_Sec.csv'):
    files.append(f)
    temp_df = pd.read_csv(f)
    data.append(temp_df)
    print(f'Δημιουργήθηκε dataframe για το {f} με {temp_df.shape}')


total = pd.concat(data, axis=0)

total_ss_times_C6 = total[(total['Gr/Cl'].str.contains('C6')) & (total['surface'] == 'Tarmac')]
total_ss_times_C6

min_value = total_ss_times_C6.groupby(['Race', 'ss'])['time_SS_sec'].min()

min_value2 =  pd.DataFrame(min_value)

min_value2 = min_value2.rename(columns={'time_SS_sec' : 'min_time'})
min_value2

total_ss_times_F = total_ss_times_C6.merge(min_value2, on=['Race', 'ss'])
#total_ss_times_F['SS.'] = total_ss_times_F['Race'] + '_' +  total_ss_times_F['ss'].apply(lambda x: '{0:0>2}'.format(x))
total_ss_times_F['SS.'] = total_ss_times_F['ss'].apply(lambda x: '{0:0>2}'.format(x))
total_ss_times_F['Crew'] = total_ss_times_F['Crew'].str[:9]
#total_ss_times_F.to_csv('greek_rallies_2023_stages_times.csv', index=False)

total_ss_times_F['diff']=total_ss_times_F['time_SS_sec'] - total_ss_times_F['min_time']
total_ss_times_F['diff%']=(total_ss_times_F['time_SS_sec'] - total_ss_times_F['min_time'])/total_ss_times_F['min_time']*100
total_ss_times_F

total_ss_times_F4 = pd.pivot_table(total_ss_times_F, values='diff', 
                                index=['Race', 'SS.'], 
                                columns='Crew', dropna=True)


fig,ax = plt.subplots()
fig.set_size_inches(40,10)
#ax.set(xlabel='Time', ylabel='Value')
#ax.xaxis.label.set(fontsize=20, position=(0.9, 0))
#ax.yaxis.label.set(fontsize=15, position=(0, 0.9))
Heatmap_ALL = sns.heatmap(total_ss_times_F4, cmap='coolwarm')
#Heatmap_ALL.set_yticklabels(total_ss_times_WRC['Crew'], size = 15)
#plt.savefig("C6.jpg")
plt.title('Tarmac' +'\nDiference between C6 Participants and Stage winer (s)')
plt.show()

total_ss_times_F5 = pd.pivot_table(total_ss_times_F, values='diff', 
                                columns=['Race', 'SS.'], 
                                index='Crew', dropna=True)
total_ss_times_F6 = pd.pivot_table(total_ss_times_F, values='diff%', 
                                columns=['Race', 'SS.'], 
                                index='Crew', dropna=True)
total_ss_times_F6

fig,ax = plt.subplots()
fig.set_size_inches(20,10)
#ax.set(xlabel='Time', ylabel='Value')
#ax.xaxis.label.set(fontsize=20, position=(0.9, 0))
#ax.yaxis.label.set(fontsize=15, position=(0, 0.9))
Heatmap_ALL = sns.heatmap(total_ss_times_F5, cmap='coolwarm', cbar=False)
#Heatmap_ALL.set_yticklabels(total_ss_times_WRC['Crew'], size = 15)
#plt.savefig("C6_2.jpg")

fig.set_size_inches(20,10)
#ax.set(xlabel='Time', ylabel='Value')tarmac_c6.py
#ax.xaxis.label.set(fontsize=20, position=(0.9, 0))
#ax.yaxis.label.set(fontsize=15, position=(0, 0.9))
Heatmap_ALL_2 = sns.heatmap(total_ss_times_F6, annot=True, fmt=',.0f',cmap='coolwarm')
#Heatmap_ALL.set_yticklabels(total_ss_times_WRC['Crew'], size = 15)
plt.title('Tarmac' +'\nDiference between C6 Participants and Stage winer (%)')
plt.savefig("C6_Grave.jpg")
plt.show()