"""
QUESTION:
Write a function named `compare_strings` that takes two strings as input and returns a boolean value indicating whether the strings are equal or not. The function must compare the strings character by character without using any built-in string comparison methods or operators. If the strings have different lengths, the function should immediately return False. Otherwise, it should iterate through each character of the strings and return False as soon as a mismatch is found. If all characters match, the function should return True.
"""

def compare_strings(string1, string2):
    # Check if the lengths of the strings are different
    if len(string1) != len(string2):
        return False
    
    # Compare each character of the strings
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            return False
    
    # If all characters are the same, return True
    return True