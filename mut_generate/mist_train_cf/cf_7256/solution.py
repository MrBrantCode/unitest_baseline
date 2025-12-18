"""
QUESTION:
Create a function named `validate_password` that takes a password string as input and returns True if it is valid and False otherwise. The password is valid if it meets the following criteria:
- It is between 10 and 16 characters long.
- It contains at least one uppercase character, one lowercase character, one digit, and two special characters.
- It does not contain any spaces.
- It does not contain any repeating characters consecutively.
"""

def validate_password(password):
    """
    Validate a password based on the following criteria:
    - It is between 10 and 16 characters long.
    - It contains at least one uppercase character, one lowercase character, one digit, and two special characters.
    - It does not contain any spaces.
    - It does not contain any repeating characters consecutively.

    Args:
        password (str): The password to be validated.

    Returns:
        bool: True if the password is valid, False otherwise.
    """

    # Check if the password length is between 10 and 16 characters
    if not 10 <= len(password) <= 16:
        return False

    uppercase = lowercase = digit = False
    specialCount = 0
    consecutive = False
    prev_char = None

    # Iterate over each character in the password
    for c in password:
        # Check if the character is a space
        if c.isspace():
            return False

        # Check if the character is an uppercase character
        if c.isupper():
            uppercase = True
        # Check if the character is a lowercase character
        elif c.islower():
            lowercase = True
        # Check if the character is a digit
        elif c.isdigit():
            digit = True
        # Check if the character is a special character
        elif not c.isalnum():
            specialCount += 1

        # Check if the character is the same as the previous character
        if prev_char is not None and c == prev_char:
            consecutive = True
        prev_char = c

    # Check if the password meets all the criteria
    return (uppercase and lowercase and digit and specialCount >= 2 and not consecutive)