"""
QUESTION:
Create a function named `validate_user_input` that takes in four parameters: `color`, `name`, `age`, and `colors`. `color` and `colors` should be valid hexadecimal color codes, `name` should not be empty, and `age` should be a positive integer within the range of 18 to 65. The function should return a boolean indicating whether the input is valid or not.

Additionally, consider implementing a feature to validate multiple favorite colors and an image upload with specific format and file size limits, as well as storing user information in a database for later retrieval.
"""

def validate_user_input(color, name, age, colors):
    """
    Validate user input.

    Args:
        color (str): A hexadecimal color code.
        name (str): The user's name.
        age (int): The user's age.
        colors (list): A list of hexadecimal color codes.

    Returns:
        bool: True if the input is valid, False otherwise.
    """

    # Check if color is a valid hexadecimal color code
    def is_valid_hex_color(hex_color):
        return isinstance(hex_color, str) and len(hex_color) == 7 and hex_color.startswith('#') and all(c in '0123456789abcdefABCDEF' for c in hex_color[1:])

    # Check if name is not empty
    if not name:
        return False

    # Check if age is a positive integer within the range of 18 to 65
    if not isinstance(age, int) or age < 18 or age > 65:
        return False

    # Check if color is a valid hexadecimal color code
    if not is_valid_hex_color(color):
        return False

    # Check if all colors in the list are valid hexadecimal color codes
    if not all(is_valid_hex_color(c) for c in colors):
        return False

    return True