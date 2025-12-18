"""
QUESTION:
Implement a function `reverse_string(input_str)` to reverse a given string using a stack data structure. The function should work correctly with alphanumeric characters, special characters, and white spaces. Optimize the solution for time and space complexity.
"""

def reverse_string(input_str):
    """
    This function takes an input string, reverses it using a stack data structure, 
    and returns the reversed string.

    Args:
        input_str (str): The input string to be reversed.

    Returns:
        str: The reversed string.
    """
    stack = list(input_str)
    result = ''
    while len(stack):
        result += stack.pop()
    return result