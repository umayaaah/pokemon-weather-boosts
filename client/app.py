from dotenv import load_dotenv
import os
import requests
from flask import Flask, render_template, request

# load api key configuration
load_dotenv()
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)


@app.route('/')
def index():
    '''
    Gets the lat and lon of the user's location from the query parameter when the user clicks the button on the webpage.
    Uses this information to call the One Call API by OpenWeather to get the local weather.
    The response is used to call the pokemon-type API which converts this to the Pokemon Go recognised weather types.
    Finally the response for the pokemon-type API is put into a query paramter for the likelihood API where the
    Pokemons with weather boosted odds are shown to the user. 

    Returns:
    A webpage containing a table of all weather boosted pokemon and their stats.
    '''
    if 'lat' in request.args and 'lon' in request.args:
        lat = request.args.get('lat')
        lon = request.args.get('lon')

        # call weather api
        weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid={API_KEY}")

        # get relevant data from weather api json response
        data_cleanup = dataCleanUp(weather_response.json())
        main, description = data_cleanup[0], data_cleanup[1]

        # call pokemon type api
        pokemon_types_response = requests.get(f"http://127.0.0.1:5002/pokemonType?main={main}&description={description}")
        pokemon_types = pokemon_types_response.json()
        
        # get pokemon types and create the parameter string for the likelihood api call
        pokemon_type_param = ','.join((pokemon_type for pokemon_type in pokemon_types if pokemon_type is not None))
        
        # call pokemon likelihood api
        likelihood_response = requests.get(f"http://127.0.0.1:5001/pokemon?type={pokemon_type_param}")

        pokemon_type_string = ''
        x = 1
        for type in pokemon_types:
            pokemon_type_string += type
            if x == len(pokemon_types)-1:
                pokemon_type_string += ' and '
            elif x < len(pokemon_types):
                pokemon_type_string += ', '
            x += 1
        # render the pokemons page with the likelihood api json response
        return render_template('pokemons.html', pokemon_likelihoods=likelihood_response.json(), weather_main=main, weather_desc=description, pokemon_types=pokemon_type_string)

    else:
        # render home page
        return render_template('index.html')


def dataCleanUp(data):
    '''
    Gets only the main weather type and the weather description from the given json

    Parameters:
    data: the json object given in the weather api response

    Returns:
    main: the main weather type
    description: the weather description
    '''
    return (data['current']['weather'][0]['main'], data['current']['weather'][0]['description'])
