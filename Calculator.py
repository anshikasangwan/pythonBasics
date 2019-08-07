from tkinter import *
root = Tk()
root.geometry("500x500")
list1 = ['1','2','3','4','5','6','7','8','9']
list2 = ['b1','b2','b3','b4','b5','b6','b7','b8','b9']
list3 = ['+','-','*','/']
list4 = ['b10','b11','b12','b13']
def addn(a):
    e1.insert(END,a)
def cal():
    ans = eval(e1.get())
    e1.delete(0,END)
    e1.insert(END,ans)
def clear():
        e1.delete(0,END)
frame1 = Frame(root,height=100,width=500)
frame1.place(x=0,y=0)
l1 = Label(root,text="DISPLAY : ",font = "times 25")
l1.place(x=20,y=25)
e1 = Entry(frame1,width=20,font="times 20")
e1.place(x=200,y=30)
frame2 = Frame(root,height=400,width=300)
frame2.place(x=50,y=100)
count = 0
for i in range(0,3):
    for j in range(0,3):
        list2[count] = Button(frame2,height=5,width=7,text=list1[count],font = "times 10 bold",command = lambda a=count: addn(list1[a])).grid(row = i, column = j)
        count += 1
b15 = Button(root,text="0",height=4,width=24,font = "times 10 bold",command = lambda: addn(a=0))
b15.place(x=50,y=370)
frame3 = Frame(root,height=200,width=100)
frame3.place(x=250,y=100)
count2 = 0
for i in range(0,4):
    list4[count2] = Button(frame3,height=5,width=7,text=list3[count2],font = "times 10 bold",command = lambda a=count2: addn(list3[a])).grid(row = i, column = 0)
    count2 += 1
b14 = Button(root,width=9,height=1,font = "times 20 bold",text="Submit",command = cal).place(x=330,y=220)
b15 = Button(root,width=9,height=1,font = "times 20 bold",text="Clear",command = clear).place(x=330,y=280)
root.mainloop()
