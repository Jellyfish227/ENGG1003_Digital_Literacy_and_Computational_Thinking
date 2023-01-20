#!/usr/bin/env python3

# test interactively: exec(open("weather_to_bring_umbrella.py").read())

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

'''
Example demonstrating abstraction
Get HK Observatory Weather report using API
Source: https://data.gov.hk/en-data/dataset/hk-hko-rss-current-weather-report

Pilot test notes: escape "King's Park" and ignore &amp;
'''

# INPUT

HKO_weather_report_API = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en"

import urllib.request
apiURL = urllib.request.urlopen(HKO_weather_report_API)
data = apiURL.read()

import json
report = json.loads(data)

# PROCESS

print("Data extraction:")
print(*report.keys(), sep=", ")

print("Rainfall info:")
shatin_rainfall = -1
for record in report["rainfall"]["data"]:
    if record["place"] == "Sha Tin":
        print(record["max"], record["unit"], "at", record["place"])
        shatin_rainfall = record["max"]

print("UV index info:")
if report["uvindex"] == "":
    print("No UV Index record available!")
    uvindex = 0
else:
    uvindex = report["uvindex"]["data"][0]["value"]
    print(uvindex, "at", report["uvindex"]["data"][0]["place"])
    print("YYYY-MM-DD HH:MM:SS Time Zone (HKT)")
    print(report["updateTime"])

# OUTPUT

if shatin_rainfall > 2 or uvindex > 6:
    print("Bring an umbrella!")
else:
    print("Neither rainy nor shinny")

