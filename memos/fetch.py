import requests, json

city_code = '10201' #前橋市
url = "https://zutool.jp/api/getweatherstatus/" + city_code
resp = requests.get(url)

response_data = resp.json()

data = response_data['today']

pressure_level = [
    "🆗",
    "🆗",
    "⤵️",
    "⚠️",
    "💣"
    ]

pressure_info = ""
date_weather_status = data

for i in range(24):
    pressure_info = pressure_info + f"{i}時 : {date_weather_status[i]['pressure']} hPa, {pressure_level[int(date_weather_status[i]['pressure_level'])]}\n"

print(pressure_info)