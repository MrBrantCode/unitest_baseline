"""
QUESTION:
Design a function named `count_unique_chars` that takes a string `text` as input and returns the number of unique characters in the string. The function should use a dictionary data structure to count the characters. The function should be case-sensitive and consider spaces and punctuation as characters. The input string can contain any ASCII characters.
"""

def count_unique_chars(text):
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return len(char_counts)