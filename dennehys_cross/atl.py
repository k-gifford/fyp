"""
Class to represent the Adaptive Traffic Light controller
"""

import os, sys

class Atl:

    def __init__(self, id, traffic_lights):
        self.id = id
        self.traffic_lights  = traffic_lights


    def getId(self):
        return self.id

    def getState(self):
        return self.traffic_lights



def main():
    dennehys_cross = Atl("354512")
    print(dennehys_cross.getId())

if __name__ == "__main__":
    main()
