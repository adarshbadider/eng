import matplotlib.pyplot as plt

data = [23, 67, 89, 78, 12, 90, 24, 78, 87, 65, 12, 1, 0, 56]
plt.hist(data, bins=5, edgecolor='black')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
