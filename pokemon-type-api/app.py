from pokemon_type import weather_pokemon_types
from weather_type import weather_type
from flask import Flask, request, jsonify

app = Flask(__name__)


#0.0.0.0:5000/pokemonType?weathermain=a&weatherdesc=b
@app.route('/pokemonType')
def get_pokemon_types():
    '''Gets the boosted pokemon types from the given weather
    
    Parameters:
    main: the main weather type
    description: the description of the weather
    
    Returns:
    pokemonTypes: A list of the boosted pokemon types'''
    try:
        #gets the main and weather description from the client
        weather = request.args.get('main')
        description = request.args.get('description')
        #runs function weather_type
        weatherType = weather_type(weather,description)
        #runs function weather_pokemon_types
        pokemonTypes = weather_pokemon_types(weatherType)
        #returns a list of pokemon types
        return jsonify(pokemonTypes)
    except:
        #if the weather type is not recognized will display this error message to the user
        return "Weather type not recognized",500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5002", debug=True)
