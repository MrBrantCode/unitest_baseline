"""
QUESTION:
Write a function called `find_odd_index` that takes a list of integers as input and returns the index of the first element that appears an odd number of times in the list. The function assumes that there is at least one element appearing an odd number of times in the list.
"""

def find_odd_index(arr):
    """
    Returns the index of the first element that appears an odd number of times in the list.
    
    Parameters:
    arr (list): A list of integers
    
    Returns:
    int: The index of the first element that appears an odd number of times
    """
    counts = {i:arr.count(i) for i in arr}
    for element in counts:
        if counts[element] % 2 != 0:
            return arr.index(element)