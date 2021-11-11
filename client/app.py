import geocoder
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    if 'lat' in request.args:
        return 'bulbasaur'
    else:
        return render_template('index.html')



def getLocation():
    myloc = geocoder.ip('me')

    lat = myloc.latlng[0]
    lon = myloc.latlng[1]
    print(myloc.latlng)

    response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid=xxxx")
    print(response.json())
