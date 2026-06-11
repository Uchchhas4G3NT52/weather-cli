import argparse
import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str, units: str = "metric") -> dict:
    """Fetch weather data for a given city from OpenWeatherMap."""
    if not API_KEY:
        print("Error: OPENWEATHER_API_KEY not set. Copy .env.example to .env and add your key.")
        sys.exit(1)

    params = {
        "q": city,
        "appid": API_KEY,
        "units": units,
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            print(f"City '{city}' not found. Please check the spelling.")
        elif response.status_code == 401:
            print("Invalid API key. Please check your OPENWEATHER_API_KEY in .env.")
        else:
            print(f"HTTP error {response.status_code}: {response.text}")
        sys.exit(1)

    except requests.exceptions.ConnectionError:
        print("Connection error. Please check your internet connection.")
        sys.exit(1)

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")
        sys.exit(1)


def display_weather(data: dict, units: str) -> None:
    """Print weather information in a readable format."""
    unit_symbol = "°C" if units == "metric" else "°F" if units == "imperial" else "K"
    speed_unit = "m/s" if units == "metric" else "mph"

    city        = data["name"]
    country     = data["sys"]["country"]
    description = data["weather"][0]["description"].capitalize()
    temp        = data["main"]["temp"]
    feels_like  = data["main"]["feels_like"]
    humidity    = data["main"]["humidity"]
    wind_speed  = data["wind"]["speed"]
    raw_vis     = data.get("visibility")
    visibility  = f"{raw_vis / 1000:.1f} km" if raw_vis is not None else "N/A"

    print("\n" + "=" * 42)
    print(f"  🌍  Weather in {city}, {country}")
    print("=" * 42)
    print(f"  🌤   Condition   :  {description}")
    print(f"  🌡   Temperature :  {temp}{unit_symbol}  (feels like {feels_like}{unit_symbol})")
    print(f"  💧   Humidity    :  {humidity}%")
    print(f"  💨   Wind Speed  :  {wind_speed} {speed_unit}")
    print(f"  👁   Visibility  :  {visibility}")
    print("=" * 42 + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="🌤  Weather CLI — real-time weather for any city.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "city",
        type=str,
        help="City name, e.g.  'London'  or  'New York'",
    )
    parser.add_argument(
        "--units",
        choices=["metric", "imperial", "standard"],
        default="metric",
        help=(
            "Unit system to use:\n"
            "  metric   → °C, m/s   (default)\n"
            "  imperial → °F, mph\n"
            "  standard → Kelvin"
        ),
    )

    args = parser.parse_args()
    data = get_weather(args.city, args.units)
    display_weather(data, args.units)


if __name__ == "__main__":
    main()
