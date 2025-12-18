"""
QUESTION:
# Palindrome strings

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. This includes capital letters, punctuation, and word dividers.

Implement a function that checks if something is a palindrome.

## Examples
```
isPalindrome("anna")   ==> true
isPalindrome("walter") ==> false
isPalindrome(12321)    ==> true
isPalindrome(123456)   ==> false
```
"""

def is_palindrome(input_value):
    """
    Checks if the given input_value is a palindrome.

    Parameters:
    input_value (str, int, etc.): The value to be checked for being a palindrome.

    Returns:
    bool: True if the input_value is a palindrome, False otherwise.
    """
    return str(input_value)[::-1] == str(input_value)