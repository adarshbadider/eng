import matplotlib.pyplot as plt

countries = ['Brazil', 'Russia', 'India', 'China', 'South Africa']
per_capita_income = [9600, 11600, 2300, 11000, 6500]

plt.scatter(countries, per_capita_income)
plt.xlabel('Countries')
plt.ylabel('Per Capita Income (USD)')
plt.title('Per Capita Income of BRICS Nations')
plt.show()
