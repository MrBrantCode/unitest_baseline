"""
QUESTION:
Create a function `is_numeric_palindrome(s)` that checks if a given string is a numeric palindrome. The function should return `True` if the string is a numeric palindrome, "Error: String is not numeric." if the string is not numeric, and "Error: Number is not a palindrome." if the numeric value is not a palindrome.
"""

def is_numeric_palindrome(s):
    if not s.isdigit():
        return "Error: String is not numeric."
    s_reversed = s[::-1]
    if s == s_reversed:
        return True
    else:
        return "Error: Number is not a palindrome."