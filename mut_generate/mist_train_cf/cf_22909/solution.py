"""
QUESTION:
Design a function named `calculate_std_dev` that takes a list of numbers as input and returns the standard deviation of the data set. The input list may contain up to 10^6 elements, including duplicates and negative numbers. If the input list is empty, the function should return None. The function should have a time complexity of O(n) and a space complexity of O(1).
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