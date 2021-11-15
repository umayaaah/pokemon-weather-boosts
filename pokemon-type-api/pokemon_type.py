'''import:
    csv 
'''
import csv

def weather_pokemon_types(weather):
    '''Gets the pokemon types which are boosted in the given weather and returns them as a list
    
    Parameters:
    weather:the boosted weather type
    
    Returns:
    pokemonTypes:A list of the boosted pokemon types
    '''
    with open('pokemon.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == weather:
                pokemonTypes=row[2].split(' ')
                return(pokemonTypes)
                