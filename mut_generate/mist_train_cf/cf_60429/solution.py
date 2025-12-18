"""
QUESTION:
Create a function named `recover_json` that takes a string representation of a malformed JSON object as input and returns a Python dictionary. The function should handle common malformations such as missing commas and quotations. If the provided JSON string is not recoverable, the function should return `None`.
"""

import re
import json

def recover_json(malformed_json):
    # Add missing commas
    no_comma_str = re.sub(r'}\s*{', '},{', malformed_json)
    
    # Add missing quotations
    no_quote_str = re.sub(r'(\b[a-zA-Z_]+\b)\s*:', r'"\1":', no_comma_str)
    
    try:
        # Try to convert string into Python dict
        return json.loads(no_quote_str)
    except ValueError:
        return None