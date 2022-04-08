import csv

fileName = "./Data/Hallsta/Data_Hallsta_test.csv" #"C:\\Users\\s9sagsel\\Desktop\\Programmering\\MälarenergiAI\\Data_Hallsta_test.csv"

newFileName1 = "./Data/Data_Hallsta_2016-18.csv" #"C:\\Users\\s9sagsel\\Desktop\\Programmering\\MälarenergiAI\\Data_Hallsta_Kallt.csv"
newFileName2 = "./Data/Data_Hallsta_2018-19.csv" #"C:\\Users\\s9sagsel\\Desktop\\Programmering\\MälarenergiAI\\Data_Hallsta_Kallt.csv"
#newFileName3 = "./Data/Data_Hallsta_2018.csv" #"C:\\Users\\s9sagsel\\Desktop\\Programmering\\MälarenergiAI\\Data_Hallsta_Kallt.csv"
#newFileName4 = "./Data/Data_Hallsta_2019.csv" #"C:\\Users\\s9sagsel\\Desktop\\Programmering\\MälarenergiAI\\Data_Hallsta_Kallt.csv"


rawData = csv.reader(open(fileName), delimiter=';')
newFile1 = csv.writer(open(newFileName1, "w", newline=''), delimiter=';')
newFile2 = csv.writer(open(newFileName2, "w", newline=''), delimiter=';')
#newFile3 = csv.writer(open(newFileName3, "w", newline=''), delimiter=';')
#newFile4 = csv.writer(open(newFileName4, "w", newline=''), delimiter=';')
# newData = []

change_point = ["2018", "10", "23", "15"]
before = True

for row in rawData:
    if row[:4] == change_point:
        before = False
    if before:
        newFile1.writerow(row)
    else:
        newFile2.writerow(row)
    #print(row[:4])
    #if (row[0] == change_point[0] and row[1] == change_point[1] and )

    #if row[0] == "2018":
    #    newFile3.writerow(row)
    #elif row[0] == "2019":
    #    newFile4.writerow(row)

# newFile.writerow()