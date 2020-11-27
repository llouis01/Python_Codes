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
for i in range(len(data)):# we don't know length of df, so do range(len(df))
    data[i] = data[i].strip().split(',') # removes the \n and splits by ,
    data[i] = [data[i][0][-5:], float(data[i][1])]


x = [datum[0] for datum in data]
y = [datum[1] for datum in data]

import matplotlib.pyplot as plt

plt.plot(y)
plt.suptitle('San Francisco, CA Housing Prices')
plt.xlabel('YY-MM')
plt.ylabel('Average Home Price')
plt.gcf().set_size_inches(12,6)
p = 20
plt.xticks(range(0, len(x),p), [x[i] for i in range(len(x)) if i % 20 ==0])
plt.show()
