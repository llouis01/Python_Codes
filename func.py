# defining functions in python

import numpy as np

import pandas as pd

num1 = input("Enter first number: ")
num2 = input("Second one: ")

def addNum(x, y):
    if x > y:
        print("First is greater")
    elif x < y:
        print("First is less")
    else:
        print("They must be equal")
    
addNum(num1, num2)

print()

print("Basic analysis of", num1, "and", num2)

x = [num1, num2]

np_nums = np.array(x)

print() # next line

print(type(np_nums))