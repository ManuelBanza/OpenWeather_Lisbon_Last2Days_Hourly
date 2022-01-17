import requests
import pandas as pd
import datetime
import time

# Definir data de ontem e dia antes de ontem

# Yesterday
yesterday = datetime.date.today() - datetime.timedelta(1)
unixtime_1d = str(int(time.mktime(yesterday.timetuple())))
# 2 days ago
before_yesterday = datetime.date.today() - datetime.timedelta(2)
unixtime_2d = str(int(time.mktime(before_yesterday.timetuple())))

# Ligar ao JSON

response = requests.get('https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=38.7167&lon=-9.1333&dt={}&units=metric&exclude=minutely,current,daily,alerts&appid=46b4f2f0a971ca74c1934cd0108dbfdf'.format(unixtime_1d))
jsondata = response.json()
jdata = jsondata['hourly']

weather_1d = pd.DataFrame(jdata)

weather_1d['dt'] = pd.to_datetime(weather_1d['dt'].astype(int), unit='s')
weather_1d['date'] = pd.to_datetime(weather_1d['dt']).dt.date
weather_1d['hour'] = pd.to_datetime(weather_1d['dt']).dt.hour


response = requests.get('https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=38.7167&lon=-9.1333&dt={}&units=metric&exclude=minutely,current,daily,alerts&appid=46b4f2f0a971ca74c1934cd0108dbfdf'.format(unixtime_2d))
jsondata = response.json()
jdata = jsondata['hourly']

weather_2d = pd.DataFrame(jdata)

weather_2d['dt'] = pd.to_datetime(weather_2d['dt'].astype(int), unit='s')
weather_2d['date'] = pd.to_datetime(weather_2d['dt']).dt.date
weather_2d['hour'] = pd.to_datetime(weather_2d['dt']).dt.hour

weather_last_2days = pd.concat([weather_2d, weather_1d])

# Get today date now to file name when export to csv or excel with encoding utf8
from datetime import datetime
weather_last_2days.to_csv(datetime.now().strftime('data_sources/output_last_2days/last-2days-meteo-lisbon-%Y-%m-%d-%H-%M-%S.csv'), encoding='utf8', index=False)