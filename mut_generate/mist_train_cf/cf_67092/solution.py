"""
QUESTION:
Write a function `find_top_elements` that takes a list of integers as input and returns a list of tuples, where each tuple contains the index and value of the top 3 highest elements in the list. The function should return the result in descending order of the values. The list indices are 0-based.
"""

def find_top_elements(arr):
    """
    This function takes a list of integers as input and returns a list of tuples.
    Each tuple contains the index and value of the top 3 highest elements in the list.
    The function returns the result in descending order of the values.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    list: A list of tuples containing the index and value of the top 3 highest elements.
    """
    return [(i, arr[i]) for i in sorted(range(len(arr)), key=lambda i: arr[i], reverse=True)[:3]]