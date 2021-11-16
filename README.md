This project contains 3 APIs

The external openWeather API takes the users latitude and longitude and returns the weather at the location
The pokemon API takes the weather and returns a list of pokemon types
The likelihood API takes the list of pokemon types and returns the boosted pokemon

All of the APIs must be run using Python3 
# Pokemon API

## Install requirements

    pip3 install -r ./pokemon-type-api/requirements.txt

## Run the API

    cd ./pokemon-type-api
    flask run --port 5002 or python3 app.py -m flask run --port 5002

# Likelihood API

## Install requirements

    pip3 install -r ./likelihood-api/requirements.txt

## Run the API

    cd ./likelihood-api
    flask run --port 5001 or python3 app.py or python3 -m flask run --port 5001

# Client

## Install requirements

    pip3 install -r ./client/requirements.txt

## Run the app

    cd ./client
    flask run --port 5000 or python3 app.py or python3 -m flask run

Run the webpage on Google Chrome using the URL http://127.0.0.1:5000

# Tests

## Install requirements

    pip3 install -r ./tests/requirements.txt

## Run tests

    cd ./testing
    python test-likelihood-api.py
    python test-pokemon-type-api.py
    python test-weather-api.py