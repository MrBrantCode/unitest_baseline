"""
QUESTION:
Write a function `foo(num)` that recursively calculates a value based on the input `num`. The function should have a base case that stops the recursion when `num` equals 0 and return 1 in this case. For other values of `num`, the function should make a recursive call with `num - 1` and add 1 to the result.
"""

def foo(num):
    """
    Recursively calculates a value based on the input num.
    
    The function has a base case that stops the recursion when num equals 0 
    and returns 1 in this case. For other values of num, the function makes 
    a recursive call with num - 1 and adds 1 to the result.

    Args:
        num (int): The input number.

    Returns:
        int: The calculated value.
    """
    if num == 0: 
        # base case: stop recursion when num equals 0
        return 1
    elif num < 0:
        # base case: stop recursion when num is less than 0
        return 1
    else:
        # recursive case: make a recursive call with num - 1 and add 1 to the result
        return foo(num - 1) + 1