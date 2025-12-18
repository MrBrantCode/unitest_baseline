"""
QUESTION:
Implement two functions, `is_palindrome` and `make_palindrome`. The `is_palindrome` function should return a boolean indicating whether the given string is a palindrome, ignoring case and non-alphanumeric characters, using recursion. The `make_palindrome` function should return the shortest possible palindrome that begins with the provided string, ignoring case and non-alphanumeric characters, by finding the longest postfix of the string that is a palindrome and appending the reverse of the prefix to the end of the original string. Note: Do not import any additional modules or libraries.
"""

def is_palindrome(string: str, l: int, r: int) -> bool:
    """ Test if given string is a palindrome, ignoring case and non-alphanumeric characters, using recursion """
    if l >= r:
        return True
    if not string[l].isalnum():
        return is_palindrome(string, l + 1, r)
    if not string[r].isalnum():
        return is_palindrome(string, l, r - 1)
    if string[l].lower() != string[r].lower():
        return False
    return is_palindrome(string, l + 1, r - 1)

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string, ignoring case and non-alphanumeric characters.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    for i in range(len(string)):
        if is_palindrome(string, i, len(string) - 1):
            prefix = string[0:i]
            return string + prefix[::-1]
    return string + string[::-1]