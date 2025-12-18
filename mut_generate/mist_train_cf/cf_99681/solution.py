"""
QUESTION:
Write a function `is_circular_palindrome_chain(words)` that takes a list of words as input and returns `True` if the list forms a circular chain of palindromes, where each word's first letter is the same as the previous word's last letter, and `False` otherwise.
"""

def is_circular_palindrome_chain(words):
    """
    Returns True if the given list of words forms a circular chain of palindromes, False otherwise.
    """
    if len(words) < 2:
        return False
    if words[0][0] != words[-1][-1]:
        return False
    for word in words:
        if word != word[::-1]:
            return False
    for i in range(len(words) - 1):
        if words[i][-1] != words[i+1][0]:
            return False
    return True