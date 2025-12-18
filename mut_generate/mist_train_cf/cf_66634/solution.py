"""
QUESTION:
Write a function `solution` that calculates the sum of all odd elements at even indices in a given non-empty list of integers. The function should operate efficiently for large inputs (up to 10^6 elements) and should have a time complexity better than O(n) and space complexity of O(1) if possible.
"""

def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions."""
    return sum(value for index, value in enumerate(lst) if index % 2 == 0 and value % 2 != 0)