from tkinter import *
from random import choice

app = Tk()

app.title("Sample")
app.geometry("220x150")
app['background'] = 'gold'

Heading = Label(app, text="Letes Code", font=("Courier", 12))
Heading.grid()

entry = Entry(app, background='grey')
entry.grid(row=2, column=0, columnspan=2, padx=20, pady=6)


def show():
    show =entry.get().split(",")
    text = 'Choice : '+choice(show)
    msg = Label(app, text=text, font=("Courier", 12), background='pink', foreground='white', relief="raised")
    msg.grid(row=4, column=0, columnspan=2, padx=20, pady=6)

    if quit["state"] == DISABLED:
        quit["state"] = NORMAL



b = Button(app, text="Enter",command=show)
b.grid(row=3, column=0, padx=20, pady=6, )


quit = Button(app, text=" Close ", command=quit, state=DISABLED, background='red', foreground='white')
quit.grid(row=3, column=1, padx=20, pady=6)


app.mainloop()










