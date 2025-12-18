"""
QUESTION:
Create a function that takes in user input for favorite color, name, and age. Validate the input to ensure the color is a valid hexadecimal color code, the name is not empty, and the age is a positive integer. Return an error message if any validation fails; otherwise, return the validated user input as a formatted string.

Note that the function should handle the following restrictions:
- The color should match the pattern #([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3}).
- The name should not be empty.
- The age should be a positive integer.
"""

def validate_user_input(color: str, name: str, age: str) -> str:
    """
    Validate user input for favorite color, name, and age.

    Args:
    color (str): Favorite color in hexadecimal code.
    name (str): User's name.
    age (str): User's age.

    Returns:
    str: Error message if validation fails; otherwise, a formatted string with validated user input.
    """

    # Validate color
    if not re.match(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', color):
        return "Invalid color code."

    # Validate name
    if name.strip() == "":
        return "Name cannot be empty."

    # Validate age
    if not age.isdigit() or int(age) <= 0:
        return "Invalid age."

    # If all validations pass, return a formatted string with user input
    return f"Favorite Color: {color}\nName: {name}\nAge: {age}"

import re