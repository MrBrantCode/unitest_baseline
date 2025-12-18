"""
QUESTION:
Write a function called `get_anagram` that takes a word as input and returns its anagram if it exists. The function should generate all possible permutations of the letters in the word, and then check each permutation against a given dictionary of words. If a permutation matches a word in the dictionary, it is considered an anagram. If no anagram is found, the function should return None. The function should be designed to work with a predefined list of words, where the anagram for a given word must also be present in the list.
"""

import itertools

def get_anagram(word, dictionary):
    """
    This function generates all possible permutations of the letters in the word 
    and checks each permutation against a given dictionary of words.

    Args:
    word (str): The word for which the anagram is to be found.
    dictionary (set): A set of words to check the permutations against.

    Returns:
    str: The anagram if found, otherwise None.
    """
    # Generate all possible permutations of the letters in the word
    permutations = itertools.permutations(word)
    
    # Check each permutation to see if it is a valid word
    for permutation in permutations:
        anagram = ''.join(permutation)
        if anagram in dictionary and anagram != word:
            return anagram
    
    # If no valid anagram is found, return None
    return None