"""
QUESTION:
Create a function named `unit_conversion` that takes two parameters: `value` and `unit`. The function should convert the given `value` from the specified `unit` to the other unit. The conversion factors are 2.54 for inches to centimeters and 1/2.54 for centimeters to inches. If the `unit` is 'inches', the function should return the converted value in centimeters. If the `unit` is 'cm', the function should return the converted value in inches. If the `unit` is neither 'inches' nor 'cm', the function should return the error message 'Unknown unit: please provide 'inches' or 'cm''.
"""

def unit_conversion(value, unit):
    if unit == 'inches':
        return value * 2.54  
    elif unit == 'cm':
        return value / 2.54  
    else:
        return 'Unknown unit: please provide \'inches\' or \'cm\''