# app.py - A simple Flask application to demonstrate a Docker CI pipeline for DevOps.
# This application will be built into a Docker image and pushed to Docker Hub as part of a CI pipeline.
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello DevOps - Docker CI Pipeline!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
