"""
QUESTION:
Write a function `reverseString` that takes a string `inputStr` as input and returns a new string with the characters reversed, handling uppercase and lowercase letters, special characters, and spaces, without using any built-in string reversal functions or methods.
"""

def reverseString(inputStr):
    reversedStr = ""
    for i in range(len(inputStr) - 1, -1, -1):
        reversedStr += inputStr[i]
    return reversedStr