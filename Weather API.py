import requests

api_key = "YOUR_API_KEY_HERE"
city = input("What city's weather would you like to see? ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if data.get("cod") != 200:
    print("City not found or API error. Please try again.")
else:
    print(f"City: {data['name']}")
    print(f"Temperature: {round(data['main']['temp'])}°C")
    print(f"Feels like: {round(data['main']['feels_like'])}°C")
    print(f"Condition: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}%")