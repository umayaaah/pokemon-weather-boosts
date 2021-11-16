'''imports:
    csv
'''
import csv

def weather_type(main,description):
    '''Gets the pokemon go recognised weather type from the weather api given weather name and description using the weather csv file
    
    Parameters:
    main: the main weather type
    description: the description of the weather
    
    Returns:
    weatherType: The pokemon go recognised weather type'''
    with open('weather.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1].lower()==main.lower() and row[2].lower() == description.lower():
                weatherType = row[3]
                return(weatherType)
        return(NullSession)