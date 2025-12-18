"""
QUESTION:
Write a program that calculates the area or circumference of a circle based on user input. The program should have a function `calculate_area(radius)` that takes a radius as input and returns the area of the circle rounded to two decimal places. Another function `calculate_circumference(radius)` should take a radius as input and return the circumference of the circle rounded to two decimal places. The radius should be validated to be a positive number within the range 0 to 1000 cm. The program should continue to prompt the user for inputs until the user chooses to exit.
"""

import math

def calculate_area(radius):
    return round(math.pi * radius**2, 2)

def calculate_circumference(radius):
    return round(2 * math.pi * radius, 2)