# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 16:34:09 2017

@author: Andreea Aniculaesei
"""

import inputNumber
import numpy as np

def displayMenu(options):
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
        
        choice = 0
        while not(np.any(choice == np.arange(len(options))+1)):
            choice = inputNumber("Please choose a menu item: ")
            
        return choice
        