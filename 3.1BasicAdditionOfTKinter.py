from tkinter import *   # Import all the module from tkinter package
w1 = Tk()   # A Class from tkinter package
w1.geometry("500x500")  # Set the Initial size of the Frame
def dis():
    a = int(e1.get())  # Get the Value from entry box and convert into integer
    b = int(e2.get())
    c = a + b
    l1['text']="Result is: ",c   # Set the Result in Label
b1 = Button(w1,text="Click Me",command=dis)  # command Attribute is used to link the function with button
b1.pack()  # Pack function fixed the element on screen according system
#b1.place(x=100,y=200)
e1 = Entry(w1)   # To get the input from input box
e1.place(x=50,y=100)  # place function is used to fixed the possition according to co-ordinate

e2 = Entry(w1)   # To get the input from input box
e2.place(x=50,y=150)
l1 = Label(w1,text="Result:")
l1.place(x=0,y=200)

w1.mainloop()  # To visible the the Frame