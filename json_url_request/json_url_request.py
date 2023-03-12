

import json
import urllib.request

def get_json_data():
    urlData = "https://data.binance.com/api/v3/ticker/24hr"
    jsonOpened = urllib.request.urlopen(urlData)
    data = jsonOpened.read()
    jsonObject = json.loads(data.decode('utf-8'))
    #print(jsonObject[0]["symbol"])
    #print(len(jsonObject))
    return jsonObject    

def extract_data(jsonObject):
    if len(jsonObject) > 0:
        for item in jsonObject:
            print(f"Symbol: "+item['symbol']+" | lastPrice: "+item['lastPrice'])

if __name__ == "__main__":
    jsonObject = get_json_data()
    extract_data(jsonObject)

