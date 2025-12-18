"""
QUESTION:
Create a function named `find_factors` that accepts an integer `n` and returns a list of its positive factors. If `n` is less than or equal to 0, the function should return an empty list. The function should optimize its calculation by only iterating up to the square root of `n`.
"""

import math

def find_factors(n):
    """
    This function finds all the positive factors of a given integer n.
    
    Args:
        n (int): The input number.
    
    Returns:
        list: A list of positive factors of n. If n is less than or equal to 0, an empty list is returned.
    """
    if n <= 0:
        return []
    factor_list = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n//i == i:  
                factor_list.append(i)
            else:  
                factor_list.append(i)
                factor_list.append(n//i)
    factor_list.append(n)
    return sorted(factor_list)