"""
QUESTION:
Write a function named `extract_numbers` that takes a dictionary or a list as input and returns the sum of all integers that are divisible by 3 and have an even number of digits. The function should be able to handle nested dictionaries and lists.
"""

def extract_numbers(data):
    """
    This function calculates the sum of all integers in a dictionary or list 
    that are divisible by 3 and have an even number of digits.

    Args:
    data (dict or list): A dictionary or list containing integers, dictionaries, and lists.

    Returns:
    int: The sum of integers that meet the conditions.
    """
    total = 0
    if isinstance(data, dict):
        for value in data.values():
            if isinstance(value, dict) or isinstance(value, list):
                total += extract_numbers(value)
            elif isinstance(value, int):
                if value % 3 == 0 and len(str(value)) % 2 == 0:
                    total += value
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict) or isinstance(item, list):
                total += extract_numbers(item)
            elif isinstance(item, int):
                if item % 3 == 0 and len(str(item)) % 2 == 0:
                    total += item
    return total