"""
QUESTION:
Write a Python function `find_max_value` that takes a list as input and returns the maximum numeric value within the list, ignoring non-numeric elements. The function should handle nested lists, dictionaries, and sets within the input list, and consider numeric strings as potential maximum values.
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

    return max_value if max_value != float('-inf') else None