import csv

fileName = "C:\\Users\\s9sagsel\\Desktop\\Programmering\\MälarenergiAI\\Data_Hallsta_test.csv"
newFileName = "C:\\Users\\s9sagsel\\Desktop\\Programmering\\MälarenergiAI\\Data_Hallsta_Kallt.csv"


rawData = csv.reader(open(fileName), delimiter=';')
newFile = csv.writer(open(newFileName, "w", newline=''), delimiter=';')
# newData = []

for row in rawData:
    print(row[1])
    if row[1] == 1 or 2 or 3 or 11 or 12:
        # newData.append(row)
        newFile.writerow(row)

# newFile.writerow()