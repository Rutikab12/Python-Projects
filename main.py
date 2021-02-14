# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
import random, string
import pyperclip
rutik_root = Tk()
#width x height
rutik_root.geometry("400x400")
#width, height
rutik_root.minsize(200,100)
rutik_root.maxsize(1200,800)
rutik_root.title("Rutik - Password Generator")

Label(rutik_root,text="Password Generator", font="arial 15 bold").pack()
Label(rutik_root,text="Rutik", font="arial 15 bold").pack(side=BOTTOM)

pass_label=Label(rutik_root,text="Password Length", font="arial 15 bold").pack()
pass_len=IntVar()
length=Spinbox(rutik_root,from_ =8, to_ = 32, textvariable = pass_len, width = 15).pack()

pass_str = StringVar()
def Generator():
    password = ''

    for x in range(0,4):
        Password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range (pass_len.get()- 4):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

Button(rutik_root,text =" Generate Password", command = Generator).pack(pady=5)
Entry(rutik_root, textvariable = pass_str).pack()

def Copy_password():
    pyperclip.copy(pass_str.get())
Button(rutik_root,text =" Copy to Clipboard", command = Copy_password).pack(pady=5)
rutik_root.mainloop()
