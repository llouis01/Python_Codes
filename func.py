# defining functions in python

import numpy as np

import pandas as pd

num1, num2, num3, num4, num5 = input("Enter 5 numbers: ").split() # must convert the entry to int then space between entries
print()

print("*** Basic analysis of your numbers ***")
print()

if num1 > num5:
    print("First is greater than last entry")
elif num1 < num5:
    print("Last entry is greater than first")
else:
    print("They must be equal")
           
    
print("The sum of your numbers is ", int(num1) + int(num2) + int(num3) + int(num4) + int(num5)) # had to cast nums to int

np_nums = np.array([int(num1), int(num2), int(num3), int(num4), int(num5)]) # put input into an array

print("Your numbers have been transformed into a ", type(np_nums)," data frame.")

print(np_nums)

print("The mean of your numbers is ", np.mean(np_nums))

print("The median is ", np.median(np_nums))

print("There is no correlation between the numbers; hence a score of ", np.corrcoef(np_nums))
print()

print("*** Using Numpy on a dataset ***")
print()

htwt = np.array(pd.read_csv("C:\\Users\\Loube\\Desktop\\htwt.csv")) # quote and \\ to import file
print(htwt)
print()
print("                 ***************             ")

males_only = htwt[htwt[:, 0]=='Male'] #subsetting to get all males
print()

print("Male Breakdown")
print()
print(males_only)

fmales_only = htwt[htwt[:, 0]=='Female']
print()

print("Female Breakdown")
print()
print(fmales_only)

print()
print("Male frame only")
male_htwt = males_only[:,1:3]
print(male_htwt)

print()
print("Females frame only")
fmale_htwt = fmales_only[:,1:3]
print(fmale_htwt)