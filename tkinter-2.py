from tkinter import *

def calculate():
    total = int(e1.get()) + int(e2.get())
    resultText = "Sum of 2 numbers: {}".format(total)
    resultLabel.config(text=resultText)

master = Tk()  # define canvas
master.geometry("300x300")
master.config(bg='lightblue')
l1 = Label(master, text='First Number:')
l2 = Label(master, text='Second Number:')
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
e1= Entry(master)
e2= Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
Button(master, text="Calculate", command=calculate).grid(row=2, column=0)
resultLabel = Label(master, text="Answer:")
resultLabel.grid(row=2, column=1)

master.mainloop()



