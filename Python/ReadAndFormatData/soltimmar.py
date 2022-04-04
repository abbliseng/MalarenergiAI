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
             'effekt'
]

df2 = pd.read_csv("./Data/Data_Hallsta_test.csv", names=col_names2, delimiter=";")
valid_dates = []
for i in range(len(df2)):
    day = str(int(df2.iloc[i]['dag']))
    ar = str(int(df2.iloc[i]['år']))
    manad = str(int(df2.iloc[i]['månad']))
    if len(day) <= 1:
        day = '0'+day
    if len(manad) <= 1:
        manad = '0'+manad
        
    date = ar+'-'+manad+'-'+day

    print(df.loc[date].values)

    #valid_dates.append(df.loc[date])
#print(valid_dates)

"""
start_index = 0
end_index = 0
for i in range(len(df)):
    if (i%1000 == 0):
        print("{0:.0%} complete.".format(i / len(df)))
        
    if (df.iloc[i]['datum'] == '2016-10-11' and df.iloc[i]['tid'] == '07:00:00'):
        start_index = i
    elif (df.iloc[i]['datum'] == '2019-02-27' and df.iloc[i]['tid'] == '23:00:00'):
        end_index = i

df = df.iloc[start_index:end_index , :]

print('Length :',end_index-start_index,':',len(df))
"""