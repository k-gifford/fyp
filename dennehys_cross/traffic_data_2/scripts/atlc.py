import os
import sys
tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
sys.path.append(tools)
import traci
import xml.etree.ElementTree as ET


class Atlc:

    def __init__(self, id, induction_loops_file_location):
        self.id = id
        self.trafficLightLogic = dict()
        self.phases = []
        self.e1_loops = []
        self.retreiveE1LoopIds(induction_loops_file_location)
        self.nsCount = 0
        self.ewCount = 0
        self.nsLoops = []
        self.ewLoops = []

        self.activePhase = 2  # simulation will start with EW direction green
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
    def assign_junction_detectors(self, north, east, south, west):
        lane = 0
        for loop in self.e1_loops:
            if lane < north:
                self.nsLoops.append(loop)

            elif lane < (north + east):
                self.ewLoops.append(loop)

            elif lane < (north + east + south):
                self.nsLoops.append(loop)

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

    def reset_ns_vehicle_counts(self):
        self.nsCount = 0

    def reset_ew_vehicle_counts(self):
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

    def increaseActivePhaseDuration(self):
        self.activePhaseDuration +=  self.nextActivePhaseDuration

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
                self.reset_ns_vehicle_counts()
            elif ns < ew:
                if self.getActivePhaseTotalRunningTime() >= 60:
                    self.setNextActivePhase(2)
                    self.reset_ns_vehicle_counts()
                else:
                    self.setNextActivePhase(0)
                    self.reset_ew_vehicle_counts()

        elif self.getActivePhase() is 2:  # if the phase is currently NS
            if ew >= ns:
                self.setNextActivePhase(0)
                self.reset_ew_vehicle_counts()
            elif ew < ns:
                if self.getActivePhaseTotalRunningTime() >= 60:
                    self.setNextActivePhase(0)
                    self.reset_ew_vehicle_counts()
                else:
                    self.setNextActivePhase(2)
                    self.reset_ns_vehicle_counts()

    """ Determing how long the next active phase should run for.
    Again, only called at a specific timestep interval """
    def determineNextActivePhaseDuration(self):
        ns = self.nsCount
        ew = self.ewCount
        default_duration = 20

        if self.activePhase != self.nextActivePhase:  # if the phases are different
            self.nextActivePhaseDuration = default_duration

        else:

            if self.activePhase is 0 and ew > 0:  # if the active phase is EW
                self.nextActivePhaseDuration = round(default_duration / ew, 0)

            elif self.activePhase is 0 and ew == 0:
                self.nextActivePhaseDuration = default_duration

            elif self.activePhase is 2 and ns > 0:  # if the active phase is NS
                self.nextActivePhaseDuration = round(default_duration / ns, 0)

            elif self.activePhase is 2 and ns == 0:
                self.nextActivePhaseDuration = default_duration


    def checkIfForceNeeded(self, steps):
        # checking if we need to force a phase change
        # if the total running time so far plus the next phase duration is > 60
        if self.getActivePhaseTotalRunningTime() + self.getNextActivePhaseDuration() >= 60:

            # then limit the phase to 60 seconds
            self.nextActivePhaseDuration = 60 - self.getActivePhaseTotalRunningTime()

            if self.getNextActivePhaseDuration() == 0:

                self.nextPhaseSettingTime = steps
                self.setNextActivePhaseDuration(20)

                if self.getActivePhase() == 0:
                    self.setNextActivePhase(2)
                    print("FORCING A PHASE CHANGE")

                elif self.getActivePhase() == 2:
                    self.setNextActivePhase(0)
                    print("FORCING A PHASE CHANGE")



        return self.nextActivePhaseDuration

    """ Next green phase determination calculator """
    def setNextGreenPhaseDeterminationTime(self, steps):

        # if the green phases are going to change
        if self.getActivePhase() != self.getNextActivePhase():

            # 20 as default
            # plus 5 because of the orange phase switch
            self.nextGreenPhaseDeterminationTime = steps + 20 + 5

        # if the phase was forced to switch
        elif self.getActivePhase() == self.getNextActivePhase() and self.getActivePhaseTotalRunningTime() >= 60:

            # 20 as default
            # plus 5 because of the orange phase switch
            self.nextGreenPhaseDeterminationTime = steps + 20 + 5

        # otherwise if the phase is staying the same then just add on the extra time
        else:

            self.nextGreenPhaseDeterminationTime += self.getNextActivePhaseDuration()

        return self.nextGreenPhaseDeterminationTime

    def getNextGreenPhaseDeterminationTime(self):

        return self.nextGreenPhaseDeterminationTime

    """ Next green phase setting time """
    def getNextPhaseSettingTime(self):

        return self.nextPhaseSettingTime

    def setNextPhaseSettingTime(self, steps):

        self.nextPhaseSettingTime = steps + self.getNextActivePhaseDuration()

        if self.activePhase == 1 or self.activePhase == 3:
            self.nextPhaseSettingTime = steps + self.activePhaseDuration

    """ Change the phase to the next phase """
    def switchToNextActivePhase(self):

        self.activePhase = self.nextActivePhase
        self.setActivePhaseDuration(self.nextActivePhaseDuration)



    """" Switch to the orange phase """
    def switchToNextOrangePhase(self):

        if self.activePhase == 0:
            self.activePhase = 1
        else:
            self.activePhase = 3

        self.setActivePhaseDuration(5)

    """ set traffic lights """
    def setTrafficLights(self):
        state = self.phases[self.getActivePhase()]
        traci.trafficlight.setRedYellowGreenState(self.id, state)


    def checkPhaseDetermination(self, step):

        if step == self.getNextGreenPhaseDeterminationTime() - 1:
            print("######################")
            print("DETERMINING NEXT PHASE")
            self.showStatus(step)
            print("----------------------")

            self.determineNextActivePhase()
            self.determineNextActivePhaseDuration()
            self.checkIfForceNeeded(step)

            if self.getActivePhase() == self.getNextActivePhase():

                self.increaseActivePhaseDuration()
                self.setNextGreenPhaseDeterminationTime(step)
                self.nextPhaseSettingTime = None
                print("1")
            else:
                self.nextPhaseSettingTime = step + 1
                print("2")
            self.showStatus(step)
            print()

    def checkPhaseSettingTime(self, step):
        if step == self.getNextPhaseSettingTime():
            print("@@@@@@@@@@@@@@@@@@@@@@@")
            print("SWITCHING TO NEXT PHASE")
            self.showStatus(step)
            print("----------------------")

            if self.getActivePhase() == 0:

                print("SWITCHING TO ORANGE PHASE")
                self.switchToNextOrangePhase()
                self.resetActivePhaseTotalRunningTime()
                self.setNextGreenPhaseDeterminationTime(step)  #
                self.setNextPhaseSettingTime(step)

            elif self.getActivePhase() == 2:

                print("SWITCHING TO ORANGE PHASE")
                self.switchToNextOrangePhase()
                self.resetActivePhaseTotalRunningTime()
                self.setNextGreenPhaseDeterminationTime(step)
                self.setNextPhaseSettingTime(step)

            else:

                print("SWITCHING TO NEXT GREEN PHASE")
                self.switchToNextActivePhase()
                self.resetActivePhaseTotalRunningTime()
                self.nextPhaseSettingTime = None


            self.showStatus(step)
            print()

    def showStatus(self, step):

        print("Current Step:", step)
        print("Current Phase:", self.getActivePhase())
        print("Current Phase Duration:", self.getActivePhaseDuration())
        print("Current Phase Total Running Time:", self.getActivePhaseTotalRunningTime())
        print("Next Phase:", self.getNextActivePhase())
        print("Next Phase Duration:", self.getNextActivePhaseDuration())
        print("Next Green Phase Determination At:", self.getNextGreenPhaseDeterminationTime())
        print("Next Phase Setting Time At:", self.getNextPhaseSettingTime())







    #
