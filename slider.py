from tkinter import *

# Create the main application window
app = Tk()
app.geometry('400x350')
app.title("Cool Slider App")
app.configure(bg='#2C3E50')  # Set a dark blue background color

# Create a frame for better organization
frame = Frame(app, bg='#34495E', padx=10, pady=10)
frame.pack(pady=20)

# Create an IntVar for the slider value
sld_val = IntVar()

# Customize the scale with color and tick marks
sld = Scale(frame, from_=1, to=10, variable=sld_val, orient=HORIZONTAL,
            bg='#2980B9', fg='white', tickinterval=1, length=300)
sld.pack()

# Function to show the slider value
def show():
    msg.config(text=f"Selected Value: {sld_val.get()}")  # Update label text

# Create a label to display the value
msg = Label(frame, text="", bg='#34495E', fg='white', font=('Arial', 14))
msg.pack(pady=10)

# Style the button with colors and font
btn = Button(frame, text="Show", command=show, bg='#27AE60', fg='white', font=('Arial', 12))
btn.pack()

app.mainloop()

