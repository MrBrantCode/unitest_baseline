"""
QUESTION:
Write a function `has_consecutive_uppercase` that takes a string as input and returns `True` if the string contains at least 3 consecutive uppercase letters, and `False` otherwise.
"""

def has_consecutive_uppercase(string):
    count = 0
    for i in range(len(string)-2):
        if string[i:i+3].isupper():
            count += 1
    return count > 0