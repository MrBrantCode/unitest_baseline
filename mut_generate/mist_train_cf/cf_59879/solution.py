"""
QUESTION:
Write a function called `reverse_string` that takes a string as input and returns the reversed string if it's not a palindrome. If the input string is a palindrome, the function should return `True`. The function should ignore spacing, punctuation, and capitalization when checking for palindromes. Do not use any built-in string reversal functions.
"""

def reverse_string(s):
    s = s.replace(' ', '').lower()
    reversed_string = ''
    for i in range(len(s)):
        reversed_string = s[i] + reversed_string
    if reversed_string == s:  # check if input string is palindrome
        return True
    return reversed_string