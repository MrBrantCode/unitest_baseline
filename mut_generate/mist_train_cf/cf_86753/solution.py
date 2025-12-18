"""
QUESTION:
Write a function named `calculate_average` that takes an array of integers as input and returns the average of the integers in the array. The function should handle arrays containing negative integers and return 0 if the array is empty. The function must be able to handle arrays with up to 10^6 elements.
"""

def calculate_average(arr):
    if len(arr) == 0:  
        return 0

    total = 0
    for num in arr:
        total += num

    average = total / len(arr)
    return average