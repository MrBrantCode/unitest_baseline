"""
QUESTION:
Write a function named `get_length_and_unique_chars` that takes a string as input and returns its length and the number of unique characters without using any built-in length function. The input string may contain special characters and spaces.
"""

def get_length_and_unique_chars(text):
    length = 0
    unique_chars = set()

    for char in text:
        length += 1
        if char not in unique_chars:
            unique_chars.add(char)

    return length, len(unique_chars)