"""
QUESTION:
Implement a function `count_alphanumeric_chars` that takes a string as input, counts the occurrence of each unique alphanumeric character (excluding whitespace characters), and returns the characters in descending order of their occurrence count. The function should have a time complexity of O(n log n).
"""

from collections import defaultdict

def count_alphanumeric_chars(s):
    # Create a dictionary to store the occurrence count of each character
    char_count = defaultdict(int)

    # Iterate through the string and increment the count for each alphanumeric character
    for char in s:
        if char.isalnum():
            char_count[char] += 1

    # Sort the dictionary by value in descending order
    sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

    # Return the characters in descending order of their occurrence count
    return [char for char, count in sorted_chars]