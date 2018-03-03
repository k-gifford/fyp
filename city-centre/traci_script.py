#!/usr/bin/env python

# using a TraCi script to extract information about traffic light states
import os, sys

# checks if the SUMO_HOME environment vairable is set
def check_env():
    if 'SUMO_HOME' in os.environ:
        tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
        sys.path.append(tools)
    else:
        sys.exit("please declare environment variable 'SUMO_HOME'")

# returns the sumo command to launch sumo
def sumo_cmd():
    # store location of sumo-gui to launch with the gui
    sumo_binary = "/usr/bin/sumo-gui"
    sumo_cmd = [sumo_binary, "-c", "osm.sumocfg"]
    return sumo_cmd


def run():

    check_env()  # check SUMO_HOME environment variable is set
    import traci  # import the traci library

    # start simulation, connecting to it using this script
    s_cmd = sumo_cmd()
    traci.start(s_cmd)
    step = 0

    # get initial traffic light state for traffic intersection 354512
    #tl_state = traci.trafficlight.getRedYellowGreenState("354504")
    #tl_program = traci.trafficlight.getProgram("354504")


    # Running the simulation for 1000 steps
    while step < 1000:

        # stake one step in the simulation
        traci.simulationStep()

        """
        # if the traffic light has changed since the last step then update
        if tl_state != traci.trafficlight.getRedYellowGreenState("354504"):

            # retrieve the current traffic light state of junction
            tl_state = traci.trafficlight.getRedYellowGreenState("354504")

            program = traci.trafficlight.getProgram("354504")
            # print(traci.trafficlight.getProgram("354512"))
            # print(traci.trafficlight.getPhase("354512"))

            if program == 'allred':
                traci.trafficlight.setProgram("354504", "0")
            else:
                traci.trafficlight.setProgram("354504", "0")
        else:
            pass
        """

        #print(traci.inductionloop.getTimeSinceDetection("e1Detector_-138139938#0_0_0"))



        # increment the simulation by 1 step
        step += 1

    # when finished all steps, close traci
    traci.close()

def main():
    run()

if __name__ == "__main__":
    main()
