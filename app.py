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
entry.grid(row=1, column=0, columnspan=2, padx=20, pady=6)

num_choise = IntVar(value='0')
sld=  Scale(app, from_=1, to=10, variable=num_choise, orient=HORIZONTAL, length=250,bg='#2980B9', fg='white', tickinterval=1 )
sld.grid(row=2, column=0, columnspan=2,padx=25, pady=10)


'''
#Radio button Section:
rd1 = Radiobutton(app, text='1', variable=num_choise, value=1, bg='#282c34', fg= 'red', font=('bold') )
rd2 = Radiobutton(app, text='2', variable=num_choise, value=2, bg='#282c34', fg= 'red', font=('bold'))
rd1.grid(row=2, column=0, padx= 30, pady= 10)
rd2.grid(row=2, column= 1, padx=30, pady= 10)
'''


def show():
    for widget in app.grid_slaves():
        if int(widget.grid_info()['row']) >= 4:
            widget.grid_forget()
    inp =entry.get().split(",")

    #here i want to check that the inp is null or not if the entry is not given i want to show a msg that give input first and i want to end the function
    if not inp[0]:
        msg = Label(app, text='Give input First !!', font=("Courier", 12), background='pink', foreground='black', relief="raised")
        msg.grid(row=4, column=0, columnspan=2, padx=20, pady=6)
        return

    if num_choise.get()!=1:
        '''
        if len(inp) < num_choise.get():
            msg = Label(app, text='Invalid input or Choice No.!!', font=("Courier", 12), background='pink',
                        foreground='black', relief="raised")
            msg.grid(row=4, column=0, columnspan=2, padx=20, pady=6)
            return'''
        ele = sample(inp, num_choise.get())
        lbl = ''
        for e in ele:
            lbl += ' ' + e
        text = 'Choice :'+ str(lbl)
        msg = Label(app, text=text, font=("Courier", 12), background='pink', foreground='black', relief="raised")
        msg.grid(row=4, column=0, columnspan=2, padx=20, pady=6)
    elif num_choise.get()==1:
        text = 'Choice : ' + str(choice(inp))
        msg = Label(app, text=text, font=("Courier", 12), background='pink', foreground='black', relief="raised")
        msg.grid(row=4, column=0, columnspan=2, padx=20, pady=6)
    elif num_choise.get()==0:
        msg = Label(app, text='Select Variable' , font=("Courier", 12), background='pink', foreground='black', relief="raised")
        msg.grid(row=4, column=0, columnspan=2, padx=20, pady=6)

    if quit["state"] == DISABLED:
        quit["state"] = NORMAL

b = Button(app, text="Enter",command=show)
b.grid(row=3, column=0, padx=20, pady=6, )


quit = Button(app, text=" Close ", command=quit, state=DISABLED, background='red', foreground='white')
quit.grid(row=3, column=1, padx=20, pady=6)


app.mainloop()












