# Team Ducks: Ryan Lee, Justin Mohabir, Selena Ho
# Duckies: Luigi, Alfred, Soy
# SoftDev
# Oct 2022
# when we run this it does nor print _main_ in the terminal
from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

