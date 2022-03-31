import csv

fileName = "C:\Code\Python\MalarenergiAI\Python\Data/vind_hastighet.csv"
writeFileName = "C:\Code\Python\MalarenergiAI\Python\Data/Testing.csv"

rawData = csv.reader(open(fileName), delimiter=';')
newFile = csv.writer(open(writeFileName, "w", newline=''), delimiter=';')
windlist = []
for row in rawData:
    windlist.append(row[-2])

rawData = csv.reader(open(fileName), delimiter=';')
print(windlist)
for i in  windlist:
    int(i)
    
    print(i)

# for row in rawData:
    # print("date: " + row[0] + ":" +row[1] +" wind: " + row[-2] + "m/s")
    
    #newFile.writerow(windlist)
    #print(wind)