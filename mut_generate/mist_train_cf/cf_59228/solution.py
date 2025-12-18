"""
QUESTION:
Create a function `compare_letter_sets` that takes two phrases as input and returns a tuple containing the number of unique letters in each phrase, the set of common letters, and the set of distinct letters. The function should ignore spaces and punctuation, and consider only alphabets as unique letters.
"""

def compare_letter_sets(phrase1: str, phrase2: str):
    """
    This function compares two phrases and returns a tuple containing the number of unique letters in each phrase, 
    the set of common letters, and the set of distinct letters.

    Parameters:
    phrase1 (str): The first phrase to compare.
    phrase2 (str): The second phrase to compare.

    Returns:
    tuple: A tuple containing the number of unique letters in each phrase, the set of common letters, and the set of distinct letters.
    """

    # Define the sets of unique alphabets in each phrase, ignoring spaces and punctuation
    set1 = set(c for c in phrase1 if c.isalpha())
    set2 = set(c for c in phrase2 if c.isalpha())

    # Calculate the unique, common and distinct letters
    unique1 = len(set1)
    unique2 = len(set2)
    common = set1 & set2
    distinct = set1 ^ set2

    return (unique1, unique2, common, distinct)