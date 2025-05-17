from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/', methods=["GET"])
def table():
    headers = {
        "X-Auth-Token": os.environ.get("FOOTBALL_API_KEY")
    }

    url = "https://api.football-data.org/v4/competitions/PL/standings"
    response = requests.get(url, headers=headers)
    data = response.json()

    teams = []
    for entry in data["standings"][0]["table"]:
        teams.append(entry["team"]["name"])
    
    response = jsonify(teams)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ =="__main__":
    app.run(debug=True)
