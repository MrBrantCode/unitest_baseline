"""
QUESTION:
Write a function named `standard_deviation` to calculate and return the standard deviation of an array of numbers using recursion. The input is an array of numbers and the output is a single number representing the standard deviation. The function should not use any external libraries such as numpy.
"""

def recursion_sum(arr):
    if len(arr)==1:
        return arr[0]
    else:
        return arr[0] + recursion_sum(arr[1:])

def standard_deviation(arr):
    mean = recursion_sum(arr) / len(arr)
    sum_squared_diff = recursion_sum([(i - mean)**2 for i in arr])
    variance = sum_squared_diff / len(arr)
    std_dev = variance ** 0.5
    return std_dev