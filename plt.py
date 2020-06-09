# working with matplotlib
import matplotlib.pyplot as plt

import numpy as np

s = np.random.normal(0, 10, 100)
x = [1991, 1995, 1999, 2004, 2009]
y = [14.5, 17.9, 21.3, 31.2, 45.8]

print(s)

plt.plot(x, y, color = 'turquoise') #.plt is better with dates on the x-axis
plt.show() # why do I get all the decimals from y

plt.hist(s, bins=10, color = 'purple') # bins to break up the data into appropriate boundaries
plt.show()
