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

    if 'type' in request.args:
        pokemon_types = request.args.get('type')
        pokemon_types = pokemon_types.split(",")
        
        boosted_pokemon_set = set()
        for pokemon_type in pokemon_types:
            for pokemon in pokemon_dict[pokemon_type]:
                boosted_pokemon_set.add(pokemon)
        
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
            
            pokemon_values["likelihood"] = min(pokemon.likelihood * scale_factor, 1.0)
            boosted_pokemon.append(pokemon_values)
        return jsonify(boosted_pokemon)
    else:
        return "An error occurred, invalid or no Pokemon types received.", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001", debug=True)