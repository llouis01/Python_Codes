# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 12:48:35 2020

@author: CMoi
"""

import pandas as pd
df = pd.DataFrame({'pre_decrease_addfund':[7, 50, 0, 44, 41],
                  'decrease':[0, 43, 0, 0, 41],
                  'add_fund':[5, 0, 38, 10, 97],
                  'total':[12, 7, 38, 54, 97]})

print(df)
print('\n')

df['all_action'] = df['decrease'] + df['add_fund']
print(df['all_action'])

df['original_base'] = df['all_action'] - df['total']
print(df['original_base'])
