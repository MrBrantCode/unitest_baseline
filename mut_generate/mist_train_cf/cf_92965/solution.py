"""
QUESTION:
Write a function called `extract_phone_number` that takes a JSON object as input, extracts the data stored in the "details" field, and then extracts the "phone" field from it. The function should handle cases where the "details" field may be missing or null and validate that the "phone" field follows the format "000-123-4567". Return the "phone" number if it exists and is valid; otherwise, return an error message.
"""

import json
import re

def extract_phone_number(json_data):
    """
    Extracts the phone number from a JSON object.

    Args:
        json_data (str): A JSON string containing user data.

    Returns:
        str: The extracted phone number if it exists and is valid, otherwise an error message.
    """
    try:
        data = json.loads(json_data)
    except json.JSONDecodeError:
        return "Invalid JSON format"

    details = data.get("details")

    if details is None:
        return "Missing or null details field"

    phone = details.get("phone")

    if phone is None:
        return "Missing phone number"

    if re.match(r"\d{3}-\d{3}-\d{4}", phone):
        return phone
    else:
        return "Invalid phone number format"