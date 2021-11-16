from data import get_pokemon_dict
from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

pokemon_dict = get_pokemon_dict()

@app.route('/pokemon')
def weather_boosted_pokemon():
  """
  This is the Pokemon Likelihood API. Call this API with the pokemon types in the query parameters and get back a json object of all Pokemon of those weather types.
  ---
  tags:
    - Pokemon Likelihood API
  parameters:
    - name: type
      in: query
      required: true
      type: array
      items:
          type: string
      description: pokemon types which are weather boosted
  responses:
    500:
      description: An error occurred, invalid or no Pokemon types received.
    200:
      description: Pokemon that have the matched weather type from the query.
      schema:
        id: Pokemon
        properties:
          name:
            type: string
            description: The Pokemon name
          score:
            type: integer
            description: The CP score
          legendary:
            type: boolean
            description: A flag for legendary Pokemon
          likelihood:
            type: double
            description: The likelihood of seeing the Pokemon in the wild
  """

  try:
    # get the value of the parameter query key for type
    pokemon_types = request.args.get('type')
    pokemon_types = pokemon_types.split(",")
    
    # for every type passed in the query parameter, if it maps to the pokemon type
    # in the pokemon dictionary, then the pokemon object is added to a set
    boosted_pokemon_set = set()
    for pokemon_type in pokemon_types:
        for pokemon in pokemon_dict[pokemon_type.capitalize()]:
            boosted_pokemon_set.add(pokemon)
    
    # for every boosted pokemon, a dictionary is created of Pokemon objects with their
    # stats and the likelihood is calculated randomly where there is a higher chance if
    # it is not a legendary type
    boosted_pokemon = []
    for pokemon in boosted_pokemon_set:
        pokemon_values = {}
        
        pokemon_values["name"] = pokemon.name
        pokemon_values["score"] = pokemon.score
        pokemon_values["legendary"] = pokemon.legendary
        
        if pokemon.legendary:
            scale_factor = 1
        else:
            scale_factor = 2
        
        pokemon_values["likelihood"] = int(min(pokemon.likelihood * scale_factor, 1.0)*100)
        boosted_pokemon.append(pokemon_values)
    
    # return a marshalled json response of the pokemon dictionary
    return jsonify(boosted_pokemon)
  except:
    return "An error occurred, invalid or no Pokemon types received.", 500


if __name__ == "__main__":
  app.run(host="127.0.0.1", port="5001", debug=True)