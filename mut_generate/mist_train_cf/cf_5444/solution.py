"""
QUESTION:
Implement a function `substring` that takes a string and two integers `a` and `b` as input, and returns a substring starting from index `a` and ending at index `b` without using any built-in substring or slice functions. If `b` exceeds the string length, it should be set to the index of the last character in the string. If any of the following conditions is met, return an empty string: the input string is empty, `a` is greater than `b`, or either `a` or `b` is negative. The function should have a time complexity of O(n), where n is the length of the string.
"""

def substring(string, a, b):
    if len(string) == 0 or a > b or a < 0 or b < 0:
        return ""
    if a >= len(string):
        return ""
    if b >= len(string):
        b = len(string) - 1

    substring = ""
    for i in range(len(string)):
        if i >= a and i <= b:
            substring += string[i]

    return substring