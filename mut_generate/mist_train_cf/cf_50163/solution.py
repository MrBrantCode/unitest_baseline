"""
QUESTION:
Create a function describing the total journey time of a car in hours as a function of its initial journey distance (d) in miles and break time (b) in hours. The car travels at 60 miles per hour initially, then takes a break of b hours, and resumes at 50 miles per hour. The car has a fuel efficiency of 30 miles per gallon at 60 mph and 35 miles per gallon at 50 mph, with a full tank of 15 gallons. If the car needs to refuel, it takes an additional 10 minutes. Consider the total distance traveled at each speed to be equal. 

Assume that the car will refuel when the total fuel consumption exceeds 15 gallons. The fuel consumption can be calculated as d1/30 + d2/35, where d1 and d2 are the distances traveled at 60 mph and 50 mph respectively. If refueling is needed, the driver will refuel after traveling 420 miles and every 420 miles thereafter, with each refueling taking 10 minutes or 1/6 hours.
"""

import math

def entance(d, b):
    if d <= 420:
        return d/75 + b
    else:
        n = math.floor(d/420)
        return d/75 + b + n/6