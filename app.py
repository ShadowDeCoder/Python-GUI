from tkinter import *
from random import choice
from random import sample

app = Tk()

app.title("Sample")
app.geometry("400x300")
app['background'] = '#282c34'

Heading = Label(app, text="Letes Code",  font=("Courier", 16, 'bold'), bg='#282c34', fg='cyan')
Heading.grid()

entry = Entry(app, background='lightblue', font=('Arial', 13))
entry.grid(row=2, column=0, columnspan=2, padx=20, pady=6)

num_choise = IntVar()
chk = Checkbutton(app, text='Double', variable=num_choise, onvalue=2, offvalue=1, bg='#282c34', fg='cyan', selectcolor='orange', font=('Arial', 12))
chk.deselect()
chk.grid(row=1, column=0, padx= 30, pady= 10)


def show():
    for widget in app.grid_slaves():
        if int(widget.grid_info()['row']) >= 4:
            widget.grid_forget()
    inp =entry.get().split(",")

    if num_choise.get()==2:
        ele = sample(inp, 2)
        text = 'Choice : '+ str(ele[0]+' '+ele[1])
    else:
        text = 'Choice : ' + str(choice(inp))



    msg = Label(app, text=text, font=("Courier", 12), background='pink', foreground='white', relief="raised")
    msg.grid(row=4, column=0, columnspan=2, padx=20, pady=6)

    if quit["state"] == DISABLED:
        quit["state"] = NORMAL




b = Button(app, text="Enter",command=show)
b.grid(row=3, column=0, padx=20, pady=6, )


quit = Button(app, text=" Close ", command=quit, state=DISABLED, background='red', foreground='white')
quit.grid(row=3, column=1, padx=20, pady=6)


app.mainloop()












