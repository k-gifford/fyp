import csv
import xml.etree.ElementTree as ET

csvfile = open('staticresults.csv', 'w')
writer = csv.DictWriter(csvfile , fieldnames=['vehicleId', 'tripDuration', 'totalWaitingTime'])
writer.writeheader()
tree = ET.parse("staticresults.xml")
root = tree.getroot()
for result in root:
    data = {'vehicleId': result.attrib['id'], 'tripDuration':result.attrib['duration'], 'totalWaitingTime': result.attrib['waitSteps']}
    writer.writerow(data)

csvfile = open('actuatedresults.csv', 'w')
writer = csv.DictWriter(csvfile , fieldnames=['vehicleId', 'tripDuration', 'totalWaitingTime'])
writer.writeheader()
tree = ET.parse("actuatedresults.xml")
root = tree.getroot()
for result in root:
    data = {'vehicleId': result.attrib['id'], 'tripDuration':result.attrib['duration'], 'totalWaitingTime': result.attrib['waitSteps']}
    writer.writerow(data)


csvfile = open('dynamicresults.csv', 'w')
writer = csv.DictWriter(csvfile , fieldnames=['vehicleId', 'tripDuration', 'totalWaitingTime'])
writer.writeheader()
tree = ET.parse("dynamicresults.xml")
root = tree.getroot()
for result in root:
    data = {'vehicleId': result.attrib['id'], 'tripDuration':result.attrib['duration'], 'totalWaitingTime': result.attrib['waitSteps']}
    writer.writerow(data)

