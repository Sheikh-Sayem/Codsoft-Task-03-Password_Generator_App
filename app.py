import tkinter as tk
from tkinter import *
import random
import string

u=string.ascii_uppercase    #uppercaseletter
l=string.ascii_lowercase    #lowercase letters
num=string.digits           #numbers
sym=string.punctuation      #symbols
show=""



def create():
    global show
    password=u+l+num+sym
    x=random.sample(password,20)  #random.sample : Returns a given sample of a sequence
    generate="".join(x)
    if show:
        show.destroy()

    show=tk.Label(root,text=generate,width=30,height=2,bg='white')
    show.pack(anchor=W,padx=10,pady=10)



def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(show.cget("text"))


root = Tk()
root.minsize(600,300)
root.maxsize(600,300)
root.title('Password Generator')
root.config(background='#070220')

l1=Label(root,text="Generate a", font=("arial 20 bold"),fg='white',bg='#070220')
l1.pack(pady=(80,5),anchor=W,padx=10)

l2=Label(root,text="Random Password", font=("arial 15 bold"),fg='green',bg='#070220')
l2.pack(pady=(0,5),anchor=W,padx=10)



b=Button(root,width=15, text="Generate",font="Arial 10 bold",bg='black', fg='white', bd=0,command=create)
b.pack(anchor=W,padx=10,pady=5)


b=Button(root,width=15, text="Copy",font="Arial 5 bold",bg='white', fg='black', bd=0,command=copy_to_clipboard)
b.pack(anchor=W,padx=10)


root.mainloop()