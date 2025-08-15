import requests
from datetime import datetime

BASE_PRICE = 50  # INR per hour

def get_weather(city_lat=17.3850, city_lon=78.4867):
    """Fetch current weather condition using Open-Meteo (no API key)."""
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={city_lat}&longitude={city_lon}&current_weather=true"
        response = requests.get(url)
        data = response.json()
        weather_code = data["current_weather"]["weathercode"]

        # Weather code mapping for rain conditions
        rainy_codes = [51, 53, 55, 61, 63, 65, 80, 81, 82]
        if weather_code in rainy_codes:
            return "rain"
        return "clear"
    except:
        return "clear"

def calculate_dynamic_price(available_slots, city_lat=17.3850, city_lon=78.4867):
    """Calculate parking price based on time, weather, and availability."""
    price = BASE_PRICE

    # Weekend adjustment
    today = datetime.now().weekday()
    if today in [5, 6]:
        price *= 1.2

    # Peak hours adjustment
    current_hour = datetime.now().hour
    if (6 <= current_hour <= 9) or (18 <= current_hour <= 21):
        price *= 1.3

    # Availability adjustment
    if available_slots < 3:
        price *= 1.25

    # Weather adjustment
    weather = get_weather(city_lat, city_lon)
    if "rain" in weather:
        price *= 1.15

    return round(price, 2)
