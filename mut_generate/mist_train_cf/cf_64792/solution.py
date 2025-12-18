"""
QUESTION:
Write two functions, `is_palindrome(s: str) -> bool` and `make_palindrome(s: str) -> int`, that take a string `s` as input. 

The `is_palindrome` function should return `True` if the string is a palindrome, ignoring case, non-alphanumeric characters, and spaces between words, and `False` otherwise.

The `make_palindrome` function should return the minimum number of characters that need to be added at the end of the supplied string to make it a palindrome, ignoring case, non-alphanumeric characters, and spaces between words.

Assume the input string only contains ASCII characters. The functions should not modify the input string.
"""

def entrance(s: str) -> int:
    """
    Find the minimum number of characters that need to be added at the end of the supplied string to make it a palindrome, 
    ignoring case, non-alphanumeric characters, and spaces between words.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome,
    - Compute the length of the string prefix that comes before the palindrome suffix.
    - Return the length of the prefix as the minimum number of characters needed to create the shortest possible palindrome.
    """
    def is_palindrome(filtered_string: str) -> bool:
        """ 
        Test if given string is a palindrome, ignoring case, non-alphanumeric characters, and spaces between words 
        """
        return filtered_string == filtered_string[::-1]

    filtered_string = ''.join(char.lower() for char in s if char.isalnum())

    for i in range(len(filtered_string)):
        if is_palindrome(filtered_string[i:]):
            return i