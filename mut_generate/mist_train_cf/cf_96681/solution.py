"""
QUESTION:
Implement a function `parse_details(json_str)` that takes a JSON string as input, extracts the "details" field, and validates the "phone" field within it. The function should return the extracted phone number if valid, or an error message otherwise. The "phone" field should be a string of exactly 12 characters and follow the format "000-000-0000". Handle cases where the "details" or "phone" fields are missing, null, or of an invalid format, and where the JSON string is malformed.
"""

import json

def parse_details(json_str):
    try:
        data = json.loads(json_str)
        if "details" in data:
            details = data["details"]
            if details is not None and isinstance(details, dict):
                if "phone" in details:
                    phone = details["phone"]
                    if isinstance(phone, str) and len(phone) == 12 and phone.count('-') == 2:
                        return phone
                    else:
                        return "Invalid phone format"
                else:
                    return "Phone field missing"
            else:
                return "Invalid details format"
        else:
            return "Details field missing"
    except json.JSONDecodeError:
        return "Invalid JSON format"