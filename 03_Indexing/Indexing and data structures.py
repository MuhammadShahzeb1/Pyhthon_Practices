#!/usr/bin/env python
# coding: utf-8

# # Indexing

# In[5]:


# make a string

a="Muhammad Shahzeb"
a


# In[6]:


a[0]


# In[7]:


a[4]


# In[8]:


# length of a strings
len(a)


# In[9]:


# as there are 16 characters so its start from 0 to 15
# so it gives error in 16 
a[16]


# In[10]:


a[15]


# In[11]:


# to select specific characters from a strings
a[1:4]


# In[12]:


a[1::5]


# In[15]:


#  last character is exlusive if we want to print whole strings than we need to add 1 in last i,e[0:n+1]
a[0:15]
a[0:16]


# In[16]:


# double ratio shows the starting and ending of a strings like My name is start from m and ends at b
a[0::15]


# In[18]:


# starting from  the right side of a strings used to get the last or second and so characters of a strings
a[-1]


# In[24]:


a[-7:16]


# ## Strings methods
# 

# In[25]:


friends="osama shoaib abdul"


# In[26]:


friends


# In[27]:


len(friends)


# In[41]:


# some built in methods to works with strings
# Capitilzie
friends.capitalize()


# In[42]:


# lowercase
friends.lower()


# In[38]:


# uppercase
friends.upper()


# In[46]:


# replace a specific character in strings
friends.replace("o","u")


# In[47]:



name="Muhammad Shahzeb Arshad"
name


# In[57]:


# counting a specific alohabet in a string
name.count("a")


# In[62]:


name.count("S")


# In[63]:



# for multiple character

name.count("ad")


# ### finding an index number in string
# 

# In[67]:


# finding index in a sring
friends.find("s")


# In[68]:


# now if we want to find shoib in friends we will use s to find index number but s is lareday in osama so it will give 1
# now the solution is simple just use starting two or three characters of any name you want find
friends.find("sh")


# In[69]:


friends.find("ib")


# In[73]:


friends[5:12]   #always add number of charctars in output index number


# ### Spliting strings

# In[74]:


# we can split long strings for devide and conquer type of processings
friends.split()

