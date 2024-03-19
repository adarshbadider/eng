import numpy as np
from bokeh.plotting import figure, show

x = np.random.random(50) * 10
y = np.random.random(50) * 10

p1 = figure(title="Simple Scatter Plot", x_axis_label="x", y_axis_label="y")
p1.circle(x, y, size=10, color="blue", alpha=0.5)

show(p1)
