"""
QUESTION:
Write a function named `aggregate_odd_int(n)` that calculates and returns the sum of all odd integers from 1 to `n` (inclusive), where `n` is a given integer, using a for loop and conditional statements.
"""

def aggregate_odd_int(n):
    aggregate_value = 0
    for num in range(1, n + 1):
        # Check if the number is odd
        if num % 2 != 0:
            # If it's odd, add to the aggregate_value
            aggregate_value += num
    return aggregate_value