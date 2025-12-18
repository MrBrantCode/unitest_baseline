"""
QUESTION:
Create a function named `validateUserRegistration` that takes four parameters: `name`, `age`, `gender`, and `email`. The function should validate the user's input according to the following rules: 
- The `name` must be at least 3 characters long.
- The `age` must be a number between 18 and 99.
- The `gender` must not be empty.
- The `email` must be in a valid format.

If any of the validation fails, the function should return an error message describing the validation failure. If all validation passes, the function should return a confirmation message with the user's information. The email validation should use a regular expression to check the format.
"""

import re

def validateUserRegistration(name, age, gender, email):
    """
    Validate user's registration information.

    Args:
        name (str): The user's name.
        age (int): The user's age.
        gender (str): The user's gender.
        email (str): The user's email.

    Returns:
        str: An error message if validation fails, otherwise a confirmation message.
    """

    # Validate name
    if len(name) < 3:
        return "Name must be at least 3 characters long."

    # Validate age
    if not isinstance(age, int) or age < 18 or age > 99:
        return "Age must be a number between 18 and 99."

    # Validate gender
    if not gender:
        return "Please select a gender."

    # Validate email
    email_regex = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
    if not re.match(email_regex, email):
        return "Email address is not valid."

    # If all validation passes, return a confirmation message
    return f"Registration successful! \nName: {name} \nAge: {age} \nGender: {gender} \nEmail: {email}"