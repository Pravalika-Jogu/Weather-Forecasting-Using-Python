import requests

# Your valid API key
API_KEY = "your_api_key_here"  # Replace with your valid API key

# Ask user for city name
city = input("Enter city name: ")

# Use the correct OpenWeatherMap URL for weather data
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Make the request to the OpenWeatherMap API
response = requests.get(url)

# Check if the response was successful
if response.status_code == 200:
    data = response.json()
    print(f"Weather in {city}:")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Weather Condition: {data['weather'][0]['description']}")
else:
    print("City not found or API Error.")
