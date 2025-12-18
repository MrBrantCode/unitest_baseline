"""
QUESTION:
Create a function named `is_isogram` that takes a string as input. The function should check if the input string is an isogram, meaning it does not contain any repeating letters. Non-alphabetic characters and case should be ignored in this check. The function should return `True` if the string is an isogram and `False` otherwise.
"""

def is_isogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1 and char.isalpha():
            return False
    return True