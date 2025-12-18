"""
QUESTION:
Write a function named `find_max_value` that takes an array of integers as input and returns the maximum value in the array without using any built-in array functions or sorting algorithms. The function should iterate through the array to find the maximum value and return it. The input array is guaranteed to have at least one element.
"""

def find_max_value(array):
    max_value = array[0]
    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]
    return max_value