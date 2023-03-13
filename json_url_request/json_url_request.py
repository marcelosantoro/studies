

import json
import urllib.request

def get_json_data():
    urlData = "https://data.binance.com/api/v3/ticker/24hr"
    jsonOpened = urllib.request.urlopen(urlData)
    status_code = jsonOpened.getcode()
    data = jsonOpened.read()
    jsonObject = json.loads(data.decode('utf-8'))
    #print(jsonObject[0]["symbol"])
    #print(len(jsonObject))
    return jsonObject, status_code    

def extract_data(jsonObject):
    count = 0
    if len(jsonObject) > 0:
        for item in jsonObject:
            print(f"Symbol: "+item['symbol']+" | lastPrice: "+item['lastPrice'])
            count += 1
            if count == 10:
                break

if __name__ == "__main__":
    try:
        jsonObject, statusCode = get_json_data()
        print(f"StatusCode: {statusCode}")
        if statusCode == 200:
            extract_data(jsonObject)
        else:
            print(f"There was a problem in URL Request... statusCode: {statusCode}")
    except Exception as e:
        print(f"Something went wrong: {e}")
