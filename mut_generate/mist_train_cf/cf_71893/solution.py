"""
QUESTION:
Write a Python function `exclude_vocalic_terms` that takes a list of words and returns a new list containing only the words with three or fewer vocalic alphabetic characters (i.e., 'a', 'e', 'i', 'o', 'u'). The function should be case-insensitive.
"""

def exclude_vocalic_terms(lst):
    """
    This function filters a list of words to include only those with three or fewer vocalic alphabetic characters.

    Args:
        lst (list): A list of words.

    Returns:
        list: A new list containing only the words with three or fewer vocalic alphabetic characters.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [word for word in lst if sum(ch.lower() in vowels for ch in word) <= 3]