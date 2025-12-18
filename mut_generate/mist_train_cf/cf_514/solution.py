"""
QUESTION:
Write a function called `get_palindromes` that takes a list of strings as input and returns a list of all strings that are palindromes. The function should have a time complexity of O(n^2), where n is the total number of characters in all the strings combined, and a space complexity of O(m), where m is the number of strings in the list that are palindromes.
"""

def get_palindromes(list_strings):
    def is_palindrome(s):
        return s == s[::-1]
    palindromes = [s for s in list_strings if is_palindrome(s)]
    return palindromes