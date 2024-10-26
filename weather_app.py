import requests
from flask import Flask, request, jsonify
import schedule
import time

app = Flask(__name__)

API_KEY = "your_api_key"
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return {
        "temp": data["main"]["temp"],
        "condition": data["weather"][0]["main"],
        "humidity": data["main"]["humidity"]
    }

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    data = fetch_weather(city)
    return jsonify(data)

def scheduled_fetch():
    for city in CITIES:
        fetch_weather(city)

# Schedule weather fetch every 5 minutes
schedule.every(5).minutes.do(scheduled_fetch)

if __name__ == '__main__':
    app.run(debug=True)
