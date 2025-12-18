"""
QUESTION:
Write a function named `count_a` that takes a string as input and returns the number of times the characters 'a' or 'á' appear in the string, regardless of case. The function should handle strings of any length, handle Unicode characters properly, and have a time complexity of O(n), where n is the length of the string.
"""

def count_a(string):
    count = 0
    for char in string:
        if char.lower() in ('a', 'á'):
            count += 1
    return count