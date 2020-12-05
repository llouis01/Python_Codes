# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

""" Input data """
f_in = open('irisData.csv','r')
data = f_in.readlines()
f_in.close()
 
""" Strip and split each row of data """
for i in range(len(data)):
    data[i] = data[i].strip().split(',')

""" Read column heading data from first row, then delete the row """
colHeadings = [x.strip() for x in data[0]]
del data[0]

""" Create lists for the data fields """
species = [x[0] for x in data]  # Use this list to discern species
SepalLengthIn = [float(x[1]) for x in data]
SepalWidthIn = [float(x[2]) for x in data]
PetalLengthIn = [float(x[3]) for x in data]
PetalWidthIn = [float(x[4]) for x in data]
color = ['r' if x == 'Iris-setosa' else ('b' if x =='Iris-versicolor' else 'g') for x in species]
# for comp. lists, (condition if true else (condition if true else))   
     
""" create variables for accessing the Figure and Axes sub-objects """
fig,ax = plt.subplots()

""" Axes sub-object properties and methods """
# ax.scatter(PetalWidthIn,PetalLengthIn,c=color, alpha=0.5,s=150)
ax.scatter(SepalLengthIn,PetalLengthIn,c=color, alpha=0.5,s=150)
ax.xaxis.set_label_text('Petal Length(in)', fontsize = 16)
ax.yaxis.set_label_text('Sepal Length (in)', fontsize = 16)
ax.xaxis.set_tick_params(labelsize=14)
ax.yaxis.set_tick_params(labelsize=14)
ax.axhline(1.0)
ax.axhline(1.9)
ax.axvline(2.3, 1)
ax.axvline(2.8)

""" Figure sub-object properties and methods """
fig.suptitle('Sepal Length versus Petal Length', fontsize = 20)
fig.set_size_inches(16,9)
fig.savefig('sepLenPetLen.jpg')

""" Display graph """
plt.show()
