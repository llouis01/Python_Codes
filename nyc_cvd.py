# NYC Covid-19 Daily Count

import matplotlib.pyplot as plt
import pandas as pd

nyc_avg = pd.read_csv("C:\\Users\\Loube\\Desktop\\nyc_avg.csv")
print(nyc_avg)

plt.plot(nyc_avg['MONTH'], nyc_avg['AVG_death'], c ='PURPLE', marker = 'o')
plt.title('Average Monthly COVID-19 Fatality Count in NYC')
plt.xlabel('Month')
plt.ylabel('Average Death Count')
plt.grid(True)
plt.show()