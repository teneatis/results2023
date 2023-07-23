
import glob
import pandas as pd
data =[]
files = []
for f in glob.glob('monte23_SS*.csv'):
    files.append(f)
    temp_df = pd.read_csv(f)
    data.append(temp_df)
    print(f'Δημιουργήθηκε dataframe για το {f} με {temp_df.shape}')

total = pd.concat(data, axis=0)
print(total.shape)
print(total)
total.to_csv('monte2023_stages.csv')
total.to_excel('monte2023_stages_excel.xlsx')
