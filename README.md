# Final Year Project: Traffic Flow Optimization in an Urban Environment

As cities grow in size and population it is becoming increasingly important to employ
intelligent traffic management practices. According to the 2017 INTIX Global Traffic report
(based on 2016 data) Cork is third most congested city in Ireland with drivers spend on average
24.5 hours stuck in traffic every year, wasting fuel, increasing emissions and impacting on
driver’s transport experience.

This project investigates the impact that different traffic light control algorithms (static, actuated
and adaptive) have on the flow of traffic in an urban environment. A busy junction within Cork
City has been examined via simulation utilising SUMO (Simulation of Urban Mobility), a
microscopic traffic simulator to model the environment, implement the algorithms and carry out
the analysis. Several performance measures such as average vehicle journey time and average
vehicle waiting time are considered using the same flows of traffic over a given time period.

# Milestones Met

Implemented the intelligent traffic light algorithm in Python, as described in this paper: http://bit.ly/2DDMs59.

Exported the traffic light phase states for the static, actuated and dynamic traffic light control algorithms and plotting them using plotly.

Extracted:
  - average vehicle waiting times and graphing the results.
  - average vehicle trip durations and graphing the results.
  - each vehicle considered waiting for every second in a 30 minute period and graphed the result for all three algorithms.

# Currently

Testing multiple hypotheses and recording their effects on the average waiting times, average journey times, etc.

