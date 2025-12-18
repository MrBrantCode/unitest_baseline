"""
QUESTION:
Create a function `is_palindrome(sequence)` that checks if a given sequence of characters is the same when its elements are reversed, returning True if it's a palindrome and False otherwise. Assume the input sequence is a string where characters can be separated by spaces, and the comparison is case-sensitive.
"""

def is_palindrome(sequence):
    return sequence == sequence[::-1]