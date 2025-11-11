# 🌦️ Flask Weather Web App

A simple and responsive **Flask-based Weather Web Application** that fetches real-time weather data for any city using the **OpenWeather API**.  
Built with Python, Flask, and HTML/CSS for a clean, user-friendly experience.

---

## Features

- Search weather for any city in the world  
- Displays temperature, weather condition, and “feels like” temperature  
- Handles invalid city names gracefully  
- Built using Flask with `waitress` for production-ready serving  
- Styled using custom CSS  

---

## Project Structure
```
Flask-Weather-WebApp/
│
├── server.py # Main Flask server file
├── weather.py # Contains API request logic
├── requirements.txt # Python dependencies
├── .env # Contains your OpenWeather API key
│
├── static/
│ └── styles/
│     └── style.css # Styling for HTML templates
│
└── templates/
├── index.html # Home page with search form
├── weather.html # Weather result display
└── city-not-found.html # Error page for invalid cities
```


---

## Setup Instructions

### 1️. Clone the Repository
```bash
git clone https://github.com/LegendTejas/API-Crash-Course.git
cd API-Crash-Course/Flask/Projects/Flask-Weather-WebApp
```


### 2️. Create and Activate a Virtual Environment
```
python -m venv .venv
source .venv/bin/activate        # On Mac/Linux
.venv\Scripts\activate           # On Windows
```


### 3️. Install Dependencies
```
pip install -r requirements.txt
```


### 4️. Add Your OpenWeather API Key

Create a .env file in the root of the project and add:
```
API_KEY=your_openweather_api_key_here
```

### 5️. Run the Application
```
python server.py
```

or (for production)

```
waitress-serve --host=0.0.0.0 --port=8000 server:app
```

Then open your browser and go to: [loclahost:8000](http://127.0.0.1:8000)


---

## How It Works

- The user enters a city name in the search bar.

- The app sends a request to the OpenWeather API using weather.py.

- Flask renders the weather details dynamically in weather.html.

- Invalid cities redirect to city-not-found.html.


---

## Technologies Used
```
Python 3
Flask
Waitress
Requests
HTML / CSS
OpenWeather API
```
