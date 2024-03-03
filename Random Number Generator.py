from tkinter import *
from random import randint

app =Tk()
app.title("Random Number Generator")
app.geometry("500x300")
Heading = Label(app, text="Generate a Random Number")
Heading.pack()

def show_msg():
    msg = Label(app, text=randint(1,200))
    msg.pack()

b = Button(app,text ="Generate", command=show_msg)
b.pack()

app.mainloop()

