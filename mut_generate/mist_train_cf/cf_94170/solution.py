"""
QUESTION:
Create a function `replace_letters` that takes a string and three parameters: a character to be replaced, its replacement, and a pair of surrounding characters. The function should return a new string where the specified character is replaced by its replacement only when it is surrounded by the given pair of characters.
"""

def replace_letters(string, replace, with_, surrounding_chars):
    """
    Replaces a specified character in a string with another character, 
    but only when the character is surrounded by a given pair of characters.

    Args:
    string (str): The input string.
    replace (str): The character to be replaced.
    with_ (str): The replacement character.
    surrounding_chars (str): A pair of surrounding characters.

    Returns:
    str: A new string with the character replaced according to the conditions.
    """

    new_string = ''
    i = 0

    while i < len(string):
        if string[i] == replace:
            if (i - 1 >= 0 and i + 1 < len(string) and 
                string[i - 1] == surrounding_chars[0] and 
                string[i + 1] == surrounding_chars[1]):
                new_string += with_
            else:
                new_string += string[i]
        else:
            new_string += string[i]
        i += 1

    return new_string