from flask import Flask, render_template, request
from pymongo import MongoClient as MC

CONNECTION_STRING = "mongodb+srv://kvnvg2:GEepZ7Mf7zqVWP5G@cluster0.dniynqz.mongodb.net/"
DATABASE = "RH_db"

app = Flask(__name__)


def get_collection():
    cluster = MC(CONNECTION_STRING)
    database = cluster[DATABASE]
    collection = database["Boking"]
    return collection

def print_mappe():
    col = get_collection().find()
    listeOfdata = []
    for c in col:
        listeOfdata.append(c) 
        
    return listeOfdata

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/login_page")
def login_page():
    return render_template("login_page.html")


@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        name = request.form ["Username"]

        passord = request.form["pw"]
        brukere = print_mappe()
        bruker = brukere[0]
        print(brukere)
        if(name==bruker["brukernavn"] and passord==bruker["passord"]):
            return render_template("start.html")


    return render_template("login_page.html")


if __name__ == "__main__":
    app.run(debug=True)

