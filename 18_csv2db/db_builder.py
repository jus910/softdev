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
student = open('students.csv', "r")

reader = csv.DictReader(student)
c.execute("create table students(name TEXT, age INTEGER, id INTEGER);")
for row in reader:
    c.execute("insert into students values('" + row['name']+"'," +row['age']+ "," +row['id']+");")
    

course = open('courses.csv', "r")

reader2 = csv.DictReader(course)
c.execute("create table courses(code TEXT, mark INTEGER, id INTEGER);")
for row in reader2:
    c.execute("insert into courses values('" + row['code']+"'," +row['mark']+ "," +row['id']+");")
    


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >


command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


