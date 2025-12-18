"""
QUESTION:
Write a function named `count_occurrences` that takes a string as input and returns the number of times the characters 'a' or 'á' (case-insensitive) appear in it. The function should handle strings of any length, Unicode characters, and mixed character sets, including emojis, without using built-in string manipulation functions or regular expressions, and with a time complexity of O(n).
"""

def count_occurrences(string):
    count = 0
    for char in string:
        if char.lower() == 'a' or char.lower() == 'á':
            count += 1
    return count