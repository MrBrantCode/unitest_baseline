"""
QUESTION:
Create a function to validate a contact form. The form has three fields: name, email, and message. All fields are required. If any field is empty, display an error message "All fields are required." If all fields are filled, clear the form and display a success message "Form submitted successfully!" The function should take no parameters.
"""

def validate_contact_form(name, email, message):
    """
    Validate the contact form by checking if all fields are filled.
    
    Args:
        name (str): The name of the user.
        email (str): The email of the user.
        message (str): The message of the user.
    
    Returns:
        tuple: A boolean indicating whether the form is valid and a message to display.
    """
    if not all([name, email, message]):
        return False, "All fields are required."
    else:
        return True, "Form submitted successfully!"