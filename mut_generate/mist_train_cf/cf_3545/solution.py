"""
QUESTION:
Implement a function called `swap` that takes two parameters `x` and `y`, and swaps their values without using a temporary variable. The function should work for variables of any data type, have a time complexity of O(1), and not use any built-in swap functions or methods. The function should return the modified values of `x` and `y`.
"""

def swap(x, y):
    """
    Swaps the values of x and y without using a temporary variable.

    Args:
        x: The first value to be swapped.
        y: The second value to be swapped.

    Returns:
        A tuple containing the modified values of x and y.
    """
    # XOR the values of x and y and store the result in x
    x = x ^ y

    # XOR the result in x with y and store the result in y
    y = x ^ y

    # XOR the result in y with x and store the result in x
    x = x ^ y

    # return the modified values of x and y
    return x, y