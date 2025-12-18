"""
QUESTION:
Create a function `sort_and_remove` that takes a dictionary where keys are words and values are their frequencies. The function should return a new dictionary with the following conditions: 
- the dictionary is sorted alphabetically by keys (words), 
- all key-value pairs with a frequency (value) less than or equal to 5 are removed.
"""

def sort_and_remove(dictionary):
    """
    This function takes a dictionary where keys are words and values are their frequencies.
    It returns a new dictionary with keys sorted alphabetically and all key-value pairs 
    with a frequency (value) less than or equal to 5 removed.

    Args:
        dictionary (dict): A dictionary where keys are words and values are their frequencies.

    Returns:
        dict: A new dictionary with keys sorted alphabetically and filtered by frequency.
    """
    sorted_dict = dict(sorted([item for item in dictionary.items() if item[1] > 5]))
    return sorted_dict