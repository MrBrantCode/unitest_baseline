"""
QUESTION:
Create a function called `calculate_wattage` that calculates the wattage of a bulb based on its voltage and amperage. The function should take two parameters: `voltage` and `amperage`, and return the calculated wattage. Assume that the wattage is calculated by multiplying the voltage and amperage. The function should not handle any exceptions or errors.
"""

def calculate_wattage(voltage, amperage):
    wattage = voltage * amperage
    return wattage