"""
Humans: Maya Mori, Justin Mohabir
Softdev
k07 -- teardown
2022-10-03
time spent: 1.2 hr

"""

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs? 

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return 1#"No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
- Changing the name of "hello_world" function doesn't change anything
- It can't return an integer
QCC:
0. Jframe??? Java neew instance of a class, constructor?
1. Seperating files
2. In a web browser
3. No hablo queso!
4. At the link 127.0.0.1:5000
5. In Processing, .draw() from another file
...
INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
 - Trial and error
 - Changing names/values
'''
