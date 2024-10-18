from tkinter import *

app = Tk()
app.geometry('250x200')

choice = StringVar(value=" ")

rad1 = Radiobutton(app, text='one', variable=choice, value='radiobutton 1 selected')
rad1.pack()

rad2 = Radiobutton(app, text='two', variable=choice, value='radiobutton 2 selected')
rad2.pack()

def show():
    msg.config(text=choice.get())

msg = Label(app, text='')
msg.pack(pady=10)


B = Button(app, text='Show', command=show)
B.pack()


app.mainloop()


