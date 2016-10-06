import plotly.plotly as py
import plotly.graph_objs as go

# Add data
from pip._vendor.distlib.compat import raw_input

node_count = ['6 Slaves', '8 Slaves', '10 Slaves', '12 Slaves', '14 Slaves']
time_taken = [2.1886, 1.5917, 1.4356, 1.165, 0.9958]

# Prompt for Username and API Key for Plotly services
user_name = raw_input("What is your username?")
API_key = raw_input("What is your API Key?")

# Authenticate user to begin creating the graph
py.sign_in(user_name,API_key)

# Create and style traces
trace0 = go.Scatter(
    x = node_count,
    y = time_taken,
    name = 'Time Taken',
    line = dict(
        color = ('rgb(225,151,76)'),
        width = 4)
)
data = [trace0]


# Edit the layout
layout = dict(
    paper_bgcolor='#151515',
    plot_bgcolor='#151515',
    font=dict(family='Courier New, monospace', size=18, color='#fff'),
    title = 'Time Taken for MapReduce Computation',
    xaxis = dict(title = 'Number of Slaves'),
    yaxis = dict(title = 'Time Taken (Hours)'),
)

# Plot and embed in ipython notebook!
fig = dict(data=data, layout=layout)
py.plot(fig, filename='styled-line')