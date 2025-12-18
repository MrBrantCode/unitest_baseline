"""
QUESTION:
Write a function named `merge_dicts` that takes two dictionaries as input. The function should combine the elements of the two dictionaries into a single dictionary. If there are duplicate keys, merge their values by applying addition. The function should return the resulting dictionary. Assume that the values in the input dictionaries are numbers.
"""

def merge_dicts(dictA, dictB):
    """Combine two dictionaries into a single dictionary. 
    If there are duplicate keys, merge their values by applying addition.
    
    Parameters:
    dictA (dict): The first dictionary.
    dictB (dict): The second dictionary.
    
    Returns:
    dict: A dictionary where the keys from both dictA and dictB are added together.
    """
    
    # create a new dictionary where the keys from both dictA and dictB are added together
    # where they overlap.
    return {key: dictA.get(key, 0) + dictB.get(key, 0) for key in set(dictA) | set(dictB)}