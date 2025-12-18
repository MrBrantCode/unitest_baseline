"""
QUESTION:
Create a function `pascal_to_bar` that takes two parameters: pressure in Pascal and decimal precision. The function should convert the pressure from Pascal to Bar (1 Pascal = 1e-5 Bar) and return the result rounded to the specified decimal precision.
"""

def pascal_to_bar(pascal, decimal_precision):
    bar = pascal * 1e-5
    return round(bar, decimal_precision)