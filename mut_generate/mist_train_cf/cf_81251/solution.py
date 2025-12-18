"""
QUESTION:
Create a function called "reverseString" that takes a string as input and returns its reverse without using built-in methods. The function should manually process the input string to generate the reversed string.
"""

def reverseString(s):
    reversedStr = ''
    for i in range(len(s) - 1, -1, -1):
        reversedStr += s[i]
    return reversedStr