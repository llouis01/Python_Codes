# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 23:17:38 2020

@author: Loube
"""

def sumEven(dct):
    total = 0
    for val in dct.values():
        total += val
        return total
        # if (val % 2 == 0):
        #     total += val
        #     return total
        
user_dct = {'hero':6,
            'battlefields':4,
            'villains':13,
            'outcome':1,
            'possibilities':999}

sumEven(user_dct)
