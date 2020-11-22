# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 21:34:11 2020

@author: Loube
"""

# put condition in parenthesis
x = lambda x: 1 if (x == True) else 0
x(True)


# update list if needed
ur_list = ['int', 3, 'chien', 'perro']
y = lambda y: type(y[0])
y(ur_list)


# 
z = lambda z: while (z > 1)  z * (z - 1)