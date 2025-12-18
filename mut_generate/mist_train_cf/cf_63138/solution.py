"""
QUESTION:
Write a function `generate_json(personal_details, professional_details)` that takes two dictionaries as input, `personal_details` and `professional_details`, and returns a properly formatted JSON string. The function should include error handling for invalid or null inputs. If the input is invalid or null, the function should return an error message. The JSON output should be formatted with an indentation of 4 spaces.
"""

import json

def generate_json(personal_details, professional_details):
    if not personal_details or not professional_details:
        return "Invalid or null inputs"
    try:
        data = {}
        data['PersonalDetails'] = personal_details
        data['ProfessionalDetails'] = professional_details
        json_data = json.dumps(data,indent=4)
        return json_data
    except (TypeError, ValueError) as e:
        return str(e)