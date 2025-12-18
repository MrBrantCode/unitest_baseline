"""
QUESTION:
Write a function named `computeSum` that takes a non-empty list of integers as input and returns the sum of even numbers located at odd indices in the list.
"""

def computeSum(lst):
    total_sum = 0
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            total_sum += lst[i]
    return total_sum