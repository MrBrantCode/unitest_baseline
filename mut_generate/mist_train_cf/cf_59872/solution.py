"""
QUESTION:
Create a function called 'process_registration' that takes in three parameters: full_name, email, and phone_number. The function should return a string that confirms the successful registration of a user with the provided information. The confirmation string should be in the format: 'You have successfully registered!\n\nName: {full_name}\nEmail: {email}\nPhone: {phone_number}'.
"""

def process_registration(full_name, email, phone_number):
    """
    Returns a confirmation string for a successful user registration.

    Args:
    full_name (str): The full name of the user.
    email (str): The email address of the user.
    phone_number (str): The phone number of the user.

    Returns:
    str: A confirmation string containing the user's registration information.
    """
    return f'You have successfully registered!\n\nName: {full_name}\nEmail: {email}\nPhone: {phone_number}'