"""
QUESTION:
Write a function `convert_to_json_string` that takes a dictionary as input, converts it to a JSON string, and replaces non-serializable data types with their string representations. The function should be able to handle sets and datetime objects. The output JSON string should have the same structure as the input dictionary, but with all non-serializable data types converted to strings.
"""

import json
from datetime import datetime

def convert_to_json_string(input_dict: dict) -> str:
    def default_encoder(obj):
        if isinstance(obj, set):
            return list(obj)
        elif isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return str(obj)

    return json.dumps(input_dict, default=default_encoder)