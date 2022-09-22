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
QCC:
OPS SUMMARY: how program operates
"""
import random as rng

krewes = {2:['bruh','1'],7:['b'],8:['c']}

def randomPerson():
    peeps=[]
    for n in krewes.values():
        peeps+=n
#     return rng.choice(peeps)
    return peeps
for i in range(100):
    print(randomPerson())
print(krewes.values())