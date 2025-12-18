"""
QUESTION:
Write a function `greater_and_indices` that takes a list of integers and a target integer as arguments. The function should return a list of tuples, where each tuple contains the index and value of an element in the original list that is greater than the target. The function should have a time complexity of O(n), where n is the number of elements in the input list, to handle large input lists efficiently.
"""

def greater_and_indices(lst, target):
    """Return a list of tuples containing the index and value of elements in the input list that are greater than the target."""
    return [(index, elem) for index, elem in enumerate(lst) if elem > target]