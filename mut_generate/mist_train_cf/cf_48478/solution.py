"""
QUESTION:
Write a function called `valid_palindrome_checker` that takes a string `s` as input and returns `True` if the string is a palindrome considering only alphanumeric characters and ignoring cases, and `False` otherwise. The function should not use the Python built-in reverse function or any string manipulation methods. The input string may contain lower case letters, upper case letters, numbers, spaces, and punctuation marks.
"""

def valid_palindrome_checker(s):
    start, end = 0, len(s) - 1 
    while start < end: 
        while not s[start].isalnum() and start < end:
            start += 1
        while not s[end].isalnum() and end > start:
            end -=1
        if s[start].lower() != s[end].lower():
            return False
        else:
            end -= 1
            start += 1
    return True