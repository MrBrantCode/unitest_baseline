"""
QUESTION:
Implement a function `initials(name)` that takes a string `name` representing a person's full name and returns a string containing their initials, which are the first letter of each word in the name, capitalized and without spaces, while ignoring any non-alphabetic characters.
"""

def entrance(name):
    parts = name.split(' ')
    letters = ''
    for part in parts:
        if part.isalpha():  
            letters += part[0].upper()  
    return letters