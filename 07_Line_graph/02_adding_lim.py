

# adding limits

import seaborn as sns
import matplotlib.pyplot as plt

flower=sns.load_dataset("iris")   #iris is builtin dataset in seaborn

sns.lineplot(x="sepal_length",y="sepal_width",data=flower)
plt.title("Line grapgh for Flowers")
plt.xlim(2)
plt.ylim(1)
plt.show()
