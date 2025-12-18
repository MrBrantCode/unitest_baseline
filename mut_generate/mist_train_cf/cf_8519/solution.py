"""
QUESTION:
Write a Python function called "calculate_sum" that calculates the sum of all elements in a given array using recursion. The function should take the array as input and return the sum. The array should be initialized using a lambda function in combination with list comprehension.
"""

def calculate_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + calculate_sum(arr[1:])