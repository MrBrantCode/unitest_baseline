"""
QUESTION:
Create a function named merge_dicts that merges two dictionaries, d1 and d2, into a new dictionary. If a value from d1 is an odd number, multiply it by 2, and if a value from d2 is an even number, reduce it by 3. The keys from both dictionaries should be preserved in the new dictionary.
"""

def merge_dicts(d1, d2):
    """
    Merges two dictionaries, d1 and d2, into a new dictionary.
    If a value from d1 is an odd number, multiply it by 2, and if a value from d2 is an even number, reduce it by 3.
    The keys from both dictionaries should be preserved in the new dictionary.

    Args:
        d1 (dict): The first dictionary.
        d2 (dict): The second dictionary.

    Returns:
        dict: A new dictionary with merged and modified values.
    """
    new_dict = {}
    
    # Insert values from d1 after checking if they are odd
    for key, value in d1.items():
        if value % 2 != 0:
            new_dict[key] = value * 2
        else:
            new_dict[key] = value

    # Insert values from d2 after checking if they are even
    for key, value in d2.items():
        if key in new_dict:  # Check if key already exists
            if value % 2 == 0:
                new_dict[key] = value - 3
            else:
                new_dict[key] = value
        else:
            if value % 2 == 0:
                new_dict[key] = value - 3
            else:
                new_dict[key] = value

    return new_dict