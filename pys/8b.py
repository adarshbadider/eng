import numpy as np
from bokeh.plotting import figure, show

x = np.arange(0, 10, 1)
y = np.random.random(10) * 100

p1 = figure(title="Simple Scatter Plot", x_axis_label="x", y_axis_label="y")
p1.circle(x, y, size=10, color="red")

show(p1)
