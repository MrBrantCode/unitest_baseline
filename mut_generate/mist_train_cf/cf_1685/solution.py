"""
QUESTION:
Implement a recursive function named `is_palindrome` that checks if a given string is a palindrome without using any built-in string manipulation functions. The function should have a time complexity of O(n), where n is the length of the string.
"""

def is_palindrome(string):
    # Base case: an empty string or a string with only one character is always a palindrome
    if len(string) <= 1:
        return True

    # Recursive case: check if the first and last characters are equal
    # If they are, recursively check if the remaining string is a palindrome
    # If they aren't, the string is not a palindrome
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False