#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


netflix_dataset = pd.read_csv(r'C:\Users\rajat\OneDrive\Desktop\Netflix_dataset.csv')
netflix_dataset


# In[3]:


netflix_dataset.head()


# In[4]:


netflix_dataset.info()


# In[5]:


netflix_dataset.isnull().sum()


# In[6]:


netflix_dataset.describe(include='all').T


# In[7]:


netflix_dataset.tail()


# In[8]:


netflix_dataset.shape


# In[9]:


netflix_dataset.size


# In[10]:


netflix_dataset.columns


# In[11]:


netflix_dataset.dtypes


# In[12]:


"""
que 1: is there any duplicate record in the dataset? if yes then remove it.
"""

duplicate = netflix_dataset[netflix_dataset.duplicated()]
duplicate


# In[13]:


drop_duplicate = netflix_dataset.drop_duplicates(inplace=True)
drop_duplicate


# In[14]:


netflix_dataset.shape


# In[15]:


"""
que 2: is there any null values present in any column? show with heatmap
"""

null_values = netflix_dataset.isnull().sum()
null_values


# In[16]:


sns.heatmap(netflix_dataset.isnull())


# In[17]:


"""
que 3: for house of cards what is the show id and who os the director of this show?
"""
netflix_dataset[netflix_dataset['Title'].str.contains('House of Cards')]


# In[18]:


netflix_dataset[netflix_dataset['Title'].isin(['House of Cards'])]


# In[19]:


"""
que 4: In which year highest number of the TV shows and Movies were released? Show with bar graph.
"""
# release date to datettime
netflix_dataset['abc'] = netflix_dataset['Release_Date'].str.split()
netflix_dataset


# In[20]:


netflix_dataset.drop(columns=['abc'], inplace=True)


# In[21]:


netflix_dataset.head()


# In[27]:


netflix_dataset['date']=netflix_dataset['Release_Date'].str.split(',')
netflix_dataset['year'] = netflix_dataset['date'].str.split(',')
netflix_dataset


# In[28]:


netflix_dataset.drop(columns=['date', 'year'], inplace=True)


# In[30]:


netflix_dataset['datetime']= pd.to_datetime(netflix_dataset['Release_Date'])
netflix_dataset


# In[35]:


year_value_counts= netflix_dataset['year'].value_counts()
year_value_counts


# In[38]:


year_value_counts.plot(kind='bar')


# In[40]:


"""
que 5: how many movies and tv shows are in the dataset? show with bar graph.
"""
netflix_dataset.head()    


# In[41]:


netflix_dataset['Category'].value_counts()


# In[42]:


netflix_dataset['Category'].value_counts().plot(kind='bar')


# In[45]:


sns.countplot(netflix_dataset['Category'])


# In[46]:


"""
que 6: show all the movies that were relesed in year 2000.
"""
netflix_dataset.head(2)


# In[48]:


netflix_dataset[netflix_dataset['year']==2000.0]


# In[62]:


"""
que 7:  Show only the Titles of all TV Shows that were released in India only.
"""
country_India=netflix_dataset[netflix_dataset['Country']=='India']
country_India['Category'].value_counts()


# In[65]:


country_India[country_India['Category']=='TV Show']


# In[66]:


"""
que 8: Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ?
"""

netflix_dataset.head(2)


# In[93]:


netflix_dataset['Director'].value_counts().head(10)


# In[100]:


"""
que 9:Show all the Records, where "Category is Movie and Type is Comedies" or "Country is United Kingdom".
"""
netflix_dataset.head(2)


# In[169]:


netflix_dataset[(netflix_dataset['Category']=='Movie')&(netflix_dataset['Type'].str.contains('Comedies')) | (netflix_dataset['Country']=='United  Kingdom')]


# In[113]:


"""
que 10: In how many movies/shows, Tom Cruise was cast ?
"""
netflix_dataset['Cast'].str.contains('Tom Cruise').value_counts()


# In[114]:


"""
que 11: What are the different Ratings defined by Netflix ?
"""
netflix_dataset['Rating'].value_counts()


# In[124]:


"""
que 12: How many Movies got the 'TV-14' rating, in Canada ?
"""
movie_canada= netflix_dataset[(netflix_dataset['Country']=='Canada') & (netflix_dataset['Rating']=='TV-14')]
movie_canada[movie_canada['Category']=='Movie']


# In[172]:


"""
que 13: How many TV Shows got the 'R' rating, after year 2018 ?
"""
tv_shows_2018 =netflix_dataset[(netflix_dataset['Rating']=='R')&(netflix_dataset['year']>2018)].sort_values(by=['year'], ascending= True)
tv_shows_2018[tv_shows_2018['Category']=='TV Show']


# In[177]:


"""
que 14:  What is the maximum duration of a Movie/Show on Netflix ?
"""
netflix_dataset['Duration'].value_counts().max()


# In[175]:


netflix_dataset['Duration'].max()


# In[174]:


netflix_dataset[['min', 'unit']]= netflix_dataset['Duration'].str.split(' ', expand=True)
netflix_dataset['min'].max()


# In[147]:


"""
que 15:  Which individual country has the Highest No. of TV Shows ?
"""
Tv_shows= netflix_dataset[netflix_dataset['Category']=='TV Show']
Tv_shows['Country'].value_counts()


# In[158]:


"""
que 16: How can we sort the dataset by Year ?
"""
netflix_dataset.sort_values(by=['year'], ascending=True)


# In[164]:


"""
que 17: Find all the instances where: Category is 'Movie' and Type is 'Dramas' or Category is 
'TV Show' & Type is 'Kids' TV'.
"""
moviedrama_or_tvkids = netflix_dataset[((netflix_dataset['Category']=='Movie')& (netflix_dataset['Type'].str.contains('Dramas')))
                                  |((netflix_dataset['Category']=='TV Show')& (netflix_dataset['Type'].str.contains('Kids')))]
moviedrama_or_tvkids


# In[ ]:




