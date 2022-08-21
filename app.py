from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
import datetime

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("index.html")