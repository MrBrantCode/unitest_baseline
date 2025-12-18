"""
QUESTION:
Write a function named `clean_json` that takes a JSON data as input and returns the cleaned JSON data. The function should recursively traverse the JSON object, convert the 'age' field to a string data type, and handle cases where the 'hobbies' field contains null values or objects with missing 'firstname' or 'lastname' fields. The function should be able to handle nested JSON objects and arrays of arbitrary depth.
"""

def clean_json(json_data):
    if isinstance(json_data, dict):
        cleaned_data = {}
        for key, value in json_data.items():
            if key == 'age':
                cleaned_data[key] = str(value)
            else:
                cleaned_data[key] = clean_json(value)
        return cleaned_data
    elif isinstance(json_data, list):
        cleaned_data = []
        for item in json_data:
            cleaned_data.append(clean_json(item))
        return cleaned_data
    elif isinstance(json_data, int):
        return str(json_data)
    elif json_data is None:
        return None
    elif isinstance(json_data, str):
        return json_data
    else:
        return None  # Handle unrecognized data types