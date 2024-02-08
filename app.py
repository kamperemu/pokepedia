from flask import Flask, render_template, request, redirect, session
import pokebase as pb
import requests

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pokelist/<int:page>")
def pokelist(page):
    pokemonList = requests.get(f"https://pokeapi.co/api/v2/pokemon?limit=50&offset={page*50}").json()
    return render_template("pokelist.html", pokemons=pokemonList['results'])

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/pokemon/<name>")
def pokemon(name):
    pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}").json()
    return render_template("pokemon.html", pokemon=pokemon)

@app.route("/ability/<name>")
def ability(name):
    ability = requests.get(f"https://pokeapi.co/api/v2/ability/{name}").json()
    return render_template("ability.html", ability=ability)