# using a TraCi script to extract information about traffic light states
import os, sys
# import csv
from atlc import Atlc

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
    sumoCmd = [sumoBinary,"-c", "osm.sumocfg"]
    import traci

    # start simulation, connecting to it using this script
    # prepare csv file to be written to
    # trafficLightData = open('trafficLightData.csv', 'w')
    # writer = csv.writer(trafficLightData)

    traci.start(sumoCmd)
    step = 1

    traci.trafficlight.setProgram("354512", "dynamic")
    #traci.trafficlight.setPhase("354512", 2)
    # create smart traffic light for dennehys cross junction
    dennehyscross = Atlc("354512", "induction_loops/e1.add.xml")
    dennehyscross.assignJunctionDetectors(2, 1, 2, 1)
    dennehyscross.retreiveTrafficLogicPhases("tl.add.xml")
    logic = dennehyscross.getTrafficLightLogic()
    print(logic)
    print(dennehyscross.phases)
    print("Active Phase:", dennehyscross.getActivePhase())
    print("Next Active Phase Determination Time:", dennehyscross.getNextGreenPhaseDeterminationTime())
    while step < 1000:

        # take one step in the simulation
        traci.simulationStep()
        dennehyscross.incrementActivePhaseTotalRunningTime()
        # update the vehicle counts for NS and EW directions
        ns = dennehyscross.detectNS()
        ew = dennehyscross.detectEW()
        #print("Active Phase:", dennehyscross.getActivePhase())
        #print("Active Phase Duration:", dennehyscross.getActivePhaseDuration())
        #print("Next Active Phase:", dennehyscross.getNextActivePhase())
        #print("Next Active Phase Duration:", dennehyscross.getNextActivePhaseDuration())
        #print(dennehyscross.determineNextActivePhase())

        """ Is it time to determine what the next active phase should be? """
        if step == dennehyscross.getNextGreenPhaseDeterminationTime() - 1:
            print("+++++++")
            print("Current step:", step)
            print("current phase", dennehyscross.getActivePhase())
            print("determining next active phase", dennehyscross.determineNextActivePhase())
            print("next active phase", dennehyscross.getNextActivePhase())
            print("next phase determination time", dennehyscross.setNextGreenPhaseDeterminationTime(step))


        """ Is it time to set the next phase? """
        if step == dennehyscross.getPhaseSettingTime():




        # increment by 1 step
        step += 1

    # when finished all steps, close traci
    traci.close()

def main():
    run()

if __name__ == "__main__":
    main()
