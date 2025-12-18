"""
QUESTION:
Create a function `replace_non_alpha` that accepts a string and a replacement character. The function should replace all non-alphabetic characters (excluding white spaces) in the string with the given replacement character and return the modified string along with the total number of replacements made. The function should handle both uppercase and lowercase alphabets.
"""

def replace_non_alpha(string, replace_char):
    """
    Replaces all non-alphabetic characters (excluding white spaces) in the string 
    with the given replacement character and returns the modified string along 
    with the total number of replacements made.

    Args:
        string (str): The input string.
        replace_char (str): The replacement character.

    Returns:
        tuple: A tuple containing the modified string and the total number of replacements.
    """
    replaced_string = ""
    replacements_count = 0
    for char in string:
        if not char.isalpha() and char != " ":
            replaced_string += replace_char
            replacements_count += 1
        else:
            replaced_string += char
    return replaced_string, replacements_count