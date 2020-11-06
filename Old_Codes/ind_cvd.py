# index nyc_cvd.csv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

nycvd = pd.read_csv("C:\\Users\\Loube\\Desktop\\nyc_cvd1.csv", index_col=0)

for dates, data in nycvd.iterrows():
    print(dates)
    print(data)
    print()