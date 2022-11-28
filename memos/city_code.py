import requests, json, re

address = "前橋市" #市区町村名を入れる

url = "https://zutool.jp/api/getweatherpoint/"+address
response = requests.get(url)
response.raise_for_status()

response_data = response.json()
result_data = json.loads(response_data['result'])
if not result_data:
    print("Error")
else:
    city_code = result_data[0]['city_code']
    print(address + "のコード: " + city_code)
