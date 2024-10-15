from tkinter import *
from random import choice, sample

app = Tk()

app.title("Sample")
app.geometry("400x300")  # Increased size for better layout
app.configure(bg='#282c34')  # Dark gray background

# Heading
Heading = Label(app, text="Let’s Code!", font=("Courier", 16, 'bold'), bg='#282c34', fg='cyan')
Heading.grid(pady=(20, 10))

# Entry Field
entry = Entry(app, background='lightblue', font=('Arial', 12))
entry.grid(row=2, column=0, columnspan=2, padx=30, pady=10)

# Checkbox
num_choice = IntVar()
chk = Checkbutton(app, text='Double', variable=num_choice, onvalue=2, offvalue=1, bg='#282c34', fg='white',
                  selectcolor='orange', font=('Arial', 12), activebackground='navy', activeforeground='white')
chk.deselect()  # Starts off unchecked
chk.grid(row=1, column=0, padx=30, pady=10)

# Show Function
def show():
    for widget in app.grid_slaves():
        if int(widget.grid_info()['row']) >= 4:
            widget.grid_forget()
    inp = entry.get().split(",")

    if num_choice.get() == 2:  # If checkbox is checked
        ele = sample(inp, 2)
        text = 'Choice: ' + str(ele[0] + ', ' + ele[1])
    else:
        text = 'Choice: ' + str(choice(inp))

    msg = Label(app, text=text, font=("Courier", 12), bg='lightgreen', fg='black', relief="raised", padx=10, pady=5)
    msg.grid(row=4, column=0, columnspan=2, padx=30, pady=10)

    if quit_button["state"] == DISABLED:
        quit_button["state"] = NORMAL

# Enter Button
b = Button(app, text="Enter", command=show, bg='coral', fg='white', font=('Arial', 12, 'bold'))
b.grid(row=3, column=0, padx=30, pady=10)

# Quit Button
quit_button = Button(app, text="Close", command=app.quit, state=DISABLED, bg='red', fg='white', font=('Arial', 12, 'bold'))
quit_button.grid(row=3, column=1, padx=30, pady=10)

app.mainloop()



