# Team Ducks: Ryan Lee, Justin Mohabir, Selena Ho
# Duckies: Luigi, Alfred, Soy
# SoftDev
# Oct 2022
# Prints statemnt in the terminal
from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go? In the terminal
    return "No hablo queso!"

app.run()

