#!/usr/bin/env python3
import csv
import xml.etree.ElementTree as ET

from plot_vehicles_waiting import *
from parse_tl_states import *
from plot_tl_states import *
import plotly.plotly as py
from plotly.graph_objs import *


def parse_static_trip_info():
    csv_file = open('static.trip.infos.csv', 'w')
    writer = csv.DictWriter(csv_file, fieldnames=['vehicleId', 'tripDuration', 'totalWaitingTime'])
    writer.writeheader()
    tree = ET.parse("static.trip.infos.xml")
    root = tree.getroot()
    duration = 0
    waiting = 0
    count = 0
    for result in root:
        data = {'vehicleId': result.attrib['id'],
                'tripDuration': result.attrib['duration'],
                'totalWaitingTime': result.attrib['waitSteps']}
        writer.writerow(data)
        duration += float(data['tripDuration'])
        waiting += float(data['totalWaitingTime'])
        count += 1
    avg_dur = duration/count
    avg_wait = waiting/count
    print("Static [Avg Dur:", avg_dur, ", Avg Wait:", avg_wait)


def parse_actuated_trip_info():
    csv_file = open('actuated.trip.infos.csv', 'w')
    writer = csv.DictWriter(csv_file, fieldnames=['vehicleId', 'tripDuration', 'totalWaitingTime'])
    writer.writeheader()
    tree = ET.parse("actuated.trip.infos.xml")
    root = tree.getroot()
    duration = 0
    waiting = 0
    count = 0
    for result in root:
        data = {'vehicleId': result.attrib['id'],
                'tripDuration': result.attrib['duration'],
                'totalWaitingTime': result.attrib['waitSteps']}
        writer.writerow(data)
        duration += float(data['tripDuration'])
        waiting += float(data['totalWaitingTime'])
        count += 1
    avg_dur = duration / count
    avg_wait = waiting / count
    print("Actuated [Avg Dur:", avg_dur, ", Avg Wait:", avg_wait)


def parse_dynamic_trip_info():
    csv_file = open('dynamic.trip.infos.csv', 'w')
    writer = csv.DictWriter(csv_file, fieldnames=['vehicleId', 'tripDuration', 'totalWaitingTime'])
    writer.writeheader()
    tree = ET.parse("dynamic.trip.infos.xml")
    root = tree.getroot()
    duration = 0
    waiting = 0
    count = 0
    for result in root:
        data = {'vehicleId': result.attrib['id'],
                'tripDuration': result.attrib['duration'],
                'totalWaitingTime': result.attrib['waitSteps']}
        writer.writerow(data)
        duration += float(data['tripDuration'])
        waiting += float(data['totalWaitingTime'])
        count += 1
    avg_dur = duration / count
    avg_wait = waiting / count
    print("Dynamic [Avg Dur:", avg_dur, ", Avg Wait:", avg_wait)

def plot_trip_infos_waiting_time():
    fields = ['vehicleId', 'tripDuration', 'totalWaitingTime']
    num_static_vehicles = 0
    csv_file = open('static.trip.infos.csv', 'r')
    reader = csv.DictReader(csv_file, fieldnames=fields)
    static = 0
    next(reader, None)  # skip the headers
    for row in reader:
        value = float(row['totalWaitingTime'])
        static += value
        num_static_vehicles += 1

    num_actuated_vehicles = 0
    csv_file = open('actuated.trip.infos.csv', 'r')
    reader = csv.DictReader(csv_file, fieldnames=fields)
    actuated = 0
    next(reader, None)  # skip the headers
    for row in reader:
        value = float(row['totalWaitingTime'])
        actuated += value
        num_actuated_vehicles += 1

    num_dynamic_vehicles = 0
    csv_file = open('dynamic.trip.infos.csv', 'r')
    reader = csv.DictReader(csv_file, fieldnames=fields)
    dynamic = 0
    next(reader, None)  # skip the headers
    for row in reader:
        value = float(row['totalWaitingTime'])
        dynamic += value
        num_dynamic_vehicles += 1

    # dividing to get average
    static = static / num_static_vehicles
    actuated = actuated / num_actuated_vehicles
    dynamic = dynamic / num_dynamic_vehicles

    layout = graph_objs.Layout(
        title='Average Vehicle Waiting Times',
        xaxis=dict(
            title='Traffic Control Algorithm',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
        yaxis=dict(
            title='Average Waiting Time (s)',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
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

    static = Bar(
        y=static,
        marker=dict(color="green"),
        name="Static Average Waiting Times"
    )
    actuated = Bar(
        y=actuated,
        marker=dict(color="blue"),
        name="Actuated Average Waiting Times"
    )
    dynamic = Bar(
        y=dynamic,
        marker=dict(color="red"),
        name="Dynamic Average Waiting Times"
    )

    data = [static, actuated, dynamic]
    fig = graph_objs.Figure(data=data, layout=layout)

    py.plot(fig, filename='average-vehicle-waiting-times')


def plot_trip_infos_journey_durations():
    fields = ['vehicleId', 'tripDuration', 'totalWaitingTime']
    num_static_vehicles = 0
    csv_file = open('static.trip.infos.csv', 'r')
    reader = csv.DictReader(csv_file, fieldnames=fields)
    static = 0
    next(reader, None)  # skip the headers
    for row in reader:
        value = float(row['tripDuration'])
        static += value
        num_static_vehicles += 1

    num_actuated_vehicles = 0
    csv_file = open('actuated.trip.infos.csv', 'r')
    reader = csv.DictReader(csv_file, fieldnames=fields)
    actuated = 0
    next(reader, None)  # skip the headers
    for row in reader:
        value = float(row['tripDuration'])
        actuated += value
        num_actuated_vehicles += 1

    num_dynamic_vehicles = 0
    csv_file = open('dynamic.trip.infos.csv', 'r')
    reader = csv.DictReader(csv_file, fieldnames=fields)
    dynamic = 0
    next(reader, None)  # skip the headers
    for row in reader:
        value = float(row['tripDuration'])
        dynamic += value
        num_dynamic_vehicles += 1

    # dividing to get average
    static = static / num_static_vehicles
    actuated = actuated / num_actuated_vehicles
    dynamic = dynamic / num_dynamic_vehicles

    layout = graph_objs.Layout(
        title='Average Vehicle Journey Times',
        xaxis=dict(
            title='Traffic Control Algorithm',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
        yaxis=dict(
            title='Average Journey Time (s)',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
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

    static = Bar(
        y=static,
        marker=dict(color="green"),
        name="Static Average Journey Time"
    )
    actuated = Bar(
        y=actuated,
        marker=dict(color="blue"),
        name="Actuated Average Journey Time"
    )
    dynamic = Bar(
        y=dynamic,
        marker=dict(color="red"),
        name="Dynamic Average Journey Time"
    )

    data = [static, actuated, dynamic]
    fig = graph_objs.Figure(data=data, layout=layout)

    py.plot(fig, filename='average-vehicle-trip_duration-times')


def parse_static_plot_waiting_vehicles():
    edge_ids = ['-33708057#2', '-33708057#1', '-138139938#0', '35202667#1', '-173864128', '462149208', '-173864145#1',
                '173864127', '-173864139', '-488360085', '33708057#3', '-173864127', '173864145#2', '74816886',
                '-74816886', '-374366365#3', '35202667#0', '-173864145#0', '173864153', '-33708057#3', '173864128',
                '414126489', '33708057#0', '35202667#2', '173864145#1', '173864139', '-173864145#2', '374366365#3',
                '-462149208', '-138139938#2', '-173864153', '-35202667#1', '488360085', '-35202667#2', '173864130',
                '33708057#2', '-374366365#4', '374366365#0', '-35202667#0', '374366365#4', '173864145#0', '138139938#2',
                '-374366365#2']

    csv_file = open('static.edge.output.data.csv', 'w')
    writer = csv.DictWriter(csv_file, fieldnames=edge_ids)
    writer.writeheader()
    tree = ET.parse("static.edge.output.xml")
    root = tree.getroot()

    # for every interval
    for interval in root:
        # for every edge in the interval
        data = dict()
        for edge in interval:
            # for every id in edge_ids
            for e_id in edge_ids:
                # if the id is the same as the edge id we are currently on
                if e_id == edge.attrib['id']:
                    if edge.attrib['sampledSeconds'] != "0.00":
                        data[e_id] = edge.attrib['waitingTime']

        writer.writerow(data)

    north_ids = ['33708057#0', '33708057#2', '33708057#3']
    south_ids = ['-35202667#2', '-35202667#1', '-35202667#0']
    north_south_waiting_vehicles = []

    west_ids = ['374366365#0', '374366365#3', '374366365#4']
    east_ids = ['-138139938#2', '-138139938#0']
    east_west_waiting_vehicles = []

    csv_file = open('static.edge.output.data.csv', 'r')
    reader = csv.DictReader(csv_file, fieldnames=edge_ids)
    next(reader, None)  # skip the headers
    for row in reader:
        north_count = 0.0
        for edge_id in north_ids:
            if row[edge_id] is not '':
                value = float(row[edge_id])
                north_count = north_count + value

        south_count = 0.0
        for edge_id in south_ids:
            if row[edge_id] is not '':
                value = float(row[edge_id])
                south_count = south_count + value
        north_south_waiting_vehicles.append(north_count + south_count)

        east_count = 0.0
        for edge_id in east_ids:
            if row[edge_id] is not '':
                value = float(row[edge_id])
                east_count = east_count + value

        west_count = 0.0
        for edge_id in west_ids:
            if row[edge_id] is not '':
                value = float(row[edge_id])
                west_count = west_count + value
        east_west_waiting_vehicles.append(east_count + west_count)

    plot_static_vehicles(north_south_waiting_vehicles, east_west_waiting_vehicles)


def parse_actuated_plot_waiting_vehicles():
    edge_ids = ['-33708057#2', '-33708057#1', '-138139938#0', '35202667#1', '-173864128', '462149208', '-173864145#1',
                '173864127', '-173864139', '-488360085', '33708057#3', '-173864127', '173864145#2', '74816886',
                '-74816886', '-374366365#3', '35202667#0', '-173864145#0', '173864153', '-33708057#3', '173864128',
                '414126489', '33708057#0', '35202667#2', '173864145#1', '173864139', '-173864145#2', '374366365#3',
                '-462149208', '-138139938#2', '-173864153', '-35202667#1', '488360085', '-35202667#2', '173864130',
                '33708057#2', '-374366365#4', '374366365#0', '-35202667#0', '374366365#4', '173864145#0', '138139938#2',
                '-374366365#2']

    csv_file = open('actuated.edge.output.data.csv', 'w')
    writer = csv.DictWriter(csv_file, fieldnames=edge_ids)
    writer.writeheader()
    tree = ET.parse("actuated.edge.output.xml")
    root = tree.getroot()

    # for every interval
    for interval in root:
        # for every edge in the interval
        data = dict()
        for edge in interval:
            # for every id in edge_ids
            for e_id in edge_ids:
                # if the id is the same as the edge id we are currently on
                if e_id == edge.attrib['id']:
                    if edge.attrib['sampledSeconds'] != "0.00":
                        data[e_id] = edge.attrib['waitingTime']

        writer.writerow(data)

    north_ids = ['33708057#0', '33708057#2', '33708057#3']
    south_ids = ['-35202667#2', '-35202667#1', '-35202667#0']
    north_south_waiting_vehicles = []

    west_ids = ['374366365#0', '374366365#3', '374366365#4']
    east_ids = ['-138139938#2', '-138139938#0']
    east_west_waiting_vehicles = []

    csv_file = open('actuated.edge.output.data.csv', 'r')
    reader = csv.DictReader(csv_file, fieldnames=edge_ids)
    next(reader, None)  # skip the headers
    for row in reader:
        north_count = 0.0
        for edge_id in north_ids:
            if row[edge_id] is not '':
                value = float(row[edge_id])
                north_count = north_count + value

        south_count = 0.0
        for edge_id in south_ids:
            if row[edge_id] is not '':
                value = float(row[edge_id])
                south_count = south_count + value
        north_south_waiting_vehicles.append(north_count + south_count)

        east_count = 0.0
        for edge_id in east_ids:
            if row[edge_id] is not '':
                value = float(row[edge_id])
                east_count = east_count + value

        west_count = 0.0
        for edge_id in west_ids:
            if row[edge_id] is not '':
                value = float(row[edge_id])
                west_count = west_count + value
        east_west_waiting_vehicles.append(east_count + west_count)

    plot_actuated_vehicles(north_south_waiting_vehicles, east_west_waiting_vehicles)


def parse_dynamic_plot_waiting_vehicles():
    edge_ids = ['-33708057#2', '-33708057#1', '-138139938#0', '35202667#1', '-173864128', '462149208', '-173864145#1',
                '173864127', '-173864139', '-488360085', '33708057#3', '-173864127', '173864145#2', '74816886',
                '-74816886', '-374366365#3', '35202667#0', '-173864145#0', '173864153', '-33708057#3', '173864128',
                '414126489', '33708057#0', '35202667#2', '173864145#1', '173864139', '-173864145#2', '374366365#3',
                '-462149208', '-138139938#2', '-173864153', '-35202667#1', '488360085', '-35202667#2', '173864130',
                '33708057#2', '-374366365#4', '374366365#0', '-35202667#0', '374366365#4', '173864145#0', '138139938#2',
                '-374366365#2']

    csv_file = open('dynamic.edge.output.data.csv', 'w')
    writer = csv.DictWriter(csv_file, fieldnames=edge_ids)
    writer.writeheader()
    tree = ET.parse("dynamic.edge.output.xml")
    root = tree.getroot()

    # for every interval
    for interval in root:
        # for every edge in the interval
        data = dict()
        for edge in interval:
            # for every id in edge_ids
            for e_id in edge_ids:
                # if the id is the same as the edge id we are currently on
                if e_id == edge.attrib['id']:
                    if edge.attrib['sampledSeconds'] != "0.00":
                        data[e_id] = edge.attrib['waitingTime']

        writer.writerow(data)

    north_ids = ['33708057#0', '33708057#2', '33708057#3']
    south_ids = ['-35202667#2', '-35202667#1', '-35202667#0']
    north_south_waiting_vehicles = []

    west_ids = ['374366365#0', '374366365#3', '374366365#4']
    east_ids = ['-138139938#2', '-138139938#0']
    east_west_waiting_vehicles = []

    csv_file = open('dynamic.edge.output.data.csv', 'r')
    reader = csv.DictReader(csv_file, fieldnames=edge_ids)
    next(reader, None)  # skip the headers
    for row in reader:
        north_count = 0.0
        for edge_id in north_ids:
            if row[edge_id] is not '':
                value = float(row[edge_id])
                north_count = north_count + value

        south_count = 0.0
        for edge_id in south_ids:
            if row[edge_id] is not '':
                value = float(row[edge_id])
                south_count = south_count + value
        north_south_waiting_vehicles.append(north_count + south_count)

        east_count = 0.0
        for edge_id in east_ids:
            if row[edge_id] is not '':
                value = float(row[edge_id])
                east_count = east_count + value

        west_count = 0.0
        for edge_id in west_ids:
            if row[edge_id] is not '':
                value = float(row[edge_id])
                west_count = west_count + value
        east_west_waiting_vehicles.append(east_count + west_count)

    plot_dynamic_vehicles(north_south_waiting_vehicles, east_west_waiting_vehicles)


"""
Plot the waiting vehicles for every time step for all three of the control algorithms
"""


def parse_plot_all_waiting_vehicles():
    edge_ids = ['-33708057#2', '-33708057#1', '-138139938#0', '35202667#1', '-173864128', '462149208', '-173864145#1',
                '173864127', '-173864139', '-488360085', '33708057#3', '-173864127', '173864145#2', '74816886',
                '-74816886', '-374366365#3', '35202667#0', '-173864145#0', '173864153', '-33708057#3', '173864128',
                '414126489', '33708057#0', '35202667#2', '173864145#1', '173864139', '-173864145#2', '374366365#3',
                '-462149208', '-138139938#2', '-173864153', '-35202667#1', '488360085', '-35202667#2', '173864130',
                '33708057#2', '-374366365#4', '374366365#0', '-35202667#0', '374366365#4', '173864145#0', '138139938#2',
                '-374366365#2']

    csv_file = open('static.edge.output.data.csv', 'r')
    reader = csv.DictReader(csv_file, fieldnames=edge_ids)
    next(reader, None)  # skip the headers
    static_vehicle_counts = []
    for row in reader:
        static = 0.0
        for e_id in edge_ids:
            if row[e_id] is not '':
                value = float(row[e_id])
                static = static + value
        static_vehicle_counts.append(static)

    csv_file = open('actuated.edge.output.data.csv', 'r')
    reader = csv.DictReader(csv_file, fieldnames=edge_ids)
    next(reader, None)  # skip the headers
    actuated_vehicle_counts = []
    for row in reader:
        actuated = 0.0
        for e_id in edge_ids:
            if row[e_id] is not '':
                value = float(row[e_id])
                actuated = actuated + value
        actuated_vehicle_counts.append(actuated)

    csv_file = open('dynamic.edge.output.data.csv', 'r')
    reader = csv.DictReader(csv_file, fieldnames=edge_ids)
    next(reader, None)  # skip the headers
    dynamic_vehicle_counts = []
    for row in reader:
        dynamic = 0.0
        for e_id in edge_ids:
            if row[e_id] is not '':
                value = float(row[e_id])
                dynamic = dynamic + value
        dynamic_vehicle_counts.append(dynamic)

    plot_all_tl_alg_vehicles(static_vehicle_counts, actuated_vehicle_counts, dynamic_vehicle_counts)


def parse_plot_ns_waiting_vehicles():
    edge_ids = ['-33708057#2', '-33708057#1', '-138139938#0', '35202667#1', '-173864128', '462149208', '-173864145#1',
                '173864127', '-173864139', '-488360085', '33708057#3', '-173864127', '173864145#2', '74816886',
                '-74816886', '-374366365#3', '35202667#0', '-173864145#0', '173864153', '-33708057#3', '173864128',
                '414126489', '33708057#0', '35202667#2', '173864145#1', '173864139', '-173864145#2', '374366365#3',
                '-462149208', '-138139938#2', '-173864153', '-35202667#1', '488360085', '-35202667#2', '173864130',
                '33708057#2', '-374366365#4', '374366365#0', '-35202667#0', '374366365#4', '173864145#0', '138139938#2',
                '-374366365#2']

    north_south_ids = ['33708057#0', '33708057#2', '33708057#3', '-35202667#2', '-35202667#1', '-35202667#0']

    csv_file = open('static.edge.output.data.csv', 'r')
    reader = csv.DictReader(csv_file, fieldnames=edge_ids)
    next(reader, None)  # skip the headers
    static_north_south_waiting_vehicles = []
    for row in reader:
        static = 0.0
        for e_id in north_south_ids:
            if row[e_id] is not '':
                value = float(row[e_id])
                static = static + value
        static_north_south_waiting_vehicles.append(static)

    csv_file = open('actuated.edge.output.data.csv', 'r')
    reader = csv.DictReader(csv_file, fieldnames=edge_ids)
    next(reader, None)  # skip the headers
    actuated_north_south_waiting_vehicles = []
    for row in reader:
        actuated = 0.0
        for e_id in north_south_ids:
            if row[e_id] is not '':
                value = float(row[e_id])
                actuated = actuated + value
        actuated_north_south_waiting_vehicles.append(actuated)

    csv_file = open('dynamic.edge.output.data.csv', 'r')
    reader = csv.DictReader(csv_file, fieldnames=edge_ids)
    next(reader, None)  # skip the headers
    dynamic_north_south_waiting_vehicles = []
    for row in reader:
        dynamic = 0.0
        for e_id in edge_ids:
            if row[e_id] is not '':
                value = float(row[e_id])
                dynamic = dynamic + value
        dynamic_north_south_waiting_vehicles.append(dynamic)

    plot_all_ns_tl_alg_vehicles(static_north_south_waiting_vehicles,
                                actuated_north_south_waiting_vehicles,
                                dynamic_north_south_waiting_vehicles)


def parse_plot_ew_waiting_vehicles():
    edge_ids = ['-33708057#2', '-33708057#1', '-138139938#0', '35202667#1', '-173864128', '462149208', '-173864145#1',
                '173864127', '-173864139', '-488360085', '33708057#3', '-173864127', '173864145#2', '74816886',
                '-74816886', '-374366365#3', '35202667#0', '-173864145#0', '173864153', '-33708057#3', '173864128',
                '414126489', '33708057#0', '35202667#2', '173864145#1', '173864139', '-173864145#2', '374366365#3',
                '-462149208', '-138139938#2', '-173864153', '-35202667#1', '488360085', '-35202667#2', '173864130',
                '33708057#2', '-374366365#4', '374366365#0', '-35202667#0', '374366365#4', '173864145#0', '138139938#2',
                '-374366365#2']

    east_west_ids = ['374366365#0', '374366365#3', '374366365#4', '-138139938#2', '-138139938#0']

    csv_file = open('static.edge.output.data.csv', 'r')
    reader = csv.DictReader(csv_file, fieldnames=edge_ids)
    next(reader, None)  # skip the headers
    static_east_west_waiting_vehicles = []
    for row in reader:
        static = 0.0
        for e_id in east_west_ids:
            if row[e_id] is not '':
                value = float(row[e_id])
                static = static + value
        static_east_west_waiting_vehicles.append(static)

    csv_file = open('actuated.edge.output.data.csv', 'r')
    reader = csv.DictReader(csv_file, fieldnames=edge_ids)
    next(reader, None)  # skip the headers
    actuated_east_west_waiting_vehicles = []
    for row in reader:
        actuated = 0.0
        for e_id in east_west_ids:
            if row[e_id] is not '':
                value = float(row[e_id])
                actuated = actuated + value
        actuated_east_west_waiting_vehicles.append(actuated)

    csv_file = open('dynamic.edge.output.data.csv', 'r')
    reader = csv.DictReader(csv_file, fieldnames=edge_ids)
    next(reader, None)  # skip the headers
    dynamic_east_west_waiting_vehicles = []
    for row in reader:
        dynamic = 0.0
        for e_id in east_west_ids:
            if row[e_id] is not '':
                value = float(row[e_id])
                dynamic = dynamic + value
        dynamic_east_west_waiting_vehicles.append(dynamic)

    plot_all_ew_tl_alg_vehicles(static_east_west_waiting_vehicles,
                                actuated_east_west_waiting_vehicles,
                                dynamic_east_west_waiting_vehicles)


def main():

    # parse_dynamic_tl_states()
    # parse_static_tl_states()
    # parse_actuated_tl_states()
    #
    # plot_static()
    # plot_actuated()
    # plot_dynamic()

    # parse_static_trip_info()
    # parse_actuated_trip_info()
    parse_dynamic_trip_info()

    # plot_trip_infos_waiting_time()
    # plot_trip_infos_journey_durations()

    # parse_static_plot_waiting_vehicles()
    # parse_actuated_plot_waiting_vehicles()
    # parse_dynamic_plot_waiting_vehicles()
    #
    # parse_plot_all_waiting_vehicles()
    # parse_plot_ns_waiting_vehicles()
    # parse_plot_ew_waiting_vehicles()


if __name__ == "__main__":
    main()

#
