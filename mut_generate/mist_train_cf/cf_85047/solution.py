"""
QUESTION:
Write a function `rounded_avg_custom_base(n, m, base)` that calculates the sum of an arithmetic series where the first term 'a' is the rounded average of all integers from n to m (inclusive) and the common difference 'd' is 1. The sum of the series up to a certain term is calculated and then converted to a custom number system with the given base. The base should be between 2 and 10 (inclusive). If n is greater than m or the base is out of range, return -1.
"""

def rounded_avg_custom_base(n, m, base):
    """
    This function calculates the sum of an arithmetic series where the first term 'a' 
    is the rounded average of all integers from n to m (inclusive) and the common 
    difference 'd' is 1. The sum of the series up to a certain term is calculated 
    and then converted to a custom number system with the given base.

    Args:
    n (int): The start of the range.
    m (int): The end of the range.
    base (int): The base of the custom number system.

    Returns:
    str: The sum of the series in the custom number system if n <= m and 2 <= base <= 10, -1 otherwise.
    """

    if n > m or base < 2 or base > 10:
        return -1
    avg = round((sum(range(n, m + 1)) / (m - n + 1)))
    total_sum = (m - n + 1) * (2 * n + (m - n)) // 2
    return custom_number_system(total_sum, base)

def custom_number_system(n, base):
    """
    This function converts a number to a custom number system.

    Args:
    n (int): The number to convert.
    base (int): The base of the custom number system.

    Returns:
    str: The number in the custom number system.
    """

    conversion = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < base:
        return conversion[n]
    else:
        return custom_number_system(n // base, base) + conversion[n % base]