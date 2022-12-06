

import seaborn as sns
import matplotlib.pyplot as plt

flower=sns.load_dataset("iris")
plt.figure(figsize=(14,7))  #width,length
sns.lineplot(x="sepal_length",y="sepal_width",data=flower)
plt.title("Line grapgh for Flowers")
sns.set_style("dark")
plt.show()