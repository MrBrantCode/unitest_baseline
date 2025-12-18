"""
QUESTION:
Create a function `string_and(a: str, b: str) -> str` that takes two strings consisting only of '1's and '0's, performs a binary AND operation on the corresponding bits of the two strings, and returns the result as a string. The function should handle strings of the same length.
"""

def string_and(a: str, b: str) -> str:
    result = ""
    for i in range(len(a)):
        if a[i] == '1' and b[i] == '1':
            result += '1'
        else:
            result += '0'
    return result