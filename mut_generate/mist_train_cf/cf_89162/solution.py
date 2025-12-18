"""
QUESTION:
Create a function called `is_palindrome` that takes a string as input, removes special characters, whitespace, numbers, and punctuation marks, and checks if the resulting string is a palindrome in a case-insensitive manner. The function should have a time complexity of O(n), where n is the length of the input string, and be able to handle strings of length up to 10^6 characters efficiently without exceeding memory limitations.
"""

def is_palindrome(s):
    # Remove special characters, whitespace, numbers, and punctuation marks
    s = ''.join(e for e in s if e.isalnum())
    # Convert the string to lowercase for case-insensitive comparison
    s = s.lower()
    # Check if the string is a palindrome
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True