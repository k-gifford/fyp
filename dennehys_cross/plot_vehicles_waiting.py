#!/usr/bin/env python3
import plotly.plotly as py
from plotly.graph_objs import *

def plotTimes(north, south):

    size = list(range(len(north)))

    layout = graph_objs.Layout(
        margin=dict(
            l=50,
            r=50,
            b=100,
            t=100,
            pad=4
        ),
        title='Vehicles Waiting',
        xaxis=dict(
            title='Time (s)',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )

        ),
        yaxis=dict(
            title='Num Vehicles',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )

        )
    )

    north_south_approach = Scatter(
        x=size,
        y=north,
        marker=dict(color="green"),
        name="NS Approaches"
    )
    east_west_approach = Scatter(
        x=size,
        y=south,
        marker=dict(color="orange"),
        name="EW Approaches"
    )



    data = [north_south_approach, east_west_approach]
    fig = graph_objs.Figure(data=data, layout=layout)

    py.plot(fig, filename='actuated-num-vehicles-waiting')