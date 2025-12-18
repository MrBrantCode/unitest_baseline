"""
QUESTION:
Write a function named 'sum_elements' that calculates the sum of all elements in a given list that are greater than 2 and less than 10. The function should return the total sum. The input list may contain any integer values.
"""

def sum_elements(lst):
    """
    This function calculates the sum of all elements in a given list 
    that are greater than 2 and less than 10.
    
    Parameters:
    lst (list): A list of integers.
    
    Returns:
    int: The total sum of the elements in the list that are greater than 2 and less than 10.
    """
    return sum(num for num in lst if 2 < num < 10)