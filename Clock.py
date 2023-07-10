from tkinter import*
from tkinter.ttk import*
from time import strftime
def clock():
    string = strftime("%H:%M:%S:%p")
    label.config (text=string)
    label.after(1000,clock)
root = Tk()
root.title("Clock")
label = Label(root, font=("Digital-7",100),background = "black", foreground="white")
label.pack(anchor = "center")
clock()
root.mainloop()