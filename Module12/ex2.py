import requests

API_KEY = "abcdef1234567890abcdef1234567890"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        weather_desc = data["weather"][0]["description"]
        temp_celsius = data["main"]["temp"]

        print(f"\nWeather in {city_name}:")
        print(f"Condition: {weather_desc.capitalize()}")
        print(f"Temperature: {temp_celsius:.2f}°C")

    except requests.exceptions.HTTPError:
        print("City not found. Please check the name and try again.")
    except requests.exceptions.Timeout:
        print("The request timed out. Please try again later.")
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching weather data.")
        print(e)

if __name__ == "__main__":
    city = input("Enter the name of the city: ")
    get_weather(city)


