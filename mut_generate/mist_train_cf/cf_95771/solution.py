"""
QUESTION:
Write a function named `contains_a` that takes a list of strings as input and returns `True` if any string (ignoring those that start with a lowercase letter) contains the letter 'a'. The function should have a time complexity of O(n), where n is the total number of characters in all the strings.
"""

def contains_a(strings):
    for string in strings:
        if string[0].islower():
            continue
        if 'a' in string:
            return True
    return False