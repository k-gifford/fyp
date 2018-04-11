#!/usr/bin/env python3
"""
Plots the trip info outputs and the traffic light state using PlotLy.
Takes the outputs that SUMO generates when running the scenario and
plots them on graphs using PlotLy.
"""
import plotly.plotly as py
from plotly.graph_objs import *
import csv


def plot_dynamic():

    dynamicfile = "dynamictlstates.csv"
    dynamic_timesteps = []
    dynamic_tl_ew_green_states = []
    dynamic_tl_ns_green_states = []
    dynamic_tl_yellow_states = []

    with open(dynamicfile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dynamic_timesteps.append(row['timestep'])
            if row['state'] == '1':
                dynamic_tl_ew_green_states.append(row['state'])
                dynamic_tl_ns_green_states.append(0)
                dynamic_tl_yellow_states.append(0)
            elif row['state'] == '-1':
                dynamic_tl_ew_green_states.append(0)
                dynamic_tl_ns_green_states.append(row['state'])
                dynamic_tl_yellow_states.append(0)
            else:
                dynamic_tl_ew_green_states.append(0)
                dynamic_tl_ns_green_states.append(0)
                dynamic_tl_yellow_states.append(row['state'])

    print(dynamic_timesteps)
    print(dynamic_tl_ew_green_states)
    print(dynamic_tl_ns_green_states)
    print(dynamic_tl_yellow_states)

    layout = graph_objs.Layout(

        title='Dynamic Traffic Light States',
        xaxis=dict(
            title='Time (s)',
            titlefont=dict(
                family='Courier New, monospace',
                size=36,
                color='#7f7f7f'
            ),
            domain=[-1, -0.5, 0.5, 1]
        ),
        yaxis=dict(
            title='State',
            titlefont=dict(
                family='Courier New, monospace',
                size=36,
                color='#7f7f7f'
            ),
            domain=[-1, -0.5, 0.5, 1]
        )
    )

    ew_green_states = Bar(
        x=dynamic_timesteps,
        y=dynamic_tl_ew_green_states,
        marker=dict(color="green"),
        name="East/West Green Light Phase"
    )
    ns_green_states = Bar(
        x=dynamic_timesteps,
        y=dynamic_tl_ns_green_states,
        marker=dict(color="lightgreen"),
        name="North/South Green Light Phase"
    )
    orange_states = Bar(
        x=dynamic_timesteps,
        y=dynamic_tl_yellow_states,
        marker=dict(color="orange"),
        name="Orange Light Phase"
    )


    data = [ew_green_states, ns_green_states, orange_states]
    fig = graph_objs.Figure(data=data, layout=layout)

    py.plot(fig, filename='dynamic-trafficlight-durations')


def plot_static():

    staticfile = "statictlstates.csv"
    static_timesteps = []
    static_tl_ew_green_states = []
    static_tl_ns_green_states = []
    static_tl_yellow_states = []

    with open(staticfile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            static_timesteps.append(row['timestep'])
            if row['state'] == '1':
                static_tl_ew_green_states.append(row['state'])
                static_tl_ns_green_states.append(0)
                static_tl_yellow_states.append(0)
            elif row['state'] == '-1':
                static_tl_ew_green_states.append(0)
                static_tl_ns_green_states.append(row['state'])
                static_tl_yellow_states.append(0)
            else:
                static_tl_ew_green_states.append(0)
                static_tl_ns_green_states.append(0)
                static_tl_yellow_states.append(row['state'])

    print(static_timesteps)
    print(static_tl_ew_green_states)
    print(static_tl_ns_green_states)
    print(static_tl_yellow_states)

    layout = graph_objs.Layout(
        title='Static Traffic Light States',
        xaxis=dict(
            title='Time (s)',
            titlefont=dict(
                family='Courier New, monospace',
                size=36,
                color='#7f7f7f'
            )
        ),
        yaxis=dict(
            title='State',
            titlefont=dict(
                family='Courier New, monospace',
                size=36,
                color='#7f7f7f'
            )
        )
    )

    ew_green_states = Bar(
        x=static_timesteps,
        y=static_tl_ew_green_states,
        marker=dict(color="green"),
        name="East/West Green Light Phase"
    )
    ns_green_states = Bar(
        x=static_timesteps,
        y=static_tl_ns_green_states,
        marker=dict(color="lightgreen"),
        name="North/South Green Light Phase"
    )
    orange_states = Bar(
        x=static_timesteps,
        y=static_tl_yellow_states,
        marker=dict(color="orange"),
        name="Orange Light Phase"
    )

    data = [ew_green_states, ns_green_states, orange_states]
    fig = graph_objs.Figure(data=data, layout=layout)

    py.plot(fig, filename='static-trafficlight-durations')


def plot_actuated():

    staticfile = "actuatedtlstates.csv"
    dynamic_timesteps = []
    dynamic_tl_ew_green_states = []
    dynamic_tl_ns_green_states = []
    dynamic_tl_yellow_states = []

    with open(staticfile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dynamic_timesteps.append(row['timestep'])
            if row['state'] == '1':
                dynamic_tl_ew_green_states.append(row['state'])
                dynamic_tl_ns_green_states.append(0)
                dynamic_tl_yellow_states.append(0)
            elif row['state'] == '-1':
                dynamic_tl_ew_green_states.append(0)
                dynamic_tl_ns_green_states.append(row['state'])
                dynamic_tl_yellow_states.append(0)
            else:
                dynamic_tl_ew_green_states.append(0)
                dynamic_tl_ns_green_states.append(0)
                dynamic_tl_yellow_states.append(row['state'])

    print(dynamic_timesteps)
    print(dynamic_tl_ew_green_states)
    print(dynamic_tl_ns_green_states)
    print(dynamic_tl_yellow_states)

    layout = graph_objs.Layout(
        title='Actuated Traffic Light States',
        xaxis=dict(
            title='Time (s)',
            titlefont=dict(
                family='Courier New, monospace',
                size=36,
                color='#7f7f7f'
            )
        ),
        yaxis=dict(
            title='State',
            titlefont=dict(
                family='Courier New, monospace',
                size=36,
                color='#7f7f7f'
            )
        )
    )

    ew_green_states = Bar(
        x=dynamic_timesteps,
        y=dynamic_tl_ew_green_states,
        marker=dict(color="green"),
        name="East/West Green Light Phase"
    )
    ns_green_states = Bar(
        x=dynamic_timesteps,
        y=dynamic_tl_ns_green_states,
        marker=dict(color="lightgreen"),
        name="North/South Green Light Phase"
    )
    orange_states = Bar(
        x=dynamic_timesteps,
        y=dynamic_tl_yellow_states,
        marker=dict(color="orange"),
        name="Orange Light Phase"
    )

    data = [ew_green_states, ns_green_states, orange_states]
    fig = graph_objs.Figure(data=data, layout=layout)

    py.plot(fig, filename='actuated-trafficlight-durations')


def main():

    plot_static()
    plot_actuated()
    plot_dynamic()

if __name__ == "__main__":
    main()