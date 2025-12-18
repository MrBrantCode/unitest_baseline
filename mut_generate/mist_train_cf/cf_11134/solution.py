"""
QUESTION:
Define a function `data_type_returned` that takes a single argument `value` and returns the data type of the result when `value` is raised to the power of 8 and then multiplied by 5. The function should be able to handle different data types of input.
"""

def data_type_returned(value):
    """
    Returns the data type of the result when 'value' is raised to the power of 8 and then multiplied by 5.

    Args:
        value: The input value to be processed.

    Returns:
        type: The data type of the result.
    """
    result = value ** 8 * 5
    return type(result)