from tkinter import *
from random import randint

app = Tk()

app.title("Sample")
app.geometry("500x300")
Heading = Label(app, text="Letes Code")
Heading.pack()

email= Entry(app)
email.pack()

passwd= Entry(app)
passwd.pack()


def show():
    Mail=email.get()
    Passwd= passwd.get()

    msg = Label(app,text=Mail)
    msg.pack()



b = Button(app, text="Enter",command=show)
b.pack()


app.mainloop()










