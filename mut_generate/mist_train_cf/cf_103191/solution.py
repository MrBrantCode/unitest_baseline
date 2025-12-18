"""
QUESTION:
Create a function named `round_number` that takes two parameters: `number` and an optional `decimal_place`. The function should return the rounded value of `number` to the nearest integer if `decimal_place` is not provided, and to the specified decimal place if `decimal_place` is provided.
"""

def round_number(number, decimal_place=None):
    if decimal_place is None:
        return round(number)
    else:
        multiplier = 10 ** decimal_place
        return round(number * multiplier) / multiplier