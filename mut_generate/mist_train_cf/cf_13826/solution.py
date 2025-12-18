"""
QUESTION:
Create a function named `find_name_recursive` that takes a JSON data structure as input and returns the value associated with the key 'name'. The JSON data structure may contain nested objects and arrays, and the function should be able to find the value of 'name' at any level of nesting. The function should return `None` if the key 'name' is not found.
"""

def find_name_recursive(data):
    """
    Recursively searches for the value associated with the key 'name' in a JSON data structure.

    Args:
        data: A JSON data structure that may contain nested objects and arrays.

    Returns:
        The value associated with the key 'name', or None if not found.
    """
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'name':
                return value
            else:
                name = find_name_recursive(value)
                if name is not None:
                    return name
    elif isinstance(data, list):
        for item in data:
            name = find_name_recursive(item)
            if name is not None:
                return name
    return None