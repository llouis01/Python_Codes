# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def attire(temp):
    if temp <= 32:
        choice = 'Wear wool overcoat'
    elif temp < 60:
        choice = 'Wear sport coat'
    else:
        choice = 'Loosen tie'
        
    return choice

temp = 99
clothes = attire(temp)
print(clothes)