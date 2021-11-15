import pandas as pd
import numpy as np

class Pokemon():
    '''Class to represent pokemon
    
    Parameters: 
    name(str): the pokemon name
    score(int): the pokemon score
    likelihood(int): the likelihood of the pokemon spawning
    legendary(bool): whether or not the pokemon is a legendary'''
    def __init__(self, name, score, likelihood, legendary):
        self.name = name
        self.score = score
        self.likelihood = likelihood
        self.legendary = legendary

def get_pokemon_dict():
    '''This function takes the pokemon csv file containing the data about the pokemon
    and turns it into an array of pokemon
    
    Returns:
    pokemon_dict: an array containing all pokemon and information about them'''
    df = pd.read_csv("pokemon.csv")
    df = df[["Name", "Type 1", "Type 2", "Total", "Legendary"]]
    df["Likelihood"] = np.random.randint(1, 20, df.shape[0])/100

    pokemon_dict = {}

    for pokemon in df.values:
        poke = Pokemon(pokemon[0], pokemon[3], pokemon[5], pokemon[4])
        poke_type1 = pokemon[1]
        poke_type2 = pokemon[2]
        
        if poke_type1 not in pokemon_dict.keys():
            pokemon_dict[poke_type1] = []
        
        if poke_type2 != np.nan and poke_type2 not in pokemon_dict.keys():
            pokemon_dict[poke_type2] = []

        pokemon_dict[poke_type1].append(poke)
        
        if poke_type2 != np.nan:
            pokemon_dict[poke_type2].append(poke)

    return pokemon_dict