#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[8]:


covid_df=pd.read_csv("C:\\Users\\NAYAN DINKAR JAGTAP\\Desktop\\DSBDA MINI PROJECT\\archive\\covid_19_india.csv")
covid_df


# In[9]:


covid_df.head(10)


# In[10]:


covid_df.info()


# In[11]:


covid_df.describe()


# In[12]:


vaccine_df=pd.read_csv("C:\\Users\\NAYAN DINKAR JAGTAP\\Desktop\\DSBDA MINI PROJECT\\archive\\covid_vaccine_statewise.csv")
vaccine_df


# In[13]:


vaccine_df.head(10)


# In[14]:


vaccine_df.describe()


# In[15]:


vaccine_df.info()


# In[16]:


vaccine_df.columns


# In[17]:


vaccine_df[['State','First Dose Administered']]


# In[18]:


vaccine_df[['State','Second Dose Administered']]


# In[19]:


df2 = vaccine_df.groupby(['State']).sum()
df2['First Dose Administered']


# In[20]:


df2 = vaccine_df.groupby(['State']).sum()
df2['Second Dose Administered']


# In[22]:


male=vaccination["Male(Individuals Vaccinated)"].sum()
print(male)


# In[23]:


female=vaccination["Female(Individuals Vaccinated)"].sum()
print(female)


# In[24]:


male=vaccination["Male(Individuals Vaccinated)"].sum()
female=vaccination["Female(Individuals Vaccinated)"].sum()
px.pie(names=["Male","Female"],values=[male,female],title="Male and Female Vaccination")


# In[25]:


male=vaccination["Male(Individuals Vaccinated)"].sum()
female=vaccination["Female(Individuals Vaccinated)"].sum()
px.pie(names=["Male","Female"],values=[male,female],title="Male and Female Vaccination" )


# In[ ]:




