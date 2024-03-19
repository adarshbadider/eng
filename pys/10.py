import pandas as pd
import plotly.express as px

df = px.data.gapminder().query("continent == 'Asia'")
fig = px.scatter_3d(df, x="gdpPercap", y="pop", z="year", color="country", title="Economic Evolution of Asian Countries Over Time")
fig.show()
