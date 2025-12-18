"""
QUESTION:
Create a function named `calculate_bottles_required` that takes in three parameters: `desired_alcohol` (the desired alcohol percentage), `desired_volume` (the desired volume of wine in milliliters), and `bottle_cost` (the cost of a single bottle of wine). The function should calculate and return the total number of bottles required to meet the desired alcohol percentage and the total cost of the bottles. Assume a standard alcohol percentage of 12% and a standard bottle size of 750ml. The function should also round up to the nearest integer to handle decimal numbers of bottles correctly.
"""

import math

def calculate_bottles_required(desired_alcohol, desired_volume, bottle_cost):
    standard_alcohol = 0.12
    standard_volume = 750
    alcohol_required = desired_volume * desired_alcohol
    bottles_required = math.ceil(alcohol_required / (standard_alcohol * standard_volume))
    total_cost = bottles_required * bottle_cost
    return bottles_required, total_cost