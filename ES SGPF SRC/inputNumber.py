# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 16:23:12 2017

@author: Andreea Aniculaesei
"""
#asks the user to type a number and continue to run until the type-in is not a number
def inputNumber(prompt):
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            pass

    return num
