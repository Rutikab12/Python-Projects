from tkinter import *

def update():
    print("Update the GUI")
    root.geometry(f"{width.get()}x{width.get()}")

root=Tk()
root.geometry("344x233")
root.title("Window Resizer")
Label(root,text="Window Resizer",font="arial 12 bold",pady=15,padx=15).pack()
width=StringVar()
height=StringVar()
Entry(root,textvariable=width).pack(pady=15)
Entry(root,textvariable=height).pack(pady=15)
Button(root,text="APPLY", command=update).pack(pady=15)





root.mainloop()