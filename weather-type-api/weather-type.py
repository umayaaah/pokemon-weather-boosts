import csv
from flask import Flask
from flask import request

lat = 53.4442574
lon = -2.2529437
response = request.get(f"https://api.openweathermap.org/data/2.5/onecall?lat=53.4442574&lon=-2.2529437&exclude=minutely,hourly,daily,alerts&appid=")
print(response.json())

def dataCleanUp(ApiJson):
    return(0)

def weather_type(main,description):
    with open('weather-weather.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1]==main and row[2] == description:
                return(row[3])