"""
QUESTION:
Create a function `adjustToFourDecimalPlaces` that takes an array of numerical values as input and returns the same array with each value converted to a 4-decimal place number. The function should follow standard floating point notation and be optimized for time and space complexity. The function should handle potential exceptions and return the error message. The input array contains numerical values that need to be rounded to 4 decimal places.
"""

def adjustToFourDecimalPlaces(arr):
    try:
        return [round(elem, 4) for elem in arr]
    except Exception as e:
        print(e)