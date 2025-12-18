"""
QUESTION:
Write a function named `sort_dictionary` that takes a dictionary of dictionaries as input and returns a new dictionary sorted by the nested 'age' in ascending order, then by 'salary' in descending order.
"""

def sort_dictionary(input_dict):
    """
    This function takes a dictionary of dictionaries as input, 
    and returns a new dictionary sorted by the nested 'age' in ascending order, 
    then by 'salary' in descending order.

    Args:
        input_dict (dict): A dictionary of dictionaries.

    Returns:
        dict: A new dictionary sorted by 'age' and 'salary'.
    """
    return dict(sorted(input_dict.items(), key=lambda item: (item[1]['age'], -item[1]['salary'])))