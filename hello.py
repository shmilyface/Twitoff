""" Minimal Flask App """

from flask import Flask

#Make the application

app = Flask (__name__)

#make the route
@app.route("/")

#Now define function
def home():
    return "Hello World!"
