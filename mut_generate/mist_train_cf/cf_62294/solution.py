"""
QUESTION:
Construct a function named `count_elements` that calculates the total count of key-value pairs in a given dictionary, including those in any nested dictionaries. The function should be able to handle dictionaries with n-depth nesting.
"""

def count_elements(data):
    """
    Calculate the total count of key-value pairs in a dictionary, 
    including those in any nested dictionaries.

    Args:
        data (dict): The dictionary to count key-value pairs from.

    Returns:
        int: The total count of key-value pairs.
    """
    count = 0
    for key in data:
        count += 1
        if isinstance(data[key], dict):
            count += count_elements(data[key])
    return count