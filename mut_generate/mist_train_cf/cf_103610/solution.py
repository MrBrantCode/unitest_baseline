"""
QUESTION:
Write a function `filter_lines` that takes two parameters: a string containing multiple lines of text and a character. The function should print all lines that end with the given character, and return the total count of lines that contain the given character.
"""

def filter_lines(text, char):
    """
    Prints all lines that end with the given character and returns the total count of lines that contain the given character.

    Args:
        text (str): A string containing multiple lines of text.
        char (str): A character.

    Returns:
        int: The total count of lines that contain the given character.
    """
    lines = text.split('\n')  # Split the string into lines
    count = sum(1 for line in lines if char in line)  # Count lines containing the character

    for line in lines:
        if line.endswith(char):
            print(line)

    return count