#!/usr/bin/env python
# coding: utf-8

# In[120]:


import pandas as pd


# In[121]:


df_swiggy = pd.read_csv("C:\\Users\\Acer\\Desktop\\self-Projects\\04 Swiggy Bangalore\\Data\\Swiggy_Bangalore_outlet (1)\\Swiggy Bangalore Outlet Details.csv")


# In[122]:


df_swiggy.columns


# In[123]:


df_swiggy.columns = ['Shop Name', 'Cuisine', 'Location', 'Rating', 'Cost for Two']


# In[124]:


df_swiggy.info()


# In[125]:


df_swiggy.describe()


# In[126]:


df_swiggy.isnull().sum()


# In[132]:


df_miss = df_swiggy['Cost for Two'].apply(lambda x:x[1:])


# In[133]:


df_swiggy = pd.concat([df_swiggy, df_miss], axis=1)


# In[117]:


df_swiggy = df_swiggy.drop(['Cost for Two'], axis=1)


# In[134]:


df_swiggy


# In[135]:


df_swiggy.columns


# In[136]:


df_swiggy.columns = ['Shop Name', 'Cuisine', 'Location', 'Rating', 'Costing for Two',
       'Cost for Two']


# In[137]:


df_swiggy.columns


# In[138]:


df_swiggy = df_swiggy.drop(['Costing for Two'], axis=1)


# In[139]:


df_swiggy['Rating'].unique()


# In[140]:


df_swiggy['Rating'].unique()


# In[141]:


df_swiggy['Cost for Two'] = df_swiggy['Cost for Two'].astype(int)


# In[142]:


df_swiggy['Cost for Two'].mean()


# In[144]:


df_swiggy['Rating'] = df_swiggy['Rating'].replace("--", "0", inplace=False)


# In[145]:


df_swiggy['Rating'].unique()


# In[146]:


df_swiggy['Rating'] = df_swiggy['Rating'].astype(float)


# In[147]:


df_new = df_swiggy['Rating'].mean()
df_new


# In[148]:


df_swiggy['Rating'].fillna(df_new, inplace = True)


# In[149]:


df_swiggy['Rating'].unique()


# In[150]:


df_swiggy['Rating'] =df_swiggy['Rating'].fillna(df_swiggy['Rating'].mean())


# In[151]:


df_swiggy['Rating'].unique()


# In[152]:


df_swiggy['Rating'] = df_swiggy['Rating'].replace(0., df_new, inplace=False)


# In[153]:


df_swiggy['Rating'].unique()


# In[75]:


## titanic_data.Age.fillna(new_age,inplace = True) 
## titanic_data.Embarked = titanic_data.Embarked.fillna(titanic_data['Embarked'].mode()[0])


# In[154]:


df_swiggy.to_csv("df_swiggy_cleaned.csv", index=False)


# In[ ]:


df_ground['Ground'] = df_ground['Ground'].str.split(',')
df_groundew = pd.DataFrame(df_ground['Ground'].tolist()).fillna('').add_prefix('Ground_')
df_ground = pd.concat([df_ground, df_groundew], axis=1)


# In[ ]:


df_ground['Ground'] = df_ground['Ground'].str.split(',')
df_groundew = pd.DataFrame(df_ground['Ground'].tolist()).fillna('').add_prefix('Ground_')
df_ground = pd.concat([df_ground, df_groundew], axis=1)


# In[155]:


df_swiggy['Cuisine'] = df_swiggy['Cuisine'].str.split(',')


# In[156]:


df_swiggy1 = pd.DataFrame(df_swiggy['Cuisine'].tolist()).fillna('').add_prefix('Cuisine_')


# In[157]:


df_swiggy = pd.concat([df_swiggy ,df_swiggy1],  axis=1)


# In[88]:





# In[158]:


df_swiggy.columns


# In[160]:


df_swiggy.columns = ['Shop Name', 'Cuisine', 'Location', 'Rating', 'Costing for Two',
       'Cost for Two', 'Cuisine_1', 'Cuisine_2', 'Cuisine_3',
       'Cuisine_4', 'Cuisine_5', 'Cuisine_6', 'Cuisine_7', 'Cuisine_8',
       'Cuisine_9', 'Cuisine_10', 'Cuisine_11', 'Cuisine_12', 'Cuisine_13',
       'Cuisine_14', 'Cuisine_15', 'Cuisine_16', 'Cuisine_17', 'Cuisine_18']


# In[161]:


df_swiggy


# In[165]:


df_swiggy = df_swiggy.drop(['Costing for Two'], axis=1)


# In[166]:


df_swiggy.info()


# In[167]:


df_swiggy.to_csv("df_swiggy_cleaned_new.csv", index=False)


# In[183]:


df_swiggy = df_swiggy.drop(['Location', 'Rating',
       'Cost for Two', 'Cuisine_1', 'Cuisine_2', 'Cuisine_3',
       'Cuisine_4', 'Cuisine_5', 'Cuisine_6', 'Cuisine_7', 'Cuisine_8',
       'Cuisine_9', 'Cuisine_10', 'Cuisine_11', 'Cuisine_12', 'Cuisine_13',
       'Cuisine_14', 'Cuisine_15', 'Cuisine_16', 'Cuisine_17', 'Cuisine_18'], axis=1)


# In[ ]:


for l in (test_list2,test_list3)]
 
print ("The extended and modified list is : " + str(test_list1))


# In[192]:


for l in 'Cuisine':
    str(l)
df_swiggy.info


# In[191]:


df_swiggy.info


# In[186]:


df_swiggy.info()


# In[ ]:




