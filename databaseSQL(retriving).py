#import sqlite3
#MySchool=sqlite3.connect('schooltest.db')
            
#sql="SELECT * from student;"
            
#curschool=MySchool.cursor()
#curschool.execute(sql)
#while True:
#    record=curschool.fetchone() #fetches the next available record from the result set
#    if record==None:
#        break
#    print (record)



import sqlite3
MySchool=sqlite3.connect('schooltest.db')
    
sql="SELECT * from student;"
            
curschool=MySchool.cursor()
curschool.execute(sql)
    
result=curschool.fetchall()   # fetches all the remaining records in the form of a list of tuples
for record in result:
    print (record)
