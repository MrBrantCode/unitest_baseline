"""
QUESTION:
Write a function `get_palindromes` that takes a list of strings as input and returns a list of strings that are palindromes. The function should have a time complexity of O(n^2), where n is the total number of characters in all the strings combined. The space complexity should be O(m), where m is the number of strings in the input list that are palindromes.
"""

def get_palindromes(list_strings):
    palindromes = []
    for s in list_strings:
        if s == s[::-1]:
            palindromes.append(s)
    return palindromes