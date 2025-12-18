"""
QUESTION:
Create a function named `contains_all_lowercase_letters` that takes a string as input and returns `True` if the string contains all lowercase letters of the English alphabet and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1).
"""

def contains_all_lowercase_letters(string):
    lowercase_letters = set("abcdefghijklmnopqrstuvwxyz")

    for char in string:
        if char.islower():
            lowercase_letters.discard(char)
            if len(lowercase_letters) == 0:
                return True

    return False