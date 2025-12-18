"""
QUESTION:
Given a list of integers, write a function `find_evens` that determines if the list contains at least one even number. If an even number exists, return `True` and its index; otherwise, return `False` and `None`. The function must handle large lists efficiently, with a maximum of 100,000 elements.
"""

def find_evens(nums):
    for i, num in enumerate(nums):
        if num % 2 == 0:
            return True, i
    return False, None