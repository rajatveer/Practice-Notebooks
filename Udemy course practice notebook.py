#!/usr/bin/env python
# coding: utf-8

# In[97]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[98]:


udemy_dataset = pd.read_csv(r"E:\Old_D\datasets\Udemy Courses.csv")
udemy_dataset


# In[99]:


udemy_dataset.info()


# In[100]:


udemy_dataset.isnull().sum()


# In[101]:


udemy_dataset.describe(include='all').T


# In[102]:


"""
que 1: What are all different subjects for which udemy is offering courses?
"""
udemy_dataset['subject'].unique()


# In[103]:


"""
que 2: which subject has maximum number of courses
"""
udemy_dataset.head(2)


# In[104]:


udemy_dataset['course_id'].groupby(udemy_dataset.subject).value_counts()


# In[105]:


udemy_dataset['subject'].value_counts()


# In[106]:


"""
que 3: show all the courses which are free of cost
"""

udemy_dataset.tail()

free_courses= udemy_dataset[udemy_dataset['price']== 'Free']
free_courses


# In[107]:


# free couses number of counts per subject
free_courses['subject'].value_counts()


# In[108]:


"""
que 4: show all the courses which are paid
"""

paid_courses = udemy_dataset[udemy_dataset['price']!= 'Free']
paid_courses


# In[109]:


# paid couses number of counts per subject
paid_courses['subject'].value_counts()


# In[110]:


"""
que 5: which are top selling courses
"""
top_Selling_courses = udemy_dataset.sort_values(['num_subscribers'], ascending=False)
top_Selling_courses


# In[111]:


"""
que 6: which are least selling courses
"""

least_selling_courses = udemy_dataset.sort_values(['num_subscribers'], ascending=True)
least_selling_courses


# In[112]:


paid_courses.dtypes


# In[113]:


paid_courses['price']= pd.to_numeric(paid_courses['price'])


# In[114]:


"""
que 7: show all courses of graphic design where the price is below 100?
"""
courses_below_100 = paid_courses[paid_courses['price']< 100]
courses_below_100


# In[115]:


courses_below_100['price'].max()


# In[116]:


"""
que 8: list all the courses that are releated with python.
"""

udemy_dataset.head()


# In[117]:


courses_contains_python= udemy_dataset[udemy_dataset['course_title'].str.contains('Python')]
courses_contains_python


# In[118]:


"""
que 9: what are the courses published in year 2015?
"""

courses_in_2015= udemy_dataset[udemy_dataset['published_timestamp'].str.contains('2015')]
courses_in_2015


# In[119]:


"""
que 9: what are the courses published in year 2015?
"""

# convert to datetime
udemy_dataset['datetime'] = pd.to_datetime(udemy_dataset.published_timestamp)

# extract to year
udemy_dataset['year'] = udemy_dataset['datetime'].dt.year
#final query

udemy_dataset[udemy_dataset.year==2015]


# In[120]:


"""
que 10: what are the max number of subscibers for each level of course
"""

udemy_dataset.groupby('level')['num_subscribers'].max()


# In[ ]:




