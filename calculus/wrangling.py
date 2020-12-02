# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:08:11 2020

@author: Loube
"""

import pandas as pd
import os

##### find files in this directory
os.chdir('C:\\Users\\Loube\\Documents\\FY_files')

##### import and cleanse data
data = pd.read_csv('FY17.csv') 

##### 