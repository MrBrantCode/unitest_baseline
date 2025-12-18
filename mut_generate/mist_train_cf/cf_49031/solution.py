"""
QUESTION:
Implement three functions: `is_palindrome`, `make_palindrome`, and `valid_palindrome`. 

The `is_palindrome` function should return a boolean value indicating whether a given string is a palindrome, considering spaces between words. The `make_palindrome` function should find the shortest palindrome starting with a provided string, ignoring case, non-alphanumeric characters, and spaces between words. The `valid_palindrome` function should validate if a string of words is a palindrome, disregarding spaces, punctuation, and capitalization. 

Restrictions: Do not use extra modules or libraries.
"""

def make_palindrome(string: str) -> str:
    string = ''.join(ch for ch in string if ch.isalnum()).lower()
    for i in range(len(string)):
        if string[i:] == string[i:][::-1]:
            return string + string[:i][::-1]
    return ''

def is_palindrome(string: str) -> bool:
    return string.replace(" ", "") == string.replace(" ", "")[::-1]

def valid_palindrome(string: str) -> bool:
    string = ''.join(ch for ch in string if ch.isalnum()).lower()
    return string == string[::-1]