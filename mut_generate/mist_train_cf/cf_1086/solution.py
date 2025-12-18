"""
QUESTION:
Create a function `calculate_list_sum` that takes a list of numbers as input and returns the sum of all the numbers in the list. The function should not use the built-in sum() function. The list may contain non-numeric values, including strings and nested lists, which should be skipped in the sum calculation. If a nested list contains numeric values, these values should be included in the sum.
"""

def calculate_list_sum(lst):
    """
    This function calculates the sum of all numbers in a list.
    It skips non-numeric values, including strings and nested lists,
    but includes numeric values in nested lists.

    Args:
        lst (list): A list containing numbers and/or non-numeric values.

    Returns:
        float: The sum of all numbers in the list.
    """
    total_sum = 0
    for element in lst:
        if isinstance(element, int) or isinstance(element, float):
            total_sum += element
        elif isinstance(element, list):
            for nested_element in element:
                if isinstance(nested_element, int) or isinstance(nested_element, float):
                    total_sum += nested_element
    return total_sum