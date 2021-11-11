import csv

def dataCleanUp(ApiJson):
    return(ApiJson['current']['weather'][0]['main'],ApiJson['current']['weather'][0]['description'])

def weather_type(main,description):
    with open('weather-weather.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1]==main and row[2] == description:
                return(row[3])