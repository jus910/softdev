# Team Ducks: Ryan Lee, Justin Mohabir, Selena Ho
# Duckies: 
# SoftDev
# Oct 2022
import random as rg
import csv
from flask import Flask

data1 = []
data = []

with open('occupations.csv','r') as csvfile:
    #data = list(csv.reader(csvfile))
    data0 = csvfile.read().split('\n')      # split each line
    for row in data0:
        data1 += [row.split("\"")]          # remove quotes

for row in data1:
    if len(row) == 1:
        data += [row[0].split(',')]
    else:
        data += [[row[1],row[-1][1:]]]

#print(data)

data = data[1:-2]

dict_data = {}
tester = {}                                 # Creates a dict for testing

# makes the dict with occupation names as keys and percents as values
for row in data:
    dict_data[row[0]] = float(row[1])
    tester[row[0]] = 0

print(dict_data)

def random_occupation():
    return rg.choices(list(dict_data.keys()),weights=list(dict_data.values()))[0]
############################################################# seperator

app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    for i in range(1000000):
        occ = random_occupation()
        if occ not in tester:
            tester[occ] = 0
        tester[occ] += 1
    return tester

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    tester={}
    app.run()
