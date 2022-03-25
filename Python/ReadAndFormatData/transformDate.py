import csv

fileName = "C:\Code\Python\MalarenergiAI\Python\Data\Data_Hallsta_torktumlad.csv"
writeFileName = "C:\Code\Python\MalarenergiAI\Python\Data\Data_Hallsta_manglad.csv"

with open(fileName, mode='r') as file:
    csvFile = csv.reader(file)
    columns = list(csvFile)

with open(writeFileName, mode='w', newline='') as wfile:

    for i in range(0, len(columns)):
            head, sep, tail = columns[i][0].partition(' ')
            
            #delar upp år, månad och dag 
            year, middle, dayMonth = head.partition('-')
            month, middle2, day = dayMonth.partition('-')

            #delar upp timme och minut
            hour, middle3, minSec = tail.partition(':')
            
            hour = int(hour)
            day = int(day)
            month = int(month)
            year = int(year)

            totalHour = 0


            if month >= 1:
                totalHour += (day*24 + hour) 

            if month >= 2 :
                totalHour += ((31)*24) 

            if month >= 3:
                if int(year%4) == 0:
                    totalHour += ((29)*24) 
                else:
                    totalHour += ((28)*24)
            
            if month >= 4:
                totalHour += ((31)*24)

            if month >= 5:
                totalHour += ((30)*24)

            if month >= 6:
                totalHour += ((31)*24) 

            if month >= 7:
                totalHour += ((30)*24) 

            if month >= 8:
                totalHour += ((31)*24)

            if month >= 9:
                totalHour += ((31)*24) 

            if month >= 10:
                totalHour += ((30)*24)

            if month >= 11:
                totalHour += ((31)*24)

            if month >= 12:
                totalHour += ((30)*24) 

            # print(totalHour)
            writer = csv.writer(wfile, delimiter=',')
            columns[i].append(totalHour)
            writer.writerow(columns[i])

                    #wfile.write(str(columns[i]))    
