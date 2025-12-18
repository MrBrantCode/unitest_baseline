"""
QUESTION:
Write a function `classify_number(x)` that classifies a given integer `x` based on its value. The function should print "x is a single-digit positive number" if `x` is between 0 and 10 (exclusive), "x is a double-digit positive number" if `x` is between 10 and 100 (exclusive), "x is a triple-digit positive number" if `x` is between 100 and 1000 (exclusive), "x is a negative number" if `x` is less than 0, and "x is a positive number with more than three digits" if `x` is 1000 or more.
"""

def classify_number(x):
    """
    Classify a given integer based on its value.

    Args:
        x (int): The integer to be classified.

    Returns:
        str: A string describing the classification of the integer.
    """
    if x < 0:
        return "x is a negative number"
    elif x < 10:
        return "x is a single-digit positive number"
    elif x < 100:
        return "x is a double-digit positive number"
    elif x < 1000:
        return "x is a triple-digit positive number"
    else:
        return "x is a positive number with more than three digits"