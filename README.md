# Weather Forecasting Using Python

This is a simple Python mini project that fetches real-time weather information of any city using the OpenWeatherMap API.

## Features
- Get real-time temperature
- Get humidity percentage
- Get current weather condition
- Easy-to-use command-line interface

## Technologies Used
- Python
- Requests library
- OpenWeatherMap API

## How It Works
1. The user is prompted to enter a city name.
2. The Python script sends a request to the OpenWeatherMap API.
3. The API responds with weather data in JSON format.
4. The script extracts and displays temperature, humidity, and weather conditions.

## Setup Instructions
1. Install Python on your system.
2. Install the `requests` library (if not already installed):

   ```
   pip install requests
   ```

3. Replace the placeholder API key in `main.py` with your **valid OpenWeatherMap API key**.

4. Run the script using:
   ```
   python main.py
   ```

## Code Example (main.py)
```python
import requests

# Your valid API key
API_KEY = "your_api_key_here"

# Ask user for city name
city = input("Enter city name: ")

# OpenWeatherMap URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# API Request
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Weather in {city}:")
    print(f"Temperature: {data['main']['temp']}Â°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Weather Condition: {data['weather'][0]['description']}")
else:
    print("City not found or API Error.")
```
### Note:
- The API key used in this project is for demonstration purposes only.
- You can generate your own free API key by signing up at: [https://openweathermap.org/api](https://openweathermap.org/api)
- Without a valid key, the project will show an API error.

 

## API Reference
- [OpenWeatherMap API](https://openweathermap.org/current)

## Author
- Pravalika Jogu
