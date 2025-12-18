"""
QUESTION:
Write a Python function `is_sorted` that checks if a given list of numbers is sorted in ascending order. The function should return `True` if the list is sorted and `False` otherwise.
"""

def is_sorted(numbers):
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))