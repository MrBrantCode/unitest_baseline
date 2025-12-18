"""
QUESTION:
Implement a function `change_first_character` that takes a string as input and returns the string with the first character changed to uppercase if it is lowercase, and the second character changed to lowercase if the first character is uppercase. The function should only modify the string if it contains at least one lowercase character and one uppercase character.
"""

def change_first_character(string):
    if string and any(char.islower() for char in string) and any(char.isupper() for char in string):
        if string[0].islower():
            string = string[0].upper() + string[1:]
        elif string[0].isupper() and len(string) > 1:
            string = string[0] + string[1].lower() + string[2:]
    
    return string