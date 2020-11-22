# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 22:46:05 2020

@author: Loube
"""

def attire(temp):
    if temp <= 32:
        choice = 'Wear wool overcoat'
    elif temp < 60:
        choice = 'Wear sport coat'
    else:
        choice = 'Loosen tie'
        
    return choice

temp = float(input('Enter today\'s temperature: '))
try:
    # temp = float(temp)
    clothes = attire(temp)
    print(clothes)
except:
    print("Input cannot be converted to float")