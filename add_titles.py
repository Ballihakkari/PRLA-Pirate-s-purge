from urllib.request import urlopen
import json
def add_titles(path):
    # thetvdb.com api key:
    authentication = {
        "apikey": "BLUIPW4H20NNHI4Y",
        "userkey": "2LM7D5BLI62BQSZF",
        "username": "egilltorfakgm"
    }
    # print(authentication)
    auth = json.dumps(authentication)
    print(auth)
    responceToken = json.loads(urlopen('https://api.thetvdb.com/login={apikey":"BLUIPW4H20NNHI4Y","userkey":"2LM7D5BLI62BQSZF","username":"egilltorfakgm"}'))
    # print(responceToken)

    # for i in json.loads(urlopen("http://mooshak.ru.is/~python/names.json").read()):
    #     if i['Nafn'].startswith(start):
    #         c1 += int(i['Fjoldi1']) 
    #         c2 += int(i['Fjoldi2'])
    # return (c1, c2)

add_titles("")