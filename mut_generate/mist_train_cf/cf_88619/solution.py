"""
QUESTION:
Write a function `count_occurrences(string)` that takes a string as input and returns the number of times the character 'a' or 'á' (case-insensitive) appears in it, handling Unicode characters and strings of any length without using built-in string manipulation functions or regular expressions, with a time complexity of O(n).
"""

def entrance(string):
    count = 0
    for char in string:
        if char.lower() == 'a' or char.lower() == 'á':
            count += 1
    return count