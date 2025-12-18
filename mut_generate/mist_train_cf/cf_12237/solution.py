"""
QUESTION:
Write a function called `is_overflow` that takes a list of function calls as input and returns True if the function calls would cause a stack overflow error and False otherwise. Assume that the function calls are represented as a list of strings where each string is a function name and a function can call another function. The list represents the order of function calls. The function `is_overflow` should not actually execute the function calls but instead determine if the calls would exceed the maximum allowed stack size.
"""

def is_overflow(function_calls):
    """
    Determine if a list of function calls would cause a stack overflow error.

    Args:
    function_calls (list): A list of function names representing the order of function calls.

    Returns:
    bool: True if the function calls would cause a stack overflow error, False otherwise.
    """
    max_stack_size = 1000  # Assuming a maximum stack size of 1000
    stack = []

    for func in function_calls:
        if len(stack) >= max_stack_size:
            return True
        stack.append(func)

    return False