import numpy as np
from bokeh.plotting import figure, show

x = np.arange(0, 10, 1)
y1 = x ** 2
y2 = x ** 3
y3 = x ** 4

p1 = figure(title="Simple Line Chart", x_axis_label="x", y_axis_label="y")
p1.line(x, y1, legend_label="Quadric Function", line_color="red")
p1.line(x, y2, legend_label="Cubic Function", line_color="blue")
p1.line(x, y3, legend_label="Quartic Function", line_color="green")

show(p1)
