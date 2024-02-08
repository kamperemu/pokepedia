from flask import Flask, render_template, request, redirect, session
import pokebase as pb

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pokelist")
def pokelist():
    pokemonList = pb.APIResourceList('pokemon')
    return render_template("pokelist.html", pokemons=pokemonList)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/pokemon/<name>")
def pokemon(name):
    pokemon = pb.pokemon(name)
    return render_template("pokemon.html", pokemon=pokemon)