import geocoder
import requests
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    if 'lat' in request.args and 'lon' in request.args:
        lat = request.args.get('lat')
        lon = request.args.get('lon')
        # call weather api
        weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid=b309d047959f93e82e4b58f1b67827c4")
        
        # call pokemon type api
        weather_types_response = ["Grass"]
        
        pokemon_type_param = ""
        for pokemon_type in weather_types_response:
            pokemon_type_param += f"type={pokemon_type}&"
        
        # call pokemon likelihood api
        likelihood_response = requests.get(f"http://127.0.0.1:5001/pokemon?{pokemon_type_param[:-1]}")
        
        # render the pokemons.html page with the above response
        return likelihood_response.content
    else:
        return render_template('index.html')


def getLocation():
    myloc = geocoder.ip('me')

    lat = myloc.latlng[0]
    lon = myloc.latlng[1]
    print(myloc.latlng)

    response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid=xxxx")
    print(response.json())
