#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import os


# In[12]:


#path = os.path.join('C:\\','Users','DELL','Downloads','archive (2)','cost of living.csv')
living = pd.read_csv("C:\\Users\\DELL\\Downloads\\archive (2)\\cost of living.csv")
#living = pd.read_csv(path)


# In[13]:


living


# In[8]:


print(path)


# In[14]:


print("C:\\Users\\DELL\\Downloads\\archive (2)\\cost of living.csv")


# In[18]:


a = 5
b = 4
print(a,"\\n",b)


# In[27]:


living = living.sort_values(["Cost of living, 2017","Countries"])


# In[28]:


living


# In[30]:


living = living.drop_duplicates("Available data")


# In[31]:


living


# In[32]:


living = pd.read_csv("C:\\Users\\DELL\\Downloads\\archive (2)\\cost of living.csv")


# In[33]:


living


# In[34]:


living.info()


# In[37]:


living.columns


# In[38]:


living.columns = living.columns.str.upper()


# In[39]:


living.columns


# In[40]:


living.columns = living.columns.str.lower()
living.columns


# In[41]:


living


# In[49]:


living1 = living.loc[living["global rank"]<8]
living1


# In[52]:


living1.drop(["available data"],axis = 1)


# In[53]:


living1.dtypes


# In[54]:


living1.shape


# In[55]:


living.head(100)


# In[56]:


living.tail(100)


# In[66]:


living.iloc[0,1]


# In[1]:





# In[ ]:




