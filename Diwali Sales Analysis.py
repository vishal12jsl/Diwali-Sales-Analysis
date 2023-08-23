#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv("d1.csv",encoding_errors='ignore')


# In[3]:


df


# In[4]:


df.shape


# In[5]:


df.info()


# In[6]:


df.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[7]:


df.info()


# In[8]:


df.isnull().sum()


# In[9]:


df.dropna(inplace=True)


# In[10]:


df.info()


# In[11]:


df['Amount']=df['Amount'].astype("int")


# In[12]:


df['Amount'].dtypes


# In[13]:


df.columns


# In[14]:


df.describe()


# ## EDA

# In[15]:


sns.countplot(x='Gender',data=df)


# In[16]:


df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


# In[17]:


sales_gen=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x="Gender",y="Amount",data=sales_gen)


# ## from the above graphs most of the buyers are females and purchasing power of females are greater than male

# ## AGE

# In[18]:


df.columns


# In[19]:


ax=sns.countplot(x='Age Group',data=df,hue='Gender')


# ## from the above graph it is clearly evident that most number of shopping enthusiast are in between 26-35 

# In[20]:


sales_age=df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


# In[21]:


sns.barplot(x='Age Group',y='Amount',data=sales_age)


# ## State

# In[22]:


df.columns


# In[23]:


sales_state=df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)


# In[24]:


sns.set(rc={'figure.figsize':(25,8)})
sns.barplot(x='State',y='Orders',data=sales_state)


# ## from the above graphs we can see that most of the total sales /amount are from uttarpradesh maharashtra and karnataka

# ## marital status

# In[25]:


df.columns


# In[26]:


ux=sns.countplot(x='Marital_Status',data=df)
sns.set(rc={'figure.figsize':(8,5)})


# In[27]:


sales_state=df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


# In[28]:


sns.barplot(x='Marital_Status',y='Amount',hue='Gender',data=sales_state)


# *from the above graphs most of the buyers are married(women)and they have high purchasing power*

# ## Occupation

# In[29]:


bx=sns.countplot(data=df,x='Occupation')
sns.set(rc={'figure.figsize':(18,5)})


# In[30]:


sales_state=df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(data=sales_state,x='Occupation',y='Amount')
sns.set(rc={'figure.figsize':(20,5)})


# *from above graphs we can see that most of the buyers are working in IT,Healthcare,Aviation*

# In[31]:


df.columns


# ## product category

# In[32]:


sns.countplot(data=df,x='Product_Category')
sns.set(rc={'figure.figsize':(25,8)})


# In[34]:


sales_state=df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

#sns.set(rc={'figure.figsize':(20,5)})

sns.barplot(data=sales_state,x='Product_Category',y='Amount')


# *from the above graphs most sold products are from food , clothing and electronics*

# In[35]:


sales_state=df.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.barplot(data=sales_state,x='Product_ID',y='Orders')


# ## Conclusion:- Married women in the age group 26-35 from UP working it IT ,healthcare and avaiation are more likely to buy products from food ,clothing and electronics

# In[ ]:




