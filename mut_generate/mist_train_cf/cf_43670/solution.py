"""
QUESTION:
Create a function `convert_angle` that takes in three parameters: the angle value and two unit parameters `from_unit` and `to_unit`. The function should convert the angle from `from_unit` to `to_unit` and return the converted angle and unit. The available units for conversion are 'gradians', 'degrees', and 'radians'. Ensure proper error handling for invalid inputs, such as non-numeric angle values and unrecognized units.
"""

import math

def convert_angle(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        return 'Error: Invalid input. Angle value should be a number.'
    
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    valid_units = ['gradians', 'degrees', 'radians']
    
    if from_unit not in valid_units or to_unit not in valid_units:
        return 'Error: Invalid unit. Available units: gradians, degrees, radians'

    if from_unit == 'gradians':
        if to_unit == 'degrees':
            return value * (180 / 200), 'degrees'
        elif to_unit == 'radians':
            return value * (math.pi / 200), 'radians'
    elif from_unit == 'degrees':
        if to_unit == 'gradians':
            return value * (200 / 180), 'gradians'
        elif to_unit == 'radians':
            return math.radians(value), 'radians'
    elif from_unit == 'radians':
        if to_unit == 'gradians':
            return value * (200 / math.pi), 'gradians'
        elif to_unit == 'degrees':
            return math.degrees(value), 'degrees'