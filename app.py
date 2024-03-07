from tkinter import *
from random import choice

app = Tk()

app.title("Sample")
app.geometry("500x300")
Heading = Label(app, text="Letes Code", font=("Courier", 12))
Heading.grid()

entry = Entry(app)
entry.grid(row=2, column=0, columnspan=2, padx=20, pady=6)


def show():
    show =entry.get().split(",")
    text = 'Choice : '+choice(show)
    msg = Label(app, text=text, font=("Courier", 12))
    msg.grid(row=4, column=0,columnspan=2, padx=20, pady=6)

    if quit["state"] == DISABLED:
        quit["state"] = NORMAL



b = Button(app, text="Enter",command=show)
b.grid(row=3, column=0, padx=20, pady=6)


quit = Button(app, text=" Close ", command=quit, state= DISABLED)
quit.grid(row=3, column=1, padx=20, pady=6)


app.mainloop()










