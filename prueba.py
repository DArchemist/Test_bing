import requests

def testBing():
    url = "https://www.bing.com/news/search?q=alvaro+uribe+velez"
    success = 0
    error = 0

    for index in range(0, 100):
        response = requests.request("GET", url)
        if response.ok:
            success += 1
        else:
            error += 1
    return success, error


print(testBing())
