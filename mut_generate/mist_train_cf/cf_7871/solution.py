"""
QUESTION:
Write a function `second_highest_odd` that takes a list of integers as input and returns the second highest odd number. If the list contains no odd numbers, or if all odd numbers in the list are duplicates, the function should return -1. The function should handle both positive and negative numbers, returning the second highest negative odd number if available, otherwise the second highest positive odd number.
"""

def second_highest_odd(lst):
    odds = [num for num in lst if num % 2 != 0]
    if len(odds) < 2 or len(set(odds)) < 2:
        return -1
    return sorted(set(odds), reverse=True)[1]