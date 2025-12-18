"""
QUESTION:
Write a function called `convert_strings` that takes a list of strings as input, where each string is either comma or semicolon separated. The function should reverse the order of the strings and concatenate them into a single string. The resulting string should not exceed 100 characters in length. The function should exclude any strings that contain special characters or numbers. If the resulting string is empty, it should return an empty string.
"""

def convert_strings(strings):
    """
    This function takes a list of strings as input, reverses their order, 
    excludes strings with special characters or numbers, and concatenates 
    them into a single string not exceeding 100 characters in length.
    
    Args:
        strings (list): A list of strings.
    
    Returns:
        str: A concatenated string.
    """
    reversed_strings = strings[::-1]
    result = ""
    for string in reversed_strings:
        if string.isalpha():
            result += string + ","
            if len(result) >= 100:
                result = result[:-1]
                break
    return result[:-1] if result else ''