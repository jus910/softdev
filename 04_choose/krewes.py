"""
Humans: Maya Mori, Justin Mohabir, Gordan Mo
Duckies: Catbat, Alfred, Blueman
Softdev
04_choose
2022-09-23
time spent:
DISCO:
  - Key must be defined
  - list is an unhashable type
  - randint(a,b) returns an integer from [a,b]
  - When you add lists, it creates 1 big list
QCC:
OPS SUMMARY: We iterated all of the values in krewes using the values()
function. Then, we added all of the names to a new list called peeps.
Then, we used the choice function from random to choose a random name
from peeps.
"""
import random as rng

#krewes = {2:['bruh','1'],7:['b'],8:['c']}
krewes = {
           2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY", "Ruiwen"], 
           7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
           8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "Wanying", "Kevin"]
         }

def randomPerson():
    peeps=[]
    for period in krewes.values():
        #print(type(n))
        peeps += period
    #print(peeps)
    return rng.choice(peeps)
    #return peeps

data = {}
#print(type(data))

peeps=[]
for period in krewes.values():
    #print(type(n))
    peeps += period
for name in peeps:
    data[name] = 0

for i in range(10000):
    data[randomPerson()] += 1

print(data)
    
    
    #print(randomPerson())
#print(krewes.values())
