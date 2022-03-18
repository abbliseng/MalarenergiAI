import requests

r = requests.get(
    'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/16.6001/lat/59.5972/data.json')

# Rå data från SMHI:s API
weatherData = r.json()

# Tom dictionary redo att fyllas med fin data
tempData = {}

# Itererar genom varje timme
for hour in weatherData["timeSeries"][0:25]:
    # Hämtar timtalet (14, 15, 16 etc.) för de kommande 24 timmarna
    time = hour["validTime"][11:13]
    for parameter in hour["parameters"]:
        # Hämtar temperaturen för aktuellt timtal
        if parameter["name"] == "t":
            # Lägger till timtal och tillhörande temperatur i dictionaryt
            tempData[time] = parameter["values"][0]


# print(tempData)

# for d in tempData:
#     print(d + ":", tempData[d])
#     print("")
