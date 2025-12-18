"""
QUESTION:
Create a function `filter_names` that takes a list of names as input and returns a dictionary where the keys are the names and the values are their lengths. The dictionary should only include names with odd lengths and exclude names that start with a vowel (both lowercase and uppercase).
"""

def filter_names(names):
    """
    This function filters a list of names and returns a dictionary with names of odd lengths 
    that do not start with a vowel (both lowercase and uppercase) as keys and their lengths as values.

    Args:
        names (list): A list of names

    Returns:
        dict: A dictionary with names of odd lengths that do not start with a vowel as keys and their lengths as values
    """
    return {name: len(name) for name in names if len(name) % 2 != 0 and name[0].lower() not in ['a', 'e', 'i', 'o', 'u']}