"""
QUESTION:
Design a function `anagram_check(lexeme_collection)` that takes a list of strings `lexeme_collection` as input and returns a boolean value indicating whether all strings in the collection are anagrams of each other. The function should be case sensitive, i.e., it treats 'A' and 'a' as different characters.
"""

def anagram_check(lexeme_collection):
    """
    This function checks if all strings in the input collection are anagrams of each other.
    
    Args:
        lexeme_collection (list): A list of strings.
    
    Returns:
        bool: True if all strings are anagrams, False otherwise.
    """
    # If the collection is empty or contains only one element, it is an anagram by default
    if len(lexeme_collection) < 2:
        return True
    
    # Sort the characters in the first string and use it as a reference
    reference = sorted(lexeme_collection[0])
    
    # Iterate over the rest of the strings in the collection
    for lexeme in lexeme_collection[1:]:
        # If the sorted characters of the current string do not match the reference, return False
        if sorted(lexeme) != reference:
            return False
    
    # If the function has not returned False after iterating over all strings, they are all anagrams
    return True