"""
QUESTION:
Implement the function `sum_of_unique_elements` that takes a list of integers `arr` as input and returns the sum of all unique elements in the list. The list may contain negative numbers and duplicates, and its length is at most 10^6 with each element's absolute value at most 10^9.
"""

def sum_of_unique_elements(arr):
    """
    This function calculates the sum of all unique elements in the given list.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    int: The sum of all unique elements in the list.
    """
    unique_elements = set()
    for num in arr:
        unique_elements.add(num)
    return sum(unique_elements)