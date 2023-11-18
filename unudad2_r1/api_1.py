import requests

api_key = 'your_api_key'
location = '42'
url = f'https://api.tomorrow.io/v4/weather/forecast?location={location}'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("Current weather:")
    print(f" Temperature: {data['data']['timelines'][0]['intervals'][0]['values']['temperature']}°F")
    print(f" Wind Speed: {data['data']['timelines'][0]['intervals'][0]['values']['windSpeed']}mph")
    print(f" Wind Direction: {data['data']['timelines'][0]['intervals'][0]['values']['windDirection']}")
    print(f" Precipitation Probability: {data['data']['timelines'][0]['intervals'][0]['values']['precipitationProbability'] * 100}%")
    print(f" Weather Code: {data['data']['timelines'][0]['intervals'][0]['values']['weatherCode']}")
else:
    print(f"Error: {response.status_code}")