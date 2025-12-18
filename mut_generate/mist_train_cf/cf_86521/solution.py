"""
QUESTION:
Implement a function `is_all_uppercase` that takes a string as input and returns True if all the characters in the string are uppercase letters from A to Z, and False otherwise. The function should handle special characters, numbers, and whitespace by returning False and should have a time complexity of O(n), where n is the length of the string. It should not use any built-in functions or libraries.
"""

def is_all_uppercase(string):
    for char in string:
        if not 'A' <= char <= 'Z':
            return False
    return True