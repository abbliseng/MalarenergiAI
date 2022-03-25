import csv

fileName = "C:\Development\AI\MalarenergiAI\Python\Data\Data_Hallsta_torktumlad.csv"
writeFileName = "C:\Development\AI\MalarenergiAI\Python\Data\Data_Hallsta_manglad.csv"

# with open(fileName, mode='r') as file:
#     csvFile = csv.reader(file)
#     columns = list(csvFile)


def calculate_hour(hour, day, month, year):

    hour, day, month, year = int(hour), int(day), int(month), int(year)
    totalHour = 0

    if month >= 1:
        totalHour += (day*24 + hour)
    if month >= 2:
        totalHour += ((31)*24)
    if month >= 3:
        if int(year % 4) == 0:
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

    return (totalHour)


rawData = csv.reader(open(fileName), delimiter=';')
newFile = csv.writer(open(writeFileName, "w", newline=''), delimiter=';')

for row in rawData:

    # for i in range(0, len(columns)):
    head, sep, tail = row[0].partition(' ')

    # delar upp år, månad och dag
    year, middle, dayMonth = head.partition('-')
    month, middle2, day = dayMonth.partition('-')

    # delar upp timme och minut
    hour, middle3, minSec = tail.partition(':')

    totalHour = calculate_hour(hour, day, month, year)
    row.append(totalHour)
    newFile.writerow(row)

# for i in range(0, len(columns)):
#     #delar upp basdatat
#     head, sep, tail = columns[i][0].partition(' ')

#     #delar upp år, månad och dag
#     year, middle, dayMonth = head.partition('-')
#     month, middle2, day = dayMonth.partition('-')

#     #delar upp timme och minut
#     hour, middle3, minSec = tail.partition(':')

    #print(calculate_hour (hour,day,month,year))

months = {
    "31": [1, 3, 5, 7, 8, 10, 12],
    "30": [4, 6, 9, 11]
}

try:
    while True:
        Y = int(input("Year: "))
        if Y >= 2016:
            break
        else:
            print("Enter a year equal to or greater than 2016.")
            continue

    while True:
        M = int(input("Month: "))
        if M > 12 or M <= 0:
            print("Enter a valid month from 1 to 12")
            continue
        else:
            break

    while True:
        D = int(input("Day: "))

        if D <= 0:
            print("A day's number can't be zero or less")
            continue
        if M in months["31"] and D > 31:
            print("Enter a number smaller than 31")
            continue
        if M in months["30"] and D > 30:
            print("Enter a number smaller than 30")
            continue
        if M == 2:
            if int(Y % 4) == 0 and D > 29:
                print("Enter a number smaller than 29")
                continue
            elif int(Y % 4) != 0 and D > 28:
                print("Enter a number smaller than 28")
                continue
            break
        else:
            break

    while True:
        H = int(input("Hour: "))
        if H < 0 or H > 23:
            print("Enter a value between 0 and 23.")
            continue
        else:
            break
except ValueError:
    print("Only numbers can be entered.")


print("Year: " + str(Y), "Month: " + str(M),
      "Day: " + str(D), "Hour: " + str(H))

print("Hour of the year: ", calculate_hour(H, D, M, Y))


#    print("Enter a valid integer of an existing date. Exampel: Year=2022, Month=03, Day=20, Hour=13. The hours are a inteval from 0 to 23")
