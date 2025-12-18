"""
QUESTION:
Create a function `is_anagram_palindrome(s)` that takes a string `s` as input and returns `True` if the characters in `s` can be rearranged to form a palindrome, and `False` otherwise. The function should assume that the input string only contains characters that can be compared using equality.
"""

def can_form_palindrome(s):
    # create character frequency dictionary
    freq = {}
    for char in s:
        if char not in freq:
            freq[char] = 0
        freq[char] += 1

    # count characters with odd frequencies
    odd_count = 0
    for v in freq.values():
        if v % 2 != 0:
            odd_count += 1
        # if more than one character has an odd frequency count
        # then it's not possible to form a palindrome
        if odd_count > 1:
            return False

    # if we got this far, a palindrome can be formed
    return True