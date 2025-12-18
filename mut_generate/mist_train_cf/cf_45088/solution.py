"""
QUESTION:
Implement two functions, `is_palindrome` and `make_palindrome`, in Python without using any additional modules or libraries.

Function `is_palindrome` should take a string as input and return a boolean indicating whether the string is a palindrome, ignoring case, non-alphanumeric characters, and spaces between words.

Function `make_palindrome` should take a string as input and return the minimum number of characters that need to be added at the end of the string to make it a palindrome, ignoring case, non-alphanumeric characters, and spaces between words. The function should use the following algorithm:
1. Find the longest postfix of the supplied string that is a palindrome.
2. Compute the length of the string prefix that comes before the palindromic suffix.
3. Return the length of the prefix as the minimum number of characters needed to create the shortest possible palindrome.
"""

def is_palindrome(s: str) -> bool:
    """ Test if given string is a palindrome, ignoring case, non-alphanumeric characters, and spaces between words """
    filtered_string = ''.join(char.lower() for char in s if char.isalnum())
    return filtered_string == filtered_string[::-1]

def make_palindrome(s: str) -> int:
    """ Find the minimum number of characters that need to be added at the end of the supplied string to make it a palindrome, ignoring case, non-alphanumeric characters, and spaces between words.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Compute the length of the string prefix that comes before the palindromic suffix.
    - Return the length of the prefix as the minimum number of characters needed to create the shortest possible palindrome.
    """
    filtered_string = ''.join(char.lower() for char in s if char.isalnum())
    
    for i in range(len(filtered_string)):
        if is_palindrome(filtered_string[i:]):
            return i