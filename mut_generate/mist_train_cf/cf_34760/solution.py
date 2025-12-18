"""
QUESTION:
Write a function `swapCase` that takes a string `s` as input and returns a new string where all uppercase letters in `s` are converted to lowercase and all lowercase letters are converted to uppercase. Non-alphabet characters in the string should remain unchanged.
"""

def swapCase(s):
    swapped = ""
    for char in s:
        if char.isalpha():
            if char.islower():
                swapped += char.upper()
            else:
                swapped += char.lower()
        else:
            swapped += char
    return swapped