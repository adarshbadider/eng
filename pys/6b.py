import matplotlib.pyplot as plt

overs = [0, 2, 4, 6, 8, 10, 12, 14]
runs_scored = [0, 7, 9, 12, 15, 23, 35, 49]

plt.plot(overs, runs_scored, marker='x', linestyle='dashed', color='pink', linewidth=2, markerfacecolor='blue', markersize=7)
plt.xlabel('Overs', color='red')
plt.ylabel('Runs Scored')
plt.title('Run Scoring in a T20 Cricket Match')
plt.grid(True)
plt.show()
