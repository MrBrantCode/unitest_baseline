"""
QUESTION:
Write a function named `count_characters` that takes a string `text` as input and returns the total number of characters in the string, excluding any whitespace characters. The function should handle strings containing uppercase and lowercase letters, numbers, special characters, and punctuation marks.
"""

def count_characters(text):
    count = 0
    for char in text:
        if not char.isspace():
            count += 1
    return count