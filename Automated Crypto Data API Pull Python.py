def api_runner():
    # official API pull Python script from CoinMarketCap

    from requests import Request, Session
    from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
    import json

    global data
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'20',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'd4c68391-6fd5-4542-a499-07d81a705582',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        #print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)




    import pandas as pd

    #converting json data into table for easier viewing
    df = pd.json_normalize(data['data'])
    df['timestamp'] = pd.to_datetime('now')

    #print(df)

    #create csv file 
    if not os.path.isfile(r"C:\Users\PC\Desktop\API_Test\API.csv"):
        df.to_csv(r"C:\Users\PC\Desktop\API_Test\API.csv", header='column_names')
    #append new data to existing file 
    else:
        df.to_csv(r"C:\Users\PC\Desktop\API_Test\API.csv", mode='a', header=False) 

   



import os 
from time import time 
from time import sleep 

#for loop for automated API pull in fixed interval, range 333 as that's the daily limit 
for i in range(333):
    api_runner()
    print('This API pull is successfully completed!')
    sleep(5)  #repeats every 30 seconds
exit()

