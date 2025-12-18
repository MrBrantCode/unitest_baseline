"""
QUESTION:
Write a function called `convert_strings` that takes a list of strings as input. The function should convert each string in the list to uppercase if it contains both uppercase and lowercase letters. If a string contains only lowercase letters, it should be converted to title case. Any strings that contain numbers or special characters should be ignored and remain unchanged.
"""

def convert_strings(strings):
    """
    This function takes a list of strings, converts each string to uppercase if it contains 
    both uppercase and lowercase letters, converts strings with only lowercase letters to 
    title case, and ignores strings with numbers or special characters.

    Args:
        strings (list): A list of strings.

    Returns:
        list: The modified list of strings.
    """

    for i in range(len(strings)):
        if any(char.isdigit() or not char.isalpha() for char in strings[i]):
            continue
        elif any(char.isupper() for char in strings[i]) and any(char.islower() for char in strings[i]):
            strings[i] = strings[i].upper()
        elif any(char.islower() for char in strings[i]):
            strings[i] = strings[i].title()

    return strings