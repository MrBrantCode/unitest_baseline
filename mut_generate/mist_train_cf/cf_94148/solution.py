"""
QUESTION:
Write a function named `change_first_character` that takes a string as input, changes the first character to uppercase if it is lowercase, and changes the second character to lowercase if the first character is uppercase. The function should return the modified string. The input string is assumed to contain at least one lowercase and one uppercase character.
"""

def change_first_character(string):
    if string[0].islower():
        string = string[0].upper() + string[1:]
    elif string[0].isupper():
        string = string[0] + string[1].lower() + string[2:]
    
    return string