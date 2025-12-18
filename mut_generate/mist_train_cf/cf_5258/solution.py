"""
QUESTION:
Write a function `get_palindromes(strings)` that takes in a list of strings and returns a new list containing only the strings that are palindromes. A palindrome is a word or phrase that reads the same backward as forward, ignoring spaces, punctuation, and capitalization. Your function should have a time complexity of O(n), where n is the length of the input list.
"""

import re

def get_palindromes(strings):
    palindromes = []
    for string in strings:
        modified_string = re.sub(r'[^a-zA-Z0-9]', '', string.lower())
        if modified_string == modified_string[::-1]:
            palindromes.append(string)
    return palindromes