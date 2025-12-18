"""
QUESTION:
Create a function `calculateCircleArea` that calculates the area of a circle given its radius as an argument, without using the mathematical constant π or any pre-defined function that calculates the value of π. The function should round the calculated area to the nearest integer and return it as the result. The function should be able to handle larger values of radius, up to a maximum of 10^9, and should have a time complexity of O(1), meaning it should execute in constant time regardless of the value of the radius.
"""

def calculateCircleArea(radius):
    MAX_RADIUS = 10 ** 9
    ROUNDING_FACTOR = 0.5
    
    radius_squared = radius * radius
    area = radius_squared * 4
    rounded_area = int(area + ROUNDING_FACTOR)
    
    if rounded_area > MAX_RADIUS * 4:
        return MAX_RADIUS * 4
    else:
        return rounded_area