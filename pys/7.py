import seaborn as sns
import matplotlib.pyplot as plt

data = [[2, 4, 6, 3, 7], [3, 6, 9, 5, 4, 8], [3, 6, 9, 5, 4, 8]]
sns.set_style('whitegrid')
sns.boxplot(data)
sns.despine()
sns.set_theme()
plt.show()
