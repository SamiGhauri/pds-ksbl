# -*- coding: utf-8 -*-
"""
Created on Mon May  1 14:36:34 2023

@author: Muhammad Maaz Maqsood
"""

import pandas as pd

df1= pd.read_csv('listings_Q2.csv')
df2=pd.read_csv('calendar_Q2.csv')
# print(df1.head())
# print(df2.head())


# Count of room types & %
df1['room_type']= df1['room_type'].astype('category')
room_type_dist= df1['room_type'].value_counts()
room_type_dist_perc= df1['room_type'].value_counts(normalize=True)
# print(room_type_dist)
# print(room_type_dist_perc)
# average price per room type
df1['price'] = df1['price'].str.strip('$')
df1['price'] = df1['price'].str.replace(',', '')
df1['price'] = df1['price'].astype(float)
# x= df1.info()
# print(x)
# Avg_p_room= df1.groupby('room_type')['price'].mean()
# print(Avg_p_room)

# __________________#

# single vs multi listings via listing per host

# Select rows with a 'host_listings_count' of 1 or greater than 1
single_listing = df1.loc[df1['host_listings_count'] == 1]
multi_listing = df1.loc[df1['host_listings_count'] > 1]

# print("Single Listing:")
# print(single_listing['host_listings_count'].count())  # count the number of rows
# print("Multi Listing:")
# print(multi_listing['host_listings_count'].count())  # count the number of rows

total_count = df1['host_listings_count'].count()
prop_single = single_listing['host_listings_count'].count() / total_count
prop_multi = multi_listing['host_listings_count'].count() / total_count

# print("Proportion of Single Listing:", prop_single)
# print("Proportion of Multi Listing:", prop_multi)

#______________#

#top host

# total listing per host

li_per_host = df1.groupby('host_name')['host_listings_count'].sum()
t_li_per_host = li_per_host.sort_values(ascending=False)

# print("Top 10 Hosts with the Most Listings:")
# print(t_li_per_host.head(10))