import csv
from flask.sessions import NullSession

def weather_pokemon_types(weather):
    '''Gets the pokemon types which are boosted in the given weather and returns them as a list
    
    Parameters:
    weather:the boosted weather type
    
    Returns:
    pokemonTypes:A list of the boosted pokemon types
    '''
    #opens the pokemon.csv file
    with open('pokemon.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            #if the weather is found within the file
            if row[1] == weather:
                pokemonTypes=row[2].split(' ')
                #return a list of pokemon types
                return(pokemonTypes)
        #if the weather is not found in the csv file throw an error
        return(NullSession)
                