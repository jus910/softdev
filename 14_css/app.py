# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask, render_template #Q0: What will happen if you remove render_template from this line? (log your prediction before you pull the trigger...)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
