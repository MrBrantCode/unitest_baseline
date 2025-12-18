"""
QUESTION:
Write a Python function called `check_anagram` that takes a single word as input, reverses the word, and checks if the reversed word is an anagram of the original word by comparing the sorted character lists of both words. The function should return True if the reversed word is an anagram of the original word, False otherwise. The function should only work with words containing alphabetic characters and should be case-sensitive.
"""

def check_anagram(word):
    """
    This function checks if the reversed word is an anagram of the original word.
    
    Args:
    word (str): The input word.
    
    Returns:
    bool: True if the reversed word is an anagram of the original word, False otherwise.
    """
    
    # Reverse the word
    reversed_word = word[::-1]
    
    # Check if the sorted list of characters in the word and the reversed word are identical
    return sorted(word) == sorted(reversed_word)