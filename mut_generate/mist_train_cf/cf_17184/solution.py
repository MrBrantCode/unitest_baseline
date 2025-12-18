"""
QUESTION:
Implement a function `count_alphanumeric_chars` that takes a string as input and returns a list of unique alphanumeric characters (excluding whitespace characters) in descending order of their occurrence count in the string. The function should have a time complexity of O(n log n).
"""

from collections import defaultdict

def count_alphanumeric_chars(string):
    char_count = defaultdict(int)
    for char in string:
        if char.isalnum():
            char_count[char] += 1
    sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    return [char for char, count in sorted_chars]