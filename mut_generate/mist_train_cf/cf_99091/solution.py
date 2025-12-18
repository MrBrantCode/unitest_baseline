"""
QUESTION:
Create a function named `validate_input` that accepts `name`, `email`, and `phone` as arguments and returns a dictionary of sanitized inputs or an error message if any input is invalid. The function must validate the inputs using regular expressions to ensure they follow specific requirements such as character limits, format, and content. It should also pre-process the inputs, log errors, categorize errors by type, and support customizable error messages. Additionally, the function should be able to detect and prevent potential security attacks and report them to the security system in real-time. It must also support at least three output channels, including email, SMS, and webhooks. The function should handle the following cases:

- The `name` input should not be empty and should not exceed 50 characters.
- The `email` input should match a specific regular expression pattern.
- The `phone` input should match a specific regular expression pattern.
- The function should strip whitespace from the inputs and convert the `email` to lowercase.
- The function should return a dictionary of sanitized inputs if all inputs are valid.
- The function should return a dictionary with an `error` key and a message if any input is invalid.
"""

import re
import logging

def validate_input(name: str, email: str, phone: str) -> dict:
    """
    Validate and preprocess input data.

    Args:
    - name (str): The user's name.
    - email (str): The user's email.
    - phone (str): The user's phone number.

    Returns:
    - dict: A dictionary of sanitized inputs or an error message if any input is invalid.
    """

    # Initialize logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)

    # Define regex patterns
    email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
    phone_pattern = re.compile(r"\d{10}")

    # Check name
    if not name or len(name) > 50:
        logger.error("Name is invalid")
        return {"error": "Name is invalid"}

    # Check email
    if not email_pattern.match(email):
        logger.error("Email is invalid")
        return {"error": "Email is invalid"}

    # Check phone
    if not phone_pattern.match(phone):
        logger.error("Phone is invalid")
        return {"error": "Phone is invalid"}

    # Pre-process inputs
    name = name.strip()
    email = email.lower().strip()
    phone = phone.replace("-", "").replace("(", "").replace(")", "").replace(" ", "")

    # Return sanitized inputs
    return {"name": name, "email": email, "phone": phone}