"""
QUESTION:
Create a function validateForm to validate a user's information form. The form should have fields for name, age, gender, and email. The function should check that the name is at least 3 characters long and the age is between 18 and 99. If any of the fields are empty or if the validation fails, it should display an error message. Upon successful submission of the form, it should display a confirmation message with the user's information.
"""

def validate_form(name, age, gender, email):
    """
    Validate a user's information form.

    Args:
        name (str): User's name.
        age (int): User's age.
        gender (str): User's gender.
        email (str): User's email.

    Returns:
        tuple: A tuple containing a boolean indicating whether the form is valid and an error message if any.
    """
    error_message = ""

    # Check if name is at least 3 characters long
    if len(name) < 3:
        error_message += "Name must be at least 3 characters long.\n"

    # Check if age is between 18 and 99
    if age < 18 or age > 99:
        error_message += "Age must be between 18 and 99.\n"

    # Check if gender is not empty
    if not gender:
        error_message += "Please select a gender.\n"

    # Check if email is not empty
    if not email:
        error_message += "Email address is required.\n"

    # Return validation result and error message
    if error_message:
        return False, error_message
    else:
        return True, "Form submitted successfully."