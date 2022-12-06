# setting order
# for setting order we will just add order variable

import seaborn as sns
import matplotlib.pyplot as plt

# load dataset
boat=sns.load_dataset("titanic")
print(boat)

# draw a plot
sns.barplot(x="sex",y="alone",hue="who", data=boat, order=["female","male"] ,color="red")
# sns.barplot(x="sex",y="alone",hue="who", data=boat, order=["female","male"], color="grey")
# sns.barplot(x="sex",y="alone",hue="who", data=boat, order=["female","male"], color="salmon")
plt.show