"""
QUESTION:
Design a function called `filter_out` that takes an array and an integer as input and returns a new array with all instances of the specified integer removed. The function should not modify the original array.
"""

def filter_out(arr, integer):
    return [x for x in arr if x != integer]