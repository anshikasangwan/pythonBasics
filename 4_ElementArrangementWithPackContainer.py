
# importing only those functions which 
# are needed 
from tkinter import Tk, mainloop, TOP 
from tkinter.ttk import Button,Label,Entry
# importing messagebox class 
from tkinter.messagebox import *

# Or we can import the all Module of tkinter package for GUI application which
# are given below

#from tkinter import *   

root=Tk()  # Create the object of Tk() class which is used to create the Frame

# creating fixed geometry of the 
# tkinter window with dimensions 200x450  where 200 px width and 450 height fo the Frame

root.geometry('600x500')

l1=Label(root,text="Enter the First Number")
l2=Label(root,text="Enter the Second Number")
e1=Entry(root)
e2=Entry(root)
l1.pack(ipadx=250)
e1.pack()
l2.pack(ipadx=250)
e2.pack()
############################## Create a  function for Add Button ###########
def add():
     #global e1,e2
     n1=int(e1.get())
     n2=int(e2.get())
     res=n1+n2
     print(showinfo("Result", "Addition of two number "+str(res))) 

########################## Ending of the function for Add button ##########
button = Button(root, text = 'Add',command=add)   # To create the Submit Button
#and attach the function with Button using command Attirbute
button.pack(side = TOP, pady = 40) 

mainloop() # It should requred for appear the frame
