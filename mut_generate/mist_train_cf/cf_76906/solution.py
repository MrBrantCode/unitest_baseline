"""
QUESTION:
Design a function named `uppercase_count` that takes a string as input and returns the total count of uppercase alphabetic characters in the string.
"""

def uppercase_count(string):
    count = 0
    for char in string:
        if char.isupper():
            count += 1
    return count