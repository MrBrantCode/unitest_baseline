"""
QUESTION:
Implement a function `parse_details(json_str)` that takes a JSON string as input, extracts the data stored in the "details" field, and validates the "phone" field within it. The function should handle cases where the "details" field is missing, null, or of an invalid format, and ensure the "phone" field follows the format "000-123-4567" with exactly 12 characters. The function should return the extracted phone number if valid, otherwise return a corresponding error message.
"""

import json
import re

def parse_details(json_str):
    try:
        data = json.loads(json_str)
        if "details" not in data or data["details"] is None:
            return "Details field missing"
        
        details = data["details"]
        if not isinstance(details, dict):
            return "Invalid details format"
        
        if "phone" not in details:
            return "Phone field missing"
        
        phone = details["phone"]
        if not isinstance(phone, str) or not re.match(r'^\d{3}-\d{3}-\d{4}$', phone):
            return "Invalid phone format"
        
        return phone
    except json.JSONDecodeError:
        return "Invalid JSON format"