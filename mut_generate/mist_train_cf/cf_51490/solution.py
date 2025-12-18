"""
QUESTION:
Create a function `calculate_total` that takes in three arrays `a`, `b`, and `c`, each of length `n`, representing numerical values. Calculate the combined total of one element from each array in the order of `a`, `b`, `c`, and increase the result by 5 units. Return the combined results of all sets in an array, maintaining the original order of values. The solution should prioritize time complexity over space complexity.
"""

def calculate_total(a, b, c):
    return [x + y + z + 5 for x, y, z in zip(a, b, c)]