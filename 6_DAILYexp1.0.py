from tkinter import *
#daily expense tikenter
m=Tk()

Label(m,text="name of product").grid(row=0)
Label(m,text="amount of ").grid(row=1)
Label(m,text="description of product").grid(row=2)
e1=Entry(m)
e2=Entry(m)
e3=Entry(m)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
def add():
    global e1,e2,e3
    
    file=open("daily_expense.txt","a")
    file.write(e1.get())
    file.write("\n")
    file.write(e2.get())
    file.write("\n")
    file.write(e3.get())
    file.write("\n")
    
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e1.focus()

    file.close()
def display():
    file=open("daily_expense.txt","r")
    
    Label(m,text=file.read()).grid(row=5,column=0)
    #text=Text(file.read())
    #text.grid(row=5,column=0)
    file.close()
    
b1=Button(m,text="display",command=display).grid(row=4,column=0)
b=Button(m,text="add",command=add).grid(row=4,column=1)
##scroll bar
scrollbar = Scrollbar(m)
scrollbar.grid(row=5,column=1,sticky='ns')
display.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=display.yview)
display.create_rectangle((200,300,300,600))

#Sb=Scale(m,orient=VERTICAL,from_=0,to=100,sliderlenght=1200,command=display)
#sb.grid(row=0,column=1,sticky='ns')
#frame2 = Frame(m)
#frame2.grid(row=3, column=0, sticky=tk.NW)

mainloop()
