# linear regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

htwt = pd.read_csv("C:\\Users\\Loube\\Desktop\\htwt.csv").head(10)

print(htwt)
print()

htwt_ = htwt.loc[:, ['Height', 'Weight']]
print()
print(htwt_)
print()

# htwt_.plot(x= 'Weight', y= 'Height')
plt.scatter(htwt_['Height'], htwt_['Weight'])
plt.title('Scatter of Height and Weight')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.show()
