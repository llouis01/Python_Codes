# logical operator

import numpy as np
import pandas as pd

htwt = pd.read_csv("C:\\Users\\Loube\\Desktop\\htwt.csv").head(10)

print(htwt)
print()

print(np.logical_and(htwt['Height']<68, htwt['Weight']<220)) # check using operators if height <68 & weight<220
print(np.logical_not(htwt['Height']>68.00)) # check if height !> 68.00
print(np.logical_or(htwt['Height']<69, htwt['Height']>67)) # with or bool op, if there's a true, value = true
print()

giant = htwt['Height']>68.5 # bool var for height > 68.5 in htwt dataframe
print(htwt[giant]) # subset htwt only for values > 68.5
print()

print(htwt[htwt['Weight']<220]) # or do it in one line with htwt where htwt is < 220