# Team Ducks: Ryan Lee, Justin Mohabir, Selena Ho
# Duckies: Luigi, Alfred, Soy
# SoftDev
# Oct 2022
# /usr/bin/python3: No module named thonny.plugins.cpython.app error
# when debug mode is on
# MUST DEDICATE A TERMINAL FOR FLASK
# we can change the hello_world() and reloading the page changes
# app.debug() = true updates 
from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo !"

app.debug = True
# new line
app.run()
