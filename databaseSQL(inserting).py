import sqlite3
MySchool=sqlite3.connect('schooltest.db')
curschool=MySchool.cursor()
mysid= int(input("Enter ID: "))
myname=input("Enter name: ")
myhouse=int(input("Enter house: "))
mymarks=float(input("Enter marks: "))
curschool.execute("INSERT INTO student (StudentID, name, age, marks) VALUES (?,?,?,?);", (mysid,myname,myhouse,mymarks))
MySchool.commit()
