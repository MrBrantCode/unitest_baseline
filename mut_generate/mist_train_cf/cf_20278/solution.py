"""
QUESTION:
Create a function called `validate_registration` that validates a user's registration information for an event. The function should take four arguments: `name`, `email`, `phone_number`, and `event`. 

The function should validate the input values according to the following rules:
- `name` should only contain alphabetic characters and be between 2 and 50 characters long.
- `email` should follow the standard email format (e.g., example@example.com).
- `phone_number` should only contain numbers and be in a valid phone number format (e.g., 123-456-7890).
- `event` should be one of at least five predefined events.

The function should return `True` if all input values are valid, and `False` otherwise.

You must implement this functionality from scratch without using any external libraries or frameworks for form validation or database handling.
"""

import re

def validate_registration(name, email, phone_number, event):
    """
    Validates a user's registration information for an event.

    Args:
    name (str): The user's name.
    email (str): The user's email.
    phone_number (str): The user's phone number.
    event (str): The event the user is registering for.

    Returns:
    bool: True if all input values are valid, False otherwise.
    """

    # List of predefined events
    events = ["Event 1", "Event 2", "Event 3", "Event 4", "Event 5"]

    # Check if name contains only alphabetic characters and is between 2 and 50 characters long
    if not re.match('^[A-Za-z]{2,50}$', name):
        return False

    # Check if email follows the standard email format
    if not re.match('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return False

    # Check if phone number is in a valid format (e.g., 123-456-7890)
    if not re.match('^\d{3}-\d{3}-\d{4}$', phone_number):
        return False

    # Check if event is one of the predefined events
    if event not in events:
        return False

    return True