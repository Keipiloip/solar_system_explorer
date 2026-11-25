
from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("SOLAR_SYSTEM_API_KEY")

URL = "https://api.le-systeme-solaire.net/rest/bodies/"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Start Flask
app = Flask(__name__)


# Home page
@app.route("/")
def index():
    return render_template("index.html")


# Planet details page
@app.route("/planet/<planet_name>")
def planet(planet_name):
    
    response = requests.get(
        f"{URL}{planet_name}", 
        headers=headers,
        timeout=10
    )

    if response.status_code == 404:
        return "planet not found.", 404
    if not response.ok:
        return"planet API returned status {response.status_code}.", 502
    
    planet_data = response.json()
    return render_template("planet.html", planet_data=planet_data,  planet_name=planet_name)



# Start application
if __name__ == "__main__":
    app.run(debug=True)

