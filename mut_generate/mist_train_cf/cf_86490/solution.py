"""
QUESTION:
Write a function `clean_json(json_data)` that takes a JSON object as input and returns the cleaned-up JSON object. The function should ensure that all fields have consistent data types and convert the 'age' field to a string data type. It should handle nested JSON objects and arrays of arbitrary depth, as well as cases where the 'hobbies' field contains null values or objects with missing 'firstname' or 'lastname' fields.
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