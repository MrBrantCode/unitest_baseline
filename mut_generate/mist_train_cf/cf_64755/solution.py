"""
QUESTION:
Implement a function `sum_of_squared_deviations(array)` that calculates the sum of squared deviations between each integer in the array and the arithmetic mean of the entire array, without using direct loop iteration over the array or advanced statistical libraries or functions for variance calculation.
"""

def sum_of_squared_deviations(array):
    n = len(array)
    sum1 = sum(array)
    sum2 = sum(x**2 for x in array)

    mean = sum1 / n
    return sum2 - n * (mean ** 2)