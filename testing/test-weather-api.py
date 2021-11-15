from dotenv import load_dotenv
import os
import requests
import timeit
import statistics

def testWeather(lat, lon):
    # load api key configuration
    load_dotenv()
    API_KEY = os.getenv("API_KEY")

    start = timeit.default_timer()
    
    # call weather api
    requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid={API_KEY}")
            
    # calculate weather api running time
    stop = timeit.default_timer()
    runtime = stop-start

    return runtime

def runTest():
    runtimes = []
    for x in range (5):
        runtime = testWeather(53.8336245, -1.7960657)
        runtimes.append(runtime)
        print(f'Test {x+1}: {runtime}')

    sd = statistics.stdev(runtimes)
    print(f'Standard Deviation: {sd}')

    average = sum(runtimes) / len(runtimes)
    print(f'Average: {average}')
    

runTest()