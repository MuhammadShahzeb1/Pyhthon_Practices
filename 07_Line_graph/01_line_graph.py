# # import library
# seaborn autumatically install these libraries

# numpy
# scipy
# pandas
# matplotlib

# import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# load dataset
flower=sns.load_dataset("iris")   #iris is builtin dataset in seaborn
print(flower)

# draw a line plot
sns.lineplot(x="sepal_length",y="sepal_width",data=flower)
plt.title("Line grapgh for Flowers")
plt.show()
