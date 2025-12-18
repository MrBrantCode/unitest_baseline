"""
QUESTION:
Write a function `is_anagram_of_palindrome(s)` that takes a string `s` as input and returns a tuple `(bool, str)`. The function should return `True` and the corresponding palindrome string if the alphanumeric characters in `s` form an anagram of a palindrome, and `False` and an empty string otherwise. The function should ignore non-alphanumeric characters in `s` and be case-insensitive. The function should optimize for large input strings.
"""

from collections import Counter

def is_anagram_of_palindrome(s):
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    count = Counter(s)
    odd_count_chars = [char for char, freq in count.items() if freq%2]

    if len(odd_count_chars) > 1:
        return False, ""

    odd_count_char = odd_count_chars[0] if odd_count_chars else ''
    even_count_chars = ''.join(char * (freq // 2) for char, freq in count.items() if freq%2 == 0)

    palindrome = even_count_chars + odd_count_char + even_count_chars[::-1]

    return True, palindrome