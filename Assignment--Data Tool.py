#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np


# In[2]:


raw_data =pd.read_csv('survey.csv')
raw_data.head()


# In[3]:


list(raw_data.columns)


# In[4]:


def treatment(df):

    treatment_df =df.groupby(["Country","state","treatment","mental_health_consequence"]).size().reset_index()
    return treatment_df


# In[5]:


df2 = treatment(raw_data)


# In[6]:


print(df2)


# In[7]:


df2.head()


# In[8]:


df2=df2.iloc[:15,:]
print(df2)


# In[9]:


plt.bar(df2.state,df2.mental_health_consequence)
plt.title("mental_health_consequence")
plt.xlabel("x axis label")
plt.ylabel("y axis label")
plt.show()


# In[13]:


plt.plot(df2.state,df2.treatment)
plt.title("treatment")
plt.xlabel("x axis label")
plt.ylabel("y axis label")
plt.show()


# In[14]:


plt.plot(df2.Country,df2.treatment)
plt.title("treatment")
plt.xlabel("x axis label")
plt.ylabel("y axis label")
plt.show()


# In[16]:


plt.bar(df2.Country,df2.mental_health_consequence)
plt.title("mental_health_consequence")
plt.xlabel("x axis label")
plt.ylabel("y axis label")
plt.show()


# In[ ]:




