"""
QUESTION:
Write a function `format_json_str` that takes a JSON string as input, and returns the input JSON string transformed into a well-structured, neatly indented output adhering to standard JSON formatting. The input JSON string can contain nested arrays, nested JSON objects, and combinations thereof. The function should be resilient, meaning it should be able to handle any invalid input (e.g. Syntactically incorrect JSON, empty input) and return a clear error message.
"""

import json

def format_json_str(input_str):
    try:
        parsed = json.loads(input_str)
        return json.dumps(parsed, indent=4)
    except ValueError as e:
        return f"Invalid input. Error: {e}"