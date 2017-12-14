# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 18:40:04 2017

@author: Andreea Aniculaesei
"""


#interaction program that displays a menu
import numpy as np
import displayMenu

menuItems = np.array(["Tecnico", "CF", "GF"])

while True:
    choice = displayMenu(menuItems);

    if choice == 1:
            name = input("Please enter your name:")
            
    elif choice == 2:
            print(name)
            
    elif choice == 3:
        break