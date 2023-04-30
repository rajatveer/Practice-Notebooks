#!/usr/bin/env python
# coding: utf-8

# In[69]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[70]:


cars_data = pd.read_csv('E:\Old_D\datasets\cars.csv')
cars_data


# In[71]:


cars_data.shape


# In[72]:


"""
que 1: Find all Null values in the dataset. If Null fill with mean of that column.
"""

cars_data.isnull().sum()


# In[73]:


# replace null rating values with mean of that colunm. 

cars_data['RATING'].fillna(value= cars_data['RATING'].mean(), inplace =True)


# In[74]:


# check if we successfully replaced with mean
cars_data.isnull().sum()


# In[75]:


"""
que 2: Check wha are the different types of makes are there in the dataset. FInd occurrence for each make?
"""

cars_data['Make'].unique()


# In[76]:


cars_data['Make'].value_counts()


# In[77]:


"""
que 3: show all the records where size is compact
"""
cars_data.loc[cars_data['Size']== 'COMPACT']


# In[78]:


"""
que 3: show all the records where size is compact or Two wheeler
"""

cars_data[cars_data['Size'].isin(['COMPACT', 'TWO-SEATER'])]


# In[80]:


"""
que 4: remove all the rocrds where (kW) is less than 40
"""

cars_data[~(cars_data["(kW)"]<40)]


# In[92]:


"""
que 5: increase all the values of CITY (kWh/100 km) column by 3
"""
pd.DataFrame(cars_data["CITY (kWh/100 km)"].apply(lambda x: x+3))


# In[ ]:




