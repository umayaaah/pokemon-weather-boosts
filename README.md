This project contains 3 APIs

The external openWeather API takes the users latitude and longitude and returns the weather at the location
The pokemon API takes the weather and returns a list of pokemon types
The likelihood API takes the list of pokemon types and returns the boosted pokemon

# Pokemon API

## Install requirements

    pip install -r ./pokemon-type-api/requirements.txt

## Run the API

    cd pokemon-type-api
    flask run --port 5002 or python3 app.py

# Likelihood API

## Install requirements

    pip install -r ./likelihood-api/requirements.txt

## Run the API

    cd likelihood-api
    flask run --port 5001 or python3 app.py

# Client

## Install requirements

    pip install -r ./client/requirements.txt

## Run the app

    cd client
    flask run --port 5000 or python3 app.py

Run the webpage on Google Chrome using the URL http://127.0.0.1:5000

# Tests

## Install requirements

    pip install -r ./tests/requirements.txt

## Run tests

    cd testing
    python test-likelihood-api.py
    python test-pokemon-type-api.py
    python test-weather-api.py