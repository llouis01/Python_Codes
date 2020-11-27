# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:38:57 2018

@author: jrbrad
"""

data = [['Jun',4.3],['Jul',4.3],['Aug',4.4],['Sep',4.2],['Oct',4.1],['Nov',4.1],['Dec',4.1],['Jan',4.1],['Feb',4.1],['Mar',4.1],['Apr',3.9],['May',3.8],]

""" Program you solution to this assignment below using 
    the variable names as defined below                 """

import matplotlib.pyplot as plt
    
x = [datum[0] for datum in data]
    
    
y = [datum[1] for datum in data]

plt.plot(y)
plt.suptitle('U.S. Unemployment Rate')
plt.xlabel('Unemployment Rate')
plt.ylabel('Month')
plt.show()