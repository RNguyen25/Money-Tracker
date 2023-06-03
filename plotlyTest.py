import plotly.express as px
import plotly.graph_objects as go

# This dataframe has 244 lines, but 4 distinct values for `day`
cock = ['food','entertainment','random','asdf']
val = [3, 2, 10, 14]
title = "what's up"
colors = ['gold', 'mediumturquoise', 'blue', 'lightgreen']

data=[go.Pie(labels=cock, values=val, textinfo='label+percent', hole=.3,title=title)]
fig = go.Figure(data)
fig.update_traces(textfont_size=14, marker = dict(colors=colors))
fig.show()
