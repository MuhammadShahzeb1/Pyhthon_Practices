# to using pallete
import seaborn as sns
import matplotlib.pyplot as plt

# load dataset
boat=sns.load_dataset("titanic")
boat

# draw a plot
# sns.barplot(x="sex",y="alone",hue="who", data=boat, order=["female","male"], color="grey")
# sns.barplot(x="sex",y="alone",hue="who", data=boat, order=["female","male"], color="salmon")
sns.barplot(x="sex",y="alone",hue="who", data=boat, order=["female","male"], color="red", ci=None, palette='pastel')
plt.show