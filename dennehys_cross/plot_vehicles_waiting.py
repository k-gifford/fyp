#!/usr/bin/env python3
import plotly.plotly as py
from plotly.graph_objs import *

range_val = [0, 8]

def plot_static_vehicles(ns, ew):

    size = list(range(len(ns)))

    layout = graph_objs.Layout(

        title='Static Vehicles Waiting',
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
            ),
            range=range_val

        ),
        legend=dict(
            traceorder='normal',
            font=dict(
                family='sans-serif',
                size=16,
                color='#000'
            ),
            bgcolor='#E2E2E2',
            bordercolor='#FFFFFF',
            borderwidth=2
        )
    )

    north_south_approach = Scatter(
        x=size,
        y=ns,
        marker=dict(color="green"),
        name="NS Approaches"
    )
    east_west_approach = Scatter(
        x=size,
        y=ew,
        marker=dict(color="orange"),
        name="EW Approaches"
    )

    data = [north_south_approach, east_west_approach]
    fig = graph_objs.Figure(data=data, layout=layout)

    py.plot(fig, filename='Static-num-vehicles-waiting')


def plot_actuated_vehicles(ns, ew):

    size = list(range(len(ns)))

    layout = graph_objs.Layout(

        title='Actuated Vehicles Waiting',
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
            ),
            range=range_val

        ),
        legend=dict(
            traceorder='normal',
            font=dict(
                family='sans-serif',
                size=16,
                color='#000'
            ),
            bgcolor='#E2E2E2',
            bordercolor='#FFFFFF',
            borderwidth=2
        )
    )

    north_south_approach = Scatter(
        x=size,
        y=ns,
        marker=dict(color="green"),
        name="NS Approaches"
    )
    east_west_approach = Scatter(
        x=size,
        y=ew,
        marker=dict(color="orange"),
        name="EW Approaches"
    )

    data = [north_south_approach, east_west_approach]
    fig = graph_objs.Figure(data=data, layout=layout)

    py.plot(fig, filename='Actuated-num-vehicles-waiting')


def plot_dynamic_vehicles(ns, ew):

    size = list(range(len(ns)))

    layout = graph_objs.Layout(

        title='Dynamic Vehicles Waiting',
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
            ),
            range=range_val

        ),
        legend=dict(
            traceorder='normal',
            font=dict(
                family='sans-serif',
                size=16,
                color='#000'
            ),
            bgcolor='#E2E2E2',
            bordercolor='#FFFFFF',
            borderwidth=2
        )
    )

    north_south_approach = Scatter(
        x=size,
        y=ns,
        marker=dict(color="green"),
        name="NS Approaches"
    )
    east_west_approach = Scatter(
        x=size,
        y=ew,
        marker=dict(color="orange"),
        name="EW Approaches"
    )

    data = [north_south_approach, east_west_approach]
    fig = graph_objs.Figure(data=data, layout=layout)

    py.plot(fig, filename='Dynamic-num-vehicles-waiting')


def plot_all_tl_alg_vehicles(static, actuated, dynamic):
    size = list(range(len(static)))

    layout = graph_objs.Layout(

        title='All Vehicles Waiting Over All Three Algorithms',
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
            ),
            range=range_val

        ),
        legend=dict(
            traceorder='normal',
            font=dict(
                family='sans-serif',
                size=16,
                color='#000'
            ),
            bgcolor='#E2E2E2',
            bordercolor='#FFFFFF',
            borderwidth=2
        )
    )

    static = Scatter(
        x=size,
        y=static,
        marker=dict(color="green"),
        name="Static"
    )
    actuated = Scatter(
        x=size,
        y=actuated,
        marker=dict(color="blue"),
        name="Actuated"
    )
    dynamic = Scatter(
        x=size,
        y=dynamic,
        marker=dict(color="red"),
        name="Dynamic"
    )

    data = [static, actuated, dynamic]
    fig = graph_objs.Figure(data=data, layout=layout)

    py.plot(fig, filename='all-num-vehicles-waiting')


def plot_all_ns_tl_alg_vehicles(static, actuated, dynamic):
    size = list(range(len(static)))

    layout = graph_objs.Layout(

        title='North/South Vehicles Waiting Over All Three Algorithms',
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
            ),
            range=range_val

        ),
        legend=dict(
            traceorder='normal',
            font=dict(
                family='sans-serif',
                size=16,
                color='#000'
            ),
            bgcolor='#E2E2E2',
            bordercolor='#FFFFFF',
            borderwidth=2
        )
    )

    static = Scatter(
        x=size,
        y=static,
        marker=dict(color="green"),
        name="Static"
    )
    actuated = Scatter(
        x=size,
        y=actuated,
        marker=dict(color="blue"),
        name="Actuated"
    )
    dynamic = Scatter(
        x=size,
        y=dynamic,
        marker=dict(color="red"),
        name="Dynamic"
    )

    data = [static, actuated, dynamic]
    fig = graph_objs.Figure(data=data, layout=layout)

    py.plot(fig, filename='north-south-all-num-vehicles-waiting')


def plot_all_ew_tl_alg_vehicles(static, actuated, dynamic):
    size = list(range(len(static)))

    layout = graph_objs.Layout(

        title='East/West Vehicles Waiting Over All Three Algorithms',
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
            ),
            range=range_val

        ),
        legend=dict(
            traceorder='normal',
            font=dict(
                family='sans-serif',
                size=16,
                color='#000'
            ),
            bgcolor='#E2E2E2',
            bordercolor='#FFFFFF',
            borderwidth=2
        )
    )

    static = Scatter(
        x=size,
        y=static,
        marker=dict(color="green"),
        name="Static"
    )
    actuated = Scatter(
        x=size,
        y=actuated,
        marker=dict(color="blue"),
        name="Actuated"
    )
    dynamic = Scatter(
        x=size,
        y=dynamic,
        marker=dict(color="red"),
        name="Dynamic"
    )

    data = [static, actuated, dynamic]
    fig = graph_objs.Figure(data=data, layout=layout)

    py.plot(fig, filename='east-west-all-num-vehicles-waiting')

