"""
QUESTION:
Create a function `calculate_sum` that takes an array of integers as input and returns the sum of all elements in the array, calculated using a recursive approach with tail recursion optimization. The function should not use any loops and should start calculating the sum from the first element of the array.
"""

def calculate_sum(arr, index=0, total=0):
    if index >= len(arr):
        return total
    else:
        total += arr[index]
        return calculate_sum(arr, index+1, total)