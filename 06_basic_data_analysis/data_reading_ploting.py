import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

reader= pd.read_csv("sample_data.csv")
print(reader)

sns.set_theme(style="ticks",color_codes=True)
# p= sns.load_dataset("")   #build in data in seaborn
p1=sns.countplot(x="gender",hue="age",data=reader)
p1.set_title("plot for counting")
plt.show()


# Imp Point: the code with pandas library and csv file is only opened in Pycharm

