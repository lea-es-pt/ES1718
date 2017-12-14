# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 16:44:09 2017

@author: Andreea Aniculaesei
"""

#import everything from tkinter
from tkinter import *

#create window object
window = Tk()
#all windows objects to be declared
#define four labels title author year isbn

l1 = Label(window, text = "Title")
l1.grid(row=0, column = 0)
window.mainloop()
