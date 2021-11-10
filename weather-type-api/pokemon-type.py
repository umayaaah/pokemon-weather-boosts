import csv

def weather_pokemon_types(weather):
    with open('weather.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == weather:
                return(row[2].strip(' '))



