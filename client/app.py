'''import modules:
    requests
    load_dotenv from dotenv
    os
    json
    Flask,render_template,request and jsonify from flask'''

import requests
from dotenv import load_dotenv
import os
import json
from flask import Flask, render_template, request, jsonify

'''load api key configuration'''
load_dotenv()
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

@app.route('/')
def index():
    """Gets the lat and lon of the users location when the click the button on the webpage.
        Uses this information to call the weather api and get the local weather.
        This is then converted to the pokemon go recognised weather types.
        Finally the pokemon with weather boosted odds are shown to the user. 

    Parameters:
    lat: Users latitude
    lon: Users longitude

    Returns:
    A webpage containing a table of all weather boosted pokemon and their stats.

   """
    if 'lat' in request.args and 'lon' in request.args:
        lat = request.args.get('lat')
        lon = request.args.get('lon')
        '''call weather api'''
        weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid={API_KEY}")
        '''get relevant data'''
        data_cleanup = dataCleanUp(weather_response.content)
        main = data_cleanup[0]
        description = data_cleanup[1]
        '''call pokemon type api'''
        weather_types_response = requests.get(f"http://127.0.0.1:5002/weatherType?main={main}&description={description}")
        weather_types = json.loads(weather_types_response.content)
        pokemon_type_param = ""
        '''get pokemon types'''
        for pokemon_type in weather_types:
            pokemon_type_param += f"type={pokemon_type}&"
        
        pokemon_type_param = pokemon_type_param[:-1]

        '''call pokemon likelihood api'''
        likelihood_response = requests.get(f"http://127.0.0.1:5001/pokemon?{pokemon_type_param}")
        
        return likelihood_response.content
        '''next: render the pokemons.html page with the above response'''

    else:
        return render_template('index.html')

def dataCleanUp(weather_response):
    '''Gets only the main weather type and the weather description from the given json
    
    Parameters:
    weather_response: the json given by the weather api
    
    Returns:
    main: the main weather type
    description: the weather description'''
    data = json.loads(weather_response)
    return (data['current']['weather'][0]['main'],data['current']['weather'][0]['description'])

