from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/', methods=["GET"])
@cross_origin(origin='*',supports_credentials=True)
def table():
    list = []
    link = f"https://www.eurosport.com/football/premier-league/standings.shtml"
    r = requests.get(link)
    data = r.text
    soup = BeautifulSoup(data,"lxml")
    tab = soup.find_all("a", class_="absolute right-1 max-w-full truncate left-8 lg:caps-s5-fx hidden md:block")
    for row in tab:
        list.append(row.string)
    response = jsonify(list)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ =="__main__":
    app.run(debug=True)
