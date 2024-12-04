
from flask import Flask, request, jsonify, render_template
from datetime import datetime
import pytz

app = Flask(__name__)
dynamic_routes = {}

def get_current_time(timezone):
    try:
        tz = pytz.timezone(timezone)
        city_time = datetime.now(tz).strftime("%H:%M")
        return city_time
    except Exception as e:
        return str(e)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/api/create", methods=["POST"])
def create_api():
    data = request.json
    city = data.get("city")
    timezone = data.get("timezone")

    if not city or not timezone:
        return jsonify({"error": "City and timezone are required"}), 400

    # Create a new route dynamically
    route = f"/api/time/{city.lower()}"
    if route not in dynamic_routes:
        dynamic_routes[route] = timezone

        # Create the dynamic route
        @app.route(route, methods=["GET"])
        def dynamic_time_route(route=route):
            city_timezone = dynamic_routes.get(route)
            time = get_current_time(city_timezone)
            return jsonify({"time": time})

    return jsonify({"message": f"API for {city} created at {route}"}), 201

# Export the app for Vercel
app = app
