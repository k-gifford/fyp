"""
Class to represent the Adaptive Traffic Light controller
"""

import os, sys
import xml.etree.ElementTree as ET

class Atl:

    def __init__(self, id, traffic_lights, induction_loops_file_location):
        self.id = id
        self.traffic_lights  = traffic_lights
        self.e1_loops = []
        self.retreiveE1LoopIds(induction_loops_file_location)

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




def main():
    dennehys_cross = Atl("354512")
    print(dennehys_cross.getId())

if __name__ == "__main__":
    main()
