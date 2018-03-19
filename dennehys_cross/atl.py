"""
Class to represent the Adaptive Traffic Light controller
"""

import os, sys
tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
sys.path.append(tools)
import traci
import xml.etree.ElementTree as ET


class Atl:

    def __init__(self, id, traffic_lights, induction_loops_file_location):
        self.id = id
        self.traffic_lights  = traffic_lights
        self.e1_loops = []
        self.retreiveE1LoopIds(induction_loops_file_location)
        self.det_counts = {}
        self.setCounts()
        self.nsCount = 0
        self.ewCount = 0
        self.nsLoops = []
        self.ewLoops = []

    def getId(self):
        return self.id

    def getState(self):
        return self.traffic_lights

    def getE1Loops(self):
        return self.e1_loops

    def retreiveE1LoopIds(self, location):
        tree = ET.parse(location)
        root = tree.getroot()
        for e1 in root:
            self.e1_loops.append(e1.attrib['id'])

    def setCounts(self):
        for loop in self.e1_loops:
            self.det_counts[loop] = 0

    """
    Takes in the number of incoming lanes from North, East, South and West,
    for a particular junction. And assigns the detectors on those lanes
    to that incoming direction - to be used for counting the incoming
    vehicles from each direction.

    """
    def assignJunctionDetectors(self, north, east, south, west):

        lane = 0
        for loop in self.e1_loops:
            if (lane < north):
                self.nsLoops.append(loop)
                lane += 1
            elif(lane < (north+east)):
                self.ewLoops.append(loop)
                lane += 1
            elif(lane < (north + east + south)):
                self.nsLoops.append(loop)
                lane += 1
            else:
                self.ewLoops.append(loop)
                lane += 1


    def getCounts(self):
        return self.det_counts

    def updateCounts(self):
        counts = self.detect()
        pointer = 0
        for loop in self.e1_loops:
            self.det_counts[loop] += counts[pointer]
            pointer+=1


    def detect(self):
        counts = []
        for loop in self.e1_loops:
            counts.append(traci.inductionloop.getLastStepVehicleNumber(loop))

        return counts



def main():
    dennehys_cross = Atl("354512")
    print(dennehys_cross.getId())

if __name__ == "__main__":
    main()
