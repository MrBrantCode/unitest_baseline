"""
QUESTION:
Create a function called `construct_json` that takes the following parameters: `name`, `age`, `address`, `job_title`, and `contact_details`. The `name` and `age` parameters are required, while `address`, `job_title`, and `contact_details` are optional. The function should return a JSON object as a string with the provided information. If `name` or `age` is missing or invalid (non-string or non-positive integer, respectively), the function should return a JSON object with an error message. If any of the optional parameters are not provided, they should be assigned a default value of "Not provided" in the returned JSON object.
"""

import json

def construct_json(name, age, address=None, job_title=None, contact_details=None):
    if not name or not age:
        return json.dumps({'error': 'Name and Age parameters are required!'})

    if not isinstance(name, str):
        return json.dumps({'error': 'Invalid name. Name should be a string.'})

    if not isinstance(age, int) or age < 0:
        return json.dumps({'error': 'Invalid age. Age should be a non-negative integer.'})

    data = {
        "Name": name,
        "Age": age,
        "Address": address if address else "Not provided",
        "Job Title": job_title if job_title else "Not provided",
        "Contact Details": contact_details if contact_details else "Not provided",
    }

    return json.dumps(data, indent=4)