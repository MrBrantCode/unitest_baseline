"""
QUESTION:
Write a function `reverseString` that takes a string `s` as input and returns the reversed string without using any built-in string reversal functions or methods, additional data structures, or explicit looping constructs such as for, while, or recursion is not allowed as per initial prompt but is accepted here, and achieves a time complexity of O(n), where n is the length of the input string.
"""

def reverseString(s):
    if len(s) <= 1:
        return s
    else:
        return reverseString(s[1:]) + s[0]