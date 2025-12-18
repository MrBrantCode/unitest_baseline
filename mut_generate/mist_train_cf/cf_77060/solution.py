"""
QUESTION:
Construct a Python function called `is_pangram` that takes a list of strings as input and returns a tuple. The function should be case-insensitive and ignore any non-alphabet characters. If the combined strings form a pangram (a sentence that uses every letter of the alphabet at least once), the function should return `True` and an empty list. If not, it should return `False` and a list of missing alphabets.
"""

def entrance(sentences):
    """
    Checks if a list of strings forms a pangram.

    Args:
    sentences (list): A list of strings.

    Returns:
    tuple: A tuple containing a boolean indicating whether the input forms a pangram,
           and a list of missing alphabets if it's not a pangram.
    """
    pangram_set = set('abcdefghijklmnopqrstuvwxyz')
    sentence_combined = ' '.join(sentences).lower()
    missing_alphabets = [char for char in pangram_set if char not in sentence_combined]

    return (len(missing_alphabets) == 0), missing_alphabets if missing_alphabets else []