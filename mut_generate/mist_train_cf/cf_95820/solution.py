"""
QUESTION:
Create a function named `change_case` that takes a string as input. The function should change the case of all alphabetic characters in the string (i.e., convert uppercase letters to lowercase and lowercase letters to uppercase), while leaving all non-alphabetic characters (including punctuation and spaces) unchanged.
"""

def change_case(input_string):
    result = ""
    for char in input_string:
        if char.isalpha():
            if char.isupper():
                result += char.lower()
            else:
                result += char.upper()
        else:
            result += char
    return result