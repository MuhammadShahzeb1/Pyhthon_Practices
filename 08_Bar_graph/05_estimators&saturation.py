# using estimator in grpaph
# to calculating mean and median we need to import a library for calculation purposes

import seaborn as sns
from numpy import median 
import matplotlib.pyplot as plt

# load dataset
boat=sns.load_dataset("titanic")
boat

# draw a plot

# to add saturation   intensity of colours   satuaration ranges from 0 to 1
sns.barplot(x="class",y="fare",hue="sex", data=boat, estimator=median,saturation=1)
plt.show()