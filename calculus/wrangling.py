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
child1 = data[data['parent_award_agency_name']=='FEDERAL BUREAU OF INVESTIGATION'].copy()
child2 = child1[child1['awarding_sub_agency_name']=='FEDERAL BUREAU OF INVESTIGATION'].copy()

# clears white space
child2['funding_office_name'].replace({' +':' '}, regex=True, inplace = True)

# consolidate all field offices into one entity
child2['funding_office_name'].replace({r'.*FIELD OFFICE':'FIELD OFFICES'},
                                      regex=True, inplace = True)

# pull out these columns for new data set
col_names = ['contract_transaction_unique_key', 'contract_award_unique_key',
             'award_id_piid', 'federal_action_obligation', 'total_dollars_obligated',
             'base_and_exercised_options_value', 'current_total_value_of_award',
             'base_and_all_options_value', 'potential_total_value_of_award',
             'action_date_fiscal_year', 'period_of_performance_start_date',
             'period_of_performance_current_end_date', 'awarding_office_name',
             'funding_office_name', 'recipient_name']

# new df with only fbi data and fewer columns
child3 = child1[col_names].copy()

# change name of certain columns
child3.rename(columns={''})