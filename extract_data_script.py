import requests
import pandas as pd

# Ligar ao JSON

response = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=38.7416502&lon=-9.1923936&units=metric&exclude=minutely,current,daily,alerts&appid=46b4f2f0a971ca74c1934cd0108dbfdf')
jsondata = response.json()
jdata = jsondata['hourly']

weather = pd.DataFrame(jdata)

weather['dt'] = pd.to_datetime(weather['dt'].astype(int), unit='s')
weather['date'] = pd.to_datetime(weather['dt']).dt.date
weather['hour'] = pd.to_datetime(weather['dt']).dt.hour

# Get today date now to file name when export to csv or excel with encoding utf8
from datetime import datetime
weather.to_csv(datetime.now().strftime('data_sources/output/meteo-lisbon-%Y-%m-%d-%H-%M-%S.csv'), encoding='utf8', index=False)
