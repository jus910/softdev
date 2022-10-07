# Team Ducks: Ryan Lee, Justin Mohabir, Selena Ho
# Duckies: Luigi, Alfred, Soy
# SoftDev
# Oct 2022
'''
## Disco 
- Changing the name of "hello_world" function doesn't change anything
- The route function can't return an integer
- Clicking on link runs helloworld
'''

from flask import Flask
app = Flask(__name__) 

@app.route("/")
def hello_world():
    print(__name__) 
    return "No hablo queso!"  

app.run() 
                
