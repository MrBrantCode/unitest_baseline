"""
QUESTION:
Write a function called `find_longest_word` that takes a string as a parameter and returns the longest word in the string, excluding punctuation marks and whitespace characters. If multiple words have the same maximum length, return the first occurrence. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.
"""

import string

def find_longest_word(s):
    words = s.split()
    longest_word = ""
    for word in words:
        word = word.strip(string.punctuation + string.whitespace)
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word