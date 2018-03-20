# using a TraCi script to extract information about traffic light states
import os, sys
# import csv
from atl import Atl

def check_env():
    # check if the SUMO_HOME environment vairable is set
    if 'SUMO_HOME' in os.environ:
        tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
        sys.path.append(tools)
    else:
        sys.exit("please declare environment variable 'SUMO_HOME'")



def run():
    check_env()
    # store location of sumo-gui (if you want to launch with the gui)
    sumoBinary = "/usr/bin/sumo-gui"
    sumoCmd = [sumoBinary, "--start" ,"-c", "osm.sumocfg"]
    import traci

    # start simulation, connecting to it using this script
    # prepare csv file to be written to
    # trafficLightData = open('trafficLightData.csv', 'w')
    # writer = csv.writer(trafficLightData)

    traci.start(sumoCmd)
    step = 0

    traci.trafficlight.setProgram("354512", "dynamic")

    # create smart traffic light for dennehys cross junction
    dennehys_cross = Atl("354512", "induction_loops/e1.add.xml")
    dennehys_cross.assignJunctionDetectors(2, 1, 2, 1)
    dennehys_cross.retreiveTrafficLogicPhases("tl.add.xml")
    logic = dennehys_cross.getTrafficLightLogic()
    print(logic)


    while step < 1000:

        # take one step in the simulation
        traci.simulationStep()
        # update the vehicle counts for NS and EW directions
        dennehys_cross.detectNS()
        dennehys_cross.detectEW()
        # incremement the total time this phase has been running

        # determine the next active phase
        if step == dennehys_cross.nextGreenPhaseCalculation - 1:
            dennehys_cross.determineNextActivePhase()
            dennehys_cross.determineNextActivePhaseDuration()
            dennehys_cross.nextGreenCalculation()
            print(dennehys_cross.getNextActivePhase())

            if dennehys_cross.getNextActivePhase != dennehys_cross.getActivePhase():
                dennehys_cross.resetVehicleCounts()
                dennehys_cross.resetActivePhaseDuration

            dennehys_cross.changePhase()

        # increment by 1 step
        step += 1

    # when finished all steps, close traci
    traci.close()

def main():
    run()

if __name__ == "__main__":
    main()
