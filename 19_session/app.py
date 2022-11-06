# Verit Li, Brian Yang, Justin Mohabir
# Team: Uh?
# SoftDev
# K19: Sessions Greetings
# 2022-11-03
# time spent: 1.0

from flask import Flask, render_template, session, request, redirect, url_for
import os
app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = 'aiukdj_+_bLQ$dj8*679(*(8&(+dd'
from flask import session

the_username = "verit"
the_password = "getstitches"

#This the landing page
@app.route('/', methods=['GET', 'POST'])
def welcome():
    if 'username' in session: #if logged in
        return render_template('response.html', user = session['username']) #welcome the user
    else: #not logged in
        return redirect(url_for('login')) #redirect to login page
    
    
#This is the login page
@app.route('/login', methods=['GET', 'POST'])  
def login():
    if request.method == 'POST': #if after submitting a user and pass through login form
        if (the_username == request.form['username'] and the_password == request.form['password']): #if user and pass correct
            session['username'] = request.form['username'] #save username to session
            return redirect(url_for('welcome')) #redirect to welcome
        else:  #user or pass are wrong
            wrongdoings = ''
            if request.form['username'] != the_username:
                wrongdoings += 'User not found, please try again'
            elif request.form['password'] != the_password:
                wrongdoings += 'Incorrect password, please try again'
            return render_template('login.html', authentication_message = wrongdoings)
    else: #accessed login page not from submitting login form
        if 'username' in session: #if already logged in
            return redirect(url_for('welcome')) #no logging in a second time!!
        else:  #not logged in
            return render_template('login.html', authentication_message = '') #go for it!



@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.debug = True
    app.run()
