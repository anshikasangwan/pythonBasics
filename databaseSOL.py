import sqlite3
MySchool=sqlite3.connect('schooltest.db')
curschool=MySchool.cursor()                 #creating connection
curschool.execute('''CREATE TABLE student (
StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT (20) NOT NULL,
age INTEGER,
marks REAL);''')

MySchool.close() 
