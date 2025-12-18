"""
QUESTION:
Write a function `count_characters` that takes a string as input and returns a dictionary where the keys are the unique characters in the string and the values are the counts of each character. The input string will consist only of lowercase letters, numbers, and special characters, with a maximum length of 100 characters.
"""

def count_characters(string):
    char_count = {}
    
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count