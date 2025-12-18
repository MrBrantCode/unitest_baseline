"""
QUESTION:
Create a function `replace_letter_with_index(string, letter)` that replaces all occurrences of a given letter in a string with either '#' if the letter is at an even index or '$' if the letter is at an odd index. If the letter is not present in the string, return an empty string.
"""

def replace_letter_with_index(string, letter):
    if letter not in string:
        return ""
    
    new_string = ""
    for i in range(len(string)):
        if string[i] == letter:
            if i % 2 == 0:
                new_string += '#'
            else:
                new_string += '$'
        else:
            new_string += string[i]
    
    return new_string