# step 1 import libraries
import seaborn as sns
import matplotlib.pyplot as plt
# step 2 set theme
sns.set_theme(style="ticks",color_codes=True)
# step 3 load data
kashti= sns.load_dataset("titanic")  
# step 4 plot graph with one variable....
# Imp point: will only show one variable for the deck
# p1=sns.countplot(x="deck",data=kashti)  # changing values on x axis from sex to who and coloring of hue from class  to alone
# we can not set anything in y axis in count plot


# plt.show()

# step 5 plot graph with 2 variables  using hue functions
# p1=sns.countplot(x="deck",data=kashti,hue="class")  # changing values on x axis from sex to who and coloring of hue from class  to alone
# Imp point: will  show two variable for the deck
# try to note the clear difference of variables with the fist one (single variable)
# to set title in a plot
# p1.set_title("plot for counting")
# plt.show()

# to analyze and playing with data we will use some methods here

# print(kashti)
# summary=kashti.


