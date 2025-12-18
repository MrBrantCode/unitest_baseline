"""
QUESTION:
Create a function named `create_tuple` that takes a string, a list, and an optional boolean `reverse` parameter (defaulting to `False`). The function should return a tuple containing the string and the list, and if `reverse` is `True`, the order of the tuple elements should be reversed. The function should handle exceptions for invalid inputs and return the string representation of the error.
"""

def create_tuple(string, list_data, reverse=False):
    try:
        result = (string, list_data)
        if reverse:
           result = result[::-1]
        return result
    except Exception as e:
        return str(e)