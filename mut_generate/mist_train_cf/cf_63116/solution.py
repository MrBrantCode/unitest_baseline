"""
QUESTION:
Create four functions: `is_palindrome`, `make_palindrome`, `find_palindromic_postfix`, and `strip_non_alphanumeric`. 

`is_palindrome` should take a string as input and return a boolean indicating whether the string is a palindrome, ignoring case and non-alphanumeric characters. 

`make_palindrome` should take a string as input and return a palindrome of the shortest possible length using the input string as the prefix, ignoring case and non-alphanumeric characters. 

`find_palindromic_postfix` should take a string as input and return the longest palindromic postfix within the string. 

`strip_non_alphanumeric` should take a string as input and return the string with all non-alphanumeric characters removed. The functions should not use any imported libraries or modules and should be case-insensitive.
"""

def is_palindrome(s: str) -> bool:
    s = strip_non_alphanumeric(s).lower()
    return s == s[::-1]

def make_palindrome(s: str) -> str:
    s = strip_non_alphanumeric(s).lower()
    postfix = find_palindromic_postfix(s)
    prefix = s[:len(s) - len(postfix)]
    return s + prefix[::-1]

def find_palindromic_postfix(s: str) -> str:
    for i in range(len(s), 0, -1):
        if is_palindrome(s[-i:]):
            return s[-i:]
    return ""

def strip_non_alphanumeric(s: str) -> str:
    return ''.join(ch for ch in s if ch.isalnum())