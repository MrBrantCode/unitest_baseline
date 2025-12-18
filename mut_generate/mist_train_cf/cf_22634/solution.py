"""
QUESTION:
Create a function named `highest_number` that takes a list of integers as input. The function should return the highest positive number in the list that is greater than 50, ignoring any negative numbers. The list can contain at most 1000 elements. If no such number exists, consider the expected output.
"""

def highest_number(List):
    """
    Returns the highest positive number in the list that is greater than 50.
    
    Args:
        List (list): A list of integers.
    
    Returns:
        int: The highest positive number in the list that is greater than 50. 
             If no such number exists, returns None.
    """
    return max((num for num in List if num > 50), default=None)