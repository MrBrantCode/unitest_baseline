"""
QUESTION:
Create a function `calculate_average` that takes an array of integers as input and returns the average of the array, rounded to the nearest integer. If the input array is empty, the function should return 0.
"""

def calculate_average(array):
    if len(array) == 0:
        return 0
    else:
        return round(sum(array) / len(array))