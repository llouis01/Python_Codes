# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 21:40:25 2020

@author: Loube
"""

# ensure to use double backslashes
f_in = open('C:\\Users\\Loube\\OneDrive - William & Mary\\Python\\Assignments\\WMPython\\Module5\\sf.csv', 'r')
data = f_in.readlines()
f_in.close() # always close file

### data wrangling
for i in range(len(data)):
    data[i] = data[i].strip().split(',') # removes the \n and splits by ,
    data[i] = [data[i][0][-5:], float(data[i][1])]
    # for j in range(len(data[i])):
    #     if j == 1:
    #         data[i][j] = float(data[i][j])
    #     if j == 0:
    #         data[i][j] = data[i][j][-5:] # slice on the timeseries