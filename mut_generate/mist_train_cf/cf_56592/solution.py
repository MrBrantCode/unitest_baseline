"""
QUESTION:
Create a function `diamond(rows, char)` that prints a diamond structure with the specified number of rows using the provided character. The function should take two parameters: `rows` (the number of rows in the diamond) and `char` (the character to use in constructing the diamond). Ensure that the function handles invalid inputs by returning a meaningful error message if `rows` is not a positive integer or `char` is not a single character string.
"""

def diamond(rows, char):
    """
    This function prints a diamond structure with the specified number of rows using the provided character.

    Parameters:
    rows (int): The number of rows in the diamond.
    char (str): The character to use in constructing the diamond.

    Returns:
    str: An error message if the input is invalid.
    """

    # Error checking
    if type(rows) != int:
        return "Error: Number of rows must be an integer."
    if type(char) != str or len(char) != 1:
        return "Error: Character must be a single character string."
    if rows <= 0:
        return "Error: Number of rows must be a positive integer."

    # Create the diamond
    for i in range(rows):
        print(' '*(rows-i-1) + char*(2*i+1))
    for i in range(rows-2, -1, -1):
        print(' '*(rows-i-1) + char*(2*i+1))