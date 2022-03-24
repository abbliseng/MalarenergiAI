import csv;

fileName = "C:\Code\Python\MalarenergiAI\Python\Data\Data_Hallsta_tvättad.csv"
writeFileName = "Data_Hallsta_torktumlad.csv"

with open(fileName, mode='r') as file:
    csvFile = csv.reader(file)
 
    with open(writeFileName, 'w') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        for lines in csvFile:
            csvwriter.writerow(lines) 
