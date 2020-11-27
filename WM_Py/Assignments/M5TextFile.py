# -*- coding: utf-8 -*-

""" Program you solution to this assignment below using 
    the variable names as defined below                 """


# import file using directory
f_in = open('C:\\Users\\Loube\\OneDrive - William & Mary\\Python\\Assignments\\WMPython\\Module5\\states.csv', 'r')
statesData = f_in.readlines()
f_in.close() # ensure data integrity and memory sustainability


# This block of code removes the extra space and splits elements in the data
for i in range(len(statesData)):
    statesData[i] = statesData[i].strip().split(',')


'''
This block of code converts the data elements into appropriate type.
First I indicate len() - 1 because by later specifying i + 1,
the index will be out of range. i + 1 is necessary because it skips
the column names list at the beginning of the data.
'''
for i in range(len(statesData)-1):
    statesData[i+1] = [str(statesData[i+1][0]),
                       int(statesData[i+1][1]),
                       int(statesData[i+1][2]),
                       float(statesData[i+1][3]),
                       float(statesData[i+1][4])]


# We can verify each element type by replacing the numbers between 0 and 4
for i in range(len(statesData)):
    print(type(statesData[i][4]))
    

# 
sums = [sum(row[i+1]) for row in statesData]
