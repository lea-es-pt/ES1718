# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 18:10:41 2017

@author: Andreea Aniculaesei
"""
from Tkinter import *

window = Tk()

l1 = Label(window, text = 'User:')
l2 = Label(window, text= 'Password:')

t1 = Entry(window, textvariable = StringVar())
t2 = Entry(window,  show= '*', textvariable = StringVar())

b1 = Button(window, text = "Login")

l1.pack()
t1.pack()
l2.pack()
t2.pack()
b1.pack()

window.mainloop()
