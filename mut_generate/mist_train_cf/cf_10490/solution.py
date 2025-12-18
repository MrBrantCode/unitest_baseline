"""
QUESTION:
Write a function named `count_alphabetic_characters` that takes a string as input and returns a dictionary where the keys are the unique alphabetic characters in the string and the values are the counts of each character. The function should ignore any non-alphabetic characters.
"""

def count_alphabetic_characters(text):
    char_count = {}
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count