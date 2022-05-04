import pandas as pd

col_names = [
             'datum',
             'tid',
             'soltimmar',
             'kvalitet'
]

df = pd.read_csv("./Data/smhi_opendata_soltimmar.csv", names=col_names, delimiter=";", index_col ="datum")
df = df.iloc[10: , :]

col_names2 = [
             'år',
             'månad',
             'dag',
             'timme',
             'temp',
             'effekt',
             'vind'
]
df2 = pd.read_csv("./Data/Data_Hallsta_test.csv", names=col_names2, delimiter=";")

datapoints = []

for i in range(len(df2)):
    år = str(int(df2.iloc[i]['år']))
    månad = str(int(df2.iloc[i]['månad']))
    dag = str(int(df2.iloc[i]['dag']))
    timme = str(int(df2.iloc[i]['timme']))
    if (len(månad)<2):
        månad = '0'+månad
    if (len(dag)<2):
        dag = '0'+dag
    if (len(timme)<2):
        timme = '0'+timme
    timme += ':00:00'
    date = år+'-'+månad+'-'+dag
    for v in df.loc[date].values:
        if (v[0] == timme):
            datapoints.append(v[1])
        
print(len(datapoints))
df2['soltimmar'] = datapoints

df2.to_csv('./Data/Data_Hallsta_vikt.csv', index=False , sep=";", header=False)