"""
QUESTION:
Write a function `replace_uppercase` that takes a string and a character as input. Replace all uppercase letters in the string with the given character if they are followed by a lowercase letter. Do not use any built-in string methods. Return the modified string and the number of replacements made.
"""

def replace_uppercase(s, c):
    count = 0
    new_string = ""
    for i in range(len(s)):
        if i < len(s) - 1 and s[i].isupper() and s[i + 1].islower():
            new_string += c
            count += 1
        else:
            new_string += s[i]
    return new_string, count