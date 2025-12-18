"""
QUESTION:
Write a recursive function `increment_value` that takes two parameters, `x` and `end_value`, representing the starting and ending values, respectively. The function should increment `x` by 1 until it reaches `end_value` without using a `goto` statement. The function should also handle potential stack overflow exceptions arising from too many recursive calls.
"""

def increment_value(x, end_value):
    """
    Recursively increments x by 1 until it reaches end_value.

    Args:
        x (int): The starting value.
        end_value (int): The ending value.

    Returns:
        int: The final value after recursive increments.
    """
    if x < end_value:
        return increment_value(x + 1, end_value)
    else:
        return x