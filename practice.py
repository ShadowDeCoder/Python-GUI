import random
from tkinter import *
from random import choice


App = Tk()
App.title('Element Picker')
App.geometry('250x250')
App['background']= 'cyan'

display = Label(App, text="Welcome",background='white')
display.grid(row=0, column=2, padx=60, pady=5)

entry = Entry(App,background='gray', foreground='white')
entry.grid(row=1, column=2, padx=30,pady=10)

def choose():
    #here i want to have a code that clear the screen and give the output later
    for widget in App.grid_slaves():
        if int(widget.grid_info()['row']) >= 6:
            widget.grid_forget()

    pick = entry.get().split(',')
    msg = Label(App, text=random.choice(pick),background='green')
    msg.grid(row=6, column=2, pady=10)

b = Button(App, text="Generate", command= choose, background='blue', foreground='white')
b.grid(row=2, column=2)

closeWindow = Button(App, text='Close', command=quit, background='red')
closeWindow.grid(row=2, column=3)


App.mainloop()








