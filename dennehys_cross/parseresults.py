#!/usr/bin/env python3
import csv
import xml.etree.ElementTree as ET

from plot_vehicles_waiting import plotTimes

"""
csv_file = open('staticresults.csv', 'w')
writer = csv.DictWriter(csv_file , fieldnames=['vehicleId', 'tripDuration', 'totalWaitingTime'])
writer.writeheader()
tree = ET.parse("staticresults.xml")
root = tree.getroot()
for result in root:
    data = {'vehicleId': result.attrib['id'], 'tripDuration':result.attrib['duration'], 'totalWaitingTime': result.attrib['waitSteps']}
    writer.writerow(data)

csv_file = open('actuatedresults.csv', 'w')
writer = csv.DictWriter(csv_file , fieldnames=['vehicleId', 'tripDuration', 'totalWaitingTime'])
writer.writeheader()
tree = ET.parse("actuatedresults.xml")
root = tree.getroot()
for result in root:
    data = {'vehicleId': result.attrib['id'], 'tripDuration':result.attrib['duration'], 'totalWaitingTime': result.attrib['waitSteps']}
    writer.writerow(data)


csv_file = open('dynamicresults.csv', 'w')
writer = csv.DictWriter(csv_file , fieldnames=['vehicleId', 'tripDuration', 'totalWaitingTime'])
writer.writeheader()
tree = ET.parse("dynamicresults.xml")
root = tree.getroot()
for result in root:
    data = {'vehicleId': result.attrib['id'], 'tripDuration':result.attrib['duration'], 'totalWaitingTime': result.attrib['waitSteps']}
    writer.writerow(data)
"""



"""
Approaching edge ids:
NORTH -> SOUTH
33708057#0
33708057#2
33708057#3

SOUTH -> NORTH
-35202667#2
-35202667#1
-35202667#0

WEST -> EAST
374366365#0
374366365#3
374366365#4

EAST -> WEST
-138139938#2
-138139938#0

for row in reader:
    north_count = 0.0
    for edge_id in north_ids:
        if row[edge_id] is not '':
            value = float(row[edge_id])
            north_count = north_count + value
    northWaitingVehicles.append(north_count)

    south_count = 0.0
    for edge_id in south_ids:
        if row[edge_id] is not '':
            value = float(row[edge_id])
            south_count = south_count + value
    southWaitingVehicles.append(south_count)

    east_count = 0.0
    for edge_id in east_ids:
        if row[edge_id] is not '':
            value = float(row[edge_id])
            east_count = east_count + value
    eastWaitingVehicles.append(east_count)

    west_count = 0.0
    for edge_id in west_ids:
        if row[edge_id] is not '':
            value = float(row[edge_id])
            west_count = west_count + value
    westWaitingVehciles.append(west_count)
"""

edgeids =['-33708057#2', '-33708057#1', '-138139938#0', '35202667#1', '-173864128', '462149208', '-173864145#1', '173864127', '-173864139', '-488360085', '33708057#3', '-173864127', '173864145#2', '74816886', '-74816886', '-374366365#3', '35202667#0', '-173864145#0', '173864153', '-33708057#3', '173864128', '414126489', '33708057#0', '35202667#2', '173864145#1', '173864139', '-173864145#2', '374366365#3', '-462149208', '-138139938#2', '-173864153', '-35202667#1', '488360085', '-35202667#2', '173864130', '33708057#2', '-374366365#4', '374366365#0', '-35202667#0', '374366365#4', '173864145#0', '138139938#2', '-374366365#2']

csv_file = open('edge.output.data.csv', 'w')
writer = csv.DictWriter(csv_file , fieldnames=edgeids)
writer.writeheader()
tree = ET.parse("edge.output.xml")
root = tree.getroot()

# for every interval
for interval in root:
    # for every edge in the interval
    data = dict()
    for edge in interval:
        # for every id in edgeids
        for id in edgeids:
            # if the id is the same as the edge id we are currently on
            if id == edge.attrib['id']:
                if edge.attrib['sampledSeconds'] != "0.00":
                    data[id] = edge.attrib['waitingTime']

    writer.writerow(data)


north_ids = ['33708057#0', '33708057#2', '33708057#3']
northWaitingVehicles = []

south_ids = ['-35202667#2', '-35202667#1', '-35202667#0']
southWaitingVehicles = []

east_ids = ['-138139938#2', '-138139938#0']
eastWaitingVehicles = []

west_ids = ['374366365#0', '374366365#3', '374366365#4']
westWaitingVehicles = []

csv_file = open('edge.output.data.csv', 'r')
reader = csv.DictReader(csv_file, fieldnames=edgeids)
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
    northWaitingVehicles.append(north_count+south_count)

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
    eastWaitingVehicles.append(east_count + west_count)

plotTimes(northWaitingVehicles, eastWaitingVehicles)
























#