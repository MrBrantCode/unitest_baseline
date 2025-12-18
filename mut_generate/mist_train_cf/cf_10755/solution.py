"""
QUESTION:
Write a Python function named `most_frequent_chars` that takes a string as input, removes non-alphanumeric characters, converts to lowercase, counts the frequency of each character, and returns characters that occur three or more times.
"""

from collections import Counter

def most_frequent_chars(s):
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(c.lower() for c in s if c.isalnum())

    # Count the frequency of each character
    char_count = Counter(cleaned_string)

    # Get the characters that occur more than or equal to 3 times
    return [char for char, count in char_count.items() if count >= 3]