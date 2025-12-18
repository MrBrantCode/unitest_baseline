"""
QUESTION:
Write a function `enhanced_solution` that takes a non-empty list of integers as input and returns the sum of all odd elements at even indices. The list can contain up to 10^6 elements. Optimize the function for performance.
"""

def enhanced_solution(lst):
    return sum(num for i, num in enumerate(lst[::2]) if num % 2 == 1)