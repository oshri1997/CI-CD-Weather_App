from flask import Flask, render_template, request
import requests
import geopandas as gpd
from shapely.geometry import Point
from dotenv import load_dotenv
import os
from prometheus_client import Counter, Histogram, generate_latest

# Create a new Flask app
app = Flask(__name__)

# Load the environment variables from the .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
# Load the world map data
world = gpd.read_file("./countries_data/ne_110m_admin_0_countries.shp")

# Prometheus metrics
REQUEST_COUNT = Counter("request_count", "Total number of requests", ["endpoint"])
REQUEST_LATENCY = Histogram(
    "request_latency_seconds", "Latency of requests in seconds", ["endpoint"]
)
city_search_count = Counter(
    "city_search_count", "Number of times each city has been looked at", ["city"]
)


# Function to get the country name from the coordinates
def get_country_from_coordinates(lat, lon):
    point = Point(lon, lat)
    for _, country in world.iterrows():
        if country.geometry.contains(point):
            return country["ADMIN"]
    return "Not Found"


# Route to render the home page
@app.route("/")
def home():
    REQUEST_COUNT.labels(endpoint="/").inc()
    with REQUEST_LATENCY.labels(endpoint="/").time():
        return render_template("index.html", error=None)


# Route to handle the search request
@app.route("/search", methods=["GET"])
def search_weather():
    REQUEST_COUNT.labels(endpoint="/search").inc()
    with REQUEST_LATENCY.labels(endpoint="/search").time():
        cityname = request.args.get("query")
        city_search_count.labels(city=cityname).inc()
        weather_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{cityname}/next7days?unitGroup=metric&elements=datetime,tempmax,tempmin,humidity&include=days&key={API_KEY}&contentType=json"

        weather_response = requests.get(weather_url)
        if weather_response.status_code != 200:
            return render_template(
                "weather.html",
                error=f"Failed to fetch data for '{cityname}'. Please try again.",
                forecast=None,
            )

        weather_data = weather_response.json()

        lat = weather_data["latitude"]
        lon = weather_data["longitude"]
        country = get_country_from_coordinates(lat, lon)

        city_info = {
            "name": cityname,
            "country": country,
        }

        forecast = []
        for day in weather_data["days"][:7]:
            forecast.append(
                {
                    "datetime": day["datetime"],
                    "day_temp": day["tempmax"],
                    "night_temp": day["tempmin"],
                    "humidity": day["humidity"],
                }
            )
        return render_template(
            "weather.html", city_info=city_info, forecast=forecast, error=None
        )


@app.route("/metrics")
def metrics():
    return generate_latest()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
