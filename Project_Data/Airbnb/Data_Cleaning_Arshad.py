# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 22:21:32 2023

@author: User
"""
# Data Cleaning removing Duplicates, NA Values and replacing values

import pandas as pd

# reading csv file
df1 = pd.read_csv('listings.csv')

print(df1.head())

# different room types
df1_room_type= df1['room_type'].astype('category')
df1_room_type= df1['room_type'].value_counts()
print(df1_room_type)

#different property types
df1_property_type = df1['property_type'].value_counts().sum()
print((df1["property_type"].value_counts().sort_values(ascending=False)).head())
 

# filling NA Values
df1_fill_na = df1[["host_response_time","host_response_rate","host_acceptance_rate"]].fillna(0)

# replacing values in neighbourhood
df1_fill_na['neighbourhood'] = df1_fill_na['neighbourhood'].replace(['Almada, SetÃºbal, Portugal','Lisboa, Portugal'],[ 
                                                  'Almada, Setubal, Portugal','Lisbon, Portugal'])

# replacing t and f with yes and no in has_availability column
df1_fill_na['has_availability'] = df1_fill_na['has_availability'].replace(['t','f'],['Yes','No'])

# removing $ sign from price columns and calculating average price
df1_fill_na['price'] = df1_fill_na['price'].str.strip('$')
df1_fill_na['price'] = df1_fill_na['price'].str.replace(',','')
df1_fill_na['price'] = df1_fill_na['price'].astype('float')

# replacing t and f with yes and no in instant_bookable
df1_fill_na['instant_bookable'] = df1_fill_na['instant_bookable'].replace(['t','f'],['Yes','No'])









