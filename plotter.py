import plotly.plotly as py
import plotly.graph_objs as go
import json
from sys import argv
from collections import defaultdict

with open('Aggregate/Years/data.json') as data_file:
    data = json.load(data_file)

d_gold = defaultdict(list)
d_tone = defaultdict(list)
reduce_tone = defaultdict(list)
reduce_gold = defaultdict(list)

for i in data['maps']:
    d_tone[i['Year']].append(i['Average_Tone'])
    d_gold[i['Year']].append(i['Goldstein'])

for k,v in d_tone.iteritems():
    reduce_tone[k] = reduce(lambda x, y: x + y, v) / len(v)

for k, v in d_gold.iteritems():
    reduce_gold[k] = reduce(lambda x, y: x + y, v) / len(v)

user_name = raw_input("What is your username?")
API_key = raw_input("What is your API Key?")

py.sign_in(user_name,API_key)
trace0 = go.Bar(
    x=reduce_tone.keys(),
    y=reduce_tone.values(),
    name='Average Tone',
    marker=dict(
        color='rgb(225,151,76)'
    )
)

trace1 = go.Bar(
    x=reduce_gold.keys(),
    y=reduce_gold.values(),
    name='Average Goldstein',
    marker=dict(
        color='rgb(211,94,96)'
    )
)

data = [trace0,trace1]
layout = go.Layout(
    paper_bgcolor='#151515',
    plot_bgcolor='#151515',
    font=dict(family='Courier New, monospace', size=18, color='#fff'),
    title='Aggregate Environmental Goldstein and Tone: Entire Dataset',
    xaxis=dict(tickangle=-45),
    barmode='group',
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='angled-text-bar')
