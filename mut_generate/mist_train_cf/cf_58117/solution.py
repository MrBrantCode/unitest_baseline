"""
QUESTION:
Construct a function `construct_contact_info` that creates a dictionary to store contact information. The dictionary should have names as keys and a nested dictionary as values, where the nested dictionary contains an 'email' key with an email address as its value and a 'phone_numbers' key with a list of phone numbers as its value.
"""

def construct_contact_info(name, email, phone_numbers):
    """
    Construct a dictionary to store contact information.

    Args:
        name (str): The person's name.
        email (str): The person's email address.
        phone_numbers (list): A list of the person's phone numbers.

    Returns:
        dict: A dictionary with the person's name as the key and a nested dictionary as the value.
    """
    return {name: {'email': email, 'phone_numbers': phone_numbers}}