"""
QUESTION:
Write a function `check_option` that takes two arguments, `low` and `high`, representing the lower and upper bounds of a range, and an `options` dictionary where the keys are the option letters and the values are the corresponding numbers. The function should return the key(s) of the option(s) that fall within the specified range.
"""

def check_option(low, high, options):
    """
    Returns the key(s) of the option(s) that fall within the specified range.

    Args:
    low (int): The lower bound of the range.
    high (int): The upper bound of the range.
    options (dict): A dictionary where the keys are the option letters and the values are the corresponding numbers.

    Returns:
    list: A list of keys of the options that fall within the specified range.
    """
    return [key for key, value in options.items() if low <= value <= high]