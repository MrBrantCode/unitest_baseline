"""
QUESTION:
Write a function named invertDictionary that takes a dictionary as input. Invert the dictionary, excluding any original keys that contain the letter 'a'. The resulting dictionary should only include keys that have a length greater than 2.
"""

def invertDictionary(dictionary):
    """
    Inverts a given dictionary, excluding keys containing 'a' and 
    resulting keys with a length greater than 2.

    Args:
    dictionary (dict): The input dictionary.

    Returns:
    dict: The inverted dictionary.
    """
    inverted_dict = {}
    for key, value in dictionary.items():
        if 'a' not in key and len(value) > 2:
            inverted_dict[value] = key
    return inverted_dict