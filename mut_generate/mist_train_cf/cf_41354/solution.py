"""
QUESTION:
Implement the function `find_palindromes(input_list)` that takes a list of strings `input_list` as input and returns a new list containing only the strings that are palindromes. The function should ignore spaces, punctuation, and capitalization when checking for palindromes. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward. The function should handle edge cases such as empty input lists and return an empty list in such cases.
"""

def find_palindromes(input_list):
    def is_palindrome(s):
        # Remove spaces and punctuation, convert to lowercase
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s == s[::-1]

    palindromes = [word for word in input_list if is_palindrome(word)]
    return palindromes