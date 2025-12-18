"""
QUESTION:
Write a function `is_anagram_of_palindrome(txt)` that determines whether a given string can be rearranged into a palindrome, ignoring case, spaces, and punctuation. The function should return `True` if the string can be rearranged into a palindrome and `False` otherwise. The input string may contain alphanumeric characters, spaces, and punctuation.
"""

def is_anagram_of_palindrome(txt):
    txt = txt.lower()
    txt = ''.join(e for e in txt if e.isalnum()) 
    chars = {}
    for c in txt:
        if c not in chars:
            chars[c] = 0
        chars[c] += 1
    odd_count_chars = sum(1 for c in chars.values() if c % 2 != 0)
    return odd_count_chars <= 1