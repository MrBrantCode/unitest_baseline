"""
QUESTION:
Create a function named `max_abs_diff` that calculates the maximum absolute difference between any two elements in a given numpy array, excluding elements that are divisible by 3. The function should take a numpy array as input and return the maximum absolute difference.
"""

import numpy as np

def max_abs_diff(arr):
    # Filter out elements that are divisible by 3
    filtered_arr = [num for num in arr if num % 3 != 0]
    
    # Check if the filtered array is not empty
    if not filtered_arr:
        return 0
    
    # Calculate the maximum absolute difference between the maximum and minimum values in the filtered array
    return abs(max(filtered_arr) - min(filtered_arr))