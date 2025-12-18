"""
QUESTION:
Create a function called `calculate_sum` that takes a list of elements as input and returns the sum of all the numeric values in the list. The function should handle cases where the list contains non-numeric values by skipping them. The function should not use the built-in `sum()` function.
"""

def calculate_sum(lst):
    """
    This function calculates the sum of all numeric values in a given list.
    
    It skips non-numeric values and does not use the built-in sum() function.
    
    Parameters:
    lst (list): A list containing various elements.
    
    Returns:
    float: The sum of all numeric values in the list.
    """
    total = 0
    for num in lst:
        if isinstance(num, (int, float)):
            total += num
    return total