"""
QUESTION:
Create a function `is_palindrome(seq)` that takes a sequence of characters as input and returns `True` if the sequence is a palindrome (i.e., reads the same backward as forward) and `False` otherwise. The function should be case-insensitive and ignore non-alphanumeric characters.
"""

def is_palindrome(seq):
    seq = seq.lower()     # Converting to lowercase
    new_seq = ''.join(filter(str.isalnum, seq))   # keep only alphanumeric characters
    return new_seq == new_seq[::-1]    # Checking if sequence is same as its reverse