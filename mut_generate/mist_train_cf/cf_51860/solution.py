"""
QUESTION:
Write a function `can_form_palindrome(s)` that determines whether a given string `s` can be rearranged into a valid palindrome. The function should return `True` if the string can be rearranged into a palindrome and `False` otherwise. The function should work for all ASCII characters and the time complexity should be O(n), where n is the length of the given string.
"""

def can_form_palindrome(s):
    char_freq = {}
    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1
    odd_count = sum(count % 2 for count in char_freq.values())
    return odd_count <= 1