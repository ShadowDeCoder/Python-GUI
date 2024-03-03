from tkinter import *

app =Tk()
app.title("Intro")
app.geometry("500x300")
welcome = Label(app, text="Welcome to my APP")
welcome.pack()

def show_msg():
    msg = Label(app, text="Hii its Sunday")
    msg.pack()

b = Button(app,text ="Click Me ", command=show_msg)
b.pack()

app.mainloop()

