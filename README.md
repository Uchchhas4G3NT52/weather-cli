# 🌤 Weather CLI

A beginner-friendly Python command-line app that fetches real-time weather for any city using the [OpenWeatherMap API](https://openweathermap.org/api).

## ✨ Features

- 🌍 Get current weather for **any city in the world**
- 🌡 Shows temperature, feels-like, humidity, wind speed, and visibility
- 🔄 Supports **metric** (°C), **imperial** (°F), and **standard** (Kelvin) units
- 🔐 API key stored safely in a `.env` file (never committed to Git)
- ⚠️ Clear, helpful error messages for bad input or connection issues

## 📦 Requirements

- Python 3.8+
- A free API key from [openweathermap.org](https://openweathermap.org/api)

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/weather-cli.git
cd weather-cli
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your API key

Copy the example env file and add your key:

```bash
cp .env.example .env
```

Open `.env` and replace `your_api_key_here` with your actual key:

```
OPENWEATHER_API_KEY=abc123yourkeyhere
```

> 💡 Get a free key at [openweathermap.org/api](https://openweathermap.org/api). The free tier is more than enough for this project.

## 🖥 Usage

```bash
# Basic usage — defaults to metric (°C)
python weather.py London

# Use imperial units (°F)
python weather.py "New York" --units imperial

# Use standard units (Kelvin)
python weather.py Tokyo --units standard
```

### Example Output

```
==========================================
  🌍  Weather in London, GB
==========================================
  🌤   Condition   :  Partly cloudy
  🌡   Temperature :  18.4°C  (feels like 17.1°C)
  💧   Humidity    :  72%
  💨   Wind Speed  :  4.2 m/s
  👁   Visibility  :  10.0 km
==========================================
```

## 📁 Project Structure

```
weather-cli/
├── weather.py        # Main script
├── requirements.txt  # Python dependencies
├── .env.example      # Template for your API key
├── .gitignore        # Keeps .env and cache out of Git
└── README.md         # This file
```

## 🛡 Security Note

Your `.env` file is listed in `.gitignore` and will **never** be pushed to GitHub. Always keep your API keys out of version control.

## 📚 What You'll Learn

Building this project teaches you:

- Making HTTP requests with the `requests` library
- Parsing JSON responses from a REST API
- Using `argparse` for command-line arguments
- Managing secrets with `python-dotenv`
- Structuring a clean, shareable Python project

## 📄 License

MIT — feel free to fork, modify, and share!
