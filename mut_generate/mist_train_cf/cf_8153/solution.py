"""
QUESTION:
Write a function named `check_name` that takes a string `name` as input. The function should check the case of the first two characters in the string and return a message based on the following conditions:
- If the name starts with a lowercase letter, check the case of the second character. If the second character is uppercase, return "My name starts with a lowercase letter followed by an uppercase letter". If the second character is not uppercase, return "My name starts with a lowercase letter followed by a lowercase letter".
- If the name starts with an uppercase letter, return "My name starts with an uppercase letter".
- If the name starts with any other character, return "My name does not start with a letter".
"""

def check_name(name: str) -> str:
    """
    Checks the case of the first two characters in the input string.

    Args:
        name (str): The input string to be checked.

    Returns:
        str: A message describing the case of the first two characters.
    """

    if name[0].islower():
        if name[1].isupper():
            return "My name starts with a lowercase letter followed by an uppercase letter"
        else:
            return "My name starts with a lowercase letter followed by a lowercase letter"
    elif name[0].isupper():
        return "My name starts with an uppercase letter"
    else:
        return "My name does not start with a letter"