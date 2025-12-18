"""
QUESTION:
Write a function `find_duplicates` that takes an array of integers as input, finds all duplicates that appear more than twice, and returns them in descending order. The function should only return integers that appear more than twice in the array.
"""

from collections import Counter

def find_duplicates(arr):
    """
    Finds all duplicates in the array that appear more than twice and returns them in descending order.

    Args:
        arr (list): A list of integers.

    Returns:
        list: A list of integers that appear more than twice in the array, sorted in descending order.
    """
    # Count the occurrences of each element in the array
    counter = Counter(arr)
    
    # Find the duplicates that appear more than twice and sort them in descending order
    return sorted([key for key, value in counter.items() if value > 2], reverse=True)