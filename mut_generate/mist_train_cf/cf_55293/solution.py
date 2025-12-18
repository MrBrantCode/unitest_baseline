"""
QUESTION:
Create a function `validate_and_add_email` that adds a new "email" field to a given JSON object if the email is in a proper format (e.g. john.doe@email.com). The function should validate the email format using a regular expression before adding it to the JSON object. The JSON object and the email to be added should be passed as input to the function.
"""

import json
import re

def validate_and_add_email(json_str, email):
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if(re.search(pattern, email)):
        json_obj = json.loads(json_str)
        json_obj["email"] = email
        return json.dumps(json_obj)
    else:
        return "Invalid email format"