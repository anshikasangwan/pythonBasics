import sqlite3
MySchool=sqlite3.connect('schooltest.db')
curschool=MySchool.cursor()
mysid= int(input("Enter ID: "))
myname=input("Enter name: ")
myhouse=int(input("Enter age: "))
mymarks=float(input("Enter marks: "))

#try block to catch exceptions
try:
    curschool.execute("INSERT INTO student (StudentID, name, age, marks) VALUES (?,?,?,?);", (mysid,myname,myhouse,mymarks))
    MySchool.commit()
    print("One record added successfully. ")


#except block to handle exceptions
except:
    print("Error in operation. ")
    MySchool.rollback()
MySchool.close()
