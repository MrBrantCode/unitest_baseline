"""
QUESTION:
Write a function `sum_dictionary_values` that calculates the sum of values in a dictionary where keys are strings. Ignore keys that contain uppercase letters, special characters, or numbers.
"""

def sum_dictionary_values(dictionary):
    """
    Calculate the sum of values in a dictionary where keys are strings.
    Ignore keys that contain uppercase letters, special characters, or numbers.

    Args:
        dictionary (dict): The dictionary to process.

    Returns:
        int: The sum of values corresponding to valid keys.
    """
    return sum(val for key, val in dictionary.items() if key.isalpha() and key.islower())