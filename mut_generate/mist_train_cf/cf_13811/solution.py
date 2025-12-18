"""
QUESTION:
Create a function called `parse_phone_number` that takes a JSON object as input. The function should extract the "phone" field from the "details" object in the JSON data, handle cases where the "details" field may be missing or null, and validate that the "phone" field follows the format "000-123-4567". If the "phone" field matches the format, return the phone number; otherwise, return an error message indicating that the phone number format is invalid or that the "details" field is missing or null.
"""

import json
import re

def parse_phone_number(json_data):
    """
    Extract the "phone" field from the "details" object in the JSON data.

    Args:
    json_data (str): A JSON object as a string.

    Returns:
    str: The phone number if it matches the format "000-123-4567", 
         otherwise an error message.
    """
    data = json.loads(json_data)
    details = data.get("details")
    
    if details is not None:
        phone = details.get("phone")
        if phone is not None and re.match(r"\d{3}-\d{3}-\d{4}", phone):
            return phone
        else:
            return "Invalid phone number format"
    else:
        return "Missing or null details field"