# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 13:12:22 2020

@author: Loube
"""


'''
Toyota
> properties
>>color, engine, location

>get or set properties
>>some properties can only get

> methods
>> does something to the object (drive, wash)
>>>after driving the car, location will update after driving it. As
>>>well as the wash method.
'''

# x = []
# dir(x)
# x.append(2)
# x.

import matplotlib.pyplot as plt

fig, ax = plt.subplots() 
ax.plot([0,1,2,3])
fig.suptitle('Test')
plt.show()
print('fig type: '+ str(type(fig)) + '\n')
print('ax type: '+ str(type(fig)) + '\n')

#### 
fig, ax = plt.subplots(nrows = 2, ncols = 2)
ax[0,0].plot([0,1,2,3])
ax[0,1].plot([0,1,3,2])
ax[1,0].plot([3,2,1,0])
ax[1,1].plot([3,1,2,0])

fig.suptitle('Test')
plt.show()

print('fig type: '+ str(type(fig)) + '\n')
print('ax type: '+ str(type(ax[0,0])) + '\n')
