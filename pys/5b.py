import matplotlib.pyplot as plt

countries = ['Brazil', 'Germany', 'Italy', 'Argentina', 'Uruguay', 'France', 'England', 'Spain']
wins = [5, 4, 4, 3, 2, 2, 1, 1]

plt.pie(wins, labels=countries, autopct='%1.1f%%', startangle=90)
plt.title('FIFA World Cup Wins by Country')
plt.axis('equal')
plt.show()
