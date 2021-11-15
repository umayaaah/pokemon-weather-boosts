import requests
import timeit
import statistics

def testLikelihood(pokemon_type_param):
    start = timeit.default_timer()

    # call pokemon likelihood api
    likelihood_response = requests.get(f"http://127.0.0.1:5001/pokemon?type={pokemon_type_param}")

    # calculate the likelihood api running time
    stop = timeit.default_timer()
    runtime = stop-start

    return runtime

def runTest():
    runtimes = []
    for x in range (5):
        runtime = testLikelihood('Poison, Grass')
        runtimes.append(runtime)
        print(f'Test {x+1}: {runtime}')

    sd = statistics.stdev(runtimes)
    print(f'Standard Deviation: {sd}')

    average = sum(runtimes) / len(runtimes)
    print(f'Average: {average}')
    

runTest()