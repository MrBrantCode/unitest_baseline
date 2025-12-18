"""
QUESTION:
Write a function named `contains_a` that takes in a list of strings. The function should return True if any of the strings that start with an uppercase letter contain the letter 'a', and False otherwise. The function should have a time complexity of O(n), where n is the total number of characters in all the strings in the list.
"""

def contains_a(strings):
    for string in strings:
        if string and string[0].isupper() and 'a' in string:
            return True
    return False