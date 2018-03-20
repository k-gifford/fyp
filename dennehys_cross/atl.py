"""
Class to represent the Adaptive Traffic Light controller
"""

import os, sys
tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
sys.path.append(tools)
import traci
import xml.etree.ElementTree as ET


class Atl:

    def __init__(self, id, induction_loops_file_location):
        self.id = id
        self.trafficLightLogic  = dict()
        self.e1_loops = []
        self.retreiveE1LoopIds(induction_loops_file_location)
        self.nsCount = 0
        self.ewCount = 0
        self.nsLoops = []
        self.ewLoops = []
        self.activePhase = 0
        self.nextActivePhase = 0
        self.activePhaseDuration = 30
        self.nextActivePhaseDuration = 20
        self.totalRunningTime = 0
        self.nextGreenPhaseCalculation = 30

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

    def detectNS(self):
        for loop in self.nsLoops:
            self.nsCount += traci.inductionloop.getLastStepVehicleNumber(loop)
        return self.nsCount

    def detectEW(self):
        for loop in self.ewLoops:
            self.ewCount += traci.inductionloop.getLastStepVehicleNumber(loop)
        return self.ewCount

    def resetVehicleCounts(self):
        self.nsCount = 0
        self.ewCount = 0


    def retreiveTrafficLogicPhases(self, location):
        tree = ET.parse(location)
        root = tree.getroot()
        for logic in root:
            i = 0
            for phase in logic.iter('phase'):
                self.trafficLightLogic[i] = [phase.attrib['duration'], phase.attrib['state']]
                i += 1

    def getTrafficLightLogic(self):
        return self.trafficLightLogic

    def getActivePhase(self):
        return self.activePhase

    def setActivePhase(self, phase):
        self.activePhase = phase

    def getNextActivePhase(self):
        return self.nextActivePhase

    def setNextActivePhase(self, phase):
        self.nextActivePhase = phase

    def getActivePhaseDuration(self):
        return self.activePhaseDuration

    def resetActivePhaseDuration(self):
        self.activePhaseDuration = 0

    def incrementTotalRunningTime(self):
        self.activePhaseDuration += 1

    def determineNextActivePhase(self):
        ns = self.nsCount
        ew = self.ewCount
        if self.getActivePhase() is 0:
            if ns >= ew:
                self.setNextActivePhase(2)
            elif ns < ew:
                if self.getActivePhaseDuration() > 60:
                    self.setNextActivePhase(2)
                    self.resetActivePhaseDuration()
            else:
                self.setNextActivePhase(0)
        elif self.getActivePhase() is 2:
            if ns >= ew:
                self.setNextActivePhase(0)
            elif ns < ew:
                if self.getActivePhaseDuration() > 60:
                    self.setNextActivePhase(0)
            else:
                self.setNextActivePhase(2)
                self.resetActivePhaseDuration()

    def determineNextActivePhaseDuration(self):
        ns = self.nsCount
        ew = self.ewCount
        if self.activePhase != self.nextActivePhase:
            self.nextActivePhaseDuration = 20
        else:
            if self.activePhase is 0 and ew > 0:
                self.nextActivePhaseDuration = self.nextActivePhaseDuration / ew
            elif self.activePhase is 0 and ew == 0:
                self.nextActivePhaseDuration = self.nextActivePhaseDuration
            elif self.activePhase is 2 and ns > 0:
                self.nextActivePhaseDuration = self.nextActivePhaseDuration / ns
            elif self.activePhase is 2 and ns == 0:
                self.nextActivePhaseDuration = self.nextActivePhaseDuration

        if self.nextActivePhaseDuration > 60:
            self.nextActivePhaseDuration = 60

    def changePhase(self):
        self.activePhase = self.nextActivePhase
        self.activePhaseDuration = self.nextActivePhaseDuration
        self.resetVehicleCounts()

    def nextGreenCalculation(self):
        self.nextGreenPhaseCalculation += self.nextActivePhaseDuration
        return self.nextGreenPhaseCalculation




def main():
    dennehys_cross = Atl("354512", "induction_loops/e1.add.xml")
    dennehys_cross.assignJunctionDetectors(2, 1, 2, 1)

if __name__ == "__main__":
    main()
