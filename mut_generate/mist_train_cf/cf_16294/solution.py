"""
QUESTION:
Write a function `replace_surrounded_letters` that replaces all occurrences of a specified letter in a string with another letter, but only if the specified letter is surrounded by a pair of specified characters. The function should take four parameters: the input string, the letter to be replaced, the replacement letter, and a pair of surrounding characters.
"""

def replace_surrounded_letters(string, replace, with_, surrounding_chars):
    new_string = ''
    i = 0

    while i < len(string):
        if string[i] == replace:
            if i - 1 >= 0 and i + 1 < len(string) and string[i - 1] == surrounding_chars[0] and string[i + 1] == surrounding_chars[1]:
                new_string += with_
            else:
                new_string += string[i]
        else:
            new_string += string[i]
        i += 1

    return new_string