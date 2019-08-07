
# importing only those functions which 
# are needed 
from tkinter import Tk, mainloop, TOP 
from tkinter.ttk import Button,Label,Entry

# Or we can import the all Module of tkinter package for GUI application which
# are given below

#from tkinter import *   

root=Tk()  # Create the object of Tk() class which is used to create the Frame

# creating fixed geometry of the 
# tkinter window with dimensions 200x450  where 200 px width and 450 height fo the Frame

root.geometry('200x450') 

l1=Label(root,text="Enter the First Number")
e1=Entry(root)

l1.pack()
e1.pack()
button = Button(root, text = 'Submit')   # To create the Submit Button
button.pack(side = TOP, pady = 5) 

mainloop() # It should requred for appear the frame
