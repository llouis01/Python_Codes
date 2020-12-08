# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:08:11 2020

@author: Loube
"""

import pandas as pd
import os
import numpy as np

##### find files in this directory
os.chdir('C:\\Users\\Loube\\Documents\\FY_files')


##### import and cleanse data
data = pd.read_csv('FY17.csv', low_memory=False)

# filter down by doj's favorite child
child1 = data[data['parent_award_agency_name']=='FEDERAL BUREAU OF INVESTIGATION'].copy()
child2 = child1[child1['awarding_sub_agency_name']=='FEDERAL BUREAU OF INVESTIGATION'].copy()

# clears white space
child2['funding_office_name'].replace({' +':' '}, regex=True, inplace = True)
child2['awarding_office_name'].replace({' +':' '}, regex=True, inplace = True)

# consolidate all field offices into one entity
child2['funding_office_name'].replace({r'.*FIELD OFFICE':'FIELD OFFICES'},
                                      regex=True, inplace = True)
child2['awarding_office_name'].replace({r'.*FIELD OFFICE':'FIELD OFFICES'},
                                      regex=True, inplace = True)

# pull out these columns for new data set
col_names = ['contract_transaction_unique_key', 'contract_award_unique_key',
             'award_id_piid', 'federal_action_obligation',
             'total_dollars_obligated','action_date_fiscal_year',
             'period_of_performance_start_date', 'awarding_office_name',
             'period_of_performance_current_end_date','funding_office_name',
             'recipient_name']

# new df with only fbi data and fewer columns
child3 = child2[col_names].copy().fillna(0)

# change name of certain columns
child3.rename(columns={'award_id_piid':'Document Number',
                       'federal_action_obligation':'Obligation',
                       'action_date_fiscal_year':'Fiscal Year',
                       'recipient_name':'Vendor',
                       'total_dollars_obligated':'Total Obligation',
                       'awarding_office_name':'Awarding Office',
                       'funding_office_name':'Funding Office'}, inplace=True)

# add new columns based on existing columns
child3['De-Obligation'] = np.where(child3['Obligation']<0,
                                    child3['Obligation'], 0)

child3['De-Obligation'] = child3['De-Obligation'].apply(lambda x: x * -1 if x < 0 else 0)

child3['Additional Obligation'] = child3['Obligation'].apply(lambda x: 0 if x < 0 else x)


# obtain pre-deob and additional obligation base amount
child3['Original Base Amount'] = child3['Obligation'] - child3['Total Obligation']
child3['Original Base Amount'] = child3['Original Base Amount'].apply(lambda x: x * -1 if x < 0 else x)
child3['All_Total'] = child3['Original Base Amount'] - child3['De-Obligation']

# re-arrange columns
col_namez = ['contract_transaction_unique_key', 'contract_award_unique_key',
             'Document Number', 'Original Base Amount', 'De-Obligation',
             'Additional Obligation', 'All_Total', 'Awarding Office', 'Funding Office',
             'Fiscal Year', 'Vendor', 'period_of_performance_start_date',
             'period_of_performance_current_end_date']

# type convert FY to string to prevent groupby calculation
child3['Fiscal Year'] = child3['Fiscal Year'].astype(str)

# copy final dataframe into new variable
final_frame = child3[col_namez].copy()
award_off = final_frame.groupby(['Awarding Office'])['All_Total'].sum()

# write to excel workbook
writer = pd.ExcelWriter('USA_17.xlsx')
final_frame.to_excel(writer)
writer.save()