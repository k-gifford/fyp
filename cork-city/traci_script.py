# using a TraCi script to extract information about traffic light states
import os, sys
# import csv

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
    sumoCmd = [sumoBinary, "-c", "osm.sumocfg"]
    import traci

    # start simulation, connecting to it using this script
    # prepare csv file to be written to
    # trafficLightData = open('trafficLightData.csv', 'w')
    # writer = csv.writer(trafficLightData)

    traci.start(sumoCmd)
    step = 0

    #get initial traffic light state for traffic intersection 354512
    tl_state = traci.trafficlight.getRedYellowGreenState("354504")
    tl_program = traci.trafficlight.getProgram("354504")


    # Running the simulation for 1000 steps
    while step < 1000:

        # stake one step in the simulation
        traci.simulationStep()

        # if the traffic light has changed since the last step then update
        if tl_state != traci.trafficlight.getRedYellowGreenState("354504"):

            tl_state = traci.trafficlight.getRedYellowGreenState("354504")
            # writer.writerows(tl_state)
            # print(tl_state)
            # print(traci.trafficlight.getCompleteRedYellowGreenDefinition("354512"))
            program = traci.trafficlight.getProgram("354504")
            # print(traci.trafficlight.getProgram("354512"))
            # print(traci.trafficlight.getPhase("354512"))

            if program == 'allred':
                traci.trafficlight.setProgram("354504", "0")
            else:
                traci.trafficlight.setProgram("354504", "0")
        else:
            pass

        # increment the simulation by 1 step
        step += 1

    # when finished all steps, close traci

    traci.close()

def main():
    run()

if __name__ == "__main__":
    main()
