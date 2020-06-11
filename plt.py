# Data Visualization with matplotlib with non-factual data

import matplotlib.pyplot as plt

import numpy as np

s = np.random.normal(0, 2, 100)
x = ['1991', '1995', '1999', '2004', '2009']
y = [14.5, 17.9, 21.3, 31.2, 45.8]

print(s)

plt.plot(x, y, color = 'purple') #.plt is better with dates on the x-axis; better for two variables generally
plt.xlabel('Year')
plt.ylabel('Median Salary')
plt.title('Median Salary in the US from 1991 to 2009')
plt.show() # why do I get all the decimals from y
plt.clf() # cleans up screen after displaying above hostogram

plt.hist(s, bins=10, color = 'purple') # bins to break up the data into appropriate boundaries
plt.xlabel('Random Output')
plt.ylabel('Range Composition')
plt.title('Histogram of a random distribution')
plt.show()
plt.clf() # cleans up screen after displaying above hostogram

print()

print(min(s), max(s))