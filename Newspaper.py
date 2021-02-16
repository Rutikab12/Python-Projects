from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.geometry("1000x800")
root.title("Daily News")
texts=[]
photos=[]
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(text)

    image=Image.open("lightbulb2.jpg")
    image=image.resize((380,220),Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root, width=200,height=70)
f0.pack()
Label(f0,text="Daily News",font="arial 15 bold").pack()
Label(f0,text="15 Jan,20 - Kolhapur,MH",font="lucida 12 bold").pack()

f1=Frame(root,width=500,height=200,pady=14)
Label(f1,text=texts[0],padx=40,pady=40).pack(side="left")
Label(f1,image=photos[0],anchor="e").pack()
f1.pack(anchor="w")

f2=Frame(root,width=500,height=200,pady=25,padx=25)
Label(f2,text=texts[1],padx=30,pady=30).pack(side="left")
Label(f2,image=photos[1],anchor="e").pack()
f2.pack(anchor="w")

f3=Frame(root,width=500,height=200,pady=25)
Label(f3,text=texts[2],padx=40,pady=40).pack(side="left")
Label(f3,image=photos[2],anchor="e").pack()
f3.pack(anchor="w")

root.mainloop()