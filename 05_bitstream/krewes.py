"""
Humans: Maya Mori, Justin Mohabir
Duckies: Catbat, Alfred
Softdev
05_bitstream
2022-09-29
time spent: 30 min
DISCO:
  - We can use the .splt("str") method to split a string into a list
  - TypeError: 'dict_keys' object is not subscriptable
    - We must 
QCC:
  - Will a student always have a Ducky?
OPS SUMMARY:
  - We first split the string into a list of tuples
  - Next we split the tuples into their own lists which we store in another list
  - Then we put the duckies and students into a dictionary with the periods as keys and a list
    contaning two lists for students and duckies for values
  - After that we get a random period and a random index for the period, which we use
    to find a random student and Ducky because their indeces should match
"""
import random as rng

str_test=''
for i in range(5):
    str_test+='8$$$bruh$$$ducky@@@'
    str_test+='8$$$mmori$$$duck2y@@@'
    str_test+='2$$$mmori$$$ducky@@@'
    str_test+='7$$$jmohabir$$$ducky@@@'
    str_test+='7$$$bruh$$$ducky2@@@'

#print(str_test)

list1=str_test.split('@@@')
#print(list1)


list2=[]

#Makes list within a list to seperate each tuple
for i in list1:
    list2+=[i.split('$$$')]
list2=list2[:-1]
#print(list2)

big_dict = {}

for i in list2:
#Makes sure that each period is in big_dict
    if i[0] in big_dict:
#Adds student and ducky to list
        big_dict[i[0]][0]+=[i[1]]
        big_dict[i[0]][1]+=[i[2]]
    else:
        #Makes list if one is not already there
        big_dict[i[0]]= [[i[1]],[i[2]]]
        
#print(big_dict)

def randomSoftDev():
    periods=list(big_dict.keys())
    #print(periods)
    rand_period=rng.choice(periods)
    #print(rand_period)
    rand_index=int((rng.random()*len(big_dict[rand_period][0])))
    #print(rand_index)
    return big_dict[rand_period][0][rand_index] + " from period " + rand_period + " with ducky " + big_dict[rand_period][1][rand_index] + " are the chosen duo!!!"
    
for i in range(10):
    print(randomSoftDev())