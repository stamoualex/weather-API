# Weather-API
A Python command-line tool that fetches real-time weather data for any city using the OpenWeatherMap API. Shows temperature, feels like, conditions, and humidity.
## Setup

1. Go to openweathermap.org and create a free account
2. After signing up, go to your profile → "My API Keys"
3. Copy your API key
4. Open `weather.py` and find this line near the top:
   api_key = "YOUR_API_KEY_HERE"
5. Replace YOUR_API_KEY_HERE with your actual key (keep the quotes)
6. Save the file

## How to Run

1. Make sure Python is installed (python.org)
2. Open your terminal and install the requests library:
   pip install requests
3. Download `weather.py` from this repo
4. Open a terminal in the folder where the file is saved
5. Run this command:
   python weather.py
6. Type any city name and hit Enter

## Example Output

City: Athens

Temperature: 28°C

Feels like: 31°C

Condition: clear sky

Humidity: 45%
