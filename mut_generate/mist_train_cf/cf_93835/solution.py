"""
QUESTION:
Create a function called `reverse_array` that takes a list of integers as input and returns a new list containing the input integers in reverse order, sorted in descending order, without modifying the original list.
"""

def reverse_array(nums):
    """Return a new list containing the input integers in reverse order."""
    return sorted(nums, reverse=True)