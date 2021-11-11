import geocoder
import requests
from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, jsonify

# load api key configuration
load_dotenv()
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

@app.route('/')
def index():
    if 'lat' in request.args and 'lon' in request.args:
        lat = request.args.get('lat')
        lon = request.args.get('lon')
        # call weather api
        weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid={API_KEY}")
        
        # call pokemon type api
        weather_types_response = ["Grass", "Poison"]
        
        pokemon_type_param = ""
        for pokemon_type in weather_types_response:
            pokemon_type_param += f"type={pokemon_type}&"
        
        pokemon_type_param = pokemon_type_param[:-1]

        # call pokemon likelihood api
        likelihood_response = requests.get(f"http://127.0.0.1:5001/pokemon?{pokemon_type_param}")
        
        return likelihood_response.content
        # next: render the pokemons.html page with the above response

    else:
        return render_template('index.html')


def getLocation():
    myloc = geocoder.ip('me')

    lat = myloc.latlng[0]
    lon = myloc.latlng[1]
    print(myloc.latlng)

    response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid=xxxx")
    print(response.json())
