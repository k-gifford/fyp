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
        if result.attrib['state'] == "GGggrrrrGGggrrrr":
            state = 1
        elif result.attrib['state'] == "rrrrGGggrrrrGGgg":
            state = -1
        elif result.attrib['state'] == "yyyyrrrryyyyrrrr":
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
        if result.attrib['state'] == "GGggrrrrGGggrrrr":
            state = 1
        elif result.attrib['state'] == "yyggrrrryyggrrrr":
            state = 1
        elif result.attrib['state'] == "rrGGrrrrrrGGrrrr":
            state = 1
        elif result.attrib['state'] == "rryyrrrrrryyrrrr":
            state = .5
        elif result.attrib['state'] == "rrrrGGggrrrrGGgg":
            state = -1
        elif result.attrib['state'] == "rrrryyggrrrryygg":
            state = -1
        elif result.attrib['state'] == "rrrrrrGGrrrrrrGG":
            state = -1
        else:
            state = -.5 # rryyrrrrrryyrrrr

        data = {'timestep': result.attrib['time'], 'state': state}
        writer.writerow(data)

def parseActuatedTlStates():
    csvfile = open('actuatedtlstates.csv', 'w')
    writer = csv.DictWriter(csvfile, fieldnames=['timestep', 'state'])
    writer.writeheader()
    tree = ET.parse("tl_states.xml")
    root = tree.getroot()
    for result in root:
        state = 0
        if result.attrib['state'] == "GGggrrrrGGggrrrr":
            state = 1
        elif result.attrib['state'] == "yyggrrrryyggrrrr":
            state = 1
        elif result.attrib['state'] == "rrGGrrrrrrGGrrrr":
            state = 1
        elif result.attrib['state'] == "rryyrrrrrryyrrrr":
            state = .5
        elif result.attrib['state'] == "rrrrGGggrrrrGGgg":
            state = -1
        elif result.attrib['state'] == "rrrryyggrrrryygg":
            state = -1
        elif result.attrib['state'] == "rrrrrrGGrrrrrrGG":
            state = -1
        else:
            state = -.5 # rryyrrrrrryyrrrr

        data = {'timestep': result.attrib['time'], 'state': state}
        writer.writerow(data)


def main():

    # parseDynamicTlStates()
    # parseStaticTlStates()
    parseActuatedTlStates()

if __name__ == "__main__":

    main()