"""
QUESTION:
Create a function called `segregate_nums` that takes a list of decimal fractions as input and returns three separate lists: one for positive numbers, one for zeros, and one for negative numbers. The function should accurately classify the fractional decimal digits without any errors.
"""

def segregate_nums(lst):
    """
    This function segregates a list of decimal fractions into three lists: 
    one for positive numbers, one for zeros, and one for negative numbers.

    Args:
    lst (list): A list of decimal fractions.

    Returns:
    tuple: Three lists for positive, zero, and negative numbers respectively.
    """
    positive = [num for num in lst if num > 0]
    zero = [num for num in lst if num == 0]
    negative = [num for num in lst if num < 0]

    return positive, zero, negative