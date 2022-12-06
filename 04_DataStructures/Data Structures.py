#!/usr/bin/env python
# coding: utf-8

# # Data Structures

# ## Basic Data Strucutres in python
# **1-Tuple**
# 
# **2-List**
# 
# **3-Dictionary**
# 
# **4-Set**
# 

# ## 1-Tuple
# - ordered collection of element.
# - enclosed in () in round braces/paranthesis.
# - different kind of elemenets can be stored.
# - once element are stored you can not change them (unmutable).
# - mutable...something that can be changed,-unmautabble.....something that cannot be changed.
# 

# In[1]:


tup1=(1,"java",True,2.5)
tup1


# In[2]:


type(tup1)


# In[3]:


tup1[1]


# In[4]:


tup1[0:4]  #last element is exclusive


# In[5]:


# count of element in tuples
len(tup1)


# In[6]:


tup2=(117,"Muhammad Shahzeb",2.8,False)
tup2


# In[7]:


# concatenation in tuple
tup1+tup2    #concatenate the elements of both tupples


# In[8]:


tup1*2


# In[9]:


tup3=(89,111,116,117)
tup3


# In[10]:


max(tup3)


# In[11]:


min(tup3)


# In[12]:


tup3*2
# adding or multiplication in tupple does not add or multiply te elements how ever it just arranged the elements with fixed nature in other words it called concatenation


# ---

# ## 2-List
# - ordered collection of element.
# - enclosed in [] in square braces.
# - different kind of elemenets can be stored.
# - once element are stored you can  change them as well (mutable).
# 
# 

# In[13]:


list1=[1,"java",True,2.5]
list1


# In[14]:


type(list1)


# In[15]:


len(list1)


# In[16]:


list1[2]


# In[17]:


list2=[117,"Muhammad Shahzeb",2.8,False]
list2


# In[18]:


# Concatenation in Lists
list1+list2


# In[19]:


list2*3


# In[20]:


# we can use differnet built in function to manipulate the data in list
# name.(then press tab ,the available function will pop up)
# reversing the list.  it reverse the elements in list and if we run twice it will also re arrange in preivious order. 
list2.reverse()
list2


# In[21]:


list1.append("Ali")
list1


# In[22]:


list3=[23,345,45,23,12,234,45,4,23,45,2,34]
len(list3)


# In[23]:


list3.sort()
list3


# In[24]:


list1+list3


# In[26]:


list4=list1+list3


# ---

# ## 3-Dictionary
# - an unordered collection of element.
# - enclosed in {} in curley braces.
# - data stored in Key and Value.
# - different kind of elemenets can be stored.
# - once element are stored you can  change them as well (mutable).
# 

# In[30]:


# Food and their prices
food1={"Samosa":30,"Pakora":100,"Raita":20,"Salad":50,"Chicken Rolls":30}
food1


# In[31]:


type(food1)


# In[32]:


# extracting data from dictionary
food1.keys()


# In[34]:


food1.values()


# In[36]:


# adding a new element in dictionary

food1["Chicken Samosa"]=40
food1


# In[37]:


# update the values
food1["Chicken Samosa"]=35
food1


# In[39]:


food2={"Date":50,"Chocolates":200,"Sawwayan":300}
food2


# In[41]:


# concatenate
# food1+food2
# above written method is not supported in  dictionaries so


# In[43]:


# to concatenate or update value we will use this method because its unordered element
food1.update(food2)
food1


# ---

# ## 4-Sets
# - an unordered and unindexed collection of element.
# - enclosed in {} in curley braces.
# - no duplicates are allowed.
# - different kind of elemenets can be stored.
# - once element are stored you can  change them as well (mutable).
# 

# In[46]:


s1={1,2,4,5,"Jhelum","Pakistan"}
s1


# In[47]:


# to add any vlaue in sets
s1.add("Hamid")
s1


# In[49]:


# Booleans are not allowed to enter in sets
s1.add(True)
s1


# In[52]:


# we can not add similar elements twice in sets / dupllication is not allwwed
s1.add("Hamid")
s1


# In[53]:


# to remove something from set
s1.remove(2)
s1


# In[55]:


# suggestion: for better understanding try to explore  all the methods in tuple, list and dioctionary.


# ---
# 
