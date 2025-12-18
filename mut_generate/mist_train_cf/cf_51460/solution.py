"""
QUESTION:
Develop a function called `compute_total_mass` that calculates the cumulative mass in kilograms of grocery items. The function should take a list of dictionaries as input, where each dictionary contains an item's name and its weight, and return the total mass of all items. The weights are represented as floating-point numbers in kilograms.
"""

def compute_total_mass(groceries):
    total_mass = 0
    for grocery in groceries:
        total_mass += grocery["weight"]
    return total_mass