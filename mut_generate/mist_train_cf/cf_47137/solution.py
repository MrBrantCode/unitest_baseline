"""
QUESTION:
Write a function named `reverse_string(s)` that takes a string `s` as input and returns the modified string with the order of words and characters reversed, while maintaining the position of non-alphabetic characters. The function should not use any external libraries or built-in string reversal functions other than `reversed()`, and it should handle strings containing any type of characters.
"""

def reverse_string(s):
    # Separate non-alphabetic characters and their positions
    non_alpha_chars = [(i, c) for i, c in enumerate(s) if not c.isalpha()]

    # Reverse the string and remove non-alphabetic characters
    reversed_str = [c for c in reversed(s) if c.isalpha()]

    # Insert non-alphabetic characters back into the reversed string
    for i, c in non_alpha_chars:
        reversed_str.insert(i, c)
    
    # Join the characters back into a single string
    result = ''.join(reversed_str)

    return result