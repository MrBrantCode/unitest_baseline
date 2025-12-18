"""
QUESTION:
Write a function `replace_uppercase` that takes two parameters: a string and a character. Replace all uppercase letters in the string with the given character, but only if the uppercase letter is followed by a lowercase letter. The function should not use any built-in string methods and return the modified string along with the count of replacements made.
"""

def replace_uppercase(string, char):
    count = 0
    new_string = ""
    for i in range(len(string)):
        if i < len(string) - 1 and string[i].isupper() and string[i + 1].islower():
            new_string += char
            count += 1
        else:
            new_string += string[i]
    return new_string, count