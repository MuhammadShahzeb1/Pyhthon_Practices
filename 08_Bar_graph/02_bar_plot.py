import seaborn as sns
import matplotlib.pyplot as plt

# load dataset
flower=sns.load_dataset("iris")
flower

# draw a plot
# sns.barplot(x="species", y="petal_length", data=flower)
# plt.show

# import seaborn as sns
# import matplotlib.pyplot as plt

# # load dataset
# boat=sns.load_dataset("titanic")
# boat

# # draw a plot
# sns.barplot(x="sex",y="alone",hue="who", data=boat)
# plt.show