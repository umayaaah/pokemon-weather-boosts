# python3 
from pokemon_type import weather_pokemon_types
from weather_type import dataCleanUp,weather_type
from flask import Flask, request, jsonify

app = Flask(__name__)


#0.0.0.0:5000/weatherType?weathermain=a&weatherdesc=b
@app.route('/weatherType')
def get_pokemon_types():
    weather = request.args.get('main')
    description = request.args.get('description')
    # weather = dataCleanUp(LocationJson)
    weatherType = weather_type(weather,description)
    pokemonTypes = weather_pokemon_types(weatherType)
    return jsonify(pokemonTypes)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5002", debug=True)
