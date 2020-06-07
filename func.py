# defining functions in python

import numpy as np

import pandas as pd

htwt = np.array(pd.read_csv("C:\\Users\\Loube\\Desktop\\htwt.csv")) # quote and \\ to import file
print(htwt[htwt[0]=="Male"])

num1, num2, num3, num4, num5 = input("Enter 5 numbers: ").split() # must convert the entry to int
print()

print("*** Basic analysis of your numbers ***")
print()

if num1 > num5:
    print("First is greater than last entry")
elif num1 < num5:
    print("Last entry is greater than first")
else:
    print("They must be equal")
           
    
print("The sum of your numbers is ", int(num1) + int(num2) + int(num3) + int(num4) + int(num5))
print()

np_nums = np.array([num1, num2, num3, num4, num5]) # put input into an array

print("Your numbers have been transformed into a ", type(np_nums)," data frame.")

print(np_nums)

print("The mean of your numbers is ", np.mean(np_nums))

print("The median is ", np.median(np_nums))

print("The correlation is random, so do not expect any meaning from ", np.corrcoef(np_nums))