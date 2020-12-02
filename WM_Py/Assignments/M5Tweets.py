# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 16:08:38 2018

@author: jrbrad
"""

""" The list below contains words that you are to exclude form your analysis """
stopWords = ['to', 'the', 'a', 'to', 'is', 'and', 'in', 'of', 'that', 'it', 'be','at', 'this', 'are', 'be', 'for', 'will', 'with', 'at', 'have','on','&amp', 'by']

""" Program you solution to this assignment below using 
    the variable names as defined below.                
    
    Recall that the data for this assignment is contained 
    in a file named length.csv                            """
    
# import file and clean data  
f_in = open('C:\\Users\\Loube\\OneDrive - William & Mary\\Python\\Assignments\\WMPython\Module5\\words.csv', 'r')
data = f_in.readlines()
f_in.close() # always close file

for i in range(len(data)):
    data[i] = data[i].strip()

data = [x for x in data if x not in stopWords] # remove stop words

# create dictionary with words in clean_data
dict1 = {w:0 for w in data}
for w in data:
    dict1[w] += 1

# sort dictionary
sorted_dict = sorted(dict1.items(), key = lambda k_v: k_v[1], reverse=True)
dict2 = sorted_dict[:10]

x = [wrd for [wrd, freq] in dict2]
y = [freq for [wrd, freq] in dict2]

# import library and create bar graph (histogram)
import matplotlib.pyplot as plt

# create objects for graph
fig, ax = plt.subplots()

# configure ax object
ax.bar(x, y, color = '#30D5C8') # the hex code is for turquoise
ax.xaxis.set_label_text("Words in Trump's Tweets", fontsize=12)
ax.yaxis.set_label_text("Number of Occurences", fontsize=12)

# configure fig object
fig.suptitle("'Make America Great Again' in Ten Words", fontsize=12)
fig.set_size_inches(13, 6)
fig.savefig('tweets.jpg')

# display graph
plt.show()