"""
QUESTION:
Implement the function `calculate_total_resistance(resistances)` that calculates the total resistance of a parallel circuit. The function should take a list of resistance values (`resistances`) as input, where each value is a float representing resistance in ohms. The function should return the total resistance of the parallel circuit as a float. The input list `resistances` will always contain at least one resistance value.
"""

def calculate_total_resistance(resistances):
    total_inverse_resistance = sum(1 / r for r in resistances)
    total_resistance = 1 / total_inverse_resistance
    return total_resistance