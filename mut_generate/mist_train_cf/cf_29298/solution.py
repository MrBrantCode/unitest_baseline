"""
QUESTION:
Implement a function `calculate_average` that takes an array of numbers as input and returns the average value as a floating-point number rounded to two decimal places. If the input array is empty, the function should return 0.00.
"""

def calculate_average(arr):
    if not arr:
        return 0.00
    else:
        average = sum(arr) / len(arr)
        return round(average, 2)