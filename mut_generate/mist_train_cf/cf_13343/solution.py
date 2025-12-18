"""
QUESTION:
Write a function `delete_chars(A, B)` that takes two strings A and B as input and returns a new string after deleting all characters in A that appear in B or more than once consecutively.
"""

def delete_chars(A, B):
    C = ''
    prev_char = None

    for char in A:
        if char not in B and char != prev_char:
            C += char
        prev_char = char

    return C