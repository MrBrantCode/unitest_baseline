"""
QUESTION:
Write a function named `calculate_mean` that takes an array of integers as input and returns the arithmetic mean of the array, which can contain both positive and negative numbers. The function should handle arrays of any length and calculate the mean by summing up all numbers and dividing by the number of elements.
"""

def calculate_mean(arr):
    total = 0
    for num in arr:
        total += num
    mean = total / len(arr)
    return mean