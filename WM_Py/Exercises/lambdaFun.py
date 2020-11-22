# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 21:34:11 2020

@author: Loube
"""

# put condition in parenthesis
x = lambda x: 1 if (x == True) else 0
x(True)


# update list if needed
ur_list = ['int', 3, 'chien', 'perro']
y = lambda y: type(y[0])
y(ur_list)


# I will call z on itself to perform the recursion
z = lambda i: i * z(i -1) if (i > 1) else 1
