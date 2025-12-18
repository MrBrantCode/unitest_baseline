"""
QUESTION:
Write a function called `toggle_string` that takes a string as input, toggles all characters in the string to their opposite case (uppercase to lowercase and vice versa), and returns the toggled string along with a dictionary containing the count of each character in the original string. The function should consider only the original characters, not the toggled ones, when counting their occurrences.
"""

def toggle_string(string):
    """
    This function takes a string as input, toggles all characters in the string to their opposite case 
    (uppercase to lowercase and vice versa), and returns the toggled string along with a dictionary 
    containing the count of each character in the original string.

    Args:
    string (str): The input string.

    Returns:
    tuple: A tuple containing the toggled string and a dictionary with character counts.
    """
    toggled_string = ""
    character_count = {}

    for char in string:
        if char.islower():
            toggled_string += char.upper()
        elif char.isupper():
            toggled_string += char.lower()
        else:
            toggled_string += char

        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    return toggled_string, character_count