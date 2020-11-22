# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 23:17:38 2020

@author: Loube
"""

def sumEven(dct):
    total = 0
    for val in dct.values():
        if isinstance(val, int): # filter non-numerical
            if (val % 2 == 0):
                total += val
    return total
        
user_dct = {'hero':6,
            'battlefields':4,
            'villains':'everyone',
            'outcome':1,
            'possibilities':999,
            'Dumbo':86}

sumEven(user_dct)
