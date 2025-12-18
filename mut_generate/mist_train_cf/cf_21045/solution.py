"""
QUESTION:
Write a function `greet(name)` that checks if a given name is valid. A valid name consists of alphabets only, is case-insensitive, does not contain consecutive whitespace characters, and only contains ASCII characters. If the name is valid, return "Hello, [name]!", otherwise return "Invalid name!". The function should also trim any leading or trailing whitespace characters from the name before printing it.
"""

def greet(name):
    """
    Checks if a given name is valid and returns a greeting if valid, otherwise returns an error message.
    
    A valid name consists of alphabets only, is case-insensitive, does not contain consecutive whitespace characters, 
    and only contains ASCII characters.
    
    :param name: The input name to be checked.
    :return: A greeting message if the name is valid, otherwise an error message.
    """
    if not name:
        return "Invalid name!"
    elif any(char.isdigit() or not char.isascii() for char in name):
        return "Invalid name!"
    elif any(char.isspace() for char in name) and any(name[i].isspace() and name[i+1].isspace() for i in range(len(name)-1)):
        return "Invalid name!"
    else:
        trimmed_name = name.strip()
        return f"Hello, {trimmed_name}!"