#!/usr/bin/env python

# using a TraCi script to extract information about traffic light states
import os, sys
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np


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

    cfp_1 = [0]
    cfp_2 = [0]
    cfp_3 = [0]
    cfp_4 = [0]
    cfp_5 = [0]
    cfps = [cfp_1, cfp_2, cfp_3, cfp_4, cfp_5]
    cfp_pointer = 0

    # Running the simulation for 1000 steps
    while step < 92:

        # stake one step in the simulation
        traci.simulationStep()

        """
        start accumulating counts of vehicles flowing over this e1Detector
        """
        cfp_1[cfp_pointer] = cfp_1[cfp_pointer] + traci.inductionloop.getLastStepVehicleNumber("e1Detector_73552050#2_0_79")
        cfp_2[cfp_pointer] = cfp_2[cfp_pointer] + traci.inductionloop.getLastStepVehicleNumber("e1Detector_73552050#2_1_80")
        cfp_3[cfp_pointer] = cfp_3[cfp_pointer] + traci.inductionloop.getLastStepVehicleNumber("e1det_61188951_0")
        cfp_4[cfp_pointer] = cfp_4[cfp_pointer] + traci.inductionloop.getLastStepVehicleNumber("e1det_61188951_1")
        cfp_5[cfp_pointer] = cfp_5[cfp_pointer] + traci.inductionloop.getLastStepVehicleNumber("e1det_-40950946#0_0")


        # print(traci.inductionloop.getLastStepVehicleNumber("e1Detector_73552050#2_0_79"))

        if step % 4 is 0:
            # next position in the cfp
            cfp_pointer += 1
            for c in cfps:
                c.append(0)

        # increment the simulation by 1 step
        step += 1
    # END WHILE
    """
    trace = go.Bar(
    x = list(range(int(step/4))),
    y = cfp_e1
    )
    data = [trace]
    py.iplot(data)
    """



    # when finished all steps, close traci
    traci.close()

def main():
    run()

if __name__ == "__main__":
    main()
