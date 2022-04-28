import requests
from datetime import datetime

def get_temp(date):
    # Ifall användaren inte matat in ett korrekt datum tas bara dagens datum
    if len(date) != 10:
        print("ERR: Incorrect input format. Using today's date.")
        date = datetime.today().strftime('%Y-%m-%d')

    r = requests.get(
        'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/16.6001/lat/59.5972/data.json')

    
    # Rå data från SMHI:s API
    weatherData = r.json()
    # Antalet träffar på inmatade datumet
    availableHours = 0
    temp = []
    windSpeed = []
    # Lägger till temperatur och vindhastighet för alla timmar för det angivna datumet i två listor
    for item in weatherData["timeSeries"]:
        if (item["validTime"][0:10] == date):
            for row in item["parameters"]:
                if row["name"] == 't':
                    temp.append(row["values"][0])
                elif row["name"] == 'ws':
                    windSpeed.append(row["values"][0])
            availableHours += 1
    # Interface
    print('Found '+str(availableHours)+' available hours for '+date+'.')
    print('Temperatures: ')
    print(temp)
    print('Wind Speeds: ')
    print(windSpeed)

    return date


#Input och funktionen
date = input('Name a date (YYYY-MM-DD). Note that a few dates ahead of time provide less amount of hours predicted.\n >>> ')
get_temp(date)