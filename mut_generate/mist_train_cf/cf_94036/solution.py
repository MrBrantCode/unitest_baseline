"""
QUESTION:
Implement a function is_palindrome(s) that takes a string s as input and returns "True" if the string is a palindrome and "False" otherwise. Palindrome strings are those that remain the same when their characters are reversed. The function should have a time complexity of O(n), where n is the length of the input string. Ignore any non-alphanumeric characters and consider case insensitivity. The function cannot use any built-in functions or libraries to reverse the string or check for palindromes.
"""

def entrance(s):
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left, right = left + 1, right - 1
    return True