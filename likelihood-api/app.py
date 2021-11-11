# python3 
from data import get_pokemon_dict
from flask import Flask, request, jsonify

app = Flask(__name__)

pokemon_dict = get_pokemon_dict()

#0.0.0.0:5000/pokemon?type=a&type=b
@app.route('/pokemon')
def poke_dict():
    pokemon_types = request.args.getlist('type')
    #[a, b]
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
    #return jsonify([{'name': poke.name, 'score': poke.score, 'likelihood': poke.likelihood} for poke in pokemon_dict["Poison"]])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001", debug=True)
