#!/usr/bin/env python3

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


time = 1800


def run_dynamic():
    check_env()
    # store location of sumo-gui (if you want to launch with the gui)
    sumo_binary = "/usr/bin/sumo-gui"
    sumo_cmd = [sumo_binary,"-c", "osm.sumocfg"]
    import traci

    # start simulation, connecting to it using this script

    traci.start(sumo_cmd)
    step = 1

    traci.trafficlight.setProgram("354512", "dynamic")
    traci.trafficlight.setPhase("354512", 0)
    # create smart traffic light for dennehys cross junction
    dennehyscross = Atlc("354512", "induction_loops/e1.add.xml")
    dennehyscross.assignJunctionDetectors(2, 2, 2, 1)
    dennehyscross.retreiveTrafficLogicPhases("tl.add.xml")
    logic = dennehyscross.getTrafficLightLogic()
    print(logic)
    print(dennehyscross.phases)
    print("Active Phase:", dennehyscross.getActivePhase())
    print("Next Active Phase Determination Time:", dennehyscross.getNextGreenPhaseDeterminationTime())

    while step < time:

        # take one step in the simulation
        dennehyscross.setTrafficLights()
        traci.simulationStep()
        dennehyscross.incrementActivePhaseTotalRunningTime()
        # update the vehicle counts for NS and EW directions
        dennehyscross.detectNS()
        dennehyscross.detectEW()

        """ Is it time to determine what the next active phase should be? """
        dennehyscross.checkPhaseDetermination(step)

        """ Is it time to switch to the next phase? """
        dennehyscross.checkPhaseSettingTime(step)

        """ Set the traffic light to the state it is supposed to be """
        dennehyscross.setTrafficLights()

        # increment by 1 step
        step += 1

    # when finished all steps, close traci
    traci.close()


def run_static():

    check_env()
    # store location of sumo-gui (if you want to launch with the gui)
    sumo_binary = "/usr/bin/sumo-gui"
    sumo_cmd = [sumo_binary, "-c", "osm.sumocfg"]
    import traci

    # start simulation, connecting to it using this script

    traci.start(sumo_cmd)
    step = 1

    traci.trafficlight.setProgram("354512", "static")

    while step < time:
        traci.simulationStep()
        step +=1

    traci.close()


def run_actuated():

    check_env()
    # store location of sumo-gui (if you want to launch with the gui)
    sumo_binary = "/usr/bin/sumo-gui"
    sumo_cmd = [sumo_binary, "-c", "osm.sumocfg"]
    import traci

    # start simulation, connecting to it using this script

    traci.start(sumo_cmd)
    step = 1

    traci.trafficlight.setProgram("354512", "actuated")

    while step < time:
        traci.simulationStep()
        step += 1

    traci.close()


def main():

    # run_actuated()
    # run_dynamic()
    run_static()


if __name__ == "__main__":

    main()
