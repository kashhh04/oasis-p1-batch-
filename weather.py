import requests

def get_weather_data(location):
    api_key = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # Use metric units for temperature in Celsius
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    return data

def display_weather(weather_data):
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]
    weather_description = weather_data["weather"][0]["description"]

    print("Weather Forecast")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Description: {weather_description.capitalize()}")

def main():
    print("Weather Forecast Application")
    location = input("Enter city name or zip code: ")

    weather_data = get_weather_data(location)

    if "main" in weather_data:
        display_weather(weather_data)
    else:
        print("Unable to retrieve weather data. Please check the location.")

if __name__ == "__main__":
    main()