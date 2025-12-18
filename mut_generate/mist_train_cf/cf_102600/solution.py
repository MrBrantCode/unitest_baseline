"""
QUESTION:
Write a function `calculate_mean(arr)` that calculates the arithmetic mean of the input array `arr`. The array may contain both positive and negative numbers.
"""

def calculate_mean(arr):
    total = 0
    for num in arr:
        total += num
    mean = total / len(arr)
    return mean