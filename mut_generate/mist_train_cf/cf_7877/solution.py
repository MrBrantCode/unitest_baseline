"""
QUESTION:
Write a function `find_max_value` that takes a list as input and returns the maximum numeric value found in the list, ignoring non-numeric elements. The function should handle nested lists, dictionaries, and sets within the input list. The input list can contain strings that can be converted to numeric values, which should be considered when finding the maximum value.
"""

def find_max_value(lst):
    max_value = float('-inf')

    def check_value(value):
        nonlocal max_value
        if isinstance(value, (int, float)):
            max_value = max(max_value, value)
        elif isinstance(value, str):
            try:
                num = float(value)
                max_value = max(max_value, num)
            except ValueError:
                pass
        elif isinstance(value, list):
            for nested_value in value:
                check_value(nested_value)
        elif isinstance(value, dict):
            for nested_value in value.values():
                check_value(nested_value)
        elif isinstance(value, set):
            for nested_value in value:
                check_value(nested_value)

    for element in lst:
        check_value(element)

    return max_value