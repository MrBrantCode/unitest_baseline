"""
QUESTION:
Design a function named `calculate_std_dev` to calculate the standard deviation of a set of data. The function should take a list of numbers as input, which may contain duplicates and negative numbers, and return the standard deviation as a number. The function should handle the case where the input list is empty by returning `None`. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the input list.
"""

import math

def calculate_std_dev(data):
    if len(data) == 0:
        return None

    sum_x = 0
    sum_x_squared = 0
    n = len(data)

    for x in data:
        sum_x += x
        sum_x_squared += x ** 2

    mean = sum_x / n
    variance = (sum_x_squared / n) - (mean ** 2)
    std_dev = math.sqrt(variance)

    return std_dev