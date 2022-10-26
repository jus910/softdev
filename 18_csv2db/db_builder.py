#Verit Li, Brian Yang, Justin Mohabir  
#Team: Uh?  
#SoftDev  
#K18 csv2db
#2022-10-25
#time spent: .6  

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >


#command = ""          # test SQL stmt in sqlite3 shell, save as string
#c.execute(command)    # run SQL statement

with open('students.csv', "r") as student:  #creates a file object allows reading into
   reader = csv.DictReader(student) #creates a iterable object where each row is a dictionary with headings as keys
   c.execute("create table students(name TEXT, age INTEGER, id INTEGER);")
   for row in reader:
   	c.execute("insert into students values('" + row['name']+"'," +row['age']+ "," +row['id']+");")
    

with open('courses.csv', "r") as course:
   reader2 = csv.DictReader(course)
   c.execute("create table courses(code TEXT, mark INTEGER, id INTEGER);")
   for row in reader2:
       c.execute("insert into courses values('" + row['code']+"'," +row['mark']+ "," +row['id']+");")
    




#==========================================================

db.commit() #save changes
db.close()  #close database


