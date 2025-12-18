"""
QUESTION:
Write a function `match_words` that takes a list of strings as input and returns a list of words that contain only lowercase letters and have at least one palindrome substring of length 3 or more.
"""

import re

def match_words(words):
    def is_palindrome(s):
        return s == s[::-1]

    def has_palindrome_substring(word, length=3):
        for i in range(len(word) - length + 1):
            if is_palindrome(word[i:i+length]):
                return True
        return False

    matched_words = []
    for word in words:
        if not re.match('^[a-z]*$', word):
            continue
        if has_palindrome_substring(word):
            matched_words.append(word)
    return matched_words