import requests, json, re

def get_point_id(address):
    url = "https://zutool.jp/api/getweatherpoint/"+address

    try:
        response = requests.get(url)
        response.raise_for_status()

    except requests.exceptions.RequestsException as e:
        print("HTTP Error: ", e)

    else:
        response_data = response.json()
        result_data = json.loads(response_data['result'])
        if not result_data:
            return None
        else:
            city_code = result_data[0]['city_code']
            return city_code

def get_weather_status(city_code):
    url = "https://zutool.jp/api/getweatherstatus/" + city_code

    try:
        response = requests.get(url)
        response.raise_for_status()

    except requests.exceptions.RequestsException as e:
        print("HTTP Error: ", e)

    else:
        response_data = response.json()
        return response_data

def get_pressure_status(city_code, date):
    pressure_level = [
        "🆗",
        "🆗",
        "⤵️",
        "⚠️",
        "💣"
    ]
    pressure_info = ""
    date_weather_status = get_weather_status(city_code)[date]
    for i in range(24):
        pressure_info = pressure_info + f"{i}時 : {date_weather_status[i]['pressure']} hPa, {pressure_level[int(date_weather_status[i]['pressure_level'])]}\n"
    return pressure_info