"""
QUESTION:
Implement a function named 'linear_search' that searches for a target element in an unsorted list of integers and returns the index of the target element if found, or -1 if not found. The function should take a list of integers and a target integer as input.
"""

def linear_search(lst, target):
    for i, num in enumerate(lst):
        if num == target:
            return i
    return -1