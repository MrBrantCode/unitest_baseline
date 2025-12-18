"""
QUESTION:
Write a function `divide_with_custom_exceptions` that takes a number `num` as input and returns the result of the division of 1 by `num`. If `num` is negative, the function should raise a `NegativeNumberException` with the message "Negative numbers are not allowed." If the result of the division is greater than 100, the function should raise a `ResultTooLargeException` with the message "Result is too large." If `num` is zero, the function should catch the ZeroDivisionError and return -1. The function should handle all exceptions and return -1 in case of any error.
"""

class NegativeNumberException(Exception):
    pass

class ResultTooLargeException(Exception):
    pass

def divide_with_custom_exceptions(num):
    """
    Returns the result of the division of 1 by num.
    
    Args:
    num (float): The number to divide by.
    
    Returns:
    float: The result of the division.
    
    Raises:
    NegativeNumberException: If num is negative.
    ResultTooLargeException: If the result of the division is greater than 100.
    """
    
    if num < 0:
        raise NegativeNumberException("Negative numbers are not allowed.")
    
    try:
        result = 1 / num
        if result > 100:
            raise ResultTooLargeException("Result is too large.")
    except ZeroDivisionError:
        return -1
    else:
        return result