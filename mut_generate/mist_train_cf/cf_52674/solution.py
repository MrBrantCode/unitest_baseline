"""
QUESTION:
Create three functions: `is_palindrome`, `make_palindrome`, and `remove_special_characters`. 

`is_palindrome(string)` should return a boolean value indicating whether the input string, after removing spaces and special characters, is a palindrome or not. The function should be case-insensitive.

`remove_special_characters(string)` should filter out non-alphanumeric characters from the string.

`make_palindrome(string)` should generate the shortest palindrome using the input string as the starting point, regardless of case. It should work by identifying the longest palindromic suffix within the provided string (after removing special characters), taking the prefix string before the palindromic suffix, reversing it, and appending it to the end of the original string. If the input string is already a palindrome, the function should return the input string as is.

Do not use any external libraries or modules. The functions should be able to handle different scenarios.
"""

def is_palindrome(string):
    string = remove_special_characters(string).lower()
    return string == string[::-1]

def remove_special_characters(string):
    return ''.join(c for c in string if c.isalnum())

def make_palindrome(string):
    string = remove_special_characters(string)
    if is_palindrome(string):
        return string

    for i in range(len(string)):
        suffix = string[i:]
        prefix = string[:i]
        if suffix == suffix[::-1]:
            return string + prefix[::-1]