import plotly.plotly as py
import plotly.graph_objs as go
import json
from collections import defaultdict
from pip._vendor.distlib.compat import raw_input

#!/usr/bin/python

__author__ = "Max James Yendall"
__credits__ = "Plotly Data Plotting Services"
__version__ = "1.0"
__email__ = "yendallmax@gmail.com"

with open('Aggregate/Years/data.json') as data_file:
    data = json.load(data_file)

# Declare default dictionary objects for data
d_gold = defaultdict(list)
d_tone = defaultdict(list)

# Dictionaries to hold aggregated data
reduce_tone = defaultdict(list)
reduce_gold = defaultdict(list)

# Populate both dictionaries and handle duplicates
for i in data['maps']:
    d_tone[i['Year']].append(i['Average_Tone'])
    d_gold[i['Year']].append(i['Goldstein'])

# Perform lambda function on each list to obtain average values
for k,v in d_tone.iteritems():
    reduce_tone[k] = reduce(lambda x, y: x + y, v) / len(v)
for k, v in d_gold.iteritems():
    reduce_gold[k] = reduce(lambda x, y: x + y, v) / len(v)

# Prompt for Username and API Key for Plotly services
user_name = raw_input("What is your username?")
API_key = raw_input("What is your API Key?")

# Authenticate user to begin creating the graph
py.sign_in(user_name,API_key)

# Map Tone values to Bar objects
tone_trace = go.Bar(
    x=reduce_tone.keys(),
    y=reduce_tone.values(),
    name='Average Tone',
    marker=dict(
        color='rgb(225,151,76)'
    )
)

# Map Goldstein values to Bar objects
goldstein_trace = go.Bar(
    x=reduce_gold.keys(),
    y=reduce_gold.values(),
    name='Average Goldstein',
    marker=dict(
        color='rgb(211,94,96)'
    )
)

# Map Bar objects to data array
data = [tone_trace,goldstein_trace]

# Ensure layout is designed well and readable
layout = go.Layout(
    paper_bgcolor='#151515',
    plot_bgcolor='#151515',
    font=dict(family='Courier New, monospace', size=18, color='#fff'),
    title='Aggregate Environmental Goldstein and Tone: Entire Dataset',
    xaxis=dict(tickangle=-45),
    barmode='group',
)

# Plot data using layout configuration
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='angled-text-bar')
