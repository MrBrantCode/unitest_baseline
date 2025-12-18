"""
QUESTION:
Create a function called `calculate_sum` that calculates the sum of every fourth element in a given integer array. The function should take an integer array `arr` as input and return the sum of every fourth element, starting from the fourth element (index 3) of the array.
"""

def calculate_sum(arr):
    return sum(arr[i] for i in range(3, len(arr), 4))