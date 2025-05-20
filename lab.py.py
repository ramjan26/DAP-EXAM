#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('C:/Users/Acer/Downloads/Electric_Vehicle_Population_Data.csv/Electric_Vehicle_Population_Data.csv')
df
df.shape
df.info(absq-
df.isnull().sum()
df = df.dropna()
df.isnull().sum()
ev_adoption_by_year = df['Model Year'].value_counts().sort_index()
plt.figure(figsize=(14,5))
ax = sns.barplot(data=df, x=ev_adoption_by_year.index, y= ev_adoption_by_year.values)
ax.bar_label(ax.containers[0], color="red")
plt.xlabel("Model Year")
plt.ylabel("Number of Vehicles Registered")
plt.title("EV growth year wise")
# Top 3 counties based on EV registrations and then analyze the distribution of EVs within the cities of those counties
ev_country_distribution = df['Country'].value_counts()
top_countries = ev_country_distribution.head(3).index
# filtering the dataset for these top counties
top_countries_data = df[df['Country'].isin(top_countries)]
top_countries_data
# analyzing the distribution of EVs within the cities of these top counties
ev_city_distribution_top_countries = top_countries_data.groupby(['Country', 'City']).size().sort_values(ascending=False).reset_index(name='Number of Vehicles')
ev_city_distribution_top_countries
# visualize the top 10 cities across these counties
top_cities = ev_city_distribution_top_countries.head(10)
top_cities
plt.figure(figsize=(12, 4))
ax1 = sns.barplot(x='Number of Vehicles', y='City', data=top_cities)
ax1.bar_label(ax1.containers[0], color="red")
plt.title('Top Cities in Top Countries by EV Registrations')
plt.xlabel('Number of Vehicles Registered')
plt.ylabel('City')
plt.legend(top_cities["Country"])
# Top 10 brands
brand = df["Make"].value_counts().head(10)
plt.figure(figsize=(14,4))
ax3 = sns.barplot(x= brand.index, y = brand.values)
ax3.bar_label(ax3.containers[0])
plt.xlabel("Brand")
plt.ylabel("Count")
plt.title("Top 10 popular brand")


# In[ ]:





# In[ ]:







