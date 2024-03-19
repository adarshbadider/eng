import matplotlib.pyplot as plt

categories = ['0-10', '10-20', '20-30', '30-40', '40-50']
values = [55, 48, 25, 68, 90]

plt.bar(categories, values, color='skyblue')
plt.xlabel('Ranges')
plt.ylabel('Frequency')
plt.title('Bar Plot Showing Frequency Distribution')
plt.show()
