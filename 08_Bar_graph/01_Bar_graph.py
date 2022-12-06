# here we will discuss about the bar graph
# import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# load dataset
flower=sns.load_dataset("iris")
flower

# draw a plot
sns.barplot(x="species", y="sepal_width", data=flower)
plt.show

print(flower)