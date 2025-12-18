"""
QUESTION:
Create a function named `modify_list` that takes a list of dictionaries as input. The function should remove any dictionaries containing the key 'name' with a value that starts with the letter 'B' (case-insensitive) and return the modified list sorted in descending order based on the 'age' key. The input list is not guaranteed to be sorted.
"""

def modify_list(input_list):
    """
    This function takes a list of dictionaries as input, removes any dictionaries 
    containing the key 'name' with a value that starts with the letter 'B' 
    (case-insensitive), and returns the modified list sorted in descending order 
    based on the 'age' key.

    Args:
        input_list (list): A list of dictionaries.

    Returns:
        list: The modified list of dictionaries.
    """
    return sorted([d for d in input_list if not d.get('name', '').lower().startswith('b')], key=lambda x: x['age'], reverse=True)