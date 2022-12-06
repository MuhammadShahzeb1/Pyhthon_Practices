# Here we will learn about the basics of Data Visualization

# Major parts
# - Mapping(Data)
# - Aesthetic(color,shape,size)
# - Geometric(objects:line,bar,points,box,map)

# step 1 import libraries
import seaborn as sns
import matplotlib.pyplot as plt
# step 2 set a theme...like setting theme on a canvas before drawing or sketching something
sns.set_theme(style="ticks",color_codes=True)   # just considering ticks as a deal no in restauraunts
# step 3 import dataset...we can also import our own data
titanic= sns.load_dataset("titanic")   #build in data in seaborn 
# step 4 plot graph   (mapping,aesthitics,geometric) 
sns.catplot(x="sex",y="survived",hue="class",kind="bar",data=titanic) #catplot is a catagory we can change it as well
# x i s x axis and y is y axis...data is above variable where we import our data
# in above line all the major parts are applied discuss in above cell

plt.show()
# Bar plots