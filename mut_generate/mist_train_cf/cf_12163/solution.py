"""
QUESTION:
Write a function named `count_a` that takes a string as input and returns the number of times the characters 'a' and 'á' appear in it, regardless of case. The function should have a time complexity of O(n), where n is the length of the string, and should not use built-in string manipulation functions or regular expressions.
"""

def count_a(string):
    count = 0
    for char in string:
        if char.lower() in ('a', 'á'):
            count += 1
    return count