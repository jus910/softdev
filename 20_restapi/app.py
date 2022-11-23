from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
import requests           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route("/", methods=['GET'])
def home():
    key = open("key_nasa.txt")
    #print(key.readline())
    link = 'https://api.nasa.gov/planetary/apod?api_key=' + key.readline()
    print(link)
    r = requests.get(link[:-1])
    dict = r.json()
    url = dict['url']
    explain = dict['explanation']
    return render_template("main.html", url = url, explain = explain)
    

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
