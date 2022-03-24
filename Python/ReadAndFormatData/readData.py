import csv

fileName = "C:\Development\AI\MalarenergiAI\Python\Data\Data_Hallsta_tvättad.csv"
writeFileName = "C:\Development\AI\MalarenergiAI\Python\Data\Data_Hallsta_torktumlad.csv"

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
