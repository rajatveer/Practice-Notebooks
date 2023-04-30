#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


police_data = pd.read_csv("E:\Old_D\datasets\Police Data.csv")
police_data


# In[5]:


police_data.shape


# In[6]:


police_data.info()


# In[7]:


police_data.isnull().sum()


# In[8]:


police_data.describe(include = 'all')


# In[9]:


"""
que: remove the column that only contains missing values
"""

police_data.drop(columns=['country_name', 'search_type'], inplace=True)


# In[10]:


police_data.shape


# In[11]:


"""
que: For Speeding, were men r=or women stopped more often?
"""

speeding = police_data[police_data.violation== 'Speeding'].driver_gender.value_counts()

speeding


# In[12]:


"""
que: does gender affect whi gets searched during a stop?
"""

police_data.head(2)


# In[13]:


who_affect_during_search = police_data.groupby(['driver_gender', 'search_conducted']).count()
who_affect_during_search


# In[14]:


same_as_above = police_data.groupby('driver_gender').search_conducted.sum()
same_as_above


# In[15]:


"""
que: what is the mean stop duration?
"""
police_data.head()


# In[16]:


police_data.stop_duration.value_counts()


# In[17]:


(police_data['stop_duration'].map({'0-15 Min': 7.5, '16-30 Min': 24, '30+ Min':35, '120': 120 })).mean()


# In[18]:


"""
que: compare the age distribution of each violation
syntax: df.groupby('coln').coln.describe()
"""
police_data.groupby('violation').driver_age.describe()


# # ****Covid Dataset****

# In[19]:


covid_dataset = pd.read_csv("E:\Old_D\datasets\covid_19_data.csv")
covid_dataset


# In[20]:


covid_dataset.shape


# In[21]:


covid_dataset.info()


# In[22]:


covid_dataset.isnull().sum()


# In[23]:


covid_dataset.describe(include='all')


# In[24]:


import seaborn as sns


# In[25]:


"""
que: Draw heatmap of isnull
"""
sns.heatmap(covid_dataset.isnull())


# In[26]:


"""
que: show the number of confirmed, Deaths and REcovered cases in each region. 
"""

covid_dataset.groupby('Region').sum()


# In[27]:


covid_dataset.groupby('Region')['Confirmed', 'Deaths', 'Recovered'].sum()


# In[28]:


"""
que: remove all the records where confirmed cases is less than 10.
"""

covid_dataset.groupby('Region')['Confirmed'].sum()


# In[29]:


covid_dataset[~(covid_dataset.Confirmed<10)]


# In[30]:


"""
que: In which regin, maximum number of confirmed cases were recorded.
"""

covid_dataset.groupby('Region')['Confirmed'].sum().sort_values(ascending=False).head()


# In[31]:


"""
que: In which region, minimum number of deaths cases were recorded
"""

covid_dataset.head()
covid_dataset.groupby('Region')['Deaths'].sum().sort_values(ascending=True).head()


# In[32]:


"""
que: How many confirmed, deaths and recovered cases were reported from India till 29 April 2020
"""

covid_dataset.head()


# In[33]:


covid_dataset[covid_dataset.Region== 'India']


# In[34]:


"""
que: Sort the dataset wrt Confirmed cases in ascending order
"""

covid_dataset.sort_values(by=['Confirmed'], ascending=True)


# In[35]:


"""
que: sort the data wrt recovered cases in descending order
"""

covid_dataset.sort_values(by=['Recovered'], ascending=False)


# # ****London Housing Dataset****

# In[36]:


london_housing_dataset = pd.read_csv("E:\Old_D\datasets\London Housing Data.csv")
london_housing_dataset


# In[37]:


london_housing_dataset.shape


# In[38]:


london_housing_dataset.info()


# In[39]:


london_housing_dataset.isnull().sum()


# In[40]:


sns.heatmap(london_housing_dataset.isnull())


# In[41]:


london_housing_dataset.head()


# In[42]:


london_housing_dataset.no_of_crimes.value_counts()


# In[43]:


pd.DataFrame(london_housing_dataset['no_of_crimes'].unique())


# In[44]:


london_housing_dataset['houses_sold'].fillna(value= london_housing_dataset['houses_sold'].mean(), inplace=True)


# In[45]:


london_housing_dataset.isnull().sum()


# In[46]:


london_housing_dataset.loc[[2665]]


# In[47]:


"""
1)  que: Convert the datatype of dat ecolumn in to date-time format
"""
london_housing_dataset['date']= pd.to_datetime(london_housing_dataset['date'])
london_housing_dataset


# In[48]:


london_housing_dataset.head()


# In[49]:


"""
que 2: add column in dataset as year which consist year only
"""

london_housing_dataset.head()


# In[50]:


london_housing_dataset.dtypes


# In[51]:


london_housing_dataset['Year'] = london_housing_dataset['date'].dt.strftime('%Y')
london_housing_dataset.head()


# In[52]:


"""
que 3: add new column year in dataframe which contains years only.
"""
london_housing_dataset['month']= london_housing_dataset['date'].dt.month
london_housing_dataset


# In[53]:


"""
que 4: remove year and month form dataset
"""

london_housing_dataset.drop(columns=['Year', 'month'], inplace=True)


# In[54]:


london_housing_dataset.head()


# In[55]:


"""
que 5: show all the records where no. of crimes is 0, how many such records are there?
"""

zero_crime = london_housing_dataset[london_housing_dataset['no_of_crimes']==0]
pd.DataFrame(zero_crime)


# In[56]:


"""
que 6: what is the maximum and minimum average price per year in england
"""

area_england = london_housing_dataset[london_housing_dataset['area']== 'england']
area_england


# In[57]:


print('Minimum averange price in england', area_england['average_price'].min())
print('Maximum averange price in england', area_england['average_price'].max())


# In[58]:


"""
que 7: what is the maximum and minimum no of crimes recorded per area.
"""
max_crime_rate_per_area = london_housing_dataset.groupby('area')['no_of_crimes'].max()
max_crime_rate_per_area.sort_values(ascending=False)


# In[59]:


min_crime_rate_per_area = london_housing_dataset.groupby('area')['no_of_crimes'].min()
min_crime_rate_per_area.sort_values(ascending=False)


# In[60]:


"""
que 8: show the total count of records of each area, where average price is less than 100000,
"""

london_housing_dataset[london_housing_dataset['average_price']<100000]


# In[61]:


london_housing_dataset[london_housing_dataset['average_price']<100000].area.value_counts()


# # ****Indian Census Dataset****

# In[2]:


indian_census_dataset = pd.read_csv('E:\Old_D\datasets\India Census 2011.csv')
indian_census_dataset


# In[3]:


indian_census_dataset.info()


# In[4]:


indian_census_dataset.describe(include='all').T


# In[5]:


indian_census_dataset.isnull().sum()


# In[7]:


indian_census_dataset.dtypes


# In[8]:


"""
que 1: hide the indexes of the dataframe.
"""

indian_census_dataset.style.hide_index()


# In[22]:


"""
que 2: how can we set caption/heading on the dataframe.
"""

indian_census_dataset.style.set_caption('Indian Census 2011 dataset')


# In[25]:


"""
que: show all the records with districts - New dilhi, Lucknow and Jaipur
"""

indian_census_dataset[indian_census_dataset['District_name'].isin(['Pune'])]


# In[27]:


indian_census_dataset[indian_census_dataset.District_name=='Pune']


# In[32]:


indian_census_dataset[indian_census_dataset['District_name'].isin(['New Delhi', 'Pune'])]


# In[33]:


"""
que 4: calculate state wise total number of population.
"""

indian_census_dataset.head()


# In[51]:


population = indian_census_dataset.groupby('State_name').Population.sum()
population 


# In[42]:


"""
que: how many male workers were there in maharashtra state?
"""
indian_census_dataset.head()


# In[50]:


indian_census_dataset[indian_census_dataset.State_name == 'MAHARASHTRA'].sum()


# In[53]:


"""
que: How to set column as index of the dataframe.
"""

indian_census_dataset.set_index('District_code')


# In[ ]:




