# Verit Li, Brian Yang, Justin Mohabir
# Team: Uh?
# SoftDev
# K12: Take and Give
# 2022-10-17
# time spent: .6

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not.
TASK: Predict which...
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests.
Process results.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.args['username']  ***")
    try:
        print(request.args['username']) #prints the the value associated with the key 'username' in ImmutableMultiDict
    except:
        print("ERROR: there is no username in args")
    print("***DIAG: request.form ***")
    print(request.form)
    print("***DIAG: request.form['username']  ***")
    try:
        print(request.form['username'])
    except:
        print("ERROR: there is no username in form")
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.args['username']  ***")
    try:
        print(request.args['username'])
    except:
        print("ERROR: there is no username in args")
    print("***DIAG: request.form ***")
    print(request.form)
    print("***DIAG: request.form['username']  ***")
    try:
        print(request.form['username'])
    except:
        print("ERROR: there is no username in form")
    print("***DIAG: request.headers ***")
    print(request.headers)
    username = request.form['username']
    return render_template('response.html', user=username, request_method = request.method) #response to a form submission

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
