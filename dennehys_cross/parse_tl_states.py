#!/usr/bin/env python3
import csv
import xml.etree.ElementTree as ET


def parse_static_tl_states():
    csv_file = open('statictlstates.csv', 'w')
    writer = csv.DictWriter(csv_file, fieldnames=['timestep', 'state'])
    writer.writeheader()
    tree = ET.parse("static.tl_states.xml")
    root = tree.getroot()
    for result in root:
        state = 0
        if result.attrib['state'] == "GGgrrrGGgrrr":
            state = 1
        elif result.attrib['state'] == "yygrrryygrrr":
            state = 1
        elif result.attrib['state'] == "rrGrrrrrGrrr":
            state = 1
        elif result.attrib['state'] == "rryrrrrryrrr":
            state = .5
        elif result.attrib['state'] == "rrrGGgrrrGGg":
            state = -1
        elif result.attrib['state'] == "rrryygrrryyg":
            state = -1
        elif result.attrib['state'] == "rrrrrGrrrrrG":
            state = -1
        else:
            state = -.5  # rryrrrrryrrr

        data = {'timestep': result.attrib['time'], 'state': state}
        writer.writerow(data)

def parse_actuated_tl_states():
    csv_file = open('actuatedtlstates.csv', 'w')
    writer = csv.DictWriter(csv_file, fieldnames=['timestep', 'state'])
    writer.writeheader()
    tree = ET.parse("actuated.tl_states.xml")
    root = tree.getroot()
    state = 0
    for result in root:

        if result.attrib['state'] == "GGgrrrGGgrrr":
            state = 1
        elif result.attrib['state'] == "yygrrryygrrr":
            state = 1
        elif result.attrib['state'] == "rrGrrrrrGrrr":
            state = 1
        elif result.attrib['state'] == "rryrrrrryrrr":
            state = .5
        elif result.attrib['state'] == "rrrGGgrrrGGg":
            state = -1
        elif result.attrib['state'] == "rrryygrrryyg":
            state = -1
        elif result.attrib['state'] == "rrrrrGrrrrrG":
            state = -1
        else:
            state = -.5  # rryrrrrryrrr



        data = {'timestep': result.attrib['time'], 'state': state}
        writer.writerow(data)


def parse_dynamic_tl_states():
    csv_file = open('dynamictlstates.csv', 'w')
    writer = csv.DictWriter(csv_file, fieldnames=['timestep', 'state'])
    writer.writeheader()
    tree = ET.parse("dynamic.tl_states.xml")
    root = tree.getroot()
    for result in root:
        state = 0
        if result.attrib['state'] == "GGgrrrGGgrrr":
            state = 1
        elif result.attrib['state'] == "rrrGGgrrrGGg":
            state = -1
        elif result.attrib['state'] == "yyyrrryyyrrr":
            state = .5
        else:
            state = -.5

        data = {'timestep': result.attrib['time'], 'state': state}
        writer.writerow(data)

def main():

    parse_dynamic_tl_states()
    parse_static_tl_states()
    parse_actuated_tl_states()

if __name__ == "__main__":

    main()