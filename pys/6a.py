import matplotlib.pyplot as plt

overs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
runs_scored = [0, 7, 8, 9, 23, 45, 76, 86, 90, 123]

plt.plot(overs, runs_scored)
plt.xlabel('Overs')
plt.ylabel('Runs Scored')
plt.title('Run Scoring in a T20 Cricket Match')
plt.grid(True)
plt.show()
