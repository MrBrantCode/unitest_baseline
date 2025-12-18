"""
QUESTION:
Write a function `is_palindrome(string)` to determine whether the given string is a palindrome or not. The input string can contain any printable ASCII characters, with a maximum length of up to 10^6 characters. The function should ignore case sensitivity and non-alphanumeric characters. It should return `True` for palindrome strings and `False` for non-palindrome strings.
"""

def entance(string):
    string = string.lower()
    string = ''.join(char for char in string if char.isalnum())
    start = 0
    end = len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True