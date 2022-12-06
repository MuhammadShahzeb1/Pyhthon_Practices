# setting styles


import seaborn as sns
import matplotlib.pyplot as plt

flower=sns.load_dataset("iris")
sns.lineplot(x="sepal_length",y="sepal_width",data=flower)
plt.title("Line grapgh for Flowers")
sns.set_style("dark")
# we have to check how to change the style
# set_style(style=None, rc=None)
plt.show()
