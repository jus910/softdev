# Verit Li, Brian Yang, Justin Mohabir
# Team: Uh?
# SoftDev
# K19: Sessions Greetings
# 2022-10-17
# time spent: .6

from flask import Flask, render_template, session, request, redirect, url_for
import os
app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = os.urandom(32)

from flask import session

the_username = "verit"
the_password = "getstitches"

#This the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        if session['username'] == the_username and session['password'] == the_password:
            return render_template("response.html", user=session['username'])
        else:
            # Must highlight what the user did wrong
            wrongdoings=""
            if session['username'] != the_username:
                wrongdoings+=' Username Wrong'
            if session['password'] != the_password:
                wrongdoings+=' Password Wrong'
            return render_template("error.html",huhs=wrongdoings)
    return render_template("login.html")

#auth is called after a form is submitted as seen in the html file
@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    session['username'] = request.form['username']
    session['password'] = request.form['password']
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.debug = True
    app.run()
