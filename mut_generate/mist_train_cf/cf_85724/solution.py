"""
QUESTION:
Calculate the number of whole bottles of soda, juice, and water needed for a party, given the number of guests, where each guest requires 1 liter of beverage. The beverages come in different bottle sizes (soda: 2 liters, juice: 1 liter, water: 1.5 liters) and must be in the ratio of 5:4:1 (soda:juice:water). The function should round up to the nearest whole number if the calculation results in a fraction.
"""

import math

def entrance(guests):
    total_liters = guests
    liters_soda = total_liters * 5 / 10
    liters_juice = total_liters * 4 / 10
    liters_water = total_liters * 1 / 10

    bottles_soda = math.ceil(liters_soda / 2) 
    bottles_juice = math.ceil(liters_juice / 1) 
    bottles_water = math.ceil(liters_water / 1.5) 
    
    return bottles_soda, bottles_juice, bottles_water