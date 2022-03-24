import csv

fileName = "C:\Code\Python\MalarenergiAI\Python\Data\Data_Sura_tvättad.csv"
writeFileName = "C:\Code\Python\MalarenergiAI\Python\Data\Data_Sura_torktumlad.csv"

with open(fileName, mode='r') as file:
    csvFile = csv.reader(file)

    with open(writeFileName, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in csvFile:
            if len(row) > 1:
                csvwriter.writerow(row)

# [0] - Datum
# [2] - Temperatur i Hallsta
# [-1] - Effekt
