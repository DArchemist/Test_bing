import requests

def testBing():
    url = "https://www.bing.com/news/search?q=alvaro+uribe+velez&qs=AS&form=QBNT&sp=2&pq=alvaro+&sk=AS1&sc=8-7&cvid=95C4011E11A74A3CAAB1E42EF92C26FF"
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
