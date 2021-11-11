import geocoder
import requests
from dotenv import load_dotenv
import os
import json
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
        data_cleanup = dataCleanUp(weather_response.content)
        main = data_cleanup[0]
        description = data_cleanup[1]
        weather_types_response = requests.get(f"http://127.0.0.1:5002/weatherType?main={main}&description={description}")
        
        weather_types = json.loads(weather_types_response.content)
        pokemon_type_param = ""
        for pokemon_type in weather_types:
            pokemon_type_param += f"type={pokemon_type}&"
        
        pokemon_type_param = pokemon_type_param[:-1]

        # call pokemon likelihood api
        likelihood_response = requests.get(f"http://127.0.0.1:5001/pokemon?{pokemon_type_param}")
        
        return likelihood_response.content
        # next: render the pokemons.html page with the above response

    else:
        return render_template('index.html')

def dataCleanUp(weather_response):
    data = json.loads(weather_response)
    return (data['current']['weather'][0]['main'],data['current']['weather'][0]['description'])


def getLocation():
    myloc = geocoder.ip('me')

    lat = myloc.latlng[0]
    lon = myloc.latlng[1]
    print(myloc.latlng)

    response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid=xxxx")
    print(response.json())
