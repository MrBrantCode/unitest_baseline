"""
QUESTION:
Write a function `find_max_value` that takes a sorted array of at least 20 integers as input. The function should return the maximum value in the array if it is greater than or equal to 1000, otherwise return a message indicating that no such maximum value exists. The solution should have a time complexity of O(n log n) or better.
"""

def find_max_value(arr):
    """
    This function takes a sorted array of integers as input, finds the maximum value, 
    and checks if it's greater than or equal to 1000. If true, it returns the maximum value; 
    otherwise, it returns a message indicating that no such maximum value exists.

    Args:
        arr (list): A sorted list of integers.

    Returns:
        int or str: The maximum value if it's greater than or equal to 1000, 
                    otherwise a message indicating that no such maximum value exists.
    """
    max_value = max(arr)
    if max_value >= 1000:
        return max_value
    else:
        return "There is no maximum value greater than or equal to 1000"