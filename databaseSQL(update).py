import sqlite3
MySchool=sqlite3.connect('schooltest.db')
            
nm=input("enter name: ")
sql="SELECT * from student WHERE name='"+nm+"';"
curschool=MySchool.cursor()
curschool.execute(sql)
record=curschool.fetchone()
print (record)
m=float(input("enter new marks: "))
sql="UPDATE student SET marks='"+str(m)+"' WHERE name='"+nm+"';"    #for delete
try:                                                                #sql="DELETE FROM students WHERE name='"+nm+"';"
    curschool.execute(sql)          
    MySchool.commit()
    print ("record updated successfully")
except:
    print ("error in update operation")
    MySchool.rollback()
MySchool.close()
