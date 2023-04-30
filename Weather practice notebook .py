#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


weather_data = pd.read_csv('E:\Old_D\datasets\Weather Data.csv')
weather_data


# In[3]:


weather_data.info()


# In[5]:


weather_data.describe().T


# In[6]:


weather_data.head()


# In[7]:


weather_data.tail()


# In[8]:


"""
How to analyze dataframe?
1) get the head.
2) get the shape.
3) get the index.
4) get the columns
5) get the data types
6) get the umber of unique
"""


# In[9]:


# head
weather_data.head()


# In[11]:


# shape
weather_data.shape


# In[12]:


# index
weather_data.index


# In[23]:


# columns
weather_data.columns


# In[14]:


#data types
weather_data.dtypes


# In[19]:


# number of unique
weather_data.nunique()


# In[21]:


# unique
weather_data['Visibility_km'].unique()


# In[24]:


# count
weather_data.count()


# In[25]:


# value counts
weather_data.value_counts()


# In[30]:


# get the value counts of perticular column
weather_data_visibility_km= pd.DataFrame(weather_data['Visibility_km'].value_counts())
weather_data_visibility_km


# In[31]:


# Que: Find all the unique wind speed values in the data.
wind_speed_unique = weather_data['Wind Speed_km/h'].unique()
wind_speed_unique


# In[47]:


# que: Find the number of times when the weather is exactly clear.
Exact_clear_weather = weather_data['Weather'].value_counts()['Clear']
Exact_clear_weather


# In[48]:


# que: find the number of times when the weather is exactly clear using groupby
Exact_clear_weather1 = weather_data['Weather'].value_counts()
df = weather_data[weather_data.Weather =='Clear']
df.groupby('Weather').get_group('Clear')


# In[56]:


df = weather_data[weather_data.Weather =='Clear']
df


# In[50]:


# Que: Fidn the number of times when the 'Wind Speed was exactly 4km/h.'
wind_speed_exactly_4 = weather_data['Wind Speed_km/h'].unique()[4]
wind_speed_exactly_4

"""
or weather_data[weather_data.Wind Speed_km/h == 4]

data[data.column=value]
"""


# In[55]:


# que: find out all the nul values in the data
null_values_in_the_data = weather_data.isnull().value_counts()
null_values_in_the_data


# In[57]:


null_values_in_the_data1 = weather_data.isnull().sum()
null_values_in_the_data1


# In[62]:


# que:  Rename the column name 'Weather' of the dataframe to 'Weather Condition'

weather_data.rename(columns = {'Weather':'Weather_Condition'})


# In[63]:


# que: What is the mean visibility
mean_visibility = weather_data['Visibility_km'].mean()
mean_visibility


# In[64]:


# que: What is the standard deviation of pressure in this data

std_of_pressure = weather_data['Press_kPa'].std()
std_of_pressure


# In[65]:


# que: What is the variance of Relative Humidity in thid data

var_of_relative_humidity = weather_data['Rel Hum_%'].var()
var_of_relative_humidity


# In[82]:


# que: Find alll instances when snow was recorded. 
snow_recorded = weather_data['Weather'].value_counts()['Snow']
snow_recorded = weather_data[weather_data['Weather'].str.contains('Snow')]
snow_recorded


# In[94]:


# que: Find all instances when Wind speed is above 24 and visibility is 25.
wind_and_visibility = weather_data[(weather_data['Wind Speed_km/h'] >24) & (weather_data['Visibility_km'] ==25)]
wind_and_visibility


# In[90]:


(weather_data['Wind Speed_km/h'] >24) & (weather_data['Visibility_km'] ==25)


# In[84]:


weather_data[weather_data['Visibility_km'] == 25]


# In[100]:


# que: what is the mean value of each column against each Weather Condidtion?

weather_data.groupby('Weather').mean()


# In[112]:


minimum_values= weather_data.groupby('Weather').min()
minimum_values


# In[113]:


maximum_value= weather_data.groupby('Weather').max()
maximum_value


# In[114]:


# que: what is the minimum and maximum value of each colmn against each weather condition

min_and_max= list[(weather_data.groupby('Weather').min()), ((weather_data.groupby('Weather').max()))]
min_and_max


# In[115]:


# que: Show all the records where weather condition is Fog

fog = weather_data[weather_data['Weather'].str.contains('Fog')]
fog


# In[124]:


# que: find all instances when Weather is CLear or visbility is above 40.

clear_and_visibility= weather_data[(weather_data['Weather'].str.contains('Clear'))| (weather_data['Visibility_km']>40)]
clear_and_visibility


# In[125]:


"""
que: Find all instances when 
A: Weather is Claer and Relative humidity is gretaer than 50
    or 
B: visibility is above 40
"""

A_or_B= weather_data[((weather_data['Weather']=='Clear') & (weather_data['Rel Hum_%']>50)) | (weather_data['Visibility_km']>40)]
A_or_B

