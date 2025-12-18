"""
QUESTION:
Write a function `get_product` that calculates the product of elements in a list that satisfy a modulo criterion and/or fall within a given range. The function should handle cases where either criterion is null. The modulo criterion is given as `x % criterion == 1` and the range criterion is a tuple `(n, m)` where `n` and `m` are inclusive. The function should return a suitable message if the range is invalid or no elements satisfy the given criteria.
"""

from functools import reduce

def get_product(lst, criterion=None, num_range=None):
    """
    Calculate the product of elements in a list that satisfy a modulo criterion and/or fall within a given range.

    Args:
        lst (list): The list of numbers.
        criterion (int, optional): The modulo criterion. Defaults to None.
        num_range (tuple, optional): The range criterion. Defaults to None.

    Returns:
        int or str: The product of elements that satisfy the criteria, or an error message if the range is invalid or no elements satisfy the criteria.
    """

    if num_range is not None:
        start, end = num_range
        if start > end:
            return "Invalid range"
        lst = list(filter(lambda x: start <= x <= end, lst))
        
    if criterion is not None:
        lst = list(filter(lambda x: x % criterion == 1, lst))
    
    if not lst:
        return "No elements satisfy the given criteria"
    
    product = reduce(lambda x, y: x * y, lst)
    
    return product