import csv
from flask.sessions import NullSession

def weather_type(main,description):
    '''Gets the pokemon go recognised weather type from the weather api given weather name and description using the weather csv file
    
    Parameters:
    main: the main weather type
    description: the description of the weather
    
    Returns:
    weatherType: The pokemon go recognised weather type'''
    #open the weather.csv file
    with open('weather.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            #if the file matches what was passed into the function
            if row[1].lower()==main.lower() and row[2].lower() == description.lower():
                weatherType = row[3]
                #return the pokemon go recognized weather type
                return(weatherType)
        #throw an error
        return(NullSession)