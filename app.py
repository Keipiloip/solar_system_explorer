
from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("SOLAR_SYSTEM_API_KEY")

# Start Flask
app = Flask(__name__)


# Home page
@app.route("/")
def index():
    return render_template("index.html")


# Planet details page
@app.route("/planet/<planet_name>")
def planet(planet_name):
    return render_template("planet.html", planet_name=planet_name)


# Start application
if __name__ == "__main__":
    app.run(debug=True)
