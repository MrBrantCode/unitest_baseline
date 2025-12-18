"""
QUESTION:
Write a function `check_anagram` that takes two strings as input, determines if they are anagrams of each other, and returns a boolean result. The function should be case-insensitive and ignore white spaces.
"""

def check_anagram(input1, input2):
    # Remove all the white spaces and convert to lowercase
    input1 = input1.replace(" ", "").lower()
    input2 = input2.replace(" ", "").lower()

    # Sort both strings and compare
    if sorted(input1) == sorted(input2):
        return True
    else:
        return False