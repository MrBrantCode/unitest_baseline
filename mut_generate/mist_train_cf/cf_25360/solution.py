"""
QUESTION:
Write a function named `sum_of_odds` that takes an array of integers as input and returns the sum of all odd numbers in the array. The function should not use built-in sum or filtering functions, and it should handle arrays of any length.
"""

def sum_of_odds(arr):
    total = 0
    for num in arr:
        if num % 2 == 1:  # Check if num is odd
            total += num
    return total