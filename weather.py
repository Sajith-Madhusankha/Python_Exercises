# Get current weather information from OpenWeatherMap API
# Author: A.W.Sajith Madhusankha
# Date: 2023/06/13
    
# install requests module using -pip install requests
# Get your API key from https://openweathermap.org/api
# Replace YOUR_OPENWEATHERMAP_API_KEY with your API key in line 43
# Run the program and enter the location
# Example: Colombo, Sri Lanka

# Import requests module
import requests

# Function to get weather information
def get_weather(api_key, location):
    # API endpoint URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    # Send HTTP GET request to the API
    response = requests.get(url)

    # Check if the response is successful
    if response.status_code == 200:
        weather_data = response.json()

        # Extract relevant weather information from the response
        weather = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        # Display weather information
        print(f"Weather: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Failed to retrieve weather information.")

# Main function
def main():
    # OpenWeatherMap API key
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"

    # Get location from the user
    location = input("Enter the location: ")

    # Get weather information
    get_weather(api_key, location)

# Call main function
if __name__ == '__main__':
    main()
