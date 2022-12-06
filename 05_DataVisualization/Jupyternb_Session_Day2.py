#!/usr/bin/env python
# coding: utf-8

# ### 01_ Quiz BMI
# <!-- # body mass index
# # input weight,hieght
# # calculate BMI
# # print BMI -->

# In[2]:


weight=int(input("please enter your weight in kg: "))
height=float(input("please enter your height in metres: "))
BMI=weight/height**2
print("Your BMI is ", BMI)


# In[3]:


# using inside a function
def BMI(weight,height):
#     weight=int(input("please enter your weight: "))
#     height=int(input("please enter your height: "))
    BMI=weight/height**2
    return BMI
    print("Your BMI is ", BMI)


# In[4]:


# BMI(55,1.74)


# In[5]:


# using if statement 
name=input("please enter your name: ")
weight=int(input("please enter your weight in kg: "))
height=float(input("please enter your height in metres: "))
BMI=weight/height**2

# print("Your BMI is ", BMI)
# now using if else statement as well
if BMI > 18:
    print(name, "Your BMI is good")
elif BMI < 18:
    print(name, "Your BMI is below average")
elif BMI > 24:
    print(name, "Your is above average")


# learning some basic of data visualaziation from session day 2 vidoe
# 

# ---

# ### 02_ Basic of Data Visualization

# ### Major parts
# - Mapping(Data)
# - Aesthetic(color,shape,size)
# - Geometric(objects:line,bar,points,box,map)

# In[8]:


import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks",color_codes=True)   # just considering ticks as a deal no in restauraunts

titanic= sns.load_dataset("titanic")   #build in data in seaborn 
sns.catplot(x="sex",y="survived",hue="class",kind="bar",data=titanic) #catplot is a catagory we can change it as well
# x i s x axis and y is y axis
# in above line all the major parts are applied discuss in above cell

plt.show()
# Bar plots


# In[10]:


# Count plot
# to check how many males and females were there

sns.set_theme(style="ticks",color_codes=True)
titanic= sns.load_dataset("titanic")   #build in data in seaborn
p1=sns.countplot(x="sex",hue="class",data=titanic)
p1.set_title("plot for counting")
plt.show()


# In[13]:


# Scatterplot
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks",color_codes=True)
titanic= sns.load_dataset("titanic")   #build in data in seaborn
g=sns.FacetGrid(titanic, row="sex",hue="alone")
g=(g.map(plt.scatter, "age", "fare").add_legend())
plt.show()


# In[14]:


type(titanic)


# In[16]:


# we can do all the above works in vs code as well


# In[17]:


print(titanic)


# In[19]:


# some manipulation in data
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks",color_codes=True)
titanic= sns.load_dataset("titanic")   
p1=sns.countplot(x="who",hue="alone",data=titanic)  # changing values on x axis from sex to who and coloring of hue from class  to alone
p1.set_title("plot for counting")
plt.show()

# analyize or compare with the previous one

