"""
QUESTION:
Implement a function named `reverseString` that takes a string `s` as input and returns the reversed string without using built-in string reversal functions or methods, additional data structures, or explicit looping constructs (for, while). The function should have a time complexity of O(n), where n is the length of the input string.
"""

def reverseString(s):
    if len(s) <= 1:
        return s
    else:
        return reverseString(s[1:]) + s[0]