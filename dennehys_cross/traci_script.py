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
    sumo_binary = "/usr/bin/sumo-gui"
    sumo_cmd = [sumo_binary,"-c", "osm.sumocfg"]
    import traci

    # start simulation, connecting to it using this script
    # prepare csv file to be written to
    # trafficLightData = open('trafficLightData.csv', 'w')
    # writer = csv.writer(trafficLightData)

    traci.start(sumo_cmd)
    step = 1

    traci.trafficlight.setProgram("354512", "dynamic")
    # traci.trafficlight.setPhase("354512", 2)
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

        """ Is it time to determine what the next active phase should be? """
        if step == dennehyscross.getNextGreenPhaseDeterminationTime() - 1:
            print("######################")
            print("DETERMINING NEXT PHASE")
            dennehyscross.showStatus(step)
            print("----------------------")

            dennehyscross.determineNextActivePhase()
            dennehyscross.determineNextActivePhaseDuration(step)

            if dennehyscross.getActivePhase() == dennehyscross.getNextActivePhase():

                dennehyscross.increaseActivePhaseDuration()
                dennehyscross.setNextGreenPhaseDeterminationTime(step)
                dennehyscross.nextPhaseSettingTime = None
                print("1")
            else:
                dennehyscross.nextPhaseSettingTime = step + 1
                print("2")

            dennehyscross.showStatus(step)
            print()

        if step == dennehyscross.getNextPhaseSettingTime():
            print("@@@@@@@@@@@@@@@@@@@@@@@")
            print("SWITCHING TO NEXT PHASE")
            dennehyscross.showStatus(step)
            print("----------------------")

            if dennehyscross.getActivePhase() == 0:

                print("SWITCHING TO ORANGE PHASE")
                dennehyscross.switchToNextOrangePhase(step)
                dennehyscross.resetActivePhaseTotalRunningTime()
                dennehyscross.setNextGreenPhaseDeterminationTime(step + 5)

            elif dennehyscross.getActivePhase() == 2:

                print("SWITCHING TO ORANGE PHASE")
                dennehyscross.switchToNextOrangePhase(step)
                dennehyscross.resetActivePhaseTotalRunningTime()
                dennehyscross.setNextGreenPhaseDeterminationTime(step + 5)

            else:

                print("SWITCHING TO NEXT GREEN PHASE")
                dennehyscross.switchToNextActivePhase()
                dennehyscross.setNextGreenPhaseDeterminationTime(step - 1)
                dennehyscross.resetActivePhaseTotalRunningTime()
                dennehyscross.nextPhaseSettingTime = None

            dennehyscross.showStatus(step)
            print()

        # increment by 1 step
        step += 1

    # when finished all steps, close traci
    traci.close()


def main():
    run()


if __name__ == "__main__":
    main()
