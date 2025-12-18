"""
QUESTION:
Create a dictionary called "contact" with five key-value pairs: "name", "age", "email", "phone", and "address". The values should meet the following criteria:
- "name": a string with at least two capitalized words separated by a space.
- "age": an integer between 18 and 100 (inclusive).
- "email": a string in the format "username@domain.com" where the username starts with a letter and the domain is valid.
- "phone": a string in the format "+XX-XXXXXXXXXX" with a valid country code and phone number digits.
- "address": a string with at least two lines, each line separated by a newline character and not exceeding 100 characters.
"""

def create_contact(name, age, email, phone, address):
    """
    Creates a dictionary called "contact" with the given information.

    Args:
    name (str): A string with at least two capitalized words separated by a space.
    age (int): An integer between 18 and 100 (inclusive).
    email (str): A string in the format "username@domain.com" where the username starts with a letter and the domain is valid.
    phone (str): A string in the format "+XX-XXXXXXXXXX" with a valid country code and phone number digits.
    address (str): A string with at least two lines, each line separated by a newline character and not exceeding 100 characters.

    Returns:
    dict: A dictionary containing the given contact information.
    """
    return {
        "name": name,
        "age": age,
        "email": email,
        "phone": phone,
        "address": address
    }