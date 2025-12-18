"""
QUESTION:
Write a function `find_odd_non_divisor` to find the nth odd integer that does not divide any element in the series 1, 1, 1, 3, 5, 9, 17, 31, 57, 105, 193, 355, 653, 1201, ... defined by T1 = T2 = T3 = 1 and Tn = Tn-1 + Tn-2 + Tn-3.
"""

def find_odd_non_divisor(n):
    """
    This function finds the nth odd integer that does not divide any element 
    in the series defined by T1 = T2 = T3 = 1 and Tn = Tn-1 + Tn-2 + Tn-3.

    Args:
    n (int): The position of the odd integer to be found.

    Returns:
    int: The nth odd integer that does not divide any element in the series.
    """
    return 3 * (2 * n - 1)