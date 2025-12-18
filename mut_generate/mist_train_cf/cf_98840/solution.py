"""
QUESTION:
Create a function called validate_inputs that accepts a dictionary of input fields with their respective validation rules and returns the sanitized inputs if all validation rules pass, or a user-friendly error message if any validation rule fails. The validation rules that must be supported include character limits (max_length), format (using regular expressions), and content restrictions (specific allowed values). The function should also allow for optional sanitization of input values using a provided function. If any errors occur during validation, they should be logged and returned in a user-friendly error message.
"""

import re
from typing import Dict, Any, Callable

def validate_inputs(input_dict: Dict[str, Dict[str, Any]]) -> Dict[str, str]:
    """
    Validate inputs based on provided rules and return sanitized inputs if all rules pass.
    
    Args:
    input_dict (Dict[str, Dict[str, Any]]): A dictionary of input fields with their respective validation rules.
    
    Returns:
    Dict[str, str]: Sanitized inputs if all validation rules pass, or a user-friendly error message if any validation rule fails.
    """

    errors = []
    
    # Loop through input_dict and apply validation rules to each input field
    for field, rules in input_dict.items():
        value = rules.get("value")

        # Check for character limit
        if rules.get("max_length") and len(value) > rules["max_length"]:
            errors.append(f"{field} must be less than {rules['max_length']} characters.")

        # Check for format
        if rules.get("format"):
            regex = re.compile(rules["format"])
            if not regex.match(value):
                errors.append(f"{field} must match format {rules['format']}.")

        # Check for content
        if rules.get("content"):
            if value not in rules["content"]:
                errors.append(f"{field} must be one of the following values: {', '.join(rules['content'])}.")

    # If there were errors, log them and return a user-friendly error message
    if errors:
        error_message = "The following errors occurred:"
        for error in errors:
            error_message += f"\n- {error}"
        print(error_message)  # Replace this line with your preferred logging method
        return {"error": error_message}

    # If there were no errors, return the sanitized inputs
    sanitized_inputs = {}
    for field, rules in input_dict.items():
        value = rules.get("value")
        if rules.get("sanitize"):
            sanitized_inputs[field] = rules["sanitize"](value)
        else:
            sanitized_inputs[field] = value
    return sanitized_inputs