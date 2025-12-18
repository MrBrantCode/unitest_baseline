"""
QUESTION:
Create a function `check_uniqueness` that takes a string as input and returns `True` if all alphabetic characters in the string are unique (case-insensitive) and `False` otherwise. The function should ignore non-alphabetic characters and disregard the case of alphabetic characters.
"""

def check_uniqueness(string):
    alphabet_set = set()

    for char in string:
        if char.isalpha():
            if char.lower() in alphabet_set:
                return False
            else:
                alphabet_set.add(char.lower())
    
    return True