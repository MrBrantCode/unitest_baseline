"""
QUESTION:
Write a function `filter_and_sort_names` that takes a list of names as input and returns a dictionary containing names with odd lengths. The function should exclude names that start with a vowel ('a', 'e', 'i', 'o', 'u') and sort the resulting dictionary in descending order based on the lengths of the names.
"""

def filter_and_sort_names(names):
    """
    This function filters a list of names to exclude those starting with a vowel and having an even length.
    It then returns a dictionary containing the remaining names, sorted in descending order of their lengths.

    Args:
        names (list): A list of names

    Returns:
        dict: A dictionary with filtered and sorted names as keys and their lengths as values
    """

    odd_length_names = {name: len(name) for name in names if len(name) % 2 != 0 and name[0].lower() not in ['a', 'e', 'i', 'o', 'u']}
    return dict(sorted(odd_length_names.items(), key=lambda item: item[1], reverse=True))