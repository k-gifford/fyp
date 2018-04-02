if step == dennehys_cross.nextGreenPhaseCalculation - 1:

        print("=  =  =  =  =  =  =  =")
        dennehys_cross.determineNextActivePhase()
        dennehys_cross.nextGreenCalculation()
        dennehys_cross.updateTrafficLogicDurations()
        print("NS: ", dennehys_cross.detectNS(), ", EW:", dennehys_cross.detectEW())
        print("Active Phase: ", dennehys_cross.getActivePhase())
        print("Active Phase Duration: ", dennehys_cross.getActivePhaseDuration())
        print("Active Phase Total Green Time: ", dennehys_cross.getcurrentPhaseTotalRunningTime())
        print("Total Running Time: ", dennehys_cross.getTotalRunningTime())
        print("Next Active Phase Duration: ", dennehys_cross.determineNextActivePhaseDuration())
        if dennehys_cross.getNextActivePhase != dennehys_cross.getActivePhase():
            dennehys_cross.resetVehicleCounts()
            dennehys_cross.resetActivePhaseDuration

        print("Next active phase: ", dennehys_cross.changePhase())




        def changePhase(self):
              if self.getActivePhase() != self.getNextActivePhase():
                  self.currentPhaseTotalRunningTime = 0
                  self.resetVehicleCounts()
              self.activePhase = self.nextActivePhase
              self.activePhaseDuration = self.nextActivePhaseDuration
              return self.activePhase

          def getNextGreenPhaseCalculation(self):
              return self.nextGreenPhaseCalculation

          def nextGreenCalculation(self, step):
              self.nextGreenPhaseCalculation = step
              self.nextGreenPhaseCalculation += self.getActivePhaseDuration()
              self.updatePhaseSettingTime(step)
              return self.nextGreenPhaseCalculation

          def updateTrafficLogicDurations(self):
              logic = [self.nextActivePhaseDuration, self.phases[self.nextActivePhase]]
              self.trafficLightLogic[self.nextActivePhase] = logic
              return self.trafficLightLogic

          def updatePhaseSettingTime(self, steps):
              self.phaseSettingTime = steps + self.activePhaseDuration


<trip id="veh1" depart="10.00" departLane="best" from="-35202667#2" to="-35202667#0" type="passenger"/>
    <trip id="veh2" depart="20.00" departLane="best" from="33708057#3" to="35202667#2" type="passenger"/>
    <trip id="veh3" depart="30.00" departLane="best" from="374366365#0" to="-33708057#1" type="passenger"/>
    <trip id="veh4" depart="40.00" departLane="best" from="-374366365#4" to="-33708057#1" type="passenger"/>
    <trip id="veh5" depart="50.00" departLane="best" from="33708057#0" to="138139938#2" type="passenger"/>
    <trip id="veh6" depart="60.00" departLane="best" from="374366365#0" to="-138139938#0" type="passenger"/>
    <trip id="veh7" depart="70.00" departLane="best" from="374366365#0" to="35202667#2" type="passenger"/>
    <trip id="veh8" depart="80.00" departLane="best" from="-35202667#2" to="-33708057#2" type="passenger"/>
    <trip id="veh9" depart="90.00" departLane="best" from="374366365#4" to="-374366365#2" type="passenger"/>
    <trip id="veh10" depart="100.00" departLane="best" from="-138139938#2" to="-33708057#1" type="passenger"/>
    <trip id="veh11" depart="110.00" departLane="best" from="374366365#0" to="33708057#3" type="passenger"/>
    <trip id="veh12" depart="120.00" departLane="best" from="374366365#0" to="35202667#2" type="passenger"/>
    <trip id="veh13" depart="130.00" departLane="best" from="-35202667#2" to="138139938#2" type="passenger"/>
    <trip id="veh14" depart="140.00" departLane="best" from="374366365#0" to="35202667#0" type="passenger"/>
    <trip id="veh15" depart="150.00" departLane="best" from="374366365#0" to="33708057#2" type="passenger"/>
    <trip id="veh16" depart="160.00" departLane="best" from="-35202667#0" to="-374366365#2" type="passenger"/>
    <trip id="veh17" depart="170.00" departLane="best" from="-138139938#2" to="-374366365#2" type="passenger"/>
    <trip id="veh18" depart="180.00" departLane="best" from="33708057#0" to="-374366365#2" type="passenger"/>
    <trip id="veh19" depart="190.00" departLane="best" from="-35202667#2" to="-35202667#0" type="passenger"/>
    <trip id="veh20" depart="200.00" departLane="best" from="-35202667#2" to="462149208" type="passenger"/>
    <trip id="veh21" depart="210.00" departLane="best" from="33708057#0" to="33708057#3" type="passenger"/>
    <trip id="veh22" depart="220.00" departLane="best" from="-33708057#2" to="35202667#2" type="passenger"/>
    <trip id="veh23" depart="230.00" departLane="best" from="-33708057#2" to="-374366365#2" type="passenger"/>
    <trip id="veh24" depart="240.00" departLane="best" from="-462149208" to="35202667#2" type="passenger"/>
    <trip id="veh25" depart="250.00" departLane="best" from="374366365#0" to="35202667#2" type="passenger"/>
    <trip id="veh26" depart="260.00" departLane="best" from="-35202667#0" to="-33708057#1" type="passenger"/>
    <trip id="veh27" depart="270.00" departLane="best" from="-35202667#2" to="-374366365#2" type="passenger"/>
    <trip id="veh28" depart="280.00" departLane="best" from="33708057#0" to="-374366365#3" type="passenger"/>
    <trip id="veh29" depart="290.00" departLane="best" from="374366365#0" to="138139938#2" type="passenger"/>
    <trip id="veh30" depart="300.00" departLane="best" from="-35202667#2" to="-35202667#1" type="passenger"/>
    <trip id="veh31" depart="310.00" departLane="best" from="-462149208" to="-374366365#2" type="passenger"/>
    <trip id="veh32" depart="320.00" departLane="best" from="33708057#0" to="462149208" type="passenger"/>
    <trip id="veh33" depart="330.00" departLane="best" from="-138139938#2" to="-33708057#1" type="passenger"/>
    <trip id="veh34" depart="340.00" departLane="best" from="-138139938#2" to="-374366365#2" type="passenger"/>
    <trip id="veh35" depart="350.00" departLane="best" from="-138139938#0" to="35202667#2" type="passenger"/>


<trip id="veh0" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh36" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh37" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh38" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh39" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh40" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh41" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh42" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh43" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh44" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh45" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh46" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh47" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh48" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh49" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh50" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh1" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh2" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh3" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh4" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh5" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh6" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh7" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh8" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh9" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh10" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh11" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh12" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh13" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh14" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh15" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>
    <trip id="veh16" depart="0.00" departLane="best" from="33708057#0" to="-138139938#2" type="passenger"/>