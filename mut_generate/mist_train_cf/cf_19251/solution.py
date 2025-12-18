"""
QUESTION:
Create a function named `swap_strings` that takes two string parameters and returns the swapped contents of the two parameters. The function should not use a temporary variable, any built-in swapping functions, or any arithmetic operations.
"""

def swap_strings(a, b):
    """
    Swaps the contents of two strings without using a temporary variable, 
    built-in swapping functions, or any arithmetic operations.

    Args:
        a (str): The first string.
        b (str): The second string.

    Returns:
        tuple: A tuple containing the swapped strings.
    """
    a = a + b
    b = a[:len(a) - len(b)]
    a = a[len(b):]
    return a, b