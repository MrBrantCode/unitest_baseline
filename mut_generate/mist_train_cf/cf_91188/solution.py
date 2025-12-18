"""
QUESTION:
Implement a function `reverse_string` that takes a string `s` as input, reverses it in place without using any additional data structures or built-in functions, and returns the reversed string. The input string is immutable, so it may be converted to a mutable format temporarily. The output should be a string.
"""

def reverse_string(s):
    """
    Reverses the input string in place without using any additional data structures or built-in functions.
    
    Args:
        s (str): The input string to be reversed.
    
    Returns:
        str: The reversed string.
    """
    word = list(s)
    left = 0
    right = len(word) - 1

    while left < right:
        word[left], word[right] = word[right], word[left]
        left += 1
        right -= 1

    return ''.join(word)