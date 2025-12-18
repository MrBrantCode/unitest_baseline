"""
QUESTION:
Create a function named `reversed_and_palindrome` that takes a string `s` as input. The function should reverse the input string and check if the reversed string is a palindrome. If the reversed string is a palindrome, return a message stating that the string is a palindrome. Otherwise, return the reversed string along with its length.
"""

def reversed_and_palindrome(s):
    reversed_s = s[::-1]
    if s == reversed_s:
        return f"{reversed_s} is a palindrome."
    else:
        return f"{reversed_s}, length: {len(reversed_s)}"