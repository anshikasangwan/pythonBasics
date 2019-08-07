from tkinter import *
root = Tk()
text = Text(root)
text.grid()
scrl = Scrollbar(root, command=text.yview)
text.config(yscrollcommand=scrl.set)
scrl.grid(row=0, column=1,sticky='ns')
root.mainloop()
