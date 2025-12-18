"""
QUESTION:
Write a function named `max_difference` that takes an array of numbers as input and returns the maximum difference between any two numbers in the array. The array must have a length of at least 3 and can contain negative numbers and float values.
"""

def max_difference(arr):
    if len(arr) < 3:
        return "Array should have a length of at least 3"
    
    max_diff = arr[1] - arr[0]  # initialize max_diff as difference between first two numbers
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            diff = arr[j] - arr[i]
            if diff > max_diff:
                max_diff = diff
    
    return max_diff