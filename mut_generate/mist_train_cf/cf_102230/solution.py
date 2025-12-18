"""
QUESTION:
Write a function `foo(num)` that takes an integer `num` and returns an integer. The function should return `1` if `num` is `0`, and for any other number, it should recursively call itself with a decremented value and add `1` to the result. However, if `num` is even, it should decrement by `2` instead of `1` and add `2` to the result.
"""

def foo(num):
    """
    Recursively calculates a value based on the input number.
    
    If num is 0, returns 1. For odd numbers, recursively calls itself with num - 1 and adds 1 to the result.
    For even numbers, recursively calls itself with num - 2 and adds 2 to the result.
    
    Args:
    num (int): The input number.
    
    Returns:
    int: The calculated value.
    """
    if num == 0:
        return 1
    elif num % 2 == 0:
        return foo(num - 2) + 2
    else:
        return foo(num - 1) + 1