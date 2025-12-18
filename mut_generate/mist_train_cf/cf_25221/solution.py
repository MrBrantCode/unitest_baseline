"""
QUESTION:
Write a function that demonstrates the use of higher-order functions in the functional programming paradigm. This function should take another function as an argument and apply it to a given input. The function should not use mutable data or state.
"""

def apply_function(func, input_value):
    """
    Applies a given function to an input value.

    Args:
        func (function): The function to apply.
        input_value: The input value to apply the function to.

    Returns:
        The result of applying the function to the input value.
    """
    return func(input_value)