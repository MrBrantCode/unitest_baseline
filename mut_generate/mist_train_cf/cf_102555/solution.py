"""
QUESTION:
Create a function named "filterAndSort" that takes two parameters: an array "arr" and a number "num". The function should filter "arr" to include only numbers greater than "num", then return the filtered array in ascending order. The function should ignore non-numeric elements in "arr" and handle edge cases such as empty arrays, arrays with no numbers, and arrays with negative numbers.
"""

def filter_and_sort(arr, num):
    """
    Filter an array to include only numbers greater than a given number, 
    then return the filtered array in ascending order.
    
    Parameters:
    arr (list): The input array.
    num (int): The number to filter by.
    
    Returns:
    list: The filtered array in ascending order.
    """
    return sorted([x for x in arr if isinstance(x, (int, float)) and x > num])