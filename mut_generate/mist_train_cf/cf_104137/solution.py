"""
QUESTION:
Write a function named `calculate_average` that takes an array of integers as input and returns the average of the array. The function should handle both negative integers and the case where the input array is empty, in which case it should return 0.
"""

def calculate_average(arr):
    if not arr:  # Handle empty array case
        return 0
    
    total = sum(arr)
    average = total / len(arr)
    return average