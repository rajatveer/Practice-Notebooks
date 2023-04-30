#!/usr/bin/env python
# coding: utf-8

# In[301]:


import pandas as pd


# In[302]:


"""
que 1: Load the dataset into a pandas dataframe. Name the variable as “survey”.
"""
survey_dataset = pd.read_csv(r'C:\Users\rajat\Downloads\Survey Dataset - Technical Interview.csv')
survey_dataset


# In[303]:


survey_dataset.info()


# In[304]:


survey_dataset.describe(include='all').T


# In[305]:


"""
que 2: How many samples were collected on each day?
"""
survey_dataset.head(2)


# In[306]:


survey_dataset['collection_date'].value_counts()


# In[307]:


"""
que 3: What proportion of the total respondents were aged less than 45?
"""
survey_dataset.dtypes


# In[308]:


age_less_than_45=survey_dataset[survey_dataset['age']<'45']
age_less_than_45


# In[309]:


len(age_less_than_45)


# In[310]:


proportion=(len(age_less_than_45)/len(survey_dataset))*100
round(proportion,2)


# In[311]:


"""
que 4: Create a new column in the dataframe “age_group”. This column should contain the age group the 
respondent belongs to. The age groups are 18-25, 25-40, 40-55 and 55+. 
The dataframe should look like this after the column creation.
"""

survey_dataset['age'].value_counts()


# In[312]:


# create a copy of dataset
survey_dataset_copy= survey_dataset.copy()
survey_dataset_copy


# In[313]:


# create a new column in copy dataset
survey_dataset_copy.insert(14, 'age group', survey_dataset_copy.age)


# In[314]:


data1= survey_dataset_copy[(survey_dataset_copy['age']>='18')&(survey_dataset_copy['age']<'25')]
data1['age group']= '18-25'


# In[315]:


data1.head()


# In[316]:


data2= survey_dataset_copy[(survey_dataset_copy['age']>='25')&(survey_dataset_copy['age']<'40')]
data2['age group']= '25-40'


# In[317]:


data2.head()


# In[318]:


data3= survey_dataset_copy[(survey_dataset_copy['age']>='40')&(survey_dataset_copy['age']<'55')]
data3['age group']= '40-55'


# In[319]:


data3.head()


# In[320]:


data4= survey_dataset_copy[(survey_dataset_copy['age']>='55')]
data4['age group']= '55+'


# In[321]:


data4.head()


# In[322]:


new_data = pd.concat([data1, data2, data3, data4])
new_data.head()


# In[323]:


new_data


# In[324]:


new_data['age group'].unique()


# In[325]:


"""
que 5: How many samples were collected for each age-group? Which age-group had the most samples?
"""
new_data['age group'].value_counts()


# In[326]:


"""
que 6: What proportion of the respondents had opted for the RJD party in both the Vote_Now and the Past_Vote questions?
"""
survey_dataset.head(2)


# In[327]:


survey_dataset['Vote_Now'].value_counts()


# In[328]:


RJD_party = survey_dataset[(survey_dataset['Vote_Now']=='RJD')&(survey_dataset['Past_Vote']=='RJD')]
RJD_party


# In[329]:


len(RJD_party)


# In[330]:


proportion_of_rjd= (len(RJD_party)/len(survey_dataset))*100
round(proportion_of_rjd,2)


# In[331]:


"""
que 7: For each day of sample collection, determine the proportion of respondents who were fully 
satisfied with the performance of the CM. So if there were a total of 1000 samples on day 1 and 300 out 
of those said they were fully satisfied, then our answer for that day would be 0.3.
"""

survey_dataset.groupby(survey_dataset['CM_satisfaction']=='Fully Satisfied').collection_date.value_counts(normalize=False)


# In[332]:


round(146/(1333+146)*100, 2)


# In[333]:


a = survey_dataset[survey_dataset['CM_satisfaction']=='Fully Satisfied'].collection_date.value_counts()
print(a)


# In[334]:


b= survey_dataset['collection_date'].value_counts()
print(b)


# In[335]:


c = (a/b)*100
print(c)


# In[336]:


"""
que 8: In a similar fashion create a day-wise proportion of respondents that opted fully dissatisfied 
with their MLA. Create a line plot of the result with date on x-axis and proportions on the y-axis.
"""
survey_dataset.groupby(survey_dataset['MLA_satisfaction']=='Fully Dissatisfied').collection_date.value_counts()


# In[337]:


x1 = survey_dataset[survey_dataset['MLA_satisfaction']=='Fully Dissatisfied'].collection_date.value_counts()
print(pd.DataFrame(x1))


# In[338]:


y = survey_dataset.collection_date.value_counts()
print(y)


# In[339]:


z=(x1/y)*100
print(pd.DataFrame(z))


# In[340]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[341]:


plt.figure(figsize=(10,10))
sns.lineplot(data=z)
plt.show()


# In[342]:


"""
que 9:Create a pivot-table (or crosstab) with index as Past_Vote, Column as Vote_Now and cell 
values as the count of samples.
Answer - survey.pivot_table(index = 'Past_Vote', columns = 'Vote_Now', values = 'response_id', aggfunc = 'count')
"""
pd.crosstab(index=survey_dataset['Past_Vote'], columns=survey_dataset['Vote_Now'], values=survey_dataset['response_id'], aggfunc = 'count')


# In[343]:


"""
que 10: Repeat the above question with the cell values as the sum of “weight”.
"""
survey_dataset.head(2)


# In[344]:


pd.crosstab(index=survey_dataset['Past_Vote'], columns=survey_dataset['Vote_Now'], values=survey_dataset['weight'], aggfunc='sum')


# In[345]:


"""
que 11: Create a dataframe by performing a group by over age_group 
and calculate the count of total samples under each age_group.
"""
pd.DataFrame(new_data['age group'].value_counts())


# In[353]:


o= pd.DataFrame(new_data.groupby(['age group']).count())
o


# In[347]:


"""
que 12: Create a dataframe by performing a group by over age_group and finding the count of total 
samples for each age_group that opted for the JD(U) party in Vote_Now.
"""

new_data['Vote_Now'].value_counts()


# In[348]:


new_data.head(2)


# In[360]:


w = new_data[new_data['Vote_Now']=='JD(U)']
p = w.groupby(w['age group']).count()
p


# In[361]:


"""
que 13: Join/Merge the two dataframes from questions 12 and 11 with the common column as age_group.
"""
pd.merge(o, p, on = 'age group')


# In[ ]:




