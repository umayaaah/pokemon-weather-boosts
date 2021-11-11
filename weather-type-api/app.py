# python3 
from pokemon_type import weather_pokemon_types
from weather_type import dataCleanUp,weather_type
from flask import Flask, request, jsonify

app = Flask(__name__)


#0.0.0.0:5000/pokemon?type=a&type=b
@app.route('/weatherType')
def get_pokemon_types(LocationJson):
    weather = dataCleanUp(LocationJson)
    weatherType = weather_type(weather[0],weather[1])
    pokemonTypes = weather_pokemon_types(weatherType)
    return(pokemonTypes)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5002", debug=True)
