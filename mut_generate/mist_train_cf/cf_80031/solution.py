"""
QUESTION:
Design a Python class named "Bicycle" with attributes for "color", "wheels", "brand", and "gears". The class should have a method "gear_ratio" that calculates the gear ratio given the number of teeth on the front and rear gears, handling the case where the number of rear teeth is zero to prevent division by zero.
"""

def entrance(front_teeth, rear_teeth):
    if rear_teeth != 0:  # prevent division by zero
        return front_teeth / rear_teeth
    else:
        return 'Error - Division by Zero'