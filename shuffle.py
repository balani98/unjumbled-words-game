import tkinter # tkinter is python interface to TK GUI toolkit 
from tkinter import *
from tkinter import messagebox
import random
from random import shuffle
root = tkinter.Tk()

def ans_check():
    global words,num,answers
    user_input=el.get()
    if user_input==answers[num]:
        messagebox.showinfo("success","yep that is right")
        Reset()
    else:
        messagebox.showinfo("Error" ," nope that isnt right")
        el.delete(0,END)

def Reset():
    global words,num,answer
    num = random.randint(0,len(words))
    lb1.configure(text=words[num])
    el.delete(0,END)

def initial():
    global words,answers,num
    lb1.configure(text=words[num])

answers=["python","youtube","google","india","london","paris","france","idli","sambhar"]
num = random.randint(0,len(answers))
words=[]
for i in answers:
    word=list(i)
    shuffle(word)
    words.append(word)

num = random.randint(0,len(words))
root.geometry("700x400")
lb1=Label(root,font='times 20')   
lb1.pack(pady=30,ipady=10,ipadx=10)
answer=StringVar()
el = Entry(root,textvariable=answer)
el.pack(ipady=5,ipadx=5)
button1=Button(root,text="check",width=20,command = ans_check)
button1.pack(pady=40)
button2=Button(root,text="Reset",width=20,command = Reset)
button2.pack()

initial()
root.mainloop()