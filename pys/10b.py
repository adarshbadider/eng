import plotly.express as px

df = px.data.gapminder()
fig = px.scatter_geo(df, locations="iso_alpha", color="continent", hover_name="country", size="pop", projection="orthographic", title="Population Distribution Across Continents")
fig.show()
