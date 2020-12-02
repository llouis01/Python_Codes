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
data = pd.read_csv('FY17.csv', low_memory=False)

# filter down by doj's favorite child
child2 = data[data['parent_award_agency_name']=='FEDERAL BUREAU OF INVESTIGATION'].copy()
child1 = child2[child2['awarding_sub_agency_name']=='FEDERAL BUREAU OF INVESTIGATION'].copy()

# clears white space
child1['funding_office_name'].replace({' +':' '}, regex=True, inplace = True)

# consolidate filed offices under one element
replace_with = [('FILED OFFICE', 'FIELD OFFICES')]


child1['funding_office_name'].replace({' FIELD OFFICE':'FIELD OFFICE'},
                                      regex=True, inplace = True)








# for old_name, new_name in replace_with:
#     child1.loc[child1['funding_office_name'].str.contains(old_name),
#                 'funding_office_name'] = new_name



print(child1.shape)