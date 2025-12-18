"""
QUESTION:
Implement a function named `ensure_decoded_json` that takes a single argument `val` and returns the decoded JSON if the input is a JSON string, or the input itself if it is already a dictionary. The function should handle potential exceptions that may occur during the decoding process and provide informative error messages. The function should meet the following requirements: 
- If the input is a dictionary, return the input as is.
- If the input is a JSON string, decode it using `json.loads` and return the decoded JSON if it is a dictionary; otherwise, return an error message indicating that the input is not a valid JSON object.
- If the input is not a valid JSON string or dictionary, return an error message indicating that the input is not valid.
"""

import json

def ensure_decoded_json(val):
    if isinstance(val, dict):
        return val
    else:
        try:
            decoded_json = json.loads(val)
            if isinstance(decoded_json, dict):
                return decoded_json
            else:
                return "Input is not a valid JSON object"
        except json.JSONDecodeError:
            return "Input is not a valid JSON string"
        except Exception as e:
            return f"An error occurred: {str(e)}"