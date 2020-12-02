# -*- coding: utf-8 -*-

""" Program you solution to this assignment below using 
    the variable names as defined below.                
    
    Recall that the data for this assignment is contained 
    in a file named length.csv                            """


import matplotlib.pyplot as plt

f_in = open("C:\\Users\\Loube\\OneDrive - William & Mary\\Python\\Assignments\\WMPython\\Module5\\length.csv", 'r')
data = f_in.readlines()
f_in.close() # always close file

# clean up data
for i in range(len(data)):
    data[i] = data[i].strip()
    data[i] = int(data[i])
    
# check data
print(data)

all_data = sorted(list(set(data))) # sort and store as one object

# create dictionary w/ #'s of characters as key
dict1 = {ch:0 for ch in all_data}
print(dict1)

# add values to the keys as the # of occurences
for ch in data:
    dict1[ch] += 1

# x and y variables for plt object
x = [ch for ch in dict1.keys()]
y = [occ for occ in dict1.values()]
  
# figure var and ax for the plot
datafig, ax = plt.subplots()

# configure ax object
ax.bar(x, y, color = 'm')
ax.xaxis.set_label_text('Number of Characters')
ax.yaxis.set_label_text('Frequency')

# configure datafig object
datafig.suptitle("Analysis of President Trump's Tweet Length")
datafig.set_size_inches(9, 6)
datafig.savefig('M5Hist.jpg')
datafig.tight_layout

# display histogram
plt.show()
