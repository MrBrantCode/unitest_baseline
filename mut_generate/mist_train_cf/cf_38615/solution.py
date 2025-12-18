"""
QUESTION:
Create a function named `find_palindromes` that takes a list of strings as input and returns a new list containing only the strings that are palindromes. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, disregarding spaces, punctuation, and capitalization. The function should ignore spaces, punctuation, and capitalization when determining if a string is a palindrome. Assume the input list will only contain strings.
"""

def find_palindromes(input_list):
    return [s for s in input_list 
            if ''.join(e for e in s if e.isalnum()).lower() == ''.join(e for e in s if e.isalnum()).lower()[::-1]]