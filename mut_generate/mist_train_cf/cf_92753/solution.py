"""
QUESTION:
Write a function `delete_chars(A, B)` that takes two strings A and B as input. The function should delete characters in A that also appear in B and any characters in A that appear more than once consecutively. The function should return the modified string A.
"""

def delete_chars(A, B):
    C = ''
    prev_char = None

    for char in A:
        if char not in B and char != prev_char:
            C += char
        prev_char = char

    return C