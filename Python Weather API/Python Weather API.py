import requests

# Get the API key to access the weather data
api_key = open('API_KEY', 'r').read()

# Get the location from the user
location = input("Enter the your location: ")

# Get the weather data
result = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}")

# Get the weather description
desciption = result.json()['weather'][0]['description']

# Get the temperature
temp = result.json()['main']['temp']

# Get the high tempature
highTemp = result.json()['main']['temp_max']

# Get the low temperature
lowTemp = result.json()['main']['temp_min']

# Get the feels like temperature
feelsLike = result.json()['main']['feels_like']

# Get the cloud cover
clouds = result.json()['clouds']['all']

# Get the wind speed
wind = result.json()['wind']['speed']

# Get the humidity
humidity = result.json()['main']['humidity']

# Kelvin to Fahrenheit
temp = round((temp - 273.15) * 9/5 + 32, 2)
highTemp = round((highTemp - 273.15) * 9/5 + 32, 2)
lowTemp = round((lowTemp - 273.15) * 9/5 + 32, 2)
feelsLike = round((feelsLike - 273.15) * 9/5 + 32, 2)

# Print the weather data
print("The weather in", location, "is", desciption)
print("The current temperature is", temp, "and Today will be a low of", lowTemp, "and a high of", highTemp)
print("It currently feels like", feelsLike, "outside.")
print("The cloud cover is", clouds, "%.")
print("The wind speed is", wind, "mph.")
print("The humidity is", humidity, "%.")