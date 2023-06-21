import requests

def get_weather_data(api_key, lat, lon):
    
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=es"
    response = requests.get(url)
    data = response.json()
    return data
