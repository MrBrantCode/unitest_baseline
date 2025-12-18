"""
QUESTION:
Write a function `check_conditions(string)` that takes a string of length 10 consisting of characters 'a' to 'd' as input and returns True if the string contains at least two occurrences of the character 'a' and the character 'b' appears before the character 'c', and False otherwise.
"""

def check_conditions(string):
    if string.count('a') < 2:
        return False
    if 'b' not in string or 'c' not in string:
        return False
    if string.index('b') > string.index('c'):
        return False
    return True