# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 12:42:14 2020

@author: Loube
"""

# Part 1
X = [9, 34, 12, 83, 13, 10, 3, 9, 4, 77, 16, 16.99]
xSmall = [x for x in X if (x<17)]
xSmall

# Part 2
x = [2, 4, 3, 2, 6, 5, 2, 8, 12]
xEven = [x for x in X if x %2 == 0]
xEven

# Part 3
y = {2: 'no', 3: 'yes', 4: 'gato', 6:'Cheval',1:'!',
     8: 'kapokapo'}
yEvenKey = {y: i for y, i in y.items() if y%2 == 0}
