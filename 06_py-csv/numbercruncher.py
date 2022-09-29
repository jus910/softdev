"""
Humans: Maya Mori, Justin Mohabir
Duckies: Catbat, Alfred
Softdev
05_bitstream
2022-09-29
time spent: 0.9
DISCO:
  - We can use the .split("str") method to split a string into a list
  - TypeError: 'dict_keys' object is not subscriptable
QCC:
  - Will a student always have a Ducky?
  - Will the file end with '@@@' all of the time?
OPS SUMMARY:
  - We read entire file as 1 string
  - We first split the string into a list of tuples
  - Next we split the tuples into their own lists which we store in another list
  - Then we put the duckies and students into a dictionary with the periods as keys and a list
    contaning two lists for students and duckies for values
  - After that we get a random period and a random index for the period, which we use
    to find a random student and Ducky because their indeces should match
"""

import random as rg

l = [1,2,3]
w = [1.0,2.0,3.5]

for i in range(10):
    print(rg.choices(l,weights=w))
    
data = {1:0,2:0,3:0}

for i in range(100000):
    data[rg.choices(l,weights=w)[0]] += 1

print(data)