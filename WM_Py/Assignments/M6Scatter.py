# -*- coding: utf-8 -*-

""" Recall that the data for this assignment is called ozoneTemp.csv """
""" Write programming code to create the scatterplot here using the
    variable names below as directed in the assignment.              """

import matplotlib.pyplot as plt

f_in = open('ozoneTemp.csv')
data = f_in.readlines()
f_in.close() # always close to prevent file corruption

# iterate through data to remove white-space and split on ','
for i in range(len(data)):
    data[i] = data[i].strip().split(',')

# extract column names then delete from data
col_names = data[0]
del data[0]

# extract ozone layer info into x and temp into y
x = [int(x[0]) for x in data]
y = [int(y[1]) for y in data]

# create obj. variables for graphs
fig, ax = plt.subplots()

# configure ax sub-object properties and methods
ax.scatter(x, y, color='m', alpha=0.5, s=150)
ax.xaxis.set_label_text('Ozone Level', fontsize=16)
ax.yaxis.set_label_text('Temperature', fontsize=16)
ax.xaxis.set_tick_params(labelsize=14)
ax.yaxis.set_tick_params(labelsize=14)

# configure fig sub-object properties and methods
fig.suptitle('Temperature versus Ozone Level')
fig.set_size_inches(16, 9)
fig.savefig('M6oz.jpg')

# display graph
plt.show()