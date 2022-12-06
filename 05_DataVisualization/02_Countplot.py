# here we will discuss basic if count plot

# Count plot
# to check how many males and females were there

import seaborn as sns
import matplotlib.pyplot as plt
# sns.set_theme(style="ticks",color_codes=True)
# titanic= sns.load_dataset("titanic")   #build in data in seaborn
# p1=sns.countplot(x="sex",hue="class",data=titanic)
# p1.set_title("plot for counting")
# plt.show()
# comment the above lines to see the manipulation in graphs

# print(titanic)
# it will show the data in titanic now by just visualizing the data we can interpret the ggrapghs according to our requirments.



sns.set_theme(style="ticks",color_codes=True)
titanic= sns.load_dataset("titanic")   
p1=sns.countplot(x="who",hue="alone",data=titanic)  # changing values on x axis from sex to who and coloring of hue from class  to alone
p1.set_title("plot for counting")
plt.show()