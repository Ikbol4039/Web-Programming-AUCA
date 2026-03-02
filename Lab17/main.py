import requests
from flask import Flask, request, jsonify

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 5,
    "page": 1
}

response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    for coin in data:
        print(coin["name"], "-", coin["current_price"], "USD")
else:
    print("Failed to retrieve data")

app = Flask(__name__)
weather_data = {
    "London": {"temperature": 15, "condition": "Cloudy"},
    "New York": {"temperature": 20, "condition": "Sunny"},
    "Tokyo": {"temperature": 18, "condition": "Rainy"}
}

@app.route("/weather")
def get_weather():
    city = request.args.get("city")
    if city in weather_data:
        return jsonify(weather_data[city])
    else:
        return jsonify({"error": "City not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

api_url = "https://api.weatherapi.com/v1/current.json"
params = {
    "key": "YOUR_API_KEY",
    "q": "London"
}

response = requests.get(api_url, params=params)
if response.status_code == 200:
    weather = response.json()
    print("Temperature:", weather["current"]["temp_c"])
else:
    print("Error fetching weather data")

example_url = "https://www.example.com:8080/path/to/resource?query=python&sort=asc#section2"
print("Example URL:", example_url)