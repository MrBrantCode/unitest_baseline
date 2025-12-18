"""
QUESTION:
Create a function `calculate_sum` that calculates the sum of the positive elements in a given array of float values and returns the result rounded to two decimal places. The function should exclude any negative values in the array.
"""

def calculate_sum(arr):
    total_sum = 0
    for num in arr:
        if num >= 0:
            total_sum += num
    total_sum = round(total_sum, 2)
    return total_sum