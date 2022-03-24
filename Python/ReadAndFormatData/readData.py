import csv;

fileName = "C:\Code\Python\MalarenergiAI\Python\Data\Data_Hallsta_tvättad.csv"
writeFileName = "Data_Hallsta_torktumlad.csv"

with open(fileName, mode='r') as file:
    csvFile = csv.reader(file)
 
    for lines in csvFile:
        print(lines)
    

