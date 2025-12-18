"""
QUESTION:
Write a recursive function `compute_average(lst)` that calculates the average of a list of numbers without using the `sum()` function. The function should handle empty lists by returning 0 and lists containing NaN (Not a Number) values by returning NaN.
"""

def compute_average(lst):
    """
    This function calculates the average of a list of numbers without using the sum() function.
    It handles empty lists by returning 0 and lists containing NaN (Not a Number) values by returning NaN.

    Args:
        lst (list): A list of numbers.

    Returns:
        float: The average of the list of numbers.
    """

    if len(lst) == 0:
        return 0
    
    if lst[0] == float('nan'):
        return float('nan')
    
    def recursive_average(lst, total, count):
        if len(lst) == 0:
            return total / count
        else:
            return recursive_average(lst[1:], total + lst[0], count + 1)
    
    return recursive_average(lst, 0, 0)