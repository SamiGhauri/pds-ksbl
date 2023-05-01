# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 22:21:32 2023

@author: User
"""

import pandas as pd

# reading csv file
df1 = pd.read_csv('listings.csv')
print(df1[['bathrooms','bathrooms_text']])

df1['bathrooms_text']=df1['bathrooms_text'].str.strip()

df1['bathrooms_text']=df1['bathrooms_text'].str.split()

df1['bathrooms']=df1['bathrooms_text'].str[0]
# df1['bathrooms']=df1['bathrooms'].astype('float')
print(df1['bathrooms'])





# # filling NA Values with zero
# df1_fill_na = df1.fillna(0)

# # replacing values in neighbourhood
# df1_fill_na['neighbourhood'] = df1_fill_na['neighbourhood'].replace(['Almada, SetÃºbal, Portugal','Lisboa, Portugal'],[ 
#                                                   'Almada, Setubal, Portugal','Lisbon, Portugal'])

# # changing lisboa to lisbon in neihbourhood_group_clensed
# df1_fill_na['neighbourhood_group_cleansed'] = df1_fill_na['neighbourhood_group_cleansed'].replace('lisboa','lisbon')


# # replacing t and f with yes and no in has_availability column
# df1_fill_na['has_availability'] = df1_fill_na['has_availability'].replace(['t','f'],['Yes','No'])

# # removing $ sign from price columns
# df1_fill_na['price'] = df1_fill_na['price'].str.strip('$')
# df1_fill_na['price'] = df1_fill_na['price'].str.replace(',','')
# df1_fill_na['price'] = df1_fill_na['price'].astype('float')

# # replacing t and f with yes and no in instant_bookable
# df1_fill_na['instant_bookable'] = df1_fill_na['instant_bookable'].replace(['t','f'],['Yes','No'])

# #findind duplicates values
# column_names = ['host_name','host_location','neighbourhood','property_type',
#                 'room_type']

# df1_drop_duplicates = df1_fill_na.drop_duplicates(subset = column_names, 
#                                                   keep = False, inplace = True)

# # save the updated csv file
# df1_fill_na.to_csv('listing_updated.csv', index = False)




