"""
QUESTION:
Create a function named `exclude_divisible_by_three` that takes a list of integers as input and returns a comma-separated string containing all numbers from the list that are not divisible by 3.
"""

def exclude_divisible_by_three(lst):
    """
    This function takes a list of integers as input and returns a comma-separated string 
    containing all numbers from the list that are not divisible by 3.
    
    Parameters:
    lst (list): A list of integers.
    
    Returns:
    str: A comma-separated string containing numbers not divisible by 3.
    """
    return ",".join(str(num) for num in lst if num % 3 != 0)