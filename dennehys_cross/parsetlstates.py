#!/usr/bin/env python3
import csv
import xml.etree.ElementTree as ET


def parseDynamicTlStates():
    csvfile = open('dynamictlstates.csv', 'w')
    writer = csv.DictWriter(csvfile, fieldnames=['timestep', 'state'])
    writer.writeheader()
    tree = ET.parse("tl_states.xml")
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

def parseStaticTlStates():
    csvfile = open('statictlstates.csv', 'w')
    writer = csv.DictWriter(csvfile, fieldnames=['timestep', 'state'])
    writer.writeheader()
    tree = ET.parse("tl_states.xml")
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

def parseActuatedTlStates():
    csvfile = open('actuatedtlstates.csv', 'w')
    writer = csv.DictWriter(csvfile, fieldnames=['timestep', 'state'])
    writer.writeheader()
    tree = ET.parse("tl_states.xml")
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


def main():

    # parseDynamicTlStates()
    parseStaticTlStates()
    # parseActuatedTlStates()

if __name__ == "__main__":

    main()