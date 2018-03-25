import os, sys
tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
sys.path.append(tools)
import traci
import xml.etree.ElementTree as ET


class Atlc:


    def __init__(self, id, induction_loops_file_location):
        self.id = id
        self.trafficLightLogic  = dict()
        self.phases = []
        self.e1_loops = []
        self.retreiveE1LoopIds(induction_loops_file_location)
        self.nsCount = 0
        self.ewCount = 0
        self.nsLoops = []
        self.ewLoops = []

        self.activePhase = 0  # simulation will start with EW direction green
        self.activePhaseDuration = 30  # initial active phase runs for 30 seconds
        self.activePhaseTotalRunningTime = 0

        self.nextActivePhase = 0
        self.nextActivePhaseDuration = 20
        self.nextPhaseSettingTime = 30
        self.nextGreenPhaseDeterminationTime = 30

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
                self.phases.append(phase.attrib['state'])
                i += 1


    def getTrafficLightLogic(self):
        return self.trafficLightLogic

    def getPhases(self):
        return self.phases

    """ Active Phase Methods """
    def getActivePhase(self):
        return self.activePhase

    def setActivePhase(self, phase):
        self.activePhase = phase

    def getActivePhaseDuration(self):
        return self.activePhaseDuration

    def setActivePhaseDuration(self, duration):
        self.activePhaseDuration = duration

    def getActivePhaseTotalRunningTime(self):
        return self.activePhaseTotalRunningTime

    def incrementActivePhaseTotalRunningTime(self):
        self.activePhaseTotalRunningTime += 1

    def resetActivePhaseTotalRunningTime(self):
        self.activePhaseTotalRunningTime = 0

    """ Next Active Phase Methods """
    def getNextActivePhase(self):
        return self.nextActivePhase

    def setNextActivePhase(self, phase):
        self.nextActivePhase = phase

    def getNextActivePhaseDuration(self):
        return self.nextActivePhaseDuration

    def setNextActivePhaseDuration(self, duration):
        self.nextActivePhaseDuration = duration

    """ Determine what the next active phase should be. This method is
    only called at a specific timestep interval """
    def determineNextActivePhase(self):
        ns = self.nsCount
        ew = self.ewCount
        if self.getActivePhase() is 0:  # if the phase is currently EW
            if ns >= ew:
                self.setNextActivePhase(2)
            elif ns < ew:
                if self.getActivePhaseTotalRunningTime() > 60:
                    self.setNextActivePhase(2)
                else:
                    self.setNextActivePhase(0)

        elif self.getActivePhase() is 2:  # if the phase is currently NS
            if ew >= ns:
                self.setNextActivePhase(0)
            elif ew < ns:
                if self.getActivePhaseTotalRunningTime() > 60:
                    self.setNextActivePhase(0)
                else:
                    self.setNextActivePhase(2)

        return self.nextActivePhase

    """ Determing how long the next active phase should run for.
    Again, only called at a specific timestep interval """
    def determineNextActivePhaseDuration(self, steps):
        ns = self.nsCount
        ew = self.ewCount
        defaultDuration = 20

        if self.activePhase != self.nextActivePhase:  # if the phases are different
            self.nextActivePhaseDuration = 20
        else:
            if self.activePhase is 0 and ew > 0:
                self.nextActivePhaseDuration = round(defaultDuration / ew, 0)
                self.updatePhaseDeterminationTime(steps)
            elif self.activePhase is 2 and ns > 0:
                self.nextActivePhaseDuration = round(defaultDuration / ns, 0)
                self.updatePhaseDeterminationTime(steps)

        # if the total running time so far plus the next phase duration is > 60
        if self.getActivePhaseTotalRunningTime() + self.getActivePhaseDuration() > 60:
            # then limit the phase to 60 seconds
            temp = self.getActivePhaseTotalRunningTime()
            time = 60 - temp
            self.nextActivePhaseDuration = time

        self.resetVehicleCounts() # now reset the vehicle counts
        return self.nextActivePhaseDuration


    """ Next green phase determination calculator """
    def setNextGreenPhaseDeterminationTime(self, steps):
        # if the green phases are going to change
        if self.getActivePhase() != self.getNextActivePhase:
            # 20 as default, plus 1 because of the nature of the checking of the time being at -1 step
            self.nextGreenPhaseDeterminationTime = steps + 21
        # otherwise if the phase is staying the same then just add on the extra time
        else:
            # plus 1 due to same reason as above
            self.nextGreenPhaseDeterminationTime += self.getNextActivePhaseDuration() + 1
        return self.nextGreenPhaseDeterminationTime

    def getNextGreenPhaseDeterminationTime(self):
        return self.nextGreenPhaseDeterminationTime

    """ Next green phase setting time """
    def getNextPhaseSettingTime(self):
        return self.nextPhaseSettingTime

    def setNextPhaseSettingTime(self, steps):
        self.nextPhaseSettingTime = steps + self.getNextActivePhaseDuration()
        

    """ Change the phase to the next phase """













    #
