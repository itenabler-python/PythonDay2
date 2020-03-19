import tkinter
import tkinter.messagebox

def displaymessage():
    tkinter.messagebox.showinfo("Python GUI", "SUBMITTED!!")


window1 = tkinter.Tk()  # define canvas
window1.geometry("300x300")
#add a button
button1 = tkinter.Button(window1, text='Start', bg='cyan', command=displaymessage)
button1.config(font=("Courier,50"))

button1.pack(side='right', expand=tkinter.YES)

window1.mainloop()