"""
QUESTION:
Write a Python function `convert_dict_to_json` that converts a dictionary into a JSON string. The function should handle potential exceptions and Unicode characters, and should return `None` if the conversion fails. Ensure that the function is efficient and reliable by handling exceptions and non-serializable data.
"""

import json

def convert_dict_to_json(input_dict):
    try:
        json_str = json.dumps(input_dict, ensure_ascii=False)
        return json_str
    except TypeError as te:
        print(f"TypeError: {te}")
        return None
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None