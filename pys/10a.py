import plotly.express as px

df = px.data.stocks()
fig = px.line(df, x='date', y='GOOG', title='Google Stock Price Over Time')
fig.show()
