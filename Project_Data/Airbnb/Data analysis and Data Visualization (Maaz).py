# -*- coding: utf-8 -*-
"""
Created on Tue May  2 20:11:02 2023

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
print(room_type_dist)
print(room_type_dist_perc)

import matplotlib.pyplot as plt

# Create a bar chart of room type count distribution
room_type_dist.plot(kind='bar')
plt.title('Room Type Count Distribution')
plt.xlabel('Room Type')
plt.ylabel('Count')
plt.show()

# Create a pie chart of room type percentage distribution
room_type_dist_perc.plot(kind='pie')
plt.title('Room Type Percentage Distribution')
plt.ylabel('')
plt.show()


# average price per room type
df1['price'] = df1['price'].str.strip('$')
df1['price'] = df1['price'].str.replace(',', '')
df1['price'] = df1['price'].astype(float)

Avg_p_room= df1.groupby('room_type')['price'].mean()
print(Avg_p_room)


# Create a bar chart of average price per room type
Avg_p_room.plot(kind='bar')
plt.title('Average Price per Room Type')
plt.xlabel('Room Type')
plt.ylabel('Avg. Price')
plt.show()

#_________________________#

# single vs multi listings via listing per host

# Select rows with a 'host_listings_count' of 1 or greater than 1
single_listing = df1.loc[df1['host_listings_count'] == 1]
multi_listing = df1.loc[df1['host_listings_count'] > 1]

# Count the number of single and multi listings
single_listing_count = single_listing['host_listings_count'].count()
multi_listing_count = multi_listing['host_listings_count'].count()

print("Single Listing:", single_listing_count)
print("Multi Listing:", multi_listing_count )


# Create a bar chart for single and multi listings
plt.bar(['Single Listing', 'Multi Listing'], [single_listing_count, multi_listing_count])
plt.title('Count of Single and Multi Listings')
plt.xlabel('Listing Type')
plt.ylabel('Count')
plt.show()

#proportion of single to multi listing
total_count = df1['host_listings_count'].count()
prop_single = single_listing['host_listings_count'].count() / total_count
prop_multi = multi_listing['host_listings_count'].count() / total_count

print("Proportion of Single Listing:", prop_single)
print("Proportion of Multi Listing:", prop_multi)

# Create a pie chart for the proportion of single and multi listings
labels = ['Single Listing', 'Multi Listing']
sizes = [prop_single, prop_multi]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Proportion of Single and Multi Listings')
plt.show()

#_________________________#

#top host

# total listing per host

li_per_host = df1.groupby('host_name')['host_listings_count'].sum()
t_li_per_host = li_per_host.sort_values(ascending=False)

# Create a table of the top 10 hosts with the most listings
top_hosts = t_li_per_host.head(10)
top_hosts_df = top_hosts.to_frame().reset_index()
top_hosts_df.columns = ['Host Name', 'Total Listings']
print(top_hosts_df)

# Create a scatter chart
plt.scatter(x=top_hosts_df['Host Name'], y=top_hosts_df['Total Listings'])
plt.title('Top 10 Hosts with the Most Listings')
plt.xlabel('Host Name')
plt.ylabel('Total Listings')
plt.show()

#__________________________#